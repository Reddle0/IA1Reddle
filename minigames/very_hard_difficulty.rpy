# Very Hard Difficulty

# Self-explanatory, this keeps all of the "Very Hard" minigame overrides (and other things related to it) in one place
# A lot of this is overriding labels and methods, you can see where "Very Hard" fits into place
# For example, existing "Else" checks now apply to "Very Hard" instead of "Hard". 
# "Elif" checks are created for "Hard" to account for this, to preserve the original dialogue
# This file would also be too long to fit into minigame_tweaks (which it originally was), so it goes here

# "Very Hard" difficulty rewards 2x Boldness points (unique to Very Hard) 
# in addition to the relationship point increase from Hard

init 300 python:
    # labels to override
    # covers every label that has difficulty options, or modifiers
    # minigame_racing_start for example isn't covered, since that doesn't touch anything related to difficulty, but minigame_racing_result_very_hard does
    config.label_overrides["math_minigame_intro"] = "math_minigame_intro_very_hard"
    config.label_overrides["math_minigame_generate_question"] = "math_minigame_generate_question_very_hard"
    config.label_overrides["math_minigame_end"] = "math_minigame_end_very_hard"

    config.label_overrides["minigame_racing"] = "minigame_racing_very_hard"
    config.label_overrides["minigame_racing_result"] = "minigame_racing_result_very_hard"

    config.label_overrides["minigame_reading"] = "minigame_reading_very_hard"
    config.label_overrides["minigame_reading_won"] = "minigame_reading_won_very_hard"
    config.label_overrides["minigame_reading_lost"] = "minigame_reading_lost_very_hard"

    config.label_overrides["minigame_repeat_pattern"] = "minigame_repeat_pattern_very_hard"
    config.label_overrides["minigame_repeat_pattern_got_all_right"] = "minigame_repeat_pattern_got_all_right_very_hard"
    config.label_overrides["minigame_repeat_pattern_too_slow"] = "minigame_repeat_pattern_too_slow_very_hard"

    config.label_overrides["minigame_slide_puzzle_initialize"] = "minigame_slide_puzzle_initialize_very_hard"
    config.label_overrides["minigame_slide_puzzle_intro"] = "minigame_slide_puzzle_intro_very_hard"
    config.label_overrides["minigame_slide_puzzle_win"] = "minigame_slide_puzzle_win_very_hard"
    config.label_overrides["minigame_slide_puzzle_too_slow"] = "minigame_slide_puzzle_too_slow_very_hard"

    config.label_overrides["minigame_table_tennis"] = "minigame_table_tennis_very_hard"
    config.label_overrides["edna_minigame_table_tennis_difficulty_response"] = "edna_minigame_table_tennis_difficulty_response_very_hard"
    config.label_overrides["edna_table_tennis_minigame_player_won_label"] = "edna_table_tennis_minigame_player_won_label_very_hard"
    config.label_overrides["edna_table_tennis_minigame_player_lost_label"] = "edna_table_tennis_minigame_player_lost_label_very_hard"

    #config.label_overrides["minigame_typing_review_intro"] = "minigame_typing_review_intro_very_hard" # has new dialogue, but omitted due to "very hard" being unlocked, and not accessible at the start of minigames
    config.label_overrides["minigame_typing_review_set_lines"] = "minigame_typing_review_set_lines_very_hard"
    config.label_overrides["minigame_typing_review_result"] = "minigame_typing_review_result_very_hard"

#################
# math minigame #
#################
label math_minigame_intro_very_hard:
    python:
        random_line = random.randint(1, 3)

    if random_line == 1:
        $ display_multiple_characters([ (n, ""), (sa, "pose leaning face neutral") ], reset = True)
        call process_character(sa, appearance = "pose leaning face neutral", text = "I bet you'll want a challenge!")
    elif random_line == 2:
        $ display_multiple_characters([ (n, ""), (sa, "pose handsbehind face neutral") ], reset = True)
        call process_character(sa, appearance = "pose handsbehind face neutral", text = "Alright, how hard do you want these questions to be?")
    else:
        $ display_multiple_characters([ (n, ""), (sa, "pose handface face neutral") ], reset = True)
        call process_character(sa, appearance = "pose handsbehind face neutral", text = "Let's crunch some numbers!")

    menu:
        "Go easy on me.":
            $ math_difficulty = "easy"
            $ math_timer = 8
            call process_character(sa, appearance = "pose handsbehind face neutral", text = "Try answering the math questions as fast as you can!")
        "Let me try the harder ones. (Boldness Opportunity)":
            call process_character(sa, appearance = "pose handsbehind face neutral", text = "These should level up your math skills!")
            $ math_difficulty = "medium"
            $ math_timer = 10
        "Give me all you've got. (Boldness Opportunity)":
            call process_character(sa, appearance = "pose handsbehind face neutral", text = "These are tough, even for me!")
            $ math_difficulty = "hard"
            $ math_timer = 12
        # very hard 
        # new dialogue for sam
        "Hit me with the brutal stuff! (Double Boldness Opportunity)":
            call process_character(sa, appearance = "pose leaning face neutral", text = "These are the spiciest of the spiciest!")
            call process_character(sa, appearance = "pose leaning face happy", text = "Don't say I didn't warn you!")
            $ math_difficulty = "very hard"
            $ math_timer = 14
            $ math_max_tries = 5

    if config.developer:
        $ math_timer = 999

    $ disable_saving()

    return

label math_minigame_generate_question_new:
    python:
        math_current_tries += 1

    if math_difficulty == "easy":
        call math_minigame_generate_question_easy
    elif math_difficulty == "medium":
        call math_minigame_generate_question_medium
    elif math_difficulty == "hard":
        call math_minigame_generate_question_hard
    else:
        # very hard is now the "else" result, instead of "hard"
        call math_minigame_generate_question_very_hard

    call math_minigame_round

    return

label math_minigame_generate_question_very_hard:
    python:
        # no division
        math_question_type_id = random.randint(1, 5)

    if math_question_type_id == 1:
        call math_minigame_generate_question_simple_operation(minimum = -250, maximum = 250, operator_choices = ["+"], operand_num = 3, number_exclusions = [0])
    elif math_question_type_id == 2:
        call math_minigame_generate_question_simple_operation(minimum = -200, maximum = 250, operator_choices = ["-"], operand_num = 3, number_exclusions = [0])
    elif math_question_type_id == 3:
        call math_minigame_generate_question_simple_operation(minimum = -12, maximum = 15, operator_choices = ["*"], operand_num = 2, number_exclusions = [0, 1])
    elif math_question_type_id == 4:
        call math_minigame_generate_question_simple_operation(minimum = -15, maximum = 60, operator_choices = ["/"], operand_num = 2, number_exclusions = [0, 1, 10], decimal_offset = True, prevent_same_operand = True)
    else:
        call math_minigame_generate_question_simple_operation(minimum = -20, maximum = 20, operator_choices = ["+", "-", "*"], operand_num = 3, number_exclusions = [0])

    return

label math_minigame_end_very_hard:
    $ enable_saving()

    if math_difficulty == "easy":
        if math_current_points >= math_max_tries:
            $ sa.add_points(2, minigame = True)

            show screen hud
            python hide:
                win_money = 4
                inventory.add_money(win_money, minigame = True)
                narrator("Got $" + str(win_money) + " for winning.")

        elif math_current_points >= math_max_tries - 2:
            $ sa.add_points(1, minigame = True)

            show screen hud
            python hide:
                win_money = 2
                inventory.add_money(win_money, minigame = True)
                narrator("Got $" + str(win_money) + " for winning.")

    elif math_difficulty == "medium":
        if math_current_points >= math_max_tries:
            call add_points_and_boldness(sa, 3, 1, minigame = True)

            show screen hud
            python hide:
                win_money = 6
                inventory.add_money(win_money, minigame = True)
                narrator("Got $" + str(win_money) + " for winning.")

        elif math_current_points >= math_max_tries - 2:
            $ sa.add_points(2)

            show screen hud
            python hide:
                win_money = 4
                inventory.add_money(win_money, minigame = True)
                narrator("Got $" + str(win_money) + " for winning.")

    # elif check for hard
    elif math_difficulty == "hard":
        if math_current_points >= math_max_tries:
            call add_points_and_boldness(sa, 4, 1, minigame = True)

            show screen hud
            python hide:
                win_money = 8
                inventory.add_money(win_money, minigame = True)
                narrator("Got $" + str(win_money) + " for winning.")

        elif math_current_points >= math_max_tries - 2:
            $ sa.add_points(3, minigame = True)

            show screen hud
            python hide:
                win_money = 6
                inventory.add_money(win_money, minigame = True)
                narrator("Got $" + str(win_money) + " for winning.")
    # elif check for very hard
    elif math_difficulty == "very hard":
        if math_current_points >= math_max_tries:
            # 2x boldness for very hard
            call add_points_and_boldness(sa, 5, 2, minigame = True)

            show screen hud
            python hide:
                win_money = 10
                inventory.add_money(win_money, minigame = True)
                narrator("Got $" + str(win_money) + " for winning.")

        elif math_current_points >= math_max_tries - 2:
            # you still get 1 boldness point here on very hard, even if you don't do perfectly
            call add_points_and_boldness(sa, 4, 1, minigame = True)

            show screen hud
            python hide:
                win_money = 8
                inventory.add_money(win_money, minigame = True)
                narrator("Got $" + str(win_money) + " for winning.")

    if math_current_points >= math_max_tries:
        # inserted if checks for hard and very hard here
        # the original check didnt have them, but i wanted new dialogue to play for very hard
        if math_difficulty == "hard":
            call process_character(sa, appearance = "pose leaning face happy", text = "Wow! You made that look easy!")
        # very hard
        if math_difficulty == "very hard":
            # new dialogue, nate aces it
            call process_character(sa, appearance = "pose leaning face happy", text = "Man, you crushed that!")
        else:
            call process_character(sa, appearance = "pose leaning face happy", text = "We're so gonna get top marks in school, [n.say_name]!")
    # original dialogue
    elif math_current_points >= math_max_tries - 2:
        call process_character(sa, appearance = "pose leaning face neutral", text = "Pretty good [n.say_name]!")
    else:
        call process_character(sa, appearance = "pose handface face concerned", text = "Maybe we could try again sometime.")

    $ renpy.block_rollback()
    $ enable_rollback()
    hide screen minigame_math_points
    call process_end_of_minigame("minigame_math")

    return

