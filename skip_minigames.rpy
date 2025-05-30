# Main Labels
init 200 python:
    config.label_overrides["minigame_math"] = "minigame_math_mod"
    config.label_overrides["minigame_racing"] = "minigame_racing_mod"
    config.label_overrides["minigame_reading"] = "minigame_reading_mod"
    config.label_overrides["minigame_repeat_pattern"] = "minigame_repeat_pattern_mod"
    config.label_overrides["minigame_slide_puzzle"] = "minigame_slide_puzzle_mod"
    config.label_overrides["minigame_table_tennis"] = "minigame_table_tennis_mod"
    config.label_overrides["minigame_typing_review"] = "minigame_typing_review_mod"

# End Labels, required for minigames to count towards completed stats #
init 200 python:
    config.label_overrides["math_minigame_end"] = "minigame_math_end_mod"
    config.label_overrides["minigame_racing_result"] = "minigame_racing_result_mod"
    config.label_overrides["minigame_reading_end"] = "minigame_reading_end_mod"
    config.label_overrides["minigame_repeat_pattern_end"] = "minigame_repeat_pattern_end_mod"
    config.label_overrides["minigame_slide_puzzle_end"] = "minigame_slide_puzzle_end_mod"
    config.label_overrides["minigame_table_tennis_end"] = "minigame_table_tennis_end_mod"
    config.label_overrides["minigame_typing_review_result"] = "minigame_typing_review_result_end_mod"

# Math # 
label minigame_math_mod(partner = None):
    $ renpy.block_rollback()
    $ enable_rollback()

    call minigame_math_end_mod

label minigame_math_end_mod:
    call add_points_and_boldness(sa, 4, 1, minigame = True)

    show screen hud
    python hide:
        win_money = 8
        inventory.add_money(win_money, minigame = True)
        narrator("Got $" + str(win_money) + " for cheating.")

    call process_end_of_minigame("minigame_math")

    return

# Racing #
label minigame_racing_mod(partner = k):
    $ renpy.block_rollback()
    $ enable_rollback()
    $ renpy.scene('screens')
    $ no_bust_art = False
    $ minigame_racing_partner = partner 

    call minigame_racing_result_mod(won = True)

label minigame_racing_result_mod(won = True):
    $ minigame_racing_finished = True

    if minigame_racing_partner == k:
        call add_points_and_boldness(k, 4, 1, minigame = True)
    elif minigame_racing_partner == janet:
        call add_points_and_boldness(janet, 4, 1, minigame = True)

    show screen hud
    python hide:
        minigame_racing_reward = 8
        inventory.add_money(minigame_racing_reward, minigame = True)
        narrator("Got $" + str(minigame_racing_reward) + " for cheating.")

    call process_end_of_minigame("minigame_racing")

    return

# Reading #
label minigame_reading_mod(partner = None):
    $ renpy.block_rollback()
    $ enable_rollback()
    $ renpy.scene('screens')
    call minigame_reading_end_mod

label minigame_reading_end_mod:
    call add_points_and_boldness(julia, 4, 1, minigame = True)

    show screen hud
    python hide:
        minigame_reading_money = 8
        inventory.add_money(minigame_reading_money, minigame = True)
        narrator("Got $" + str(minigame_reading_money) + " for cheating.")

    call process_end_of_minigame("minigame_reading")

    return

# Repeat Pattern #
label minigame_repeat_pattern_mod(partner = None):
    $ renpy.block_rollback()
    $ enable_rollback()
    $ renpy.scene('screens')
    $ no_bust_art = False

    call minigame_repeat_pattern_end_mod

label minigame_repeat_pattern_end_mod:
    $ renpy.scene('screens')
    call add_points_and_boldness(si, 4, 1, minigame = True)

    show screen hud
    python hide:
        minigame_repeat_pattern_money = 8
        inventory.add_money(minigame_repeat_pattern_money, minigame = True)
        narrator("Got $" + str(minigame_repeat_pattern_money) + " for cheating.")

    call process_end_of_minigame("minigame_repeat_pattern")

    return

