# Air Hockey minigame - wiring and Grandma Edna's lines.
#
# The engine file (minigame_air_hockey.rpy) is the game itself. This file does
# three jobs, and it never edits a single base game file to do any of them:
#
#   1. It teaches every character how to host an air hockey game, by giving them
#      the plain answers the engine asks for: what colour to paint the mallet
#      and the puck, how big to draw them, what sound a hit makes, and the names
#      of the talking labels further down.
#
#   2. It adds the words "Air Hockey Minigame" to the minigame menu, and it lets
#      Grandma Edna offer the game from the same moment that already unlocked her
#      tennis game.
#
#   3. It holds Edna's spoken lines for the greeting, the difficulty choice, and
#      the win and the loss. THESE LINES ARE PLACEHOLDERS. They are here only so
#      the game runs all the way through. Rewrite them in your own voice.
#
# NO ART FILES NEEDED: the mallet and the puck are painted in code as plain
# round discs, so there is nothing to add to your images folder. The size
# numbers below set how big each disc is drawn (the mallet 120 across, the puck
# 70 across), and the colour answers below set what colour each one is. Change
# any of them to taste.


init 1 python:

    # This runs in the moment just after the base game has finished building its
    # characters, so the shared character type already exists for us to add to.
    #
    # The character we play against answers all of the questions below. We give
    # every character the same starting answers by adding these to IA_Actor, the
    # shared type that all the characters are built from. A single character can
    # answer differently later by being given their own version of one of these.

    # The background picture behind the pieces. This is the air hockey table
    # image. Put air_hockey_table.png in your mod's images folder so Ren'Py
    # registers the name "air_hockey_table", or define that image yourself.
    def minigame_air_hockey_background(self):
        return "air_hockey_table"
    IA_Actor.minigame_air_hockey_background = minigame_air_hockey_background

    # The sound a mallet makes when it strikes the puck. None means no sound.
    # Put a filename here, like "puck_hit.ogg", once you have one.
    def minigame_air_hockey_hit_sound(self):
        return None
    IA_Actor.minigame_air_hockey_hit_sound = minigame_air_hockey_hit_sound

    # How big across the mallet disc is, in the table's own units (the table is
    # 800 units wide). The engine also uses this to work out when the puck is
    # touching the mallet.
    def minigame_air_hockey_mallet_width(self):
        return 120
    IA_Actor.minigame_air_hockey_mallet_width = minigame_air_hockey_mallet_width

    # The same, for how big across the puck disc is.
    def minigame_air_hockey_puck_width(self):
        return 70
    IA_Actor.minigame_air_hockey_puck_width = minigame_air_hockey_puck_width

    # The colours the mallet and the puck are painted. The mallet is a strong red
    # so it reads as the striker you push, and the puck a near-black so it stands
    # out clearly on the blue table. Any Ren'Py colour works here, written as a
    # hex string like "#ffcc00".
    def minigame_air_hockey_mallet_color(self):
        return "#d23b3b"
    IA_Actor.minigame_air_hockey_mallet_color = minigame_air_hockey_mallet_color

    def minigame_air_hockey_puck_color(self):
        return "#10141a"
    IA_Actor.minigame_air_hockey_puck_color = minigame_air_hockey_puck_color

    # The names of the four talking labels for this game. Each name is built from
    # the character's own short name, so for Edna the greeting name comes out as
    # "edna_minigame_air_hockey_greeting", which matches the label written near
    # the bottom of this file. Any other character that hosts the game needs its
    # own set of four labels named in this same way.
    def minigame_air_hockey_greeting_label(self):
        return self.internal_name + "_minigame_air_hockey_greeting"
    IA_Actor.minigame_air_hockey_greeting_label = minigame_air_hockey_greeting_label

    def minigame_air_hockey_difficulty_response_label(self):
        return self.internal_name + "_minigame_air_hockey_difficulty_response"
    IA_Actor.minigame_air_hockey_difficulty_response_label = minigame_air_hockey_difficulty_response_label

    def minigame_air_hockey_difficulty_player_won_label(self):
        return self.internal_name + "_air_hockey_minigame_player_won_label"
    IA_Actor.minigame_air_hockey_difficulty_player_won_label = minigame_air_hockey_difficulty_player_won_label

    def minigame_air_hockey_difficulty_player_lost_label(self):
        return self.internal_name + "_air_hockey_minigame_player_lost_label"
    IA_Actor.minigame_air_hockey_difficulty_player_lost_label = minigame_air_hockey_difficulty_player_lost_label

    # The minigame menu shows a friendly name beside each game. The base game
    # keeps a list of those names but has never heard of air hockey. We swap in a
    # version that gives our name when it is asked about air hockey, and for every
    # other game simply asks the original version, exactly as before. Saving the
    # original first is what lets us still fall through to it.
    base_minigame_option_label = IA_Actor.minigame_option_label
    def minigame_option_label(self, call_label):
        if call_label == "minigame_air_hockey":
            return "Air Hockey Minigame"
        return base_minigame_option_label(self, call_label)
    IA_Actor.minigame_option_label = minigame_option_label

    # Which games a character offers in their menu. We let Edna offer air hockey
    # once the player has reached her minigame intro, which is the very same
    # unlock her tennis game already waits on. We keep every game she already
    # offered and add air hockey to the end of her list. To hand the game to a
    # different character instead, copy this short block onto them and change the
    # unlock name to whatever fits that character.
    base_edna_available_minigames = Edna.available_minigames
    def edna_available_minigames(self):
        games = base_edna_available_minigames(self)
        if "edna_scene_minigame_intro" in store.scenes_completed:
            games.extend(["minigame_air_hockey"])
        return games
    Edna.available_minigames = edna_available_minigames