###################
# racing minigame #
###################
label minigame_racing_very_hard(partner = k):
    $ renpy.scene('screens')
    $ no_bust_art = False
    $ diceroll = random.randint(1,3)
    $ minigame_racing_partner = partner
    $ exec("minigame_racing_forced_" + partner.internal_name + "_face = \"\"")

    if partner != janet and partner.outfit != "clothes":
        call character_leave_dissolve(partner)
        $ renpy.pause(1)

    if partner == k:
        if diceroll == 1:
            call process_conversation_beginning([ (n, "outfit clothesjacket"), (k, "outfit clothes pose armcross face neutral") ])
            call process_character(k, appearance = "pose armcross face neutral", text = "So you want to race huh?")
            call process_character(k, appearance = "pose armcross face neutral", text = "Alright, let's head out.")
        elif diceroll == 2:
            call process_conversation_beginning([ (n, "outfit clothesjacket"), (k, "outfit clothes pose armcross face neutral") ])
            call process_character(k, appearance = "pose armcross face neutral", text = "Let's see how well you do this time.")
        else:
            call process_conversation_beginning([ (n, "outfit clothesjacket"), (k, "outfit clothes pose armsup face neutral") ])
            call process_character(k, appearance = "pose armsup face neutral", text = "Today's as good as any for some running!")

        $ play_music("audio/music/Fashion.ogg", fadeout=1.0, fadein = 1.0)
        call process_new_location("bg racing_track", char_tuple_array = [ (n, "outfit clothesjacket"), (k, "outfit clothes") ])
    elif partner == janet:
        if diceroll == 1:
            $ display_multiple_characters([ (n, "outfit clothesjacket"), (janet, "outfit clothes pose handface face neutral blush false") ])
            call process_character(janet, appearance = "pose handface face neutral blush false", text = "Nothing beats a refreshing swim!")
            call process_character(janet, appearance = "pose handface face neutral blush false", text = "I'm ready when you are!")
        elif diceroll == 2:
            $ display_multiple_characters([ (n, "outfit clothesjacket"), (janet, "outfit clothes pose handchest face happy blush false") ])
            call process_character(janet, appearance = "pose handchest face happy blush false", text = "I like the front crawl stroke when swimming.")
            call process_character(janet, appearance = "pose handchest face happy blush false", text = "I feel like I can glide through the waves with ease when doing that technique!")
        else:
            $ display_multiple_characters([ (n, "outfit clothesjacket"), (janet, "outfit clothes pose handhips face happy blush false") ])
            call process_character(janet, appearance = "pose handhips face happy blush false", text = "You'll turn into a fish with all the swimming you'll be doing!")

        $ play_music("audio/music/Fashion.ogg", fadeout=1.0, fadein = 1.0)
        call process_new_location("bg swimming_minigame", char_tuple_array = [ (n, "outfit swimsuit"), (janet, "outfit swimsuit") ])

    python:
        minigame_racing_press_multiplier = 1.0
        minigame_racing_update_speed = 0.2
        minigame_racing_finished = False
        minigame_racing_started = False
        minigame_racing_finish_x = 1900
        minigame_racing_difficulty = "easy"
        minigame_racing_forced_nate_face = None
        minigame_racing_forced_kira_face = None
        minigame_racing_win_lose_big_threshold = .30
        minigame_racing_player_boost = minigame_racing_player_boost_amount() + 1
        minigame_racing_textbutton_clicked = False
        minigame_racing_bet_amount = 0

        minigame_racing_system_message = ""
        minigame_racing_button_index = 0
        minigame_racing_buttons_to_press = []
        minigame_racing_buttons_objs = []
        minigame_racing_button_to_press = ""
        minigame_racing_prompt_prefix = "Mash"

    if partner == k:
        menu:
            "Easy":
                call process_character(k, appearance = "pose handhip face curious", text = "I'll practically have to walk to make it this easy!")
                call minigame_racing_easy_settings
            "Medium (Boldness Opportunity)":
                call process_character(k, appearance = "pose handhip face neutral", text = "Stepping up your game, not bad.")
                call minigame_racing_medium_settings
            "Hard (Boldness Opportunity)":
                call process_character(k, appearance = "pose armsup face happy", text = "Heh, alright [n.say_name].")
                call process_character(k, appearance = "pose armsup face happy", text = "You ask for a challenge, I'll deliver!")
                call minigame_racing_hard_settings
            # very hard
            # new dialogue for kira
            "Very Hard (Double Boldness Opportunity)":
                call process_character(k, appearance = "pose armsup face happy", text = "Now we're talking.")
                call process_character(k, appearance = "pose armsup face happy", text = "Don't complain when I leave you in the dust!")
                call minigame_racing_very_hard_settings
    elif partner == janet:
        menu:
            "Easy":
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character(janet, appearance = "pose handchest face neutral blush false", text = "I'll just kick with my feet.")
                    call process_character(janet, appearance = "pose handchest face neutral blush false", text = "That should keep my pace slow and steady.")
                else:
                    call process_character(janet, appearance = "pose handhips face neutral blush false", text = "Even going slower, this is still a top notch way to exercise!")

                call minigame_racing_easy_settings
            "Medium (Boldness Opportunity)":
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character(janet, appearance = "pose handchest face neutral blush false", text = "This is the usual pace I go at.")
                else:
                    call process_character(janet, appearance = "pose handface face neutral blush false", text = "Hope our splashing won't attract the sharks!")
                    call process_character(janet, appearance = "pose handface face happy blush false", text = "I'm just kidding!")
                    call process_character(janet, appearance = "pose handface face happy blush false", text = "They aren't around here!")

                call minigame_racing_medium_settings
            "Hard (Boldness Opportunity)":
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character(janet, appearance = "pose handface face neutral blush false", text = "Our arms will feel like lead after we're done!")
                else:
                    call process_character(janet, appearance = "pose handhips face happy blush false", text = "You seem to have some of your older sister's competitive spirit!")

                call minigame_racing_hard_settings
            # very hard
            # new dialogue for janet
            "Very Hard (Double Boldness Opportunity)":
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character(janet, appearance = "pose handface face happy blush false", text = "Oh, you want to race me at full pace?")
                    call process_character(janet, appearance = "pose handface face happy blush false", text = "Then let's make some waves!")
                else:
                    call process_character(janet, appearance = "pose handchest face happy blush false", text = "This one will leave your shoulders burning!")

                call minigame_racing_very_hard_settings

    if partner == k:
        if store.inventory.money >= 2:
            show screen hud
            window hide
            menu:
                "Don't bet anything":
                    pass
                "Bet $2" if store.inventory.money >= 2:
                    $ minigame_racing_bet_amount = 2
                "Bet $3" if store.inventory.money >= 3:
                    $ minigame_racing_bet_amount = 3
                "Bet $4" if store.inventory.money >= 4 and minigame_racing_difficulty != "easy":
                    $ minigame_racing_bet_amount = 4
                # make it so you can bet $5 on "very hard" still
                "Bet $5" if store.inventory.money >= 5 and (minigame_racing_difficulty == "hard" or minigame_racing_difficulty == "very hard"):
                    $ minigame_racing_bet_amount = 5
                # bet $6 is exclusive to "very hard"
                "Bet $6" if store.inventory.money >= 6 and minigame_racing_difficulty == "very hard":
                    $ minigame_racing_bet_amount = 6

            window hide
            if minigame_racing_bet_amount > 0:
                pause 0.75
                $ inventory.add_money(-minigame_racing_bet_amount)
                pause 1.75

            hide screen hud

    python:
        #minigame_racing_total_kira_distance = minigame_racing_finish_x - minigame_racing_kira_x
        #minigame_racing_kira_step_amount = math.ceil( ( minigame_racing_total_kira_distance/minigame_racing_desired_kira_finish_duration ) * minigame_racing_update_speed )
        #minigame_racing_kira_step_amount = int(minigame_racing_kira_step_amount)

        clear_characters()
        quick_menu = False
        generate_racing_button_presses()
        set_current_racing_button_obj()

    window hide
    $ disable_rollback()
    $ disable_saving()
    show screen minigame_racing(partner)
    call minigame_countdown(2.99, "minigame_racing_start", xalign = 0.5, yalign = 0.5, show_decimal = False, call_instead_of_show = True, addend = 1, red_text = False)

    return

label minigame_racing_very_hard_settings:
    python:
        minigame_racing_press_multiplier = 0.90
        minigame_racing_difficulty = "very hard"
        minigame_racing_desired_kira_finish_duration = 135 # added 45, to match the easy and medium difference
        minigame_racing_kira_step_amount = 9

        minigame_racing_player_x = 200 # player is further behind by 40
        minigame_racing_kira_x = 560 # kira is much further ahead

    return

init 200 python:
    def generate_racing_button_presses():
        if store.minigame_racing_difficulty == "easy":
            generate_easy_racing_button_presses()
        elif store.minigame_racing_difficulty == "medium":
            generate_medium_racing_button_presses()
        # elif check for hard
        elif store.minigame_racing_difficulty == "hard":
            generate_hard_racing_button_presses()
        # very hard is the else check
        else:
            generate_very_hard_racing_button_presses()

        return

    # very hard is always 3 button combos minimum, sometimes can even be 4
    def generate_very_hard_racing_button_presses():
        store.minigame_racing_buttons_objs = []

        # 3 = each combo has 3 buttons to press
        # 5 / 6 = generate 5 or 6 of those combos 
        # bumped up to 6 to make it more challenging, unique to very hard
        # no single button presses either, only multiple
        store.minigame_racing_buttons_objs.extend( generate_multiple_button_presses(3, 6))
        # 4 button, 5 combos to press
        store.minigame_racing_buttons_objs.extend( generate_multiple_button_presses(4, 5) )

        random.shuffle(store.minigame_racing_buttons_objs)

        return

