# Air Hockey minigame.
#
# This is built the same way as the table tennis minigame in the base game:
# a Displayable does all the moving and drawing, and a handful of labels below
# run the greeting, the difficulty choice, and the win/lose results.
#
# HOW THE ANGLED LOOK IS DONE
#
# The table is shown at an angle, leaning away from us into the distance, the
# way an arcade air hockey table looks when you stand at one end. The important
# thing to understand is that NONE of the bouncing maths is angled. All of the
# moving, bouncing and scoring happens on a plain flat rectangle, exactly like a
# real table seen straight down from the ceiling. That flat rectangle is called
# the play field below, and it is where every sum is done, because sums on a
# flat rectangle are simple and never go wrong.
#
# The angle is added only at the very end, when we draw. We take each flat point
# and work out where on the screen it should appear on the tilted table: points
# near us are drawn low and wide, points far away are drawn high up and squeezed
# together. Lines that are really parallel on the table lean towards each other
# as they go away, and that leaning is the whole into-the-distance effect.
#
# Because the player slides their mallet with the mouse, and the mouse lives on
# the tilted picture, we also run that same step backwards: we take where the
# mouse is on screen and work out which flat point on the table it is pointing
# at. That backwards step is the only fiddly bit, and it is explained where it
# happens.
#
# Nothing here needs any picture files. The table, the lines, the goals, the two
# mallets and the puck are all painted in code as plain shapes and colours.

