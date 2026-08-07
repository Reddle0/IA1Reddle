## Pong Minigame (Kacey) ##
init 100 python:
    def minigame_table_tennis_background(self):
        return "bg kacey_pong_field"

    Gloryhole_Girl.minigame_table_tennis_background = minigame_table_tennis_background

    def minigame_table_tennis_hit_sound(self):
        return "mods/leftovers_mod/audio/sounds/minigames/pong_boop.ogg"

    Gloryhole_Girl.minigame_table_tennis_hit_sound = minigame_table_tennis_hit_sound

#   def minigame_table_tennis_paddle_width(self):
#       return 8

#   def minigame_table_tennis_paddle_height(self):
#       return 160

#    def minigame_table_tennis_ball_width(self):
#        return 15

#    def minigame_table_tennis_ball_height(self):
#        return 23

    def minigame_table_tennis_ball_image(self):
        return "mods/leftovers_mod/images/pong_ball.png"

    Gloryhole_Girl.minigame_table_tennis_ball_image = minigame_table_tennis_ball_image

    def minigame_table_tennis_paddle_image(self):
       return "mods/leftovers_mod/images/pong_paddle.png"

    Gloryhole_Girl.minigame_table_tennis_paddle_image = minigame_table_tennis_paddle_image

#   def minigame_table_tennis_greeting_label(self):
#       return self.internal_name + "_minigame_table_tennis_greeting"

#   def minigame_table_tennis_difficulty_response_label(self):
#       return self.internal_name + "_minigame_table_tennis_difficulty_response"

#   def minigame_table_tennis_difficulty_player_won_label(self):
#       return self.internal_name + "_table_tennis_minigame_player_won_label"

#   def minigame_table_tennis_difficulty_player_lost_label(self):
#       return self.internal_name + "_table_tennis_minigame_player_lost_label"

label gloryhole_girl_minigame_table_tennis_greeting:
    $ diceroll = random.randint(1,3)

    if diceroll == 1:
        $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (gloryhole_girl, "outfit clothes pose handsfront face happy blush false") ])
        call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
        gloryhole_girl.c "Have you got everything, [n.say_name]?"
        call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
        gloryhole_girl.c "If so, let's head over to the arcade!"
    elif diceroll == 2:
        $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (gloryhole_girl, "outfit clothes pose handface face neutral blush false") ])
        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "We'll run out of quarters at this rate with these visits!"
        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "Hehe."
    else:
        $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (gloryhole_girl, "outfit clothes pose leaning face happy blush false") ])
        call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
        gloryhole_girl.c "You must play video games for hours [n.say_name]!"
        call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
        gloryhole_girl.c "I'm the same way!"

    return

label gloryhole_girl_minigame_table_tennis_difficulty_response:
    $ diceroll = random.randint(1,2)

    if minigame_table_tennis_difficulty == "easy":
        if diceroll == 1:
            call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
            gloryhole_girl.c "I'll go easy on you!"
            call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
            gloryhole_girl.c "These retro videogames are more slower-paced compared to what you're used to!"
        else:
            call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
            gloryhole_girl.c "Okay!"
            call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
            gloryhole_girl.c "Whenever you're ready, [n.say_name]!"
    elif minigame_table_tennis_difficulty == "medium":
        if diceroll == 1:
            call process_character(gloryhole_girl, appearance = "pose handhip face neutral blush false")
            gloryhole_girl.c "Always keep your eye out for the ball on the screen!"
            call process_character(gloryhole_girl, appearance = "pose handhip face neutral blush false")
            gloryhole_girl.c "Even when it's going really fast!"
        else:
            call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
            gloryhole_girl.c "I didn't realize how fun this could be until I started playing with you, [n.say_name]!"
            call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
            gloryhole_girl.c "I hope you keep coming back for more!"
    else:
        if diceroll == 1:
            call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
            gloryhole_girl.c "We'll end up making the controllers sweaty at this rate!"
        else:
            call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
            gloryhole_girl.c "Let's play like everything is at stake!"
            call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
            gloryhole_girl.c "That means I won't be going easy on you!"

    return

label gloryhole_girl_table_tennis_minigame_player_won_label:
    if minigame_table_tennis_difficulty == "easy":
        $ gloryhole_girl.add_points(2, minigame = True)
        $ minigame_table_tennis_win_money = 4
        $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (gloryhole_girl, "outfit clothes pose leaning face neutral blush false") ])
        call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
        gloryhole_girl.c "Next time, I won't go easy on you [n.say_name]!"
        call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
        gloryhole_girl.c "I hope you're ready for that!"
    elif minigame_table_tennis_difficulty == "medium":
        call add_points_and_boldness(gloryhole_girl, 3, 1, minigame = True)
        $ minigame_table_tennis_win_money = 6
        $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (gloryhole_girl, "outfit clothes pose handface face happy blush false") ])
        call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
        gloryhole_girl.c "Aww, I lost..."
    else:
        call add_points_and_boldness(gloryhole_girl, 4, 1, minigame = True)
        $ minigame_table_tennis_win_money = 8
        $ diceroll = random.randint(1,2)
        if diceroll == 1:
            $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (gloryhole_girl, "outfit clothes pose leaning face shock blush false") ])
            call process_character(gloryhole_girl, appearance = "pose leaning face shock blush false")
            gloryhole_girl.c "Wiped out..."
            call process_character(gloryhole_girl, appearance = "pose leaning face shock blush false")
            gloryhole_girl.c "Woah, I didn't stand a chance!"
        else:
            $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (gloryhole_girl, "outfit clothes pose handsfront face happy blush false") ])
            call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
            gloryhole_girl.c "And looks like we have a winner!"
            call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
            gloryhole_girl.c "Maybe retro videogames are your true calling!"

    return

label gloryhole_girl_table_tennis_minigame_player_lost_label:
    if minigame_table_tennis_difficulty == "easy":
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (gloryhole_girl, "outfit clothes pose handface face neutral blush false") ])
        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "Hehe, better luck next time [n.say_name]!"
    elif minigame_table_tennis_difficulty == "medium":
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (gloryhole_girl, "outfit clothes pose handsfront face neutral blush false") ])
        call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
        gloryhole_girl.c "Maybe these older videogames are too retro for you..."
        call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
        gloryhole_girl.c "Oh well!"
    else:
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (gloryhole_girl, "outfit clothes pose leaning face neutral blush false") ])
        call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
        gloryhole_girl.c "You almost had me there [n.say_name]!"
        call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
        gloryhole_girl.c "Keep at it!"

    return