label minigame_racing_result_very_hard(won = False):
    hide screen minigame_racing_button_prompts
    call minigame_stopwatch_stop
    $ minigame_racing_finished = True
    $ enable_saving()

    if won:
        if minigame_racing_partner == k:
            if minigame_racing_difficulty == "easy":
                call add_points(k, 2, minigame = True)
            elif minigame_racing_difficulty == "medium":
                call add_points_and_boldness(k, 3, 1, minigame = True)
            elif minigame_racing_difficulty == "hard":
                call add_points_and_boldness(k, 4, 1, minigame = True)
            # very hard is the else check
            else:
                # 2x boldness
                call add_points_and_boldness(k, 5, 2, minigame = True)

            if minigame_racing_difficulty == "easy" or minigame_racing_difficulty == "medium":
                if minigame_racing_player_x > int(minigame_racing_kira_x + (minigame_racing_kira_x * minigame_racing_win_lose_big_threshold)):
                    $ minigame_racing_forced_kira_face = "_Curious"
                    call process_character(k, appearance = "", text = "I shouldn't have gone so easy on you!")
                else:
                    $ minigame_racing_forced_kira_face = "_Happy"
                    call process_character(k, appearance = "", text = "That's it, yeah!")
            # "hard" is now an elif check
            elif minigame_racing_difficulty == "hard":
                if minigame_racing_player_x > int(minigame_racing_kira_x + (minigame_racing_kira_x * minigame_racing_win_lose_big_threshold)):
                    $ minigame_racing_forced_kira_face = "_Happy"
                    call process_character(k, appearance = "", text = "(Looks like my little bro has more tenacity than I thought)")
                else:
                    $ minigame_racing_forced_kira_face = "_Neutral"
                    call process_character(k, appearance = "", text = "(Well whaddya know...)")
            # "very hard" is now the else check
            # new dialogue for kira
            else:
                if minigame_racing_player_x > int(minigame_racing_kira_x + (minigame_racing_kira_x * minigame_racing_win_lose_big_threshold)):
                    $ minigame_racing_forced_kira_face = "_Embarrassed"
                    call process_character(k, appearance = "", text = "(Holy shit, that was impressive)")
                else:
                    $ minigame_racing_forced_kira_face = "_Embarrassed"
                    call process_character(k, appearance = "", text = "(Maybe [n.say_name] should try out for the Olympics too)")

            if minigame_racing_bet_amount > 0:
                show screen hud
                window hide
                pause 0.5
                $ inventory.add_money(minigame_racing_bet_amount * 2, minigame = True)
                pause 1.5

        elif minigame_racing_partner == janet:
            if minigame_racing_difficulty == "easy":
                $ minigame_racing_reward = 4
                call process_character(janet, appearance = "pose handface face happy blush false", text = "I shouldn't have gone as slow as I did!")
                call process_character(janet, appearance = "pose handface face happy blush false", text = "You kept up with ease!")
                call add_points_and_boldness(janet, 2, 1, minigame = True)
            elif minigame_racing_difficulty == "medium":
                $ minigame_racing_reward = 6
                call process_character(janet, appearance = "pose handhips face happy blush false", text = "My nephew is quite the swimmer!")
                call add_points_and_boldness(janet, 3, 1, minigame = True)
            # "hard" is now an elif check
            elif minigame_racing_difficulty == "hard":
                $ minigame_racing_reward = 8
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character(janet, appearance = "pose handface face happy blush false", text = "I think you're part dolphin!")
                    call process_character(janet, appearance = "pose handface face happy blush false", text = "That's the only way to explain your speed!")
                else:
                    call process_character(janet, appearance = "pose handchest face happy blush false", text = "If I could swim like that when I was your age...")
                    call process_character(janet, appearance = "pose handchest face happy blush false", text = "I'd have a rack of trophies!")

                call add_points_and_boldness(janet, 4, 1, minigame = True)
            # "very hard" is now the else check
            # new dialogue for janet
            else:
                $ minigame_racing_reward = 10
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character(janet, appearance = "pose handface face happy blush false", text = "You were flying through that water!")
                    call process_character(janet, appearance = "pose handface face happy blush false", text = "I could barely keep up with you!")
                else:
                    call process_character(janet, appearance = "pose handhips face happy blush false", text = "That was a proper race!")
                    call process_character(janet, appearance = "pose handhips face happy blush false", text = "You've built up some serious stamina!")

                # 2x boldness
                call add_points_and_boldness(janet, 5, 2, minigame = True)

            show screen hud
            window hide
            pause 0.5
            $ inventory.add_money(minigame_racing_reward, minigame = True)
            pause 1.5
    else:
        if minigame_racing_partner == k:
            if minigame_racing_kira_x > int(minigame_racing_player_x + (minigame_racing_player_x * minigame_racing_win_lose_big_threshold)):
                $ minigame_racing_forced_kira_face = "_Curious"
                # default lose dialogue
                call process_character(k, appearance = "", text = "What was that?")
                call process_character(k, appearance = "", text = "I know you're more capable.")
            else:
                # very hard dialogue, unique
                if minigame_racing_difficulty == "very hard":
                    $ minigame_racing_forced_kira_face = "_Curious"
                    call process_character(k, appearance = "", text = "That was close.")
                    call process_character(k, appearance = "", text = "You're getting tougher to beat.")
                else:
                    # original loss "else" dialogue
                    $ minigame_racing_forced_kira_face = "_Neutral"
                    call process_character(k, appearance = "", text = "That was close [n.say_name]!")
                    call process_character(k, appearance = "", text = "Just have to push hard during that final stretch!")
        elif minigame_racing_partner == janet:
            if minigame_racing_difficulty == "easy":
                call process_character(janet, appearance = "pose handface face concerned blush false", text = "Did you pass out part of the way?")
            elif minigame_racing_difficulty == "medium":
                call process_character(janet, appearance = "pose handhips face neutral blush false", text = "Don't get pulled out by the current!")
            elif minigame_racing_difficulty == "hard":
                call process_character(janet, appearance = "pose handchest face neutral blush false", text = "Hey, you tried!")
                call process_character(janet, appearance = "pose handchest face neutral blush false", text = "I get wiped out going this fast too!")
            else:
                # very hard
                # new dialogue for janet
                call process_character(janet, appearance = "pose handface face neutral blush false", text = "That pace is no joke!")
                call process_character(janet, appearance = "pose handface face neutral blush false", text = "You'll feel that one tomorrow!")

    $ renpy.block_rollback()
    $ enable_rollback()
    $ quick_menu = True

    $ renpy.scene('screens')
    call process_end_of_minigame("minigame_racing")
    return

####################
# reading minigame #
####################
init 300 python:
    # inherits all from the original MinigameGaugeDisplayable class
    class MinigameGaugeDisplayable_Very_Hard(MinigameGaugeDisplayable):

        def __init__(self, difficulty = "easy", lose_label = None):
            MinigameGaugeDisplayable.__init__(self)

            self.difficulty = difficulty
            self.lose_label = lose_label

            # difficulty
            # originally included just the very hard if check
            # but other difficulties were not working as intended (i.e "hard" only needing 6 hits)
            # so i've made sure the other difficulty values are here to avoid that
            if self.difficulty == "easy":
                self.dial_speed = 600
                self.DIAL_MAX_SPEED = 800
                self.hits_to_win = 6
                self.minigame_duration = 12
                self.SWEET_SPOT_MINIMUM_HEIGHT = 125
            elif self.difficulty == "medium":
                self.dial_speed = 650
                self.DIAL_MAX_SPEED = 900
                self.hits_to_win = 7
                self.minigame_duration = 12
                self.SWEET_SPOT_MINIMUM_HEIGHT = 100
            elif self.difficulty == "hard":
                self.dial_speed = 700
                self.DIAL_MAX_SPEED = 950
                self.hits_to_win = 8
                self.minigame_duration = 15
                self.SWEET_SPOT_MINIMUM_HEIGHT = 90
            else:
                self.dial_speed = 800 # good luck
                self.DIAL_MAX_SPEED = 1050 # bumped up by 100 to match the difference between easy and medium
                self.hits_to_win = 12 # double that of easy
                self.minigame_duration = 9 # reduced by 6, less time than easy/medium
                self.SWEET_SPOT_MINIMUM_HEIGHT = 75 # lowest sweet spot

            # "Dictionary" minigame booster, same as base
            # just in case it needs it
            if store.inventory.has_item(11):
                self.SWEET_SPOT_MINIMUM_HEIGHT += 50
                self.hits_to_win -= 1
                self.dial_speed -= 50
                self.DIAL_MAX_SPEED -= 100
                self.minigame_duration += 5