# ----------------------------------------------------------------------------
# PLACEHOLDER LINES BELOW
#
# Everything from here down is Edna talking. It is written only so the game
# plays cleanly from the first hello to the final result. Replace all of it with
# your own writing.
#
# The shape to keep in each label is: first show the characters on screen with
# display_multiple_characters, then for every line set Edna's pose and face with
# process_character and give her the line right after. The poses she can stand in
# are handclasp, handhip and fisthip, and the faces she can make are happy,
# neutral, concerned and shock.
#
# The win label is the one place that also does bookkeeping: it hands out points
# and sets how much money the win is worth, and those amounts climb with the
# difficulty. Keep that part when you rewrite the words.
# ----------------------------------------------------------------------------

label edna_minigame_air_hockey_greeting:
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (edna, "outfit clothes pose handclasp face happy blush false") ])
    call process_character(edna, appearance = "pose handclasp face happy blush false")
    edna.c "I've got the table all warmed up for us."
    call process_character(edna, appearance = "pose handclasp face happy blush false")
    edna.c "Pick up a mallet and we'll play a few rounds!"

    return

label edna_minigame_air_hockey_difficulty_response:
    if minigame_air_hockey_difficulty == "easy":
        call process_character(edna, appearance = "pose handclasp face neutral blush false")
        edna.c "I'll keep my shots nice and gentle to start."
    elif minigame_air_hockey_difficulty == "medium":
        call process_character(edna, appearance = "pose handhip face neutral blush false")
        edna.c "I'll pick up the pace a little this time."
    else:
        call process_character(edna, appearance = "pose fisthip face neutral blush false")
        edna.c "No going easy on you now, [n.say_name]!"

    return

label edna_air_hockey_minigame_player_won_label:
    if minigame_air_hockey_difficulty == "easy":
        $ edna.add_points(2, minigame = True)
        $ minigame_air_hockey_win_money = 4
        $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose fisthip face neutral blush false") ])
        call process_character(edna, appearance = "pose fisthip face neutral blush false")
        edna.c "Nicely done. You're a natural at this!"
    elif minigame_air_hockey_difficulty == "medium":
        call add_points_and_boldness(edna, 3, 1, minigame = True)
        $ minigame_air_hockey_win_money = 6
        $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose handclasp face happy blush false") ])
        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "And the win goes to my grandson!"
    else:
        call add_points_and_boldness(edna, 4, 1, minigame = True)
        $ minigame_air_hockey_win_money = 8
        $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose fisthip face shock blush false") ])
        call process_character(edna, appearance = "pose fisthip face shock blush false")
        edna.c "You beat me fair and square, [n.say_name]!"

    return

label edna_air_hockey_minigame_player_lost_label:
    if minigame_air_hockey_difficulty == "easy":
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose handclasp face concerned blush false") ])
        call process_character(edna, appearance = "pose handclasp face concerned blush false")
        edna.c "So close! Keep your eye on the puck, [n.say_name]."
    elif minigame_air_hockey_difficulty == "medium":
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose handhip face neutral blush false") ])
        call process_character(edna, appearance = "pose handhip face neutral blush false")
        edna.c "Watch where my mallet sends it next time!"
    else:
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose fisthip face neutral blush false") ])
        call process_character(edna, appearance = "pose fisthip face neutral blush false")
        edna.c "Almost had it! Give it another go."

    return