init python:

    # Used below to trace the round pieces as many-sided shapes.
    import math

    class AirHockey(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The look of the pieces is chosen by the character we play against,
            # the same way the tennis game reads its look off its partner. The
            # width is the size across the round piece; we draw both pieces as
            # circles, so we only keep the width.
            self.hit_sound = store.minigame_air_hockey_partner.minigame_air_hockey_hit_sound()
            self.MALLET_DIAMETER = store.minigame_air_hockey_partner.minigame_air_hockey_mallet_width()
            self.PUCK_DIAMETER = store.minigame_air_hockey_partner.minigame_air_hockey_puck_width()
            self.MALLET_COLOR = store.minigame_air_hockey_partner.minigame_air_hockey_mallet_color()
            self.PUCK_COLOR = store.minigame_air_hockey_partner.minigame_air_hockey_puck_color()

            # The "Click to Begin" prompt. It sits low on the table, on the open
            # ice below the centre, so it stays clear of the scoreboard and the
            # scores now painted on it at the top.
            self.ctb = Text(_("Click to Begin"), size=48, xalign = 0.5, yalign = 0.6)

            # THE PLAY FIELD (the table seen flat from straight above)
            #
            # fx runs from 0 at the left wall to FIELD_W at the right wall.
            # fy runs from 0 at the far end (the opponent's goal, drawn at the
            # top) to FIELD_H at the near end (our goal, drawn at the bottom).
            # So a small fy is far away and a large fy is close to us. These two
            # sizes are in made-up "table units", not screen pixels; the drawing
            # step turns them into pixels later.
            self.FIELD_W = 800.0
            self.FIELD_H = 1300.0

            # We treat both round pieces as circles when working out hits, so we
            # keep half of each width as its radius.
            self.MALLET_RADIUS = self.MALLET_DIAMETER / 2
            self.PUCK_RADIUS = self.PUCK_DIAMETER / 2

            # The goal openings. Both ends use the same width, and we draw the red
            # crease semicircle ourselves further down (the table picture no longer
            # has them painted on), so the crease you see always lines up with the
            # opening the puck really scores through. The width is set together with
            # the speeds just below, because it changes with the difficulty: a wider
            # opening is harder to guard, and that is on purpose. With a narrow
            # opening a player can park a mallet across their own goal and stop
            # everything, dragging a match on with no end; a wider opening leaves
            # room a parked mallet can't cover, so that trick stops working. The
            # puck scores when it crosses an end line inside the opening, measured
            # straight on the play field. Each value is half the opening's width.

            # Where the opponent parks its mallet when defending: a little in
            # front of its own goal at the far end, with room to step out and
            # meet the puck.
            self.OPPONENT_HOME_Y = 220.0

            # Speeds change with the difficulty the player picked. serve_speed is
            # how fast the puck leaves the centre, max_speed is the fastest it is
            # ever allowed to go, and opponent_speed is how fast the opponent's
            # mallet can chase. A slower opponent is easier to beat, which is why
            # easy gives the opponent the lowest speed. goal_half is set here too,
            # since the opening grows with the difficulty: wider on harder.
            if store.minigame_air_hockey_difficulty == "easy":
                self.serve_speed = 650.0
                self.max_speed = 1200.0
                self.opponent_speed = 560.0
                goal_half = self.FIELD_W * 0.12

            elif store.minigame_air_hockey_difficulty == "medium":
                self.serve_speed = 800.0
                self.max_speed = 1700.0
                self.opponent_speed = 760.0
                goal_half = self.FIELD_W * 0.15

            else:
                self.serve_speed = 950.0
                self.max_speed = 2100.0
                self.opponent_speed = 980.0
                goal_half = self.FIELD_W * 0.18

            # Both ends use that one width, so each crease comes out the same size
            # across the field.
            self.FAR_GOAL_HALF = goal_half
            self.NEAR_GOAL_HALF = goal_half

            # Every time a mallet hits the puck we add a small fixed nudge
            # (hit_bonus) so rallies don't peter out. min_after_hit is only a low
            # floor to stop the puck stalling dead against a mallet; it is kept
            # low on purpose so a gentle hit really does stay gentle and a hard
            # hit really flies, instead of every hit coming off at the same speed.
            self.hit_bonus = self.serve_speed * 0.12
            self.min_after_hit = self.serve_speed * 0.3

            # How much of a mallet's swing speed gets passed into the puck on a
            # hit. 1.0 passes on the full swing; lower feels lighter. This is the
            # main dial for how weighty a hit feels: turn it up if shots feel
            # soft, down if the puck shoots off too easily.
            self.HIT_STRENGTH = 0.8

            # The puck starts on the centre spot.
            self.px = self.FIELD_W / 2
            self.py = self.FIELD_H / 2

            # Pick the serve direction now. It heads up or down the table at
            # random with a little sideways lean, so the player can't assume
            # which way it will go. We turn that direction into an actual speed
            # (vx, vy is how far the puck moves each second).
            dir_y = random.choice([-1.0, 1.0])
            dir_x = random.uniform(-0.5, 0.5)
            length = (dir_x * dir_x + dir_y * dir_y) ** 0.5
            self.vx = self.serve_speed * dir_x / length
            self.vy = self.serve_speed * dir_y / length

            # The player's mallet starts in front of our near goal. The
            # opponent's mallet starts in front of its far goal.
            self.player_x = self.FIELD_W / 2
            self.player_y = self.FIELD_H - self.OPPONENT_HOME_Y
            self.opp_x = self.FIELD_W / 2
            self.opp_y = self.OPPONENT_HOME_Y

            # Where the player's mallet was on the previous frame. We compare it
            # against where the mallet is now to work out how fast the player is
            # swinging, which is what decides how hard the puck gets hit. It
            # starts at the mallet's own starting spot so the first frame counts
            # as no swing.
            self.player_prev_x = self.player_x
            self.player_prev_y = self.player_y

            # The puck waits on the centre spot until the player clicks to serve.
            self.stuck = True

            # The time of the previous drawn frame, so we can tell how much time
            # has passed and move things by the right amount.
            self.oldst = None

            # Who scored. Stays None until a goal goes in.
            self.winner = None

            # THE ANGLED VIEW (how the flat field is turned into screen pixels)
            #
            # These five numbers are the whole trick of the tilt, and they are
            # worked out from the screen size so the table stays centred at any
            # resolution. The far edge of the table is drawn high up and narrow;
            # the near edge is drawn low down and wide. Nudge these to change how
            # steep the tilt looks.
            #
            # The four edge numbers trace the table picture's white surface: where
            # its far and near rails sit up and down the screen, and how wide the
            # surface is at each end. This table has flat (sharp) corners, so the
            # straight walls sit right on the rail the whole way round, corners
            # included, with nothing poking out and nothing cut off. They were read
            # off the 1920x1080 picture and then checked against the live game with
            # the boundary overlay: the bottom needed widening a little, because the
            # game draws the table a touch wider at the bottom than the raw file
            # shows. If you swap the table picture, turn the boundary overlay on
            # (developer menu below) and redo these.
            self.FAR_Y = config.screen_height * 0.2296   # screen height of the far edge
            self.NEAR_Y = config.screen_height * 0.8269  # screen height of the near edge
            self.FAR_HALF_W = config.screen_width * 0.1672  # half the table's drawn width, far end
            self.NEAR_HALF_W = config.screen_width * 0.3367 # half the table's drawn width, near end
            self.MID_X = config.screen_width * 0.5        # the screen centre the table is built around

            # How squashed the round pieces look. Because we view the table on a
            # slant, a circle lying on it looks like an oval that is shorter
            # top-to-bottom than side-to-side. 1.0 would be a full circle; lower
            # is flatter.
            self.DISC_SQUASH = 0.55

        # Turns a flat field point into the screen point where it should be
        # drawn on the tilted table. Returns whole pixels, ready to draw with.
        def field_to_screen(self, fx, fy):
            # How far down the table this point is: 0 at the far edge, 1 at the
            # near edge.
            t = fy / self.FIELD_H
            # The up-and-down: slide straight from the far height to the near
            # height as we come down the table.
            sy = self.FAR_Y + t * (self.NEAR_Y - self.FAR_Y)
            # The table is drawn wider the closer it gets, so its half width
            # grows from the far value to the near value over that same slide.
            half_w = self.FAR_HALF_W + t * (self.NEAR_HALF_W - self.FAR_HALF_W)
            # The left-and-right: 0 at the left wall, 1 at the right, 0.5 dead
            # centre. We push out from the screen centre by how far from the
            # middle this point sits.
            nx = fx / self.FIELD_W
            sx = self.MID_X + (nx - 0.5) * 2 * half_w
            return (int(sx), int(sy))

        # The half width of the drawn table at depth t (0 far, 1 near). The round
        # pieces use this to size themselves: pieces near us draw big, pieces far
        # away draw small.
        def half_width_at(self, t):
            return self.FAR_HALF_W + t * (self.NEAR_HALF_W - self.FAR_HALF_W)

        # Turns a screen point (where the mouse is) back into a flat field point,
        # so we can move the player's mallet to wherever they are pointing on the
        # tilted table. This is field_to_screen run backwards.
        def screen_to_field(self, sx, sy):
            # Undo the up-and-down first, which tells us how far down the table
            # the mouse is. Kept between 0 and 1 so a mouse off the table edge
            # still gives a sensible answer.
            t = (sy - self.FAR_Y) / (self.NEAR_Y - self.FAR_Y)
            t = max(0.0, min(1.0, t))
            fy = t * self.FIELD_H
            # Now that we know the depth, we know how wide the table is drawn
            # there, so we can undo the left-and-right.
            half_w = self.half_width_at(t)
            nx = (sx - self.MID_X) / (2 * half_w) + 0.5
            fx = nx * self.FIELD_W
            return (fx, fy)

        def visit(self):
            return [ self.ctb ]

        # Works out the new puck position, handles every bounce and goal, and
        # draws the whole tilted table.
        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            # Figure out how much time passed since the last frame. On the very
            # first frame there is no previous time, so we treat it as zero.
            if self.oldst is None:
                self.oldst = st
            dtime = st - self.oldst
            self.oldst = st

            # Remember where the AI mallet sits before we move it this frame, so
            # we can measure how fast it ends up moving (used to give its hits
            # weight, the same as the player's swing).
            opp_prev_x = self.opp_x
            opp_prev_y = self.opp_y

            # Move the opponent's mallet.
            #
            # If the puck is on the opponent's side (the far half) it goes for
            # the puck and aims a touch beyond it, so when it makes contact it
            # shoves the puck back down toward us. If the puck is on our side it
            # falls back in front of its own goal and slides left and right to
            # guard it.
            if self.py < self.FIELD_H / 2:
                target_x = self.px
                target_y = self.py - 8
            else:
                target_x = self.px
                target_y = self.OPPONENT_HOME_Y

            # Keep the spot it is aiming for on its own half and inside the walls.
            target_x = max(target_x, self.MALLET_RADIUS)
            target_x = min(target_x, self.FIELD_W - self.MALLET_RADIUS)
            target_y = max(target_y, self.MALLET_RADIUS)
            target_y = min(target_y, self.FIELD_H / 2 - self.MALLET_RADIUS)

            # Step the mallet toward that spot, but no further than its speed
            # allows this frame. This cap is what keeps the opponent beatable
            # instead of snapping straight onto the puck. (For a tougher or
            # gentler opponent, change opponent_speed up in __init__.)
            ax = target_x - self.opp_x
            ay = target_y - self.opp_y
            adist = (ax * ax + ay * ay) ** 0.5
            step = self.opponent_speed * dtime
            if adist <= step or adist == 0:
                self.opp_x = target_x
                self.opp_y = target_y
            else:
                self.opp_x += step * ax / adist
                self.opp_y += step * ay / adist

            # Keep the opponent's mallet on its own half and inside the walls.
            self.opp_x = max(self.opp_x, self.MALLET_RADIUS)
            self.opp_x = min(self.opp_x, self.FIELD_W - self.MALLET_RADIUS)
            self.opp_y = max(self.opp_y, self.MALLET_RADIUS)
            self.opp_y = min(self.opp_y, self.FIELD_H / 2 - self.MALLET_RADIUS)

            # Work out how fast each mallet is moving this frame, in field units
            # per second. The player's mallet was last placed by the mouse on the
            # previous frame, so its speed is how far it has shifted since then.
            # These speeds are what let a hard swing send the puck flying while a
            # gentle touch only nudges it, which is what stops the puck feeling
            # weightless.
            if dtime > 0:
                player_vx = (self.player_x - self.player_prev_x) / dtime
                player_vy = (self.player_y - self.player_prev_y) / dtime
                opp_vx = (self.opp_x - opp_prev_x) / dtime
                opp_vy = (self.opp_y - opp_prev_y) / dtime
            else:
                player_vx = 0.0
                player_vy = 0.0
                opp_vx = 0.0
                opp_vy = 0.0

            # While the puck is waiting to be served it just sits on the centre
            # spot.
            if self.stuck:
                self.px = self.FIELD_W / 2
                self.py = self.FIELD_H / 2

            # Bounces the puck off one mallet sitting at (mx, my), and gives back
            # True if it actually made contact. mallet_vx, mallet_vy is how fast
            # that mallet is moving, so a hard swing into the puck sends it off
            # faster. push_y is only used in the rare case where the puck sits
            # dead in the middle of the mallet with no clear way out: -1 shoves
            # it up the table for the player, 1 shoves it down for the opponent.
            def hit_mallet(mx, my, push_y, mallet_vx, mallet_vy):
                gap_x = self.px - mx
                gap_y = self.py - my
                dist = (gap_x * gap_x + gap_y * gap_y) ** 0.5
                reach = self.MALLET_RADIUS + self.PUCK_RADIUS

                # Closer than the two radii added together means they are
                # touching, so the puck is being hit.
                if dist < reach:

                    # The line pointing from the mallet's middle out to the
                    # puck's middle, made length one so it is a pure direction.
                    # Where on the mallet the puck struck sets this line, which is
                    # how a shot gets aimed.
                    if dist > 0:
                        nx = gap_x / dist
                        ny = gap_y / dist
                    else:
                        nx = 0.0
                        ny = push_y

                    # Lift the puck out so it sits just clear of the mallet rather
                    # than buried inside it.
                    self.px = mx + nx * (reach + 1)
                    self.py = my + ny * (reach + 1)

                    # Bounce the puck's own speed off the mallet face, but only if
                    # it was actually heading inward. This is the standard way to
                    # bounce off a surface: take away twice the part of the speed
                    # that points into it.
                    moving_in = self.vx * nx + self.vy * ny
                    if moving_in < 0:
                        self.vx -= 2 * moving_in * nx
                        self.vy -= 2 * moving_in * ny

                    # Add the mallet's own push. We take how fast the mallet is
                    # driving straight into the puck (its speed measured along the
                    # hit line) and add a share of it. A glancing touch adds
                    # little; a square, hard hit adds a lot. HIT_STRENGTH up in
                    # __init__ dials how weighty this feels.
                    mallet_push = mallet_vx * nx + mallet_vy * ny
                    if mallet_push < 0:
                        mallet_push = 0
                    self.vx += nx * mallet_push * self.HIT_STRENGTH
                    self.vy += ny * mallet_push * self.HIT_STRENGTH

                    # Keep rallies lively, but never past this difficulty's top
                    # speed and never so slow the puck stalls against the mallet.
                    current = (self.vx * self.vx + self.vy * self.vy) ** 0.5
                    new_speed = min(current + self.hit_bonus, self.max_speed)
                    if new_speed < self.min_after_hit:
                        new_speed = self.min_after_hit

                    # Stretch the speed to that amount while keeping the
                    # direction. If it was barely moving, send it straight out
                    # along the hit line.
                    if current > 1:
                        self.vx *= new_speed / current
                        self.vy *= new_speed / current
                    else:
                        self.vx = nx * new_speed
                        self.vy = ny * new_speed

                    if self.hit_sound is not None:
                        renpy.sound.play(self.hit_sound, channel=1)

                    return True

                return False

            # Move and check the puck in several small slices instead of one big
            # jump. This is the important part for stopping the puck passing
            # through a mallet: if we slid the puck (or swung a mallet) the whole
            # frame's distance at once, a fast puck or a fast swing could skip
            # clean over the other and the hit would be missed. Cutting the frame
            # into eight slices keeps every move small enough to always catch.
            if not self.stuck:

                STEPS = 8
                part = dtime / STEPS

                # Only let one mallet hit land per frame, so the same contact
                # can't be counted several slices running and rocket the puck.
                mallet_hit = False

                for step in range(STEPS):

                    # Slide the puck its small slice.
                    self.px += self.vx * part
                    self.py += self.vy * part

                    # Where each mallet is partway through the frame, sliding
                    # evenly from where it started to where it ended, so a fast
                    # swing gets checked the whole way along its path.
                    frac = (step + 1.0) / STEPS
                    player_mx = self.player_prev_x + (self.player_x - self.player_prev_x) * frac
                    player_my = self.player_prev_y + (self.player_y - self.player_prev_y) * frac
                    opp_mx = opp_prev_x + (self.opp_x - opp_prev_x) * frac
                    opp_my = opp_prev_y + (self.opp_y - opp_prev_y) * frac

                    # Try the two mallets, unless one already connected this frame.
                    if not mallet_hit:
                        if hit_mallet(player_mx, player_my, -1.0, player_vx, player_vy):
                            mallet_hit = True
                        elif hit_mallet(opp_mx, opp_my, 1.0, opp_vx, opp_vy):
                            mallet_hit = True

                    # Off the left wall. We only flip the puck when it is heading
                    # into the wall, so it can't get stuck flipping back and forth.
                    left_limit = self.PUCK_RADIUS
                    if self.px <= left_limit and self.vx < 0:
                        self.px = left_limit + (left_limit - self.px)
                        self.vx = -self.vx

                    # Off the right wall.
                    right_limit = self.FIELD_W - self.PUCK_RADIUS
                    if self.px >= right_limit and self.vx > 0:
                        self.px = right_limit - (self.px - right_limit)
                        self.vx = -self.vx

                    # The far end of the table, the opponent's goal. The goal
                    # opening is centred and measured on the play field, so if the
                    # puck's field position is within it, it slides in for our goal
                    # once fully past the line. Otherwise it hit solid rail and
                    # bounces back.
                    far_limit = self.PUCK_RADIUS
                    if abs(self.px - self.FIELD_W / 2) < self.FAR_GOAL_HALF:
                        if self.py < -self.PUCK_RADIUS:
                            self.winner = "player"
                    else:
                        if self.py <= far_limit and self.vy < 0:
                            self.py = far_limit + (far_limit - self.py)
                            self.vy = -self.vy

                    # The near end of the table, our goal, the same idea mirrored.
                    # A goal here is the opponent scoring.
                    near_limit = self.FIELD_H - self.PUCK_RADIUS
                    if abs(self.px - self.FIELD_W / 2) < self.NEAR_GOAL_HALF:
                        if self.py > self.FIELD_H + self.PUCK_RADIUS:
                            self.winner = "opponent"
                    else:
                        if self.py >= near_limit and self.vy > 0:
                            self.py = near_limit - (self.py - near_limit)
                            self.vy = -self.vy

                    # Once a goal is in, stop slicing; the round is over.
                    if self.winner:
                        break

            # Remember where the player's mallet ended up this frame, so next
            # frame we can tell how far and how fast it moved.
            self.player_prev_x = self.player_x
            self.player_prev_y = self.player_y

            # From here down we draw the moving pieces. The table itself is now
            # the background picture, so each frame we only paint the two mallets
            # and the puck.
            #
            # We paint them onto their own see-through layer the size of the
            # screen, then drop that finished layer onto the game. Keeping the
            # painting on one separate layer (rather than painting straight onto
            # the game and also dropping other things on top) keeps the two ways
            # of drawing from treading on each other.
            disc_layer = renpy.Render(config.screen_width, config.screen_height)
            canvas = disc_layer.canvas()

            # A short straight stroke on the pieces layer, drawn as a thin filled
            # shape because the drawing tool can't paint a real line on its own. We
            # take the stroke's direction, step out to each side to get its two long
            # edges, and fill the strip between them. Used for the creases right
            # below and for the debug walls further down.
            def stroke(p1, p2, color, thick = 3):
                x1, y1 = p1
                x2, y2 = p2
                dx = x2 - x1
                dy = y2 - y1
                length = (dx * dx + dy * dy) ** 0.5
                if length < 1.0:
                    return
                side_x = -dy / length * thick
                side_y = dx / length * thick
                canvas.polygon(color, [
                    (int(x1 + side_x), int(y1 + side_y)),
                    (int(x2 + side_x), int(y2 + side_y)),
                    (int(x2 - side_x), int(y2 - side_y)),
                    (int(x1 - side_x), int(y1 - side_y)),
                ])

            # The red crease semicircle in front of a goal, in the same red the rest
            # of the table's markings use. We walk points evenly around a half
            # circle drawn flat on the field, its flat side on the end line and its
            # curve bulging in toward the centre, run each point through the same
            # tilt the table uses, then join them up with short strokes. The radius
            # is the goal's half width, so the crease is exactly the opening the
            # puck scores through. Drawn before the pieces, so a mallet or the puck
            # rides over the top of it.
            def draw_crease(center_fx, center_fy, radius, bulge):
                steps = 32
                points = []
                for i in range(steps + 1):
                    ang = math.pi * i / steps
                    fx = center_fx + radius * math.cos(ang)
                    fy = center_fy + bulge * radius * math.sin(ang)
                    points.append(self.field_to_screen(fx, fy))
                for i in range(steps):
                    stroke(points[i], points[i + 1], "#c71225")

            # Far crease sits on the far end line and bulges down into the field;
            # near crease sits on the near end line and bulges up toward the centre.
            draw_crease(self.FIELD_W / 2, 0, self.FAR_GOAL_HALF, 1)
            draw_crease(self.FIELD_W / 2, self.FIELD_H, self.NEAR_GOAL_HALF, -1)

            # Draws one round piece lying flat on the table. Because the table
            # is drawn smaller the further away it is, a piece far up the table
            # is drawn small and a piece near us is drawn big. And because we
            # look at the table on a slant, the piece is drawn shorter
            # top-to-bottom than side-to-side, so it reads as a disc resting on
            # the surface.
            #
            # The drawing tool here can fill in shapes with straight sides but
            # cannot paint a circle or oval on its own (those calls aren't built
            # into Ren'Py's drawing), so we trace the oval ourselves as a
            # 24-sided shape: walk evenly around a circle, stretch each point out
            # wide and squash it short, then fill the whole outline in. Twenty
            # four sides is plenty to look round.
            def draw_disc(fx, fy, field_radius, color):
                cx, cy = self.field_to_screen(fx, fy)
                t = fy / self.FIELD_H
                # How many screen pixels one table unit is across at this depth.
                across = (2 * self.half_width_at(t)) / self.FIELD_W
                rw = field_radius * across       # half the oval's width on screen
                rh = rw * self.DISC_SQUASH       # half its height, squashed by the slant
                points = []
                steps = 24
                for i in range(steps):
                    ang = (2 * math.pi) * i / steps
                    points.append((int(cx + rw * math.cos(ang)), int(cy + rh * math.sin(ang))))
                canvas.polygon(color, points)

            # Draw the three pieces from the back of the table to the front, so a
            # piece closer to us correctly overlaps one further away. A smaller
            # fy is further away, so sorting by fy puts the far ones first.
            pieces = [
                (self.opp_y, self.opp_x, self.MALLET_RADIUS, self.MALLET_COLOR),
                (self.py, self.px, self.PUCK_RADIUS, self.PUCK_COLOR),
                (self.player_y, self.player_x, self.MALLET_RADIUS, self.MALLET_COLOR),
            ]
            pieces.sort()
            for piece_fy, piece_fx, piece_radius, piece_color in pieces:
                draw_disc(piece_fx, piece_fy, piece_radius, piece_color)

            # DEBUG OVERLAY. When the developer switch is on, trace the field's
            # real walls, goal mouths and halfway line straight onto the table,
            # so you can check by eye that the picture's rails line up with where
            # the pieces actually bounce. Every line is built from the same field
            # corners the bouncing uses and run through the same tilt, so what you
            # see is exactly where the walls are, not a separate guess.
            if store.minigame_air_hockey_debug_boundaries:
                # The four corners of the play field, run through the tilt.
                far_left = self.field_to_screen(0, 0)
                far_right = self.field_to_screen(self.FIELD_W, 0)
                near_right = self.field_to_screen(self.FIELD_W, self.FIELD_H)
                near_left = self.field_to_screen(0, self.FIELD_H)

                # The two side walls in green. The puck bounces off these.
                stroke(far_left, near_left, "#00ff66")
                stroke(far_right, near_right, "#00ff66")

                # The far edge: solid rail in green to each side, the goal opening
                # in orange in the middle. The orange spans the goal's half width,
                # so it lands right on the red crease we drew. The puck bounces off
                # the green and scores through the orange.
                far_goal_left = self.field_to_screen(self.FIELD_W / 2 - self.FAR_GOAL_HALF, 0)
                far_goal_right = self.field_to_screen(self.FIELD_W / 2 + self.FAR_GOAL_HALF, 0)
                stroke(far_left, far_goal_left, "#00ff66")
                stroke(far_goal_left, far_goal_right, "#ff9900")
                stroke(far_goal_right, far_right, "#00ff66")

                # The near edge, the same split, the orange again landing on the
                # near crease.
                near_goal_left = self.field_to_screen(self.FIELD_W / 2 - self.NEAR_GOAL_HALF, self.FIELD_H)
                near_goal_right = self.field_to_screen(self.FIELD_W / 2 + self.NEAR_GOAL_HALF, self.FIELD_H)
                stroke(near_left, near_goal_left, "#00ff66")
                stroke(near_goal_left, near_goal_right, "#ff9900")
                stroke(near_goal_right, near_right, "#00ff66")

                # The halfway line in cyan. The opponent stays above it, the
                # player below it.
                stroke(self.field_to_screen(0, self.FIELD_H / 2),
                       self.field_to_screen(self.FIELD_W, self.FIELD_H / 2), "#00ccff")

            # Drop the finished layer of pieces onto the game.
            r.blit(disc_layer, (0, 0))

            # The "Click to Begin" prompt, shown only while the puck is waiting.
            if self.stuck:
                ctb = renpy.render(Fixed( self.ctb, xysize = ( config.screen_width, config.screen_height ) ), config.screen_width, config.screen_height, st, at)
                r.blit(ctb, (0, 0))

            # The developer cheat switches force a result for testing.
            if store.minigame_air_hockey_instant_lose_mode:
                self.winner = "opponent"
            if store.minigame_air_hockey_instant_win_mode:
                self.winner = "player"

            # If a goal went in, ask Ren'Py to run an event right away so the
            # click handler below notices the winner and ends the round.
            if self.winner:
                renpy.timeout(0)

            # Draw again as soon as possible so the puck keeps moving smoothly.
            renpy.redraw(self, 0)

            return r

        # Handles the mouse and touch input.
        def event(self, ev, x, y, st):
            import pygame

            # Turn where the mouse is pointing on the tilted table back into a
            # flat field point, then keep the player's mallet in our near half
            # and inside the walls. The player is not allowed to reach over the
            # halfway line, same as a real air hockey table.
            fx, fy = self.screen_to_field(x, y)
            fx = max(fx, self.MALLET_RADIUS)
            fx = min(fx, self.FIELD_W - self.MALLET_RADIUS)
            fy = max(fy, self.FIELD_H / 2 + self.MALLET_RADIUS)
            fy = min(fy, self.FIELD_H - self.MALLET_RADIUS)

            if renpy.mobile:
                # On a touch screen only drag the mallet while a finger is held.
                if pygame.mouse.get_pressed()[0]:
                    self.player_x = fx
                    self.player_y = fy
            else:
                self.player_x = fx
                self.player_y = fy

            # A click on a mouse, or lifting a finger on touch, serves the puck.
            if renpy.mobile:
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                    self.stuck = False
            else:
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

            # Once there is a winner, hand it back so the round can end.
            # Otherwise ignore the event and keep playing.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()


label minigame_air_hockey(partner = edna):
    $ minigame_air_hockey_partner = partner

    call process_new_location(minigame_air_hockey_partner.minigame_air_hockey_background())

    $ no_bust_art = False

    python:
        minigame_air_hockey_player_score = 0
        minigame_air_hockey_partner_score = 0
        # How many goals it takes to win the match. Three keeps a game short like
        # the other minigames; bump it to 7 if you want a full air hockey match.
        minigame_air_hockey_partner_win_threshold = 3

    $ minigame_air_hockey_instant_win_mode = False
    $ minigame_air_hockey_instant_lose_mode = False
    $ minigame_air_hockey_debug_boundaries = False
    if config.developer:
        "CONFIG/DEVELOPER MODE"
        menu:
            "Activate Instant Win Mode":
                $ minigame_air_hockey_instant_win_mode = True
            "Activate Instant Lose Mode":
                $ minigame_air_hockey_instant_lose_mode = True
            "Activate neither":
                pass
        menu:
            "Boundary overlay (debug)?"
            "Show where the walls and goals are drawn":
                $ minigame_air_hockey_debug_boundaries = True
            "Hide it":
                pass

    $ renpy.call(minigame_air_hockey_partner.minigame_air_hockey_greeting_label())

    window hide
    menu:
        "Easy":
            $ minigame_air_hockey_difficulty = "easy"
        "Medium (Boldness Opportunity!)":
            $ minigame_air_hockey_difficulty = "medium"
        "Hard (Boldness Opportunity!)":
            $ minigame_air_hockey_difficulty = "hard"

    $ renpy.call(minigame_air_hockey_partner.minigame_air_hockey_difficulty_response_label())

    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()

    show screen minigame_air_hockey_score_display

    jump minigame_air_hockey_round

    return

screen minigame_air_hockey_score_display:
    # Two things show the score. First, the scoreboard hanging from the rail at the
    # top has two dark panels either side of a centre divider, and we light each
    # side's score onto its own panel in red, the way a real scoreboard does: the
    # player on the left, the opponent on the right. The panel centres were measured
    # off the table picture, since the board is painted into it, so they hold at
    # 1920x1080. The numbers sit a few pixels right of those exact centres on
    # purpose: the font leaves a sliver of space on the right of a digit, so without
    # the nudge the number reads as sitting slightly left. Each score is padded to
    # two digits, so 1 shows as "01".
    text str(minigame_air_hockey_player_score).zfill(2) xcenter 902 ycenter 128 size 52 bold True color "#ff3b3b" outlines [ (2, "#ff000080", 0, 0) ]
    text str(minigame_air_hockey_partner_score).zfill(2) xcenter 1027 ycenter 128 size 52 bold True color "#ff3b3b" outlines [ (2, "#ff000080", 0, 0) ]

    # Second, each side's name and score sit in the top corners as plain labels, so
    # it stays clear which side belongs to the player and which to the opponent.
    text n.say_name + ": " + str(minigame_air_hockey_player_score) xalign 0.05 size 64
    text minigame_air_hockey_partner.say_name + ": " + str(minigame_air_hockey_partner_score) xalign 0.95 size 64

label minigame_air_hockey_round:
    window hide

    python:
        ui.add(AirHockey())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    window show None

    # Updating the score is all we do between rounds now. There used to be a "you
    # scored" / "they scored" line here, but it popped the dialogue box up every
    # round and broke the flow, so it's gone. The window is still shown just above
    # so the win and lose dialogue at the end of the match still appears.
    if winner == "opponent":
        $ minigame_air_hockey_partner_score += 1

    else:
        $ minigame_air_hockey_player_score += 1

    if minigame_air_hockey_player_score >= minigame_air_hockey_partner_win_threshold:
        jump minigame_air_hockey_win
    elif minigame_air_hockey_partner_score >= minigame_air_hockey_partner_win_threshold:
        jump minigame_air_hockey_lose
    else:
        jump minigame_air_hockey_round

    return

label minigame_air_hockey_lose:
    $ renpy.call(minigame_air_hockey_partner.minigame_air_hockey_difficulty_player_lost_label())

    jump minigame_air_hockey_end

    return

label minigame_air_hockey_win:
    $ renpy.scene('screens')
    show screen hud
    $ minigame_air_hockey_win_money = 4

    $ renpy.call(minigame_air_hockey_partner.minigame_air_hockey_difficulty_player_won_label())

    python hide:
        inventory.add_money(minigame_air_hockey_win_money, minigame = True)
        narrator("Got $" + str(minigame_air_hockey_win_money) + " for winning.")

    jump minigame_air_hockey_end

    return

label minigame_air_hockey_end:
    $ renpy.scene('screens')

    $ enable_saving()
    $ renpy.block_rollback()
    $ enable_rollback()

    call process_end_of_minigame("minigame_air_hockey")

    return