label minigame_reading_very_hard(partner = None):
    $ renpy.scene('screens')
    $ diceroll = random.randint(1,3)

    if diceroll == 1:
        $ display_multiple_characters([ (n, ""), (julia, "pose handface face neutral blush false") ], reset = True)
        call process_character(julia, appearance = "pose handface face neutral blush false", text = "I couldn't put down this most recent book.")
        call process_character(julia, appearance = "pose handface face neutral blush false", text = "Maybe you'll like it too.")
    elif diceroll == 2:
        $ display_multiple_characters([ (n, ""), (julia, "pose handup face happy blush false") ], reset = True)
        call process_character(julia, appearance = "pose handup face happy blush false", text = "A dictionary will come in handy for some of these books [n.say_name].")
    else:
        $ display_multiple_characters([ (n, ""), (julia, "pose handup face happy blush false") ], reset = True)
        call process_character(julia, appearance = "pose handup face happy blush false", text = "I'm only picking out the best page turners!")

    $ diceroll = random.randint(1,2)
    menu:
        "Easy":
            $ minigame_reading_difficulty = "easy"
            if diceroll == 1:
                call process_character(julia, appearance = "pose handface face neutral blush false", text = "Lighter fare huh?")
                call process_character(julia, appearance = "pose handface face neutral blush false", text = "I don't blame you.")
            else:
                call process_character(julia, appearance = "pose handface face happy blush false", text = "I blew through that book in one day.")
        "Medium (Boldness Opportunity)":
            $ minigame_reading_difficulty = "medium"
            if diceroll == 1:
                call process_character(julia, appearance = "pose handup face neutral blush false", text = "Not a bad choice.")
            else:
                call process_character(julia, appearance = "pose handup face neutral blush false", text = "There's a solid story in that one.")
        "Hard (Boldness Opportunity)":
            $ minigame_reading_difficulty = "hard"
            if diceroll == 1:
                call process_character(julia, appearance = "pose armcross face neutral blush false", text = "Good luck on that one.")
                call process_character(julia, appearance = "pose armcross face neutral blush false", text = "That has at least five different plotlines.")
            else:
                call process_character(julia, appearance = "pose armcross face neutral blush false", text = "You sure you want to read that one?")
                call process_character(julia, appearance = "pose armcross face neutral blush false", text = "Hats off to you if you can remember it all!")
        # self-explanatory, new dialogue for julia
        "Very Hard (Double Boldness Opportunity)":
            $ minigame_reading_difficulty = "very hard"
            if diceroll == 1:
                call process_character(julia, appearance = "pose armcross face happy blush false", text = "Even I got lost with that one.")
                call process_character(julia, appearance = "pose armcross face happy blush false", text = "Let's see if your brain survives it.")
            else:
                call process_character(julia, appearance = "pose handup face neutral blush false", text = "That book jumps all over the place.")
                call process_character(julia, appearance = "pose handup face neutral blush false", text = "If you keep up with it, I'll be impressed.")

    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()
    window hide

    python:
        # old class
        #ui.add(MinigameGaugeDisplayable(difficulty = minigame_reading_difficulty, lose_label = "minigame_reading_lost"))
        #won = ui.interact(suppress_overlay=True, suppress_underlay=True)
        # new class
        ui.add(MinigameGaugeDisplayable_Very_Hard(difficulty = minigame_reading_difficulty, lose_label = "minigame_reading_lost"))
        won = ui.interact(suppress_overlay=True, suppress_underlay=True)

    # calls the new very hard label override
    call minigame_reading_won_very_hard

    return

label minigame_reading_won_very_hard:
    $ diceroll = random.randint(1,4)

    pause 1.0

    $ display_multiple_characters([ (n, "pose handfist face happy blush false"), (julia, "") ], reset = True)

    $ minigame_reading_money = 0

    if minigame_reading_difficulty == "easy":
        call process_character(julia, appearance = "pose handup face happy blush false", text = "Looks like you do have some reading comprehension.")
        $ julia.add_points(2, minigame = True)
        $ minigame_reading_money = 4
    elif minigame_reading_difficulty == "medium":
        call process_character(julia, appearance = "pose armcross face happy blush false", text = "I'm already hearing some new vocabulary from you!")
        call add_points_and_boldness(julia, 3, 1, minigame = True)
        $ minigame_reading_money = 6
    # elif check for hard
    elif minigame_reading_difficulty == "hard":
        call process_character(julia, appearance = "pose handup face happy blush false", text = "I think you got smarter after reading that book!")
        call add_points_and_boldness(julia, 4, 1, minigame = True)
        $ minigame_reading_money = 8
    # "very hard" is now the else check
    else:
        call process_character(julia, appearance = "pose armcross face happy blush false", text = "Okay, yeah, that was impressive.")
        call process_character(julia, appearance = "pose armcross face happy blush false", text = "You kept track of all of that somehow.")
        # 2x boldness
        call add_points_and_boldness(julia, 5, 2, minigame = True)
        $ minigame_reading_money = 10

    show screen hud
    python hide:
        inventory.add_money(minigame_reading_money, minigame = True)
        narrator("Got $" + str(minigame_reading_money) + " for winning.")

    call minigame_reading_end
    return

label minigame_reading_lost_very_hard:
    $ diceroll = random.randint(1,4)

    pause 1.0
    $ display_multiple_characters([ (n, "pose behindhead face curious blush false"), (julia, "") ], reset = True)
    pause 0.5

    if minigame_reading_difficulty == "easy":
        call process_character(julia, appearance = "pose handface face concerned blush false", text = "Wow, [n.say_name]...")
        call process_character(julia, appearance = "pose handface face concerned blush false", text = "I think you'll need some tutoring.")
    # new "elif" dialogue for "very hard"
    # julia doesn't pity you, she understands if you fail
    elif minigame_reading_difficulty == "very hard":
        call process_character(julia, appearance = "pose armcross face neutral blush false", text = "That one's tough to follow.")
        call process_character(julia, appearance = "pose armcross face neutral blush false", text = "Don't worry, most people would get lost in it too.")
    else:
        call process_character(julia, appearance = "pose armcross face neutral blush false", text = "I'd do a second read through if I were you.")

    call minigame_reading_end

    return

###########################
# repeat pattern minigame #
###########################
label minigame_repeat_pattern_very_hard(partner = None):
    $ renpy.scene('screens')
    $ no_bust_art = False

    if partner:
        $ minigame_repeat_pattern_partner = partner
    else:
        $ minigame_repeat_pattern_partner = si

    if minigame_repeat_pattern_partner == si:
        $ diceroll = random.randint(1,2)

        if diceroll == 1:
            $ display_multiple_characters([ (n, ""), (si, "pose handsup") ], reset = True)
            call process_character(si, appearance = "pose handsup", text = "I just finished one.")
            call process_character(si, appearance = "pose handsup", text = "You should give it a try.")
        elif diceroll == 2:
            $ display_multiple_characters([ (n, ""), (si, "pose handsfront face neutral") ], reset = True)
            call process_character(si, appearance = "pose handsfront face neutral", text = "Your young brain can handle these.")
            call process_character(si, appearance = "pose handsfront face happy", text = "Unlike your mom here!")

    menu:
        "Easy":
            $ minigame_repeat_pattern_difficulty = "easy"
            $ minigame_repeat_pattern_number_of_buttons_to_match = 4
        "Medium (Boldness Opportunity)":
            $ minigame_repeat_pattern_difficulty = "medium"
            $ minigame_countdown_duration = 45
            $ minigame_repeat_pattern_number_of_buttons_to_match = 5
        "Hard (Boldness Opportunity)":
            $ minigame_repeat_pattern_difficulty = "hard"
            $ minigame_countdown_duration = 60
            $ minigame_repeat_pattern_number_of_buttons_to_match = 6
        # very hard
        "Very Hard (Double Boldness Opportunity)":
            $ minigame_repeat_pattern_difficulty = "very hard"
            $ minigame_countdown_duration = 75 # bumped up by 15 to match the medium to hard difference
            $ minigame_repeat_pattern_number_of_buttons_to_match = 7

    if minigame_repeat_pattern_partner == si:
        if minigame_repeat_pattern_difficulty == "easy":
            call process_character(si, appearance = "pose handsfront face neutral", text = "These puzzles are pretty relaxing.")
        elif minigame_repeat_pattern_difficulty == "medium":
            call process_character(si, appearance = "pose handsup face neutral", text = "Just think it out, and you'll solve it.")
        # elif check for hard
        elif minigame_repeat_pattern_difficulty == "hard":
            call process_character(si, appearance = "pose armunder face neutral", text = "I'd take your time with this one, sweetie!")
        # "very hard" is now the else check
        else:
            call process_character(si, appearance = "pose armunder face neutral", text = "This one moves fast, so make sure to really focus on it.")

    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()

    python:
        minigame_repeat_pattern_time_between_flashes = 1.5
        minigame_repeat_pattern_patterns_to_win = 3
        minigame_repeat_pattern_buttons = {}
        minigame_repeat_pattern_button_width = 240
        minigame_repeat_pattern_button_height = 240
        minigame_repeat_pattern_instruction_text = "Watch The Pattern"
        minigame_repeat_pattern_display_wrong_text_on_buttons = False
        minigame_repeat_pattern_patterns_solved = 0
        minigame_repeat_pattern_correctness_phase = False

        # if playing on very hard:
        # the time between flashes is reduced to 1.2, from 1.5
        # the amount of patterns that play out is increased to 4, from 3
        if minigame_repeat_pattern_difficulty == "very hard":
            minigame_repeat_pattern_time_between_flashes = 1.2
            minigame_repeat_pattern_patterns_to_win = 4

        minigame_repeat_pattern_buttons_array = []
        minigame_repeat_pattern_buttons_array.append(Repeat_Pattern_Button(color = "#e10000", flash_color = "#ff6464", key = "red"))
        minigame_repeat_pattern_buttons_array.append(Repeat_Pattern_Button(color = "#0000e1", flash_color = "#6464FF", key = "blue"))
        minigame_repeat_pattern_buttons_array.append(Repeat_Pattern_Button(color = "#00e100", flash_color = "#64FF64", key = "green"))
        minigame_repeat_pattern_buttons_array.append(Repeat_Pattern_Button(color = "#e1e100", flash_color = "#FFFF96", key = "yellow"))

        minigame_repeat_pattern_disable_button_interaction = True

    python hide:
        for button in store.minigame_repeat_pattern_buttons_array:
            store.minigame_repeat_pattern_buttons[button.key] = button

    if config.developer:
        "DEVELOPER MODE: Only one pattern"
        $ minigame_repeat_pattern_number_of_buttons_to_match = 1
        $ minigame_repeat_pattern_patterns_to_win = 1

    call minigame_repeat_round

    return

