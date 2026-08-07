# sam side story player-facing labels
#
# these labels keep the same base behavior, but swap in sam-safe bust art
# while the branch is active so the game doesn't go looking for nate.

init 9999 python:
    config.label_overrides["navigation_boldness_fail"] = "sam_side_story_navigation_boldness_fail"
    config.label_overrides["school_morning_wake_lines"] = "sam_side_story_school_morning_wake_lines"
    config.label_overrides["morning_wake_lines"] = "sam_side_story_morning_wake_lines"
    config.label_overrides["sleep_lines"] = "sam_side_story_sleep_lines"

label sam_side_story_navigation_boldness_fail:
    hide screen hud_zone_select

    if store.sam_side_story_mode:
        call process_character(sa, appearance = "outfit clothes pose handface face curious position right", text = "I'm not feeling {b}confident{/b} enough for that just yet...")
    else:
        call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious", text = "I'm not {b}confident{/b} enough to go there right now.")

    call navigation_menu
    return

label sam_side_story_school_morning_wake_lines:
    if not store.sam_side_story_mode:
        $ n.reset_appearance(show_bust = False)
        python:
            random_line_array = []
            random_line_array.append({"char": n, "appearance": "yea", "text": "Hope I'm not late."})
            random_line_array.append({"char": n, "appearance": "yea", "text": "Time for school."})

        call random_line(random_line_array)
        $ clear_characters(Dissolve(0.3))
        return

    $ sa.reset_appearance(show_bust = False)
    python:
        random_line_array = []
        random_line_array.append({"char": sa, "appearance": "outfit clothes pose handface face neutral", "text": "Okay... let's not be late."})
        random_line_array.append({"char": sa, "appearance": "outfit clothes pose handsbehind face happy", "text": "Time for school!"})

    call random_line(random_line_array)
    $ clear_characters(Dissolve(0.3))
    return

label sam_side_story_morning_wake_lines:
    if not store.sam_side_story_mode:
        $ n.reset_appearance(show_bust = False)
        if has_fucked_everyone_in_home:
            $ n.outfit = "nudesoft"
        else:
            $ n.outfit = "underwear"

        python:
            random_line_array = []
            random_line_array.append({"char": n, "appearance": "yea", "text": "{i}Yawn{/i}...A new day begins!"})
            random_line_array.append({"char": n, "appearance": "yea", "text": "Time to be up and about!"})
            random_line_array.append({"char": n, "appearance": "yea", "text": "Wonder what I should do today?"})
            random_line_array.append({"char": n, "appearance": "yea", "text": "Rested and ready to go for the day!"})

        call random_line(random_line_array)
        $ clear_characters(Dissolve(0.3))
        return

    $ sa.reset_appearance(show_bust = False)
    python:
        wake_lines_outfit = "underwear"
        if store.has_fucked_everyone_in_home:
            wake_lines_outfit = "nude"

        random_line_array = []
        random_line_array.append({"char": sa, "appearance": "outfit " + wake_lines_outfit + " pose handface face neutral", "text": "{i}Yawn{/i}... okay, I'm up!"})
        random_line_array.append({"char": sa, "appearance": "outfit " + wake_lines_outfit + " pose handsbehind face happy", "text": "Let's make today fun."})
        random_line_array.append({"char": sa, "appearance": "outfit " + wake_lines_outfit + " pose handface face curious", "text": "Ooooh, what am I doing today?"})
        random_line_array.append({"char": sa, "appearance": "outfit " + wake_lines_outfit + " pose leaning face happy", "text": "New day, let's go!"})

    call random_line(random_line_array)
    $ clear_characters(Dissolve(0.3))
    return

label sam_side_story_sleep_lines:
    if not store.sam_side_story_mode:
        $ n.reset_appearance(show_bust = False)
        python:
            sleep_lines_outfit = "underwear"
            if store.has_fucked_everyone_in_home:
                sleep_lines_outfit = "nudesoft"

            random_line_array = []
            random_line_array.append({"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Sleeep..."})
            random_line_array.append({"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Gotta get some rest..."})
            random_line_array.append({"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Alright, time for bed."})
            random_line_array.append({"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "My bed sure looks comfortable..."})

        call random_line(random_line_array)
        return

    $ sa.reset_appearance(show_bust = False)
    python:
        sleep_lines_outfit = "underwear"
        if store.has_fucked_everyone_in_home:
            sleep_lines_outfit = "nude"

        random_line_array = []
        random_line_array.append({"char": sa, "appearance": "outfit " + sleep_lines_outfit + " pose leaning face flirty", "text": "Mmm... sleepy time!"})
        random_line_array.append({"char": sa, "appearance": "outfit " + sleep_lines_outfit + " pose handface face flirty", "text": "I seriously need some sleep..."})
        random_line_array.append({"char": sa, "appearance": "outfit " + sleep_lines_outfit + " pose handsbehind face happy", "text": "All right, bed it is!"})
        random_line_array.append({"char": sa, "appearance": "outfit " + sleep_lines_outfit + " pose leaning face neutral", "text": "Yup, I'm definitely crashing."})

    call random_line(random_line_array)
    return