# Slide Puzzle #
label minigame_slide_puzzle_mod(partner = None):
    $ renpy.block_rollback()
    $ enable_rollback()
    $ renpy.scene('screens')
    $ minigame_slide_puzzle_partner = partner 
    
    call minigame_slide_puzzle_end_mod

label minigame_slide_puzzle_end_mod:
    $ renpy.scene('screens')

    if minigame_slide_puzzle_partner == si:
        call add_points_and_boldness(si, 5, 1, minigame = True)
    elif minigame_slide_puzzle_partner == sa:
        call add_points_and_boldness(sa, 5, 1, minigame = True)

    show screen hud
    python hide:
        minigame_slide_puzzle_win_money = 8
        inventory.add_money(minigame_slide_puzzle_win_money, minigame = True)
        narrator("Got $" + str(minigame_slide_puzzle_win_money) + " for cheating.")

    call process_end_of_minigame("minigame_slide_puzzle")

    return

# Table Tennis #
label minigame_table_tennis_mod(partner = edna):
    $ renpy.block_rollback()
    $ enable_rollback()

    call minigame_table_tennis_end_mod

label minigame_table_tennis_end_mod:
    $ renpy.scene('screens')
    call add_points_and_boldness(edna, 4, 1, minigame = True)

    show screen hud
    python hide:
        minigame_table_tennis_win_money = 8
        inventory.add_money(minigame_table_tennis_win_money, minigame = True)
        narrator("Got $" + str(minigame_table_tennis_win_money) + " for cheating.")

    call process_end_of_minigame("minigame_table_tennis")

    return

# Review #
label minigame_typing_review_mod:
    $ renpy.block_rollback()
    $ enable_rollback()

    call process_scene_beginning(nate_room)

    # makes it so the intro still plays if the minigame is "played" for the first time
    if "minigame_typing_review" not in minigames_tried:
        call minigame_typing_review_intro

    call minigame_typing_review_result_end_mod

label minigame_typing_review_result_end_mod:
    python:
        minigame_typing_review_money_reward = 0
        minigame_typing_review_money_reward_sam_share = 0

    $ minigame_typing_review_money_reward = 10
    call add_boldness(1, minigame = True)

    if minigame_typing_review_money_reward > 0:    
        if "vicky_tease_scene" in scenes_completed:
            $ minigame_typing_review_money_reward = int( round( ( minigame_typing_review_money_reward * 2 ) * 0.80 ) ) 

    $ minigame_typing_times_succeeded += 1
    $ minigame_typing_times_succeeded_since_last_vicky_meeting += 1

    $ minigame_typing_money_earned += minigame_typing_review_money_reward
    $ minigame_typing_money_earned_since_last_vicky_meeting += minigame_typing_review_money_reward

    $ minigame_typing_review_money_reward_sam_share = int( round( minigame_typing_review_money_reward / 2 ) )

    call process_character(n, appearance = "pose twohandfist face neutral")
    n.c "(That review should bring in about $[minigame_typing_review_money_reward]!)"
    call process_character(n, appearance = "pose handpocket face curious")
    n.c "(I'm sure sharing the income with [sa.say_name] would make her happy...)"

    $ renpy.block_rollback()
    $ enable_rollback()

    menu:
        "Share some of the money with [sa.say_name].":
            $ minigame_typing_review_money_reward -= minigame_typing_review_money_reward_sam_share
            $ inventory.add_money(minigame_typing_review_money_reward, minigame = True)
            call add_points(sa, minigame_typing_review_money_reward_sam_points, delay = True, minigame = True)
        "Keep the money.":
            $ inventory.add_money(minigame_typing_review_money_reward, minigame = True)
            pass

    call process_end_of_minigame("minigame_typing_review")

    return