label minigame_repeat_pattern_got_all_right_very_hard:
    call hide_minigame_countdown
    $ minigame_repeat_pattern_instruction_text = "Pattern Solved!"
    $ minigame_repeat_pattern_patterns_solved += 1
    $ store.minigame_repeat_pattern_disable_button_interaction = True
    $ minigame_repeat_pattern_correctness_phase = True
    pause 1.0

    if minigame_repeat_pattern_patterns_solved >= minigame_repeat_pattern_patterns_to_win:
        $ minigame_repeat_pattern_correctness_phase = False
        $ minigame_repeat_pattern_money = 0
        pause 0.5

        if minigame_repeat_pattern_partner == si:
            if minigame_repeat_pattern_difficulty == "easy":
                $ minigame_repeat_pattern_money = 4
                $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
                $ si.add_points(2, minigame = True)
                call process_character(si, appearance = "pose handsup face happy", text = "Good job [n.say_name]!")
            elif minigame_repeat_pattern_difficulty == "medium":
                $ minigame_repeat_pattern_money = 6
                $ display_multiple_characters([ (n, ""), (si, "") ], reset = True)
                call add_points_and_boldness(si, 3, 1, minigame = True)
                call process_character(si, appearance = "pose handsup face happy", text = "You're getting good!")
            # elif check for hard
            elif minigame_repeat_pattern_difficulty == "hard":
                $ minigame_repeat_pattern_money = 8
                $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
                call add_points_and_boldness(si, 4, 1, minigame = True)
                call process_character(si, appearance = "pose handsup face happy", text = "Excellent [n.say_name]! Excellent!")
            # "very hard" is now the else check
            else:
                $ minigame_repeat_pattern_money = 10
                $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
                # 2x boldness
                call add_points_and_boldness(si, 5, 2, minigame = True)
                call process_character(si, appearance = "pose handsup face happy", text = "You really remembered all of that?")
                call process_character(si, appearance = "pose handsup face happy", text = "You have a brilliant mind, and a brilliant memory!")

        show screen hud
        python hide:
            inventory.add_money(minigame_repeat_pattern_money, minigame = True)
            narrator("Got $" + str(minigame_repeat_pattern_money) + " for winning.")

        call minigame_repeat_pattern_end
    else:
        pause 2.0
        call minigame_repeat_round

    return

label minigame_repeat_pattern_too_slow_very_hard:
    call hide_minigame_countdown
    $ minigame_repeat_pattern_correctness_phase = False
    $ store.minigame_repeat_pattern_disable_button_interaction = True
    pause 0.5

    if minigame_repeat_pattern_partner == si:
        if minigame_repeat_pattern_difficulty == "easy":
            $ display_multiple_characters([ (n, "face curious"), (si, "pose handsup face curious") ])
            call process_character(si, appearance = "pose handsup face curious", text = "I hope those video games aren't making this tougher.")
        # new "elif" dialogue for "very hard"
        # similar to julia, simone doesn't pity you, she understands if you fail
        elif minigame_repeat_pattern_difficulty == "very hard":
            $ display_multiple_characters([ (n, "face curious"), (si, "pose armunder face neutral") ])
            call process_character(si, appearance = "pose armunder face neutral", text = "That one moved very quickly.")
            call process_character(si, appearance = "pose armunder face neutral", text = "You almost had it though.")
        else:
            $ display_multiple_characters([ (n, "face curious"), (si, "pose handsfront face neutral") ])
            call process_character(si, appearance = "pose handsfront face neutral", text = "You'll get the hang of it.")

    call minigame_repeat_pattern_end

    return

#########################
# slide puzzle minigame #
#########################
label minigame_slide_puzzle_initialize_very_hard:
    python:
        # very hard
        if minigame_slide_puzzle_difficulty == "very hard":
            minigame_slide_puzzle_rows = 5
            minigame_slide_puzzle_columns = 5
        # elif check for hard
        elif minigame_slide_puzzle_difficulty == "hard":
            minigame_slide_puzzle_rows = 4
            minigame_slide_puzzle_columns = 4
        # medium/easy
        else:
            minigame_slide_puzzle_rows = 3
            minigame_slide_puzzle_columns = 3

        if minigame_slide_puzzle_difficulty == "easy":
            minigame_slide_puzzle_time_limit = False
        else:
            minigame_slide_puzzle_time_limit = True

        if minigame_slide_puzzle_difficulty == "medium":
            minigame_countdown_duration = 300     
        # elif check for hard
        elif minigame_slide_puzzle_difficulty == "hard":
            minigame_countdown_duration = 600
        # elif check for very hard
        elif minigame_slide_puzzle_difficulty == "very hard":
            minigame_countdown_duration = 720

        minigame_slide_puzzle_gap_row = minigame_slide_puzzle_rows - 1
        minigame_slide_puzzle_gap_column = minigame_slide_puzzle_columns - 1
        minigame_slide_puzzle_layout = []
        minigame_slide_puzzle_layout_slot_index = 0
        minigame_slide_puzzle_layout_width = 1280
        minigame_slide_puzzle_layout_height = 720
        minigame_slide_puzzle_piece_width = int(minigame_slide_puzzle_layout_width / float(minigame_slide_puzzle_rows))
        minigame_slide_puzzle_piece_height = int(minigame_slide_puzzle_layout_height / float(minigame_slide_puzzle_columns))
        minigame_slide_puzzle_base_displayable_full_path = minigame_slide_puzzle_random_picture()
        minigame_slide_puzzle_check_for_win = False
        minigame_slide_puzzle_disable_puzzle_interaction = False
        minigame_slide_puzzle_scrambled_at_least_once = False
        minigame_slide_puzzle_times_to_scramble = 80

        if config.developer and 1 == 2:
            #minigame_slide_puzzle_time_limit = True
            #minigame_countdown_duration = 6
            minigame_slide_puzzle_times_to_scramble = 1

        # if playing on very hard:
        # the time limit is doubled, to account for the difficulty
        if minigame_slide_puzzle_difficulty == "very hard":
            minigame_slide_puzzle_times_to_scramble = 160

        minigame_slide_puzzle_base_displayable = Transform(Image(minigame_slide_puzzle_base_displayable_full_path), size = (minigame_slide_puzzle_layout_width, minigame_slide_puzzle_layout_height))

        for row_i in range(0, minigame_slide_puzzle_rows):
            minigame_slide_puzzle_layout.append([])
            for col_i in range(0, minigame_slide_puzzle_columns):
                if minigame_slide_puzzle_gap_row != row_i or minigame_slide_puzzle_gap_column != col_i:
                    minigame_slide_puzzle_layout[row_i].append(Slide_Puzzle_Piece(minigame_slide_puzzle_base_displayable, minigame_slide_puzzle_layout_slot_index, row = row_i, column = col_i))
                else:
                    minigame_slide_puzzle_layout[row_i].append(None)
                minigame_slide_puzzle_layout_slot_index += 1

        while not minigame_slide_puzzle_scrambled_at_least_once or minigame_slide_puzzle_test_win():
            minigame_slide_puzzle_scrambled_at_least_once = True

            for i in range(0, minigame_slide_puzzle_times_to_scramble):
                candidates = []

                old_row = minigame_slide_puzzle_gap_row
                old_col = minigame_slide_puzzle_gap_column

                # check above
                if old_row != 0:
                    candidates.append( (old_row - 1, old_col) )

                # check below
                if old_row != store.minigame_slide_puzzle_rows - 1:
                    candidates.append( (old_row + 1, old_col) )

                # check left
                if old_col != 0:
                    candidates.append( (old_row, old_col - 1) )

                # check right
                if old_col != store.minigame_slide_puzzle_columns - 1:
                    candidates.append( (old_row, old_col + 1) )

                # choose
                candidate = random.choice(candidates)
                new_row = candidate[0]
                new_col = candidate[1]

                puzzle_piece_to_swap = minigame_slide_puzzle_layout[new_row][new_col]
                minigame_slide_puzzle_perform_swap(new_row, new_col, old_row, old_col, puzzle_piece_to_swap)
                minigame_slide_puzzle_gap_row = new_row
                minigame_slide_puzzle_gap_column = new_col

        minigame_slide_puzzle_check_for_win = True

    return

label minigame_slide_puzzle_intro_very_hard(partner = None):
    $ no_bust_art = False

    if config.developer and 1 == 2:
        "DEBUG/DEVELOPER MODE: Reduced difficulty."

    if partner:
        $ minigame_slide_puzzle_partner = partner
    else:
        $ minigame_slide_puzzle_partner = si

    if minigame_slide_puzzle_partner == si:
        $ diceroll = random.randint(1,3)

        if diceroll == 1:
            $ display_multiple_characters([ (n, ""), (si, "pose handsup") ], reset = True)
            call process_character(si, appearance = "pose handsup", text = "I just finished one.")
            call process_character(si, appearance = "pose handsup", text = "You should give it a try.")
        elif diceroll == 2:
            $ display_multiple_characters([ (n, ""), (si, "pose armunder face happy") ], reset = True)
            call process_character(si, appearance = "pose armunder face happy", text = "I don't know how some people finish these so fast!")
        else:
            $ display_multiple_characters([ (n, ""), (si, "pose handsfront face neutral") ], reset = True)
            call process_character(si, appearance = "pose handsfront face neutral", text = "Your young brain can handle these.")
            call process_character(si, appearance = "pose handsfront face happy", text = "Unlike your mom here!")
    elif minigame_slide_puzzle_partner == sa:
        if not minigame_sliding_puzzle_sam_intro_done:
            $ minigame_sliding_puzzle_sam_intro_done = True
            $ display_multiple_characters([ (n, ""), (sa, "pose handsbehind face neutral") ], reset = True)

            if "minigame_slide_puzzle_first_time_intro" in si.conversations_completed:
                call process_character(sa, appearance = "pose handsbehind face neutral", text = "I heard Mom is trying out these new puzzles?")
                call process_character(n, appearance = "pose handpocket face neutral", text = "Yeah.")
                call process_character(n, appearance = "pose handpocket face neutral", text = "She said they are good for memory.")
            else:
                call process_character(sa, appearance = "pose handsbehind face neutral", text = "Mom told me about these puzzles she's been doing.")
                call process_character(n, appearance = "pose handpocket face neutral", text = "Oh yeah?")
                call process_character(n, appearance = "pose handpocket face neutral", text = "What are they?")
                call process_character(sa, appearance = "pose handface face neutral", text = "I think they're called \"sliding\" puzzles?")
                call process_character(sa, appearance = "pose handface face neutral", text = "Mom says they help her with memory.")
                call process_character(n, appearance = "pose handpocket face neutral", text = "Interesting...")

            call process_character(sa, appearance = "pose leaning face neutral", text = "I think we should try some of them!")
            call process_character(sa, appearance = "pose handface face curious", text = "Doing math all the time fries my brain...")
            call process_character(n, appearance = "pose handfist face neutral", text = "Sure!")
            call process_character(n, appearance = "pose handfist face neutral", text = "I'm up for some puzzle action!")
            call process_character(sa, appearance = "pose leaning face happy", text = "Nice!")
            call process_character(sa, appearance = "pose leaning face happy", text = "Let me get some for us!")

            call character_leave_dissolve(sa)
            $ renpy.pause(1)

            call process_character(sa, appearance = "pose handsbehind face neutral", text = "Looks like there are different levels of challenge for them!")
            call process_character(sa, appearance = "pose handface face neutral", text = "I wonder what level we should start with...")
        else:
            $ diceroll = random.randint(1,3)
            if diceroll == 1:
                $ display_multiple_characters([ (n, ""), (sa, "pose handface face neutral") ], reset = True)
                call process_character(sa, appearance = "pose handface face neutral", text = "I'll take this over math for sure!")
            elif diceroll == 2:
                $ display_multiple_characters([ (n, ""), (sa, "pose leaning face neutral") ], reset = True)
                call process_character(sa, appearance = "pose leaning face neutral", text = "These puzzles should be in a video game!")
            else:
                $ display_multiple_characters([ (n, ""), (sa, "pose handsbehind face neutral") ], reset = True)
                call process_character(sa, appearance = "pose handsbehind face neutral", text = "I wonder what puzzle we should try this time?")

    window hide
    menu:
        "Easy":
            $ minigame_slide_puzzle_difficulty = "easy"
        "Medium (Boldness Opportunity)":
            $ minigame_slide_puzzle_difficulty = "medium"
        "Hard (Boldness Opportunity)":
            $ minigame_slide_puzzle_difficulty = "hard"
        # very hard
        "Very Hard (Double Boldness Opportunity)":
            $ minigame_slide_puzzle_difficulty = "very hard"

    if minigame_slide_puzzle_partner == si:
        if minigame_slide_puzzle_difficulty == "easy":
            call process_character(si, appearance = "pose handsfront face neutral", text = "These puzzles are pretty relaxing.")
        elif minigame_slide_puzzle_difficulty == "medium":
            call process_character(si, appearance = "pose handsup face neutral", text = "Just think it out, and you'll solve it.")
        # elif check for hard
        elif minigame_slide_puzzle_difficulty == "hard":
            call process_character(si, appearance = "pose armunder face neutral", text = "I'd take your time with this one sweetie!")
        # "very hard" is now the else check
        # new dialogue for simone
        else:
            call process_character(si, appearance = "pose armunder face neutral", text = "Oh, that one looks mean.")
            call process_character(si, appearance = "pose armunder face neutral", text = "Take it one piece at a time, sweetie.")
    elif minigame_slide_puzzle_partner == sa:
        if minigame_slide_puzzle_difficulty == "easy":
            call process_character(sa, appearance = "pose handsbehind face neutral", text = "Let's take it easy this time!")
        elif minigame_slide_puzzle_difficulty == "medium":
            call process_character(sa, appearance = "pose handsbehind face neutral", text = "There's definitely a strategy to it!")
            call process_character(sa, appearance = "pose handsbehind face neutral", text = "I've almost got the hang of it!")
        # elif check for hard
        elif minigame_slide_puzzle_difficulty == "hard":
            call process_character(sa, appearance = "pose handface face curious", text = "I'm focusing my brainpower on this one!")
        # "very hard" is now the else check
        # new dialogue for sam
        else:
            call process_character(sa, appearance = "pose leaning face neutral", text = "My brain is on maximum overdrive for this one!")
            call process_character(sa, appearance = "pose leaning face neutral", text = "Now I really want to beat it!")

    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()

    return

label minigame_slide_puzzle_win_very_hard:
    $ minigame_slide_puzzle_disable_puzzle_interaction = True
    call hide_minigame_countdown
    pause 1.0
    hide screen slide_puzzle_screen
    hide screen hard_block_screen

    if minigame_slide_puzzle_difficulty == "easy":
        $ minigame_slide_puzzle_win_money = 4
    elif minigame_slide_puzzle_difficulty == "medium":
        $ minigame_slide_puzzle_win_money = 6
    # elif check for hard
    elif minigame_slide_puzzle_difficulty == "hard":
        $ minigame_slide_puzzle_win_money = 8
    # "very hard" is now the else check
    else:
        $ minigame_slide_puzzle_win_money = 10

    $ renpy.pause(0.25)
    if minigame_slide_puzzle_partner == si:
        if minigame_slide_puzzle_difficulty == "easy":
            $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
            $ si.add_points(3, minigame = True)
            call process_character(si, appearance = "pose handsup face happy", text = "Good job [n.say_name]!")
        elif minigame_slide_puzzle_difficulty == "medium":
            $ display_multiple_characters([ (n, ""), (si, "") ], reset = True)
            call add_points_and_boldness(si, 4, 1, minigame = True)
            call process_character(si, appearance = "pose handsup face happy", text = "You're getting good!")
        # elif check for hard
        elif minigame_slide_puzzle_difficulty == "hard":
            $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
            call add_points_and_boldness(si, 5, 1, minigame = True)
            call process_character(si, appearance = "pose handsup face happy", text = "Excellent [n.say_name]! Excellent!")
        # "very hard" is now the else check
        # new dialogue for simone
        else:
            $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
            # 2x boldness
            call add_points_and_boldness(si, 6, 2, minigame = True)
            call process_character(si, appearance = "pose handsup face happy", text = "Perfect, simply perfect!")
            call process_character(si, appearance = "pose handsup face happy", text = "I'm so proud of you, sweetie!")
    elif minigame_slide_puzzle_partner == sa:
        if minigame_slide_puzzle_difficulty == "easy":
            $ display_multiple_characters([ (n, ""), (sa, "pose handface face happy") ])
            $ sa.add_points(3, minigame = True)
            call process_character(sa, appearance = "pose handface face happy", text = "Hey, not bad!")
        elif minigame_slide_puzzle_difficulty == "medium":
            $ display_multiple_characters([ (n, ""), (sa, "pose handface face happy") ])
            call add_points_and_boldness(sa, 4, 1, minigame = True)
            call process_character(sa, appearance = "pose handface face happy", text = "Oh, so that's how it's done!")
            call process_character(sa, appearance = "pose handface face happy", text = "Nice [n.say_name]!")
        # elif check for hard
        elif minigame_slide_puzzle_difficulty == "hard":
            $ display_multiple_characters([ (n, ""), (sa, "pose handface face happy") ])
            call add_points_and_boldness(sa, 5, 1, minigame = True)
            call process_character(sa, appearance = "pose handface face happy", text = "Wow!")
            call process_character(sa, appearance = "pose handface face happy", text = "I didn't even see that solution!")
            call process_character(sa, appearance = "pose handface face happy", text = "You're a puzzle wizard [n.say_name]!")
        else:
            $ display_multiple_characters([ (n, ""), (sa, "pose handface face happy") ])
            # 2x boldness, new dialogue
            call add_points_and_boldness(sa, 6, 2, minigame = True)
            call process_character(sa, appearance = "pose handface face happy", text = "No way!")
            call process_character(sa, appearance = "pose handface face happy", text = "You must be the best puzzle solver in the whole wide world!")

    show screen hud
    python hide:
        inventory.add_money(minigame_slide_puzzle_win_money, minigame = True)
        narrator("Got $" + str(minigame_slide_puzzle_win_money) + " for winning.")

    call minigame_slide_puzzle_end

    return

label minigame_slide_puzzle_too_slow_very_hard:
    $ minigame_slide_puzzle_disable_puzzle_interaction = True
    call hide_minigame_countdown
    pause 1.0
    hide screen slide_puzzle_screen
    hide screen hard_block_screen

    if minigame_slide_puzzle_partner == si:
        if minigame_slide_puzzle_difficulty == "easy":
            $ display_multiple_characters([ (n, "face curious"), (si, "pose handsup face curious") ])
            call process_character(si, appearance = "pose handsup face curious", text = "I hope those video games aren't making this tougher.")
        # new "elif" dialogue for "very hard"
        # similar to julia, simone doesn't pity you, she understands if you fail
        elif minigame_slide_puzzle_difficulty == "very hard":
            $ display_multiple_characters([ (n, "face curious"), (si, "pose armunder face neutral") ])
            call process_character(si, appearance = "pose armunder face neutral", text = "Oh, my goodness...")
            call process_character(si, appearance = "pose armunder face neutral", text = "I wouldn't worry about such a difficult puzzle, sweetie.")
        else:
            $ display_multiple_characters([ (n, "face curious"), (si, "pose handsfront face neutral") ])
            call process_character(si, appearance = "pose handsfront face neutral", text = "You'll get the hang of it.")
    elif minigame_slide_puzzle_partner == sa:
        if minigame_slide_puzzle_difficulty == "easy":
            $ display_multiple_characters([ (n, "face curious"), (sa, "pose handface face curious") ])
            call process_character(sa, appearance = "pose handface face curious", text = "Guess our memory isn't too good, huh?")
        # new "elif" dialogue for "very hard"
        # similar to julia/simone, sam understands if you fail, but wants to try again with you
        elif minigame_slide_puzzle_difficulty == "very hard":
            $ display_multiple_characters([ (n, "face curious"), (sa, "pose handface face curious") ])
            call process_character(sa, appearance = "pose handface face curious", text = "Man, what a beast of a puzzle!")
            call process_character(sa, appearance = "pose handface face curious", text = "I still want another shot at it though!")
        else:
            $ display_multiple_characters([ (n, "face curious"), (sa, "pose handface face curious") ])
            call process_character(sa, appearance = "pose handface face curious", text = "Aw, and we were getting there!")

    call minigame_slide_puzzle_end

    return

#########################
# table tennis minigame #
#########################
init 300 python:
    # inherits all from the original TableTennis class
    class TableTennis_Very_Hard(TableTennis):
        def __init__(self):
            TableTennis.__init__(self)

            if store.minigame_table_tennis_difficulty == "very hard":
                self.original_bspeed = 1025.0
                self.computerspeed = 1100
                self.max_bspeed = 2800
                self.bspeed = self.original_bspeed
                self.leeway = 8

label minigame_table_tennis_very_hard(partner = edna):
    $ minigame_table_tennis_partner = partner

    call process_new_location(minigame_table_tennis_partner.minigame_table_tennis_background())

    $ no_bust_art = False

    python:
        minigame_table_tennis_player_score = 0
        minigame_table_tennis_partner_score = 0
        minigame_table_tennis_partner_win_threshold = 2

    $ minigame_table_tennis_instant_win_mode = False
    $ minigame_table_tennis_instant_lose_mode = False
    if config.developer:
        "CONFIG/DEVELOPER MODE"
        menu:
            "Activate Instant Win Mode":
                $ minigame_table_tennis_instant_win_mode = True
            "Activate Instant Lose Mode":
                $ minigame_table_tennis_instant_lose_mode = True
            "Activate neither":
                pass

    $ renpy.call(minigame_table_tennis_partner.minigame_table_tennis_greeting_label())

    window hide
    menu:
        "Easy":
            $ minigame_table_tennis_difficulty = "easy"
        "Medium (Boldness Opportunity)":
            $ minigame_table_tennis_difficulty = "medium"
        "Hard (Boldness Opportunity)":
            $ minigame_table_tennis_difficulty = "hard"
        # very hard
        "Very Hard (Double Boldness Opportunity)":
            $ minigame_table_tennis_difficulty = "very hard"
            # if playing on very hard, you have an additional win threshold
            $ minigame_table_tennis_partner_win_threshold = 3

    $ renpy.call(minigame_table_tennis_partner.minigame_table_tennis_difficulty_response_label())

    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()

    show screen minigame_table_tennis_score_display

    jump minigame_table_tennis_round_very_hard

    return

label minigame_table_tennis_round_very_hard:
    window hide

    python:
        ui.add(TableTennis_Very_Hard())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    window show None

    if winner == "opponent":
        $ minigame_table_tennis_partner_score += 1
        "You lost this round."

    else:
        $ minigame_table_tennis_player_score += 1
        "You won this round!"

    if minigame_table_tennis_player_score >= minigame_table_tennis_partner_win_threshold:
        jump minigame_table_tennis_win
    elif minigame_table_tennis_partner_score >= minigame_table_tennis_partner_win_threshold:
        jump minigame_table_tennis_lose
    else:
        jump minigame_table_tennis_round_very_hard

    return

label edna_minigame_table_tennis_difficulty_response_very_hard:
    $ diceroll = random.randint(1,2)

    if minigame_table_tennis_difficulty == "easy":
        if diceroll == 1:
            call process_character(edna, appearance = "pose handclasp face neutral blush false")
            edna.c "It's best to start off slow."
            call process_character(edna, appearance = "pose handclasp face neutral blush false")
            edna.c "You'll work your way up in no time!"
        else:
            call process_character(edna, appearance = "pose fisthip face neutral blush false")
            edna.c "Let me know if I start going too fast."
            call process_character(edna, appearance = "pose fisthip face neutral blush false")
            edna.c "It's a force of habit sometimes!"
    elif minigame_table_tennis_difficulty == "medium":
        if diceroll == 1:
            call process_character(edna, appearance = "pose handhip face neutral blush false")
            edna.c "I'll hit with my topspin on occasion."
            call process_character(edna, appearance = "pose handhip face neutral blush false")
            edna.c "Watch out for it!"
        else:
            call process_character(edna, appearance = "pose handclasp face neutral blush false")
            edna.c "Since I started playing, I've noticed I can move my feet better."
            call process_character(edna, appearance = "pose handclasp face happy blush false")
            edna.c "It must be helping my joints!"
    # elif check for hard
    elif minigame_table_tennis_difficulty == "hard":
        if diceroll == 1:
            call process_character(edna, appearance = "pose fisthip face neutral blush false")
            edna.c "You'll feel it in your legs after this!"
            call process_character(edna, appearance = "pose fisthip face neutral blush false")
            edna.c "I usually put ice on them."
        else:
            call process_character(edna, appearance = "pose handclasp face neutral blush false")
            edna.c "I've been working on improving my serve."
            call process_character(edna, appearance = "pose handclasp face happy blush false")
            edna.c "Let me see what you think!"
    # "very hard" is now the else check
    # new dialogue for edna
    else:
        if diceroll == 1:
            call process_character(edna, appearance = "pose handhip face happy blush false")
            edna.c "Alright, no holding back this time."
            call process_character(edna, appearance = "pose handhip face happy blush false")
            edna.c "Let's see what you've really got!"
        else:
            call process_character(edna, appearance = "pose fisthip face happy blush false")
            edna.c "This is the pace that gets the heart pumping!"
            call process_character(edna, appearance = "pose fisthip face happy blush false")
            edna.c "Stay light on your feet!"

    return

label edna_table_tennis_minigame_player_won_label_very_hard:
    if minigame_table_tennis_difficulty == "easy":
        $ edna.add_points(2, minigame = True)
        $ minigame_table_tennis_win_money = 4
        $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose fisthip face neutral blush false") ])
        call process_character(edna, appearance = "pose fisthip face neutral blush false")
        edna.c "You're more than capable at this [n.say_name]."
        call process_character(edna, appearance = "pose fisthip face neutral blush false")
        edna.c "I know you can handle the next level!"
    
    elif minigame_table_tennis_difficulty == "medium":
        call add_points_and_boldness(edna, 3, 1, minigame = True)
        $ minigame_table_tennis_win_money = 6
        $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose handclasp face happy blush false") ])
        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "And my grandson claims victory!"
    
    # elif check for hard
    elif minigame_table_tennis_difficulty == "hard":
        call add_points_and_boldness(edna, 4, 1, minigame = True)
        $ minigame_table_tennis_win_money = 8
        $ diceroll = random.randint(1,2)
        if diceroll == 1:
            $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose fisthip face shock blush false") ])
            call process_character(edna, appearance = "pose fisthip face shock blush false")
            edna.c "You smoked me [n.say_name]!"
            call process_character(edna, appearance = "pose fisthip face shock blush false")
            edna.c "Pretty soon you'll be getting trophies!"
        else:
            $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose handhip face happy blush false") ])
            call process_character(edna, appearance = "pose handhip face happy blush false")
            edna.c "You've got a good swing [n.say_name]!"
            call process_character(edna, appearance = "pose handhip face happy blush false")
            edna.c "And you're light on your feet!"
    
    # "very hard" is now the else check
    # new dialogue for edna
    else:
        # 2x boldness
        call add_points_and_boldness(edna, 5, 2, minigame = True)
        $ minigame_table_tennis_win_money = 10
        $ diceroll = random.randint(1,2)
        if diceroll == 1:
            $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose handclasp face happy blush false") ])
            call process_character(edna, appearance = "pose handclasp face happy blush false")
            edna.c "Now that was a match!"
            call process_character(edna, appearance = "pose handclasp face happy blush false")
            edna.c "You earned every point of that win!"
        else:
            $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose fisthip face happy blush false") ])
            call process_character(edna, appearance = "pose fisthip face happy blush false")
            edna.c "You kept your nerve the whole way through."
            call process_character(edna, appearance = "pose fisthip face happy blush false")
            edna.c "That's how you close out a game!"

    return

label edna_table_tennis_minigame_player_lost_label_very_hard:
    if minigame_table_tennis_difficulty == "easy":
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose handclasp face concerned blush false") ])
        call process_character(edna, appearance = "pose handclasp face concerned blush false")
        edna.c "Maybe your racket is too heavy for you [n.say_name]?"
    
    elif minigame_table_tennis_difficulty == "medium":
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose handhip face neutral blush false") ])
        call process_character(edna, appearance = "pose handhip face neutral blush false")
        edna.c "Keep your eye on the ball, as they say!"
        call process_character(edna, appearance = "pose handhip face neutral blush false")
        edna.c "Don't take your eyes off of it!"
    
    # elif check for hard
    elif minigame_table_tennis_difficulty == "hard":
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose fisthip face neutral blush false") ])
        call process_character(edna, appearance = "pose fisthip face neutral blush false")
        edna.c "Almost [n.say_name]!"
        call process_character(edna, appearance = "pose fisthip face neutral blush false")
        edna.c "Keep working at it!"
    # "very hard" is now the else check
    # new dialogue for edna
    else:
        $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose handhip face neutral blush false") ])
        call process_character(edna, appearance = "pose handhip face neutral blush false")
        edna.c "Reading my shots is the key to victory."
        call process_character(edna, appearance = "pose handhip face neutral blush false")
        edna.c "You were so close!"

    return

###################
# typing minigame #
###################
init python:
    def minigame_typing_review_very_hard_lines():
        lines = []

        lines.extend(minigame_typing_review_medium_sentences(store.minigame_typing_lines_number, force_the = True))
        lines.extend(minigame_typing_review_medium_sentences(store.minigame_typing_lines_number, force_the = False))
        lines.extend(minigame_typing_review_edgy_lines())

        return lines

label minigame_typing_review_intro_very_hard:
    call process_character(n, appearance = "pose handpocket face neutral", text = "(I should write as many reviews as I can for the [video_sharing_site] channel)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(I'm sure it {b}will take time{/b} to write it though)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(I wonder what kind of review I should do?)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(I could write a {b}casual review{/b}, that will be easy...)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(But it probably won't get many views or income)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(I could also write an {b}in-depth review{/b}, and be more thorough)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(That will get more views and income)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(Or I could challenge myself, and write a {b}controversial{/b} review)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(The channel will definitely get attention and income from that!)")
    # new dialogue to reference very hard, but omitted because very hard is unlocked, not accessible at the start of the minigame
    #call process_character(n, appearance = "pose handpocket face neutral", text = "(Or I could go all in and write a full breakdown.)")
    #call process_character(n, appearance = "pose handpocket face neutral", text = "(That would take the most work, but it should pay off if I can pull it off right!)")
    call process_character(n, appearance = "pose handpocket face neutral", text = "(Alright, time to get started!)")

    return

label minigame_typing_review_set_lines_very_hard:
    python:
        minigame_typing_lines = []
        minigame_typing_review_game_quality = random.randint(1,3)

        if minigame_typing_review_game_quality == 1:
            # poor game
            minigame_typing_review_adjectives = minigame_typing_review_bad_adjectives()
        elif minigame_typing_review_game_quality == 2:
            # okay game
            minigame_typing_review_adjectives = minigame_typing_review_neutral_adjectives()
        else:
            # good game
            minigame_typing_review_adjectives = minigame_typing_review_good_adjectives()

    menu:
        "I'll do a casual review.":
            $ minigame_typing_review_difficulty = "easy"
            $ minigame_typing_review_money_reward_sam_points = 1
            $ minigame_countdown_duration = 60
            $ minigame_typing_lines_number = 7
            $ minigame_typing_lines = minigame_typing_review_casual_lines()
        "I'll do an in-depth review. (Boldness Opportunity)":
            $ minigame_typing_review_difficulty = "medium"
            $ minigame_typing_review_money_reward_sam_points = 1
            $ minigame_countdown_duration = 70
            $ minigame_typing_lines_number = 7
            $ minigame_typing_lines = minigame_typing_review_indepth_lines()
        "I'll do a controversial review. (Boldness Opportunity)":
            $ minigame_typing_review_difficulty = "hard"
            $ minigame_typing_review_money_reward_sam_points = 2
            # always a bad game
            $ minigame_typing_review_game_quality = 1
            $ minigame_typing_review_adjectives = minigame_typing_edgy_bad_adjectives()
            $ minigame_countdown_duration = 95
            $ minigame_typing_lines_number = 7
            $ minigame_typing_lines = minigame_typing_review_edgy_lines()
        # very hard
        "I'll do a full tear-down! (Double Boldness Opportunity)":
            $ minigame_typing_review_difficulty = "very hard"
            $ minigame_typing_review_money_reward_sam_points = 4 # 2x points for sam
            $ minigame_typing_review_game_quality = 1 # always a bad game, just like hard mode
            $ minigame_countdown_duration = 110 # bumped up by 15 to match the medium to hard difference
            $ minigame_typing_lines_number = 9
            $ minigame_typing_lines = minigame_typing_review_very_hard_lines()

    $ minigame_countdown_duration += minigame_typing_review_countdown_boost_amount()
    $ minigame_countdown_duration += minigame_typing_review_countdown_addend

    $ disable_saving()

    if config.developer:
        "DEBUG/DEVELOPER MODE: Only one line."

    if minigame_typing_review_game_quality == 1:
        if minigame_typing_review_difficulty == "easy":
            call process_character(n, appearance = "pose handpocket face curious", text = "(This crappy game doesn't need much to be said about it)")
        elif minigame_typing_review_difficulty == "medium":
            call process_character(n, appearance = "pose handpocket face curious", text = "(It's impressive how many things are wrong with this latest game)")
        # elif check for hard
        elif minigame_typing_review_difficulty == "hard":
            call process_character(n, appearance = "pose twohandfist face happy", text = "(This review should stir up plenty of discussion online!)")
        # "very hard" is now the else check
        else:
            call process_character(n, appearance = "pose handpocket face neutral", text = "(If I'm going to rip this game apart, I should do it properly!)")
    
    elif minigame_typing_review_game_quality == 2:
        if minigame_typing_review_difficulty == "easy":
            call process_character(n, appearance = "pose handpocket face neutral", text = "(I think a quick and easy review is fine for this game)")
        elif minigame_typing_review_difficulty == "medium":
            call process_character(n, appearance = "pose behindhead face neutral", text = "(This game isn't perfect, but it deserves a full review)")
        # new "elif" dialogue for "very hard"
        # unused because very hard (just like hard) always results in a bad game
        #elif minigame_typing_review_difficulty == "very hard":
        #    call process_character(n, appearance = "pose handpocket face neutral", text = "(Alright, full breakdown time.)")
    
    else:
        if minigame_typing_review_difficulty == "easy":
            call process_character(n, appearance = "pose handfist face happy", text = "(Nothing but good things to say about this game!)")
        elif minigame_typing_review_difficulty == "medium":
            call process_character(n, appearance = "pose twohandfist face happy", text = "(Where to begin when talking about this awesome game!)")
        # new "elif" dialogue for "very hard"
        # unused because very hard (just like hard) always results in a bad game
        #elif minigame_typing_review_difficulty == "very hard":
        #    call process_character(n, appearance = "pose twohandfist face happy", text = "(This one deserves a proper deep dive!)")

    $ clear_characters()
    python:
        minigame_typing_lines = minigame_typing_lines[:minigame_typing_lines_number]
        random.shuffle(minigame_typing_lines)
        minigame_typing_lines = minigame_typing_replace_in_lines(minigame_typing_lines)

    return

label minigame_typing_review_result_very_hard:
    $ minigame_typing_review_started = False
    $ enable_saving()

    call hide_minigame_countdown
    python:
        ratio = minigame_typing_lines_correct / float(minigame_typing_lines_number)
        mingame_typing_wpm = int((minigame_typing_words_typed * 60) / countdown_elapsed)
        minigame_typing_review_money_reward = 0
        minigame_typing_review_money_reward_sam_share = 0

    # "Time remaining: [countdown_remaining]"
    # "WPM: [mingame_typing_wpm]"

    if ratio <= 0.0:
        call process_character(n, appearance = "pose behindhead face curious", text = "(Man, I had some serious writer's block)")
    elif ratio < minigame_typing_review_second_place_threshold:
        call process_character(n, appearance = "pose behindhead face concerned", text = "(Eh, I don't think this review is good enough to publish)")
    elif ratio < 1.0:
        call process_character(n, appearance = "pose handpocket face neutral", text = "(Not bad! I think people will like this)")

        if minigame_typing_review_difficulty == "easy":
            $ minigame_typing_review_money_reward = 4
        elif minigame_typing_review_difficulty == "medium":
            $ minigame_typing_review_money_reward = 6
        # elif check for hard
        elif minigame_typing_review_difficulty == "hard":
            $ minigame_typing_review_money_reward = 8
        # "very hard" is now the else check
        else:
            $ minigame_typing_review_money_reward = 10
    else:
        call process_character(n, appearance = "pose handfist face happy", text = "(This review turned out great!)")

        if minigame_typing_review_difficulty == "hard":
            call process_character(n, appearance = "pose behindhead face neutral", text = "(That was awesome to write so explicit!)")
        # elif check for very hard
        elif minigame_typing_review_difficulty == "very hard":
            call process_character(n, appearance = "pose handfist face happy", text = "(That should give the channel a real boost.)")

        if minigame_typing_review_difficulty == "easy":
            $ minigame_typing_review_money_reward = 6
        elif minigame_typing_review_difficulty == "medium":
            call add_boldness(1, minigame = True)
            $ minigame_typing_review_money_reward = 8
        # elif check for hard
        elif minigame_typing_review_difficulty == "hard":
            call add_boldness(1, minigame = True)
            $ minigame_typing_review_money_reward = 10
        else:
            # 2x boldness
            call add_boldness(2, minigame = True)
            $ minigame_typing_review_money_reward = 12

    if minigame_typing_review_money_reward > 0:
        if "vicky_tease_scene" in scenes_completed:
            $ minigame_typing_review_money_reward = int(round((minigame_typing_review_money_reward * 2) * 0.80))

        $ minigame_typing_times_succeeded += 1
        $ minigame_typing_times_succeeded_since_last_vicky_meeting += 1

        $ minigame_typing_money_earned += minigame_typing_review_money_reward
        $ minigame_typing_money_earned_since_last_vicky_meeting += minigame_typing_review_money_reward

        $ minigame_typing_review_money_reward_sam_share = int(round(minigame_typing_review_money_reward / 2))
        show screen hud
        call process_character(n, appearance = "pose twohandfist face neutral", text = "(That review should bring in about $[minigame_typing_review_money_reward]!)")
        # while we're at it, fix the typo here in this dialogue
        call process_character(n, appearance = "pose handpocket face curious", text = "(I'm sure sharing the income with [sa.say_name] would make her happy...)")
        menu:
            "Share some of the money with [sa.say_name].":
                $ minigame_typing_review_money_reward -= minigame_typing_review_money_reward_sam_share
                $ inventory.add_money(minigame_typing_review_money_reward, minigame = True)
                call process_character(n, appearance = "pose handpocket face happy", text = "(She deserves a reward for all her hard work on the stream!)")

                call add_points(sa, minigame_typing_review_money_reward_sam_points, delay = True, minigame = True)
            "Keep the money.":
                $ inventory.add_money(minigame_typing_review_money_reward, minigame = True)
                call process_character(n, appearance = "pose handpocket face happy", text = "(I'll save up to buy something cool later on!)")

    $ renpy.block_rollback()
    $ enable_rollback()
    hide screen hud
    hide screen minigame_typing_review_info

    call process_end_of_minigame("minigame_typing_review")

    return
