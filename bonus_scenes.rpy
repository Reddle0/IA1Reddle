#label bonus_scene_progress:
#    $ clear_characters(Dissolve(0.3))
#    python:
#        stats.current_zone = advance_time_return_location.zone()
#        stats.current_location = advance_time_return_location

#    call day_reset_locations_chars
#    call nate_room_empty_leftovers

#    return

label process_end_of_bonus_scene(conversation_name, char, default = False):
    if started_main_game:
        $ clear_characters(Dissolve(0.3))
        python:
            stats.current_zone = advance_time_return_location.zone()
            stats.current_location = advance_time_return_location

        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        call debug_menu

    return

## Sam Intro ##
screen intro_title_leftovers_sam_mod:
    add Solid("#000")
    vbox:
        xalign 0.5
        if not persistent.use_incestral_awakening_name:
            text "Insexual" size 180 xalign 0.5
        else:
            text "Incestral" size 180 xalign 0.5

        text "Awakening:" size 180 xalign 0.5

        text "Sam's Awakening" size 180 xalign 0.5

label leftovers_bonus_scene_list:
    menu:
        "(Sam's Awakening) Intro":
            call intro_0_leftovers_sam_mod
        "(Sam's Awakening) Julia's Arrival":
            call julia_arrival_leftovers_sam_mod
        "(Sam's Awakening) Kira Conversations":
            call kira_convos_bonus_leftovers_sam_mod
        "(Sam's Awakening) Simone Conversations":
            call simone_convos_bonus_leftovers_sam_mod
        "(Sam's Awakening) Julia Conversations":
            call julia_convos_bonus_leftovers_sam_mod
        "(Sam's Awakening) Miscellaneous Conversations":
            call other_convos_bonus_leftovers_sam_mod
        "(Sam's Awakening) Stream Talk":
            call stream_talk_bonus_leftovers_sam_mod
        "Back":
            call nate_room_empty
            return

    return

label kira_convos_bonus_leftovers_sam_mod:
    menu:
        "Kira Conversation 1":
            call kira_convo_1_leftovers_sam_mod
        "Kira Conversation 2":
            call kira_convo_2_leftovers_sam_mod
        "Kira Conversation 3":
            call kira_convo_3_leftovers_sam_mod
        "Kira Conversation 4":
            call kira_convo_4_leftovers_sam_mod
        "Kira Conversation 5":
            call kira_convo_5_leftovers_sam_mod
        "Kira Conversation 6":
            call kira_convo_6_leftovers_sam_mod
        "Kira Conversation 7":
            call kira_convo_7_leftovers_sam_mod
        "Kira Conversation 8":
            call kira_convo_8_leftovers_sam_mod
        "Kira Conversation 9":
            call kira_convo_9_leftovers_sam_mod
        "Kira Conversation 10":
            call kira_convo_10_leftovers_sam_mod
        "Kira Conversation 11":
            call kira_convo_11_leftovers_sam_mod
        "Kira Conversation 12":
            call kira_convo_12_leftovers_sam_mod
        "Kira Conversation 13":
            call kira_convo_13_leftovers_sam_mod
        "Kira Conversation 14":
            call kira_convo_14_leftovers_sam_mod
        "Back":
            call nate_room_empty
            return

    return

label simone_convos_bonus_leftovers_sam_mod:
    menu:
        "Simone Conversation 1":
            call simone_convo_1_leftovers_sam_mod
        "Simone Conversation 2":
            call simone_convo_2_leftovers_sam_mod
        "Simone Conversation 3":
            call simone_convo_3_leftovers_sam_mod
        "Simone Conversation 4":
            call simone_convo_4_leftovers_sam_mod
        "Simone Conversation 5":
            call simone_convo_5_leftovers_sam_mod
        "Simone Conversation 6":
            call simone_convo_6_leftovers_sam_mod
        "Simone Conversation 7":
            call simone_convo_7_leftovers_sam_mod
        "Simone Conversation 8":
            call simone_convo_8_leftovers_sam_mod
        "Simone Conversation 9":
            call simone_convo_9_leftovers_sam_mod
        "Simone Conversation 10":
            call simone_convo_10_leftovers_sam_mod
        "Simone Conversation 11":
            call simone_convo_11_leftovers_sam_mod
        "Simone Conversation 12":
            call simone_convo_12_leftovers_sam_mod
        "Simone Conversation 13":
            call simone_convo_13_leftovers_sam_mod
        "Simone Conversation 14":
            call simone_convo_14_leftovers_sam_mod
        "Back":
            call nate_room_empty
            return

    return

label julia_convos_bonus_leftovers_sam_mod:
    menu:
        "Julia Conversation 1":
            call julia_convo_1_leftovers_sam_mod
        "Julia Conversation 2":
            call julia_convo_2_leftovers_sam_mod
        "Julia Conversation 3":
            call julia_convo_3_leftovers_sam_mod
        "Julia Conversation 4":
            call julia_convo_4_leftovers_sam_mod
        "Back":
            call nate_room_empty
            return

    return

label other_convos_bonus_leftovers_sam_mod:
    menu:
        "Janet Conversation":
            call janet_convo_leftovers_sam_mod
        "Edna Conversation":
            call edna_convo_leftovers_sam_mod
        "Back":
            call nate_room_empty
            return

    return

label stream_talk_bonus_leftovers_sam_mod:
    menu:
        "Stream Talk 1":
            call stream_talk_1_sam_mod_leftovers
        "Stream Talk 2":
            call stream_talk_2_sam_mod_leftovers
        "Stream Talk 3":
            call stream_talk_3_sam_mod_leftovers
        "Stream Talk 4":
            call stream_talk_4_sam_mod_leftovers
        "Stream Talk 5":
            call stream_talk_5_sam_mod_leftovers
        "Stream Talk 6":
            call stream_talk_6_sam_mod_leftovers
        "Stream Talk 7":
            call stream_talk_7_sam_mod_leftovers
        "Back":
            call nate_room_empty
            return

    return

label intro_0_leftovers_sam_mod:
    $ renpy.block_rollback()
    $ renpy.scene('screens')

    if wholesome_mode:
        call intro_4_leftovers_sam_mod

    call bust_art_background("bg black")
    $ play_music("audio/music/Daily_Music_01.ogg", fadein = 2.0, fadeout = 1.0)
    "{i}Beep! Beep! Beep!{/i}"
    "{i}Five more minutes...{/i}"
    "{i}Beep! Beep! Beep!{/i}"
    "{i}Mmph... Fine...{p=1.0}Yawn...{/i}"
    "{i}My ears are ringing..{p=1.0}I don't think I'll ever get used to alarm clocks.{/i}"
    "{i}“Do what you want, sleep when you want!”\nThat's my motto.{/i}"
    "{i}School sorta twists that thinking on its head a bit though.{/i}"
    "{i}Still...{p=1.0}I can't believe school went by just like that.{/i}"
    "{i}It's been a quick start to the summer, that's for sure!{/i}"
    "{i}It went by so fast.{/i}"

    call bust_art_background("bg family_portrait")
    "{i}Our old home got sold in a couple weeks.{/i}"
    "{i}And then moving trucks arrived a couple days later.{/i}"
    "{i}It hasn't been too long since we moved into this house.{/i}"
    "{i}It took a lot of effort, but we got there in the end.{/i}"

    $ process_character(si, "outfit clothes position right")
    "{i}All thanks to Mom!{/i}"
    "{i}Her name is [si.say_name].{/i}"
    "{i}She's always looking out for us.{/i}"
    "{i}A bit too much though, I think.{p=1.0}I've never seen her get any time to herself!{/i}"
    "{i}She's laid down a couple house rules, and asked us to keep things tidy in the new house.{/i}"
    "{i}She definitely can be stern at times...{p=0.5}Especially when it comes down to some things...{/i}"
    "{i}But she's as good a mom as any mom can be.{/i}"
    "{i}All in all, I think she's pretty awesome!{/i}"
    "{i}Speaking of awesome...{/i}"

    $ clear_characters()
    $ process_character(k, "outfit clothes position right")
    "{i}My big sis [k.say_name].{/i}"
    "{i}If \"awesome\" had a picture in the dictionary, it would be [k.say_name]!{/i}"
    "{i}And I do mean \"big\" sis.{/i}"
    "{i}She's amazing! And so tall!{/i}"
    "{i}I don't know how she does it.{/i}"
    "{i}Mom said she inherited some \"Amazon\" genes\nfrom our ancestors.{p=1.0}Whatever that means.{/i}"
    "{i}She's really good at sports.{p=0.5}I don't think I've ever seen her lose.{/i}"
    "{i}She's won practically every sport game she's ever played in.{/i}"
    "{i}You pick a sport, she'll kick your butt - no doubt about it!{/i}"
    "{i}She's proud of her trophies she won in those championships.{/i}"
    "{i}I think I even remember her trying out for the Olympics one time!{/i}"
    "{i}But I don't think it worked out for her.{/i}"
    "{i}She didn't want to talk about it after that.{/i}"
    "{i}She only mentioned the part where \"her breasts got too big and slowed her down.\"{/i}"
    "{i}It's a bummer. I wanted to cheer her on!{/i}"
    "{i}Now she works at the local gym as a fitness teacher.{/i}"
    "{i}I bet she still kicks everyone's butts there!{/i}"
    "{i}She says what she's thinking all the time.{p=1.0}I don't think Mom likes that, though.{/i}"
    "{i}Still, she's always got me and my brother's back when we need it!{/i}"
    "{i}Oh!{/i}"

    $ clear_characters()
    $ process_character(n, "outfit clothesjacket pose handpocket position right")
    "{i}My twin brother, [n.say_name].{/i}"
    "{i}It's always been me and [n.say_name] against the world.\nWe've never been apart.{/i}"
    "{i}Everything I like, he likes.{p=1.0}It's like looking in a mirror!{/i}"
    "{i}He's shy though.{p=0.5}He says he gets too nervous talking to other people.{/i}"
    "{i}That isn't us, I mean.\nHe only ever talks to family.{/i}"
    "{i}You can tell him anything, and he'll listen.{/i}"
    "{i}When I'm stressed, I always go to [n.say_name].{/i}"
    "{i}He's a good \"Player 2\"!{p=1.0}We play all sorts of video games together.{/i}"
    "{i}More often than not, we lose track of time when playing together!{/i}"

    $ clear_characters()
    $ process_character(sa, "outfit clothes position right")
    "{i}It's gonna be a fresh start with a new home. I can't wait!{/i}"
    "{i}I liked the old house, but don't get me wrong...{p=1.0}I love this new house!{/i}"
    "{i}We still haven't finished unpacking, though.{/i}"
    "{i}There's a lot of work to do, especially on my end.{/i}"
    "{i}The sooner everything is set up, the better.\n[n.say_name] and I will be good to go!{/i}"
    $ renpy.pause(1)
    "{i}I'll bet I'll meet lots of new people here.{/i}"
    "{i}Grandma lives in a beach house not too far away from us.{/i}"
    "{i}And our Auntie isn't too far away either.{/i}"
    $ renpy.pause(1)
    "{i}Basically, to sum all of this up, we're one happy family!{/i}"
    "{i}There's nothing we can't do together!{/i}"
    $ renpy.pause(1)

    "{i}And finally, last but certainly not least, we have me!{/i}"
    "{i}I'm always up to date on technology.{/i}"
    "{i}The internet helps me out a lot with that. It's really cool!{/i}"
    "{i}I tell [n.say_name] everything I learnt browsing.{/i}"
    "{i}I've even got a sneaky scheme of my own while we're here.{/i}"
    "{i}A [video_sharing_site] account, of course!{/i}"
    "{i}It's a place where you can share all kinds of awesome videos.{/i}"
    "{i}[n.say_name] and I are planning on doing a daily livestream over the summer using [video_sharing_site].{/i}"
    "{i}The site's got a big following, so we should get tons of viewers watching us!{/i}"
    "{i}We're also posting anime and video game reviews.{p=0.5}He'll start writing reviews for us soon.{/i}"
    "{i}I've been a busy bee setting up everything we need for our great summer plan.{/i}"
    "{i}And if we're lucky, we could do it all year round!{/i}"
    "{i}There's a saying people use on the internet.{p=1.0}\"The world is your oyster.\"{/i}"
    "{i}I think they may be right!{/i}"

    "Alright! Time to get moving, {color=[sa.color]}[sa.say_name] [last_name]{/color}!"

    $ stop_music(fadeout=3)
    $ quick_menu = False

    $ clear_characters()
    with Dissolve(0.5)
    show screen intro_title_leftovers_sam_mod
    with Dissolve(1.0)

label intro_05_leftovers_sam_mod:
    $ renpy.pause(1.5)
    call process_scene_beginning(bg = "bg sam_room_evening")
    $ play_music("audio/music/Lounge5.ogg", fadein = 2.0, fadeout = 1.0)

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "{i}Yawn...{/i}"

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "(I've never been up this late before)"

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "(But I'm just about done setting everything up!)"

    call process_character(sa, appearance = "outfit underwear pose handface face curious")
    sa.c "(So many updates I had to run...)"

    "{i}Dun-dun!{/i}"

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "(Oh! Finally!)"

    call process_character(sa, appearance = "outfit underwear pose handsbehind face neutral")
    sa.c "(Alright, moment of truth!)"

    call process_character(sa, appearance = "outfit underwear pose handsbehind face neutral")
    sa.c "(Here we go...)"

    $ renpy.pause(0.5)

    call process_character(sa, appearance = "outfit underwear pose handface face curious")
    sa.c "..."

    $ renpy.pause(0.5)

    call process_character(sa, appearance = "outfit underwear pose handface face happy")
    sa.c "(Yess!)"

    call process_character(sa, appearance = "outfit underwear pose handface face happy")
    sa.c "(I did it! {w=1.0}The computer gear is all set to go!)"

    call process_character(sa, appearance = "outfit underwear pose handface face happy")
    sa.c "(About time, that took a while!)"

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "(Still a couple things left to do yet, but we're almost there, I can feel it!)"

    call process_character(sa, appearance = "outfit underwear pose leaning face happy")
    sa.c "(The first-ever \"Twinsticks\" stream... I'm so excited!)"

#    $ scenes_completed.add("intro_05_leftovers_sam_mod")
    call intro_06_leftovers_sam_mod

label intro_06_leftovers_sam_mod:
    $ renpy.pause(1.5)
    $ play_music("audio/music/Daily_Music_03.ogg", fadein = 2.0, fadeout = 1.0)

    call process_scene_beginning(bg = "bg sam_room_daytime", char_tuple_array = [ (sa, "outfit underwear pose handface face neutral") ], force_bg_change = True)
    $ renpy.scene('screens')
    $ quick_menu = True

    $ renpy.pause(1)

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "{i}Yawn...{/i}"

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "(Good morning, world!)"

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "(New day, new me!)"

    call process_character(sa, appearance = "outfit underwear pose handface face happy")
    sa.c "({cps=40}How about it, [n.say_name]-){/cps}{w=0.75}{nw}"

    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit underwear pose handface face embarrassed")
    sa.c "([n.say_name]?)"

    call process_character(sa, appearance = "outfit underwear pose handsbehind face sad")
    sa.c "(Oh...)"

    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit underwear pose handsbehind face sad")
    sa.c "(I'm so used to...)"

    call process_character(sa, appearance = "outfit underwear pose handsbehind face concerned")
    sa.c "(It's weird not sharing a room with him)"

    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit underwear pose handface face concerned")
    sa.c "(Anyway...)"

    call process_character(sa, appearance = "outfit underwear pose handface face concerned")
    sa.c "(I'd better get dressed for the day)"

    call process_character(sa, appearance = "outfit underwear pose handface face concerned")
    sa.c "(Mom told me my clothes are in this drawer)"

    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "(There!)"

    call character_leave_dissolve(sa)

    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit clothes pose handface face neutral")
    sa.c "(Hum-hum-hum...)"

    call process_character(sa, appearance = "outfit clothes pose handsbehind face neutral")
    sa.c "{cps=40}Actually, my hair looks a little messy, maybe I should-{/cps}{w=0.75}{nw}"

#    $ scenes_completed.add("intro_06_leftovers_sam_mod")
    call intro_1_leftovers_sam_mod

label intro_1_leftovers_sam_mod:
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    $ n.c_full("Hey.")

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Oh hey [n.say_name]!"

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "Just wanted to see how you were doing."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Aw, thanks for checking on me."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "We shared a room for all our lives, and now we each have our own."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "At least we are right next to each other."

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "That's true."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "I was up late last night setting up all the computer gear."

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "Oh?"

    call process_character(n, appearance = "pose handfist face neutral")
    n.c "Can we stream yet?"

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "Almost!"

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "Can't waste any time when trying to build a following."

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "(Yup, it can't wait!)"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "The stream will be up and running tomorrow."

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "It's gonna be so much fun!"

#    call process_character(sa, appearance = "pose handface face neutral")
#    sa.c "(Speaking of which...)"

#    "{i}Invite [n.say_name] to join you for some game streaming?{/i}"

#    menu:
#        "Yeah!":
#            $ n.add_points(1, tag = "intro_1_sam_join_streaming")
#            call process_character(sa, appearance = "pose leaning face happy")
#            sa.c "Aww yeah!\nOur stream channel is a go!"

#        "Not right now.":
#            call process_character(n, appearance = "pose handpocket face neutral")
#            call process_character(sa, appearance = "pose handsbehind face neutral")
#            sa.c "Well, hopefully you can hop in when you get a chance."

    $ renpy.pause(1)

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Anyway, Mom's probably waiting for us downstairs."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Hope she's making omelettes!"

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "(My favorite!)"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "We can talk about what we're gonna do for our first stream later, [n.say_name]."

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "Let's move before [k.say_name] gobbles them all down!"

#    $ scenes_completed.add("intro_1_leftovers_sam_mod")
    call intro_2_leftovers_sam_mod
    return

label intro_2_leftovers_sam_mod:
    call process_scene_beginning(bg = "bg kitchen_daytime")

    $ sa.position = "left"
    $ k.position = "right"
    $ si.position = "right"
    $ n.position = "right"

    call process_character(si, appearance = "outfit clothes pose handsfront face happy")
    $ si.c_full("It's first come, first serve!")

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "Egg white omelettes, with fresh spinach and tomato..."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "Rye bread from the bakery..."

    call process_character(si, appearance = "pose handsup face happy")
    si.c "And milk and orange juice. Take your pick!"

    call process_character(sa, appearance = "outfit clothes pose handface face happy", replace = True)
    sa.c "(Oooh, OJ! Sweet!)"

    call process_character(sa, appearance = "pose leaning face happy", replace = True)
    sa.c "I call dibs on the omelettes and orange juice!"

    call character_leave_dissolve(sa)

    $ renpy.pause(1)

    $ display_multiple_characters([ (si, "outfit clothes pose handsfront face neutral blush false"), (n, "outfit clothesjacket pose twohandfist face neutral blush false position left") ])

    call process_character(n, appearance = "pose twohandfist face neutral")
    n.c "This breakfast is so great!"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "Glad you like it!\n[k.say_name] suggested the recipe."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral", replace = True)
    $ k.c_full("It gives a lot of nutrition.")

    call process_character(k, appearance = "outfit clothes pose armsup face neutral")
    k.c "Which I need to keep these guns loaded."

    call character_leave_dissolve(n)

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "(Guns...?)"

    call process_character(n, appearance = "pose handpocket face curious", replace = True)
    n.c "We don't have any guns in the house?"

    call character_leave_dissolve(k)

    call process_character(si, appearance = "pose armunder face happy")
    si.c "Haha, it's just an expression [n.say_name]!"

    call character_leave_dissolve(n)
    call character_leave_dissolve(si)
    $ renpy.pause(1)

    call process_character(sa, appearance = "pose handface face happy", replace = True)
    sa.c "(Alright, enough munchies! It's fun-time!)"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Mom!\nIs the pool ready yet?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "Almost, sweetie.{p=1.0}I've scheduled a technician to stop by to fix the pump."

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "Yess!"

    $ n.position = "right"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "[n.say_name], we should see who can swim from one end of the pool to the other without taking a breath!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "(I've got this in the bag. You just watch, [n.say_name]!)"

    call character_leave_dissolve(si)

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "Well uh..."

    call character_leave_dissolve(sa)
    $ k.position = "left"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Gotta work on increasing your lung capacity [n.say_name]!"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "You don't want to get beat by a girl do you?"

    $ n.position = "right"

    call process_character(n, appearance = "pose handpocket face concerned")
    n.c "What do you mean?{p=1.0}You've beaten every boy you've swam against."

    call process_character(k, appearance = "pose handhip face happy")
    k.c "I'm just teasing."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "But seriously I can't wait for that pool to be up and running."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "The climate here is a lot warmer."

    call character_leave_dissolve(n)

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Now that we live close to Grandma, we'll have to see if we can visit her at the beach some time!"

    call character_leave_dissolve(k)

    call process_character(sa, appearance = "pose leaning face neutral",  replace = True)
    sa.c "(Her cookies are the best!)"

    $ renpy.pause(1)

    call process_character(si, appearance = "pose handsfront face neutral",  replace = True)
    si.c "So what's everyone's plan for the day?"

    call process_character(sa, appearance = "pose handsbehind face curious", replace = True)
    sa.c "(Hmm...)"

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "(What should I do today...?)"

    $ k.position = "right"

    call process_character(k, appearance = "pose handhip face concerned", replace = True)
    k.c "I gotta head out to work."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "But I'm looking forward to some cardio training!"

    call process_character(sa, appearance = "pose handface face curious", replace = True)
    sa.c "Since the pool's not up yet..."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "(Oh, I know!)"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "I'll play some video games!"

    $ n.position = "left"

    call character_leave_dissolve(sa)

    call process_character(n, appearance = "pose handpocket face neutral")

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "What's your plan [n.say_name]?"

    call character_leave_dissolve(n)

    call process_character(sa, appearance = "pose handface face neutral",  replace = True)
    sa.c "(Say video games, say video games...)"

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "(But maybe he has something else planned for today)"

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "(Like helping Mom with moving the last of the boxes)"

#    $ scenes_completed.add("intro_2_leftovers_sam_mod")

    python:
        random_line = random.randint(1, 3)

    if random_line == 1:

        $ n.position = "right"

        call process_character(n, appearance = "pose handpocket face neutral")
        n.c "I'll relax outside in the sun."

        call character_leave_dissolve(sa)
        $ si.position = "left"

        call process_character(si, appearance = "pose handsfront face neutral")
        si.c "Remember to put sunscreen on!"

        call character_leave_dissolve(n)
        call character_leave_dissolve(si)

        call process_character(sa, appearance = "pose handsbehind face neutral", replace = True)
        sa.c "(Aww... {w=1.0}I can still have fun solo, though!)"

        call intro_3_didnt_choose_leftovers_sam_mod
    elif random_line == 2:

        $ n.position = "right"

        call process_character(n, appearance = "pose handpocket face neutral")
        n.c "{b}I'll play some video games with {color=[sa.color]}[sa.say_name]{/color}!{/b}"

        $ n.add_points(1, tag = "intro_2_what_plan_sam")

        call process_character(sa, appearance = "pose leaning face happy")
        sa.c "All right! Co-op mode!"

        call process_character(sa, appearance = "pose leaning face happy")
        sa.c "(And I know just the game!)"

        call intro_3_chose_sam_leftovers_sam_mod
    else:

        $ n.position = "right"

        call process_character(n, appearance = "pose handpocket face neutral")
        n.c "I'll move some more storage boxes with you {color=[si.color]}Mom{/color}."

        call character_leave_dissolve(sa)
        $ si.position = "left"

        call process_character(si, appearance = "pose handsup face happy")
        si.c "Thank you [n.say_name]!"

        call process_character(si, appearance = "pose handsup face happy")
        si.c "I could use some help with it!"

        call character_leave_dissolve(n)

        call process_character(sa, appearance = "pose handsbehind face concerned", replace = True)
        sa.c "(It'd be nice to help, but they're... {w=1.0}so heavy...)"

        call process_character(sa, appearance = "pose handsbehind face concerned")
        sa.c "([k.say_name] had to take over for me)"

        call process_character(sa, appearance = "pose handsbehind face concerned")
        sa.c "(I felt bad, but she didn't mind)"

        call process_character(sa, appearance = "pose handsbehind face neutral")
        sa.c "(Oh well... {w=1.0}I can still have fun solo, though!)"

        call intro_3_didnt_choose_leftovers_sam_mod

    return

label intro_3_didnt_choose_leftovers_sam_mod:
    call fade_to_black(1)
    "{i}One Hour Later...{/i}"

    call static_still_ctc("bg sam_1_sam_playing")

    call process_character(sa)
    sa.c "(Man, this game got so many good reviews!)"

    call process_character(sa)
    sa.c "(I think I see why now)"

    call process_character(sa)
    sa.c "([n.say_name] doesn't know what he's missing!)"

    call process_character(sa)
    sa.c "(I'll see about reeling him in to play some co-op next time)"

#    $ scenes_completed.add("intro_3_didnt_choose_leftovers_sam_mod")
    call intro_4_leftovers_sam_mod

    return

label intro_3_chose_sam_leftovers_sam_mod:
    call process_scene_beginning(bg = "bg sam_room_daytime", char_tuple_array = [ (sa, "outfit clothes pose handface face neutral blush false position left"), (n, "outfit clothesjacket pose handpocket face neutral blush false position right") ])

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "This game got so many good reviews."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "I watched GameGrinch play through the first hour."

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "\"Soultwister.\""

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Yeah, it's a shmup."

    call process_character(n, appearance = "pose handpocket face curious")
    n.c "A shmup?"

    call process_character(sa, appearance = "pose leaning face curious")
    sa.c "(Ah, yeah, that's right)"

    call process_character(sa, appearance = "pose leaning face curious")
    sa.c "[n.say_name] doesn't know much about them)"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Oh uh, it's a term online they use to describe those top down shooter games."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "\"Shoot-em-up.\""

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "\"Shmup.\""

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "(Say that five times fast!)"

    call process_character(n, appearance = "pose handpocket face happy")
    n.c "Ooh, I see."

    call process_character(n, appearance = "pose handfist face happy")
    n.c "So how does co-op mode work?"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "(I'm glad you asked!)"

    call process_character(n, appearance = "pose handpocket face neutral")
    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "We both control one ship."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "One person controls the ship's movement.\nThe other uses the weapons."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "So we have to coordinate our attacks."

    call process_character(n, appearance = "pose handpocket face happy")
    n.c "That sounds pretty cool."

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Did you want to control movement or weapons?"

    call process_character(sa, appearance = "pose leaning face curious")
    sa.c "(Wonder what he'll pick...)"

    python:
        random_line = random.randint(1, 3)

    if random_line == 1:
        call process_character(n, appearance = "pose twohandfist face neutral")
        n.c "I'll handle the movement."

        call process_character(sa, appearance = "pose leaning face neutral")
        sa.c "I'll blast the enemies with my laser weapons!"
    elif random_line == 2:
        call process_character(n, appearance = "pose twohandfist face neutral")
        n.c "I'll handle the weapons."

        call process_character(sa, appearance = "pose handface face curious")
        sa.c "Time to show off my dodging skills!"
    else:
        call process_character(n, appearance = "pose behindhead face neutral")
        n.c "{b}You can pick instead.{/b}"

        $ n.add_points(1, tag = "intro_3_chose_sam_controls_leftovers_sam_mod")

        call process_character(sa, appearance = "pose handsbehind face neutral blush true")
        sa.c "Aw, thanks!"

        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "(That made me blush a little...)"

        call process_character(sa, appearance = "pose handsbehind face happy blush false")
        sa.c "Alright, I'll choose random!"

    call process_character(n, appearance = "pose handpocket face neutral")
    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Okay, almost ready."

    call process_character(sa, appearance = "pose leaning face curious")
    sa.c "(Hmm... {w=1.0}What difficulty should we go with...)"

    call process_character(sa, appearance = "pose leaning face curious")
    sa.c "(How about...)"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "I think we'll go with normal difficulty for now."

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "(I'll let [n.say_name] get used to the controls first)"

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "How many achievements are in this game?"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Oh an insane amount!\nYou can unlock like, I think 40 different weapons."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "It's crazy."

    call process_character(n, appearance = "pose twohandfist face happy")
    n.c "Well, might as well start unlocking them!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "(That's the spirit!)"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "I know Eric on GameGrinch found a secret weapon on the first level."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "I think I remember where it is.{p=1.0}We have to blow up a rock blocking a cave."

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "Just let me know when you see it."

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "You got it."

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "And game is launched!"

#    $ scenes_completed.add("intro_3_chose_sam_leftovers_sam_mod")
    call intro_4_leftovers_sam_mod

    return

label intro_4_leftovers_sam_mod:
    $ stop_music(fadeout=3)
    $ week.time = "night"
    call process_scene_beginning(sam_room)

    $ temp_variable = "kira"
    python:
        if "intro_3_chose_sam" in scenes_completed:
            temp_variable = "sam"
        if "intro_3_chose_simone" in scenes_completed:
            temp_variable = "simone"
#    $ stop_music(fadeout=3)
#    call process_scene_beginning(bg = "bg sam_room_evening")

#    $ temp_variable = "sam"
#    python:
#        if "intro_3_didnt_choose_sam_mod" in scenes_completed:
#            temp_variable = "kirasimone"

    if temp_variable == "kirasimone":
        call process_character(sa, appearance = "outfit underwear pose handface face neutral")
        sa.c "(That game was a lot of fun!)"

        call process_character(sa, appearance = "outfit underwear pose handsbehind face concerned")
        sa.c "(Too bad [n.say_name] didn't join, though)"

        call process_character(sa, appearance = "outfit underwear pose handsbehind face concerned")
        sa.c "(He would have loved it!)"

        call process_character(sa, appearance = "outfit underwear pose handsbehind face embarrassed")
        sa.c "(The final boss was the hardest one ever!)"
    if temp_variable == "sam":
        call process_character(n)
        n.c "Goodnight [sa.say_name]."

        call process_character(sa, appearance = "outfit underwear pose leaning face neutral")
        sa.c "G'night, [n.say_name]!"

        call process_character(sa, appearance = "outfit underwear pose handface face neutral")
        sa.c "(It's fun playing with [n.say_name] again!)"

        call process_character(sa, appearance = "outfit underwear pose handface face neutral")
        sa.c "(We had a ton of fun!)"

        call process_character(sa, appearance = "outfit underwear pose handface face concerned")
        sa.c "(Shame about the final boss, though)"

        call process_character(sa, appearance = "outfit underwear pose handface face concerned")
        sa.c "(Man, that was hard!)"

    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit underwear pose handface face embarrassed")
    sa.c "(Oh! The stream! I almost forgot!)"

    call process_character(sa, appearance = "outfit underwear pose handface face embarrassed")
    sa.c "(I should get that set up ASAP!)"

    call process_character(sa, appearance = "outfit underwear pose leaning face happy")
    sa.c "(Gotta make sure it's ready to broadcast to the world!)"

    call fade_to_black(1)
    "{i}One Hour Later...{/i}"
    call process_scene_beginning(bg = "bg sam_room_evening")

    call process_character(sa, appearance = "outfit underwear pose handface face happy")
    sa.c "And... {w=1.0}there we go!"

    call process_character(sa, appearance = "outfit underwear pose handface face happy")
    sa.c "This was definitely a busy day for me!"

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "But my eyes are still wide-open!\nNo way am I ready for bed just yet."

    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit underwear pose handface face curious")
    sa.c "(Hmm...)"

    call process_character(sa, appearance = "outfit underwear pose handface face curious")
    sa.c "(What to do...)"

    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit underwear pose handface face neutral")
    sa.c "Ooh, maybe I could see what everyone else is up to!"

    call character_leave_dissolve(sa)

    "{i}Welcome to \"Sam's Awakening!\"{/i}"
    "{i}This mod - as the name suggests - implements Sam (Nate's twin sister) as a playable character.{/i}"
    "{i}However, an option has been provided at the start of a new game to still have the option to play as Nate for the vanilla experience if you wish to do that.{/i}"
    "{i}When playing as Sam, several things will change.\nFor instance, all thoughts and feelings are from her point of view (POV) instead of Nate's.{/i}"
    "{i}All options previously found in Nate's bedroom will now be instead be found in Sam's bedroom when playing as her.{/i}"
    "{i}Numerous dialogue changes, additions and other miscellaneous changes to gameplay have also been included to account for a playable Sam.{/i}"
    "{i}The relationship between Sam and the others will be different compared to their relationship with Nate. Expect different dynamics.{/i}"
    "{i}Each day you'll have the opportunity to explore and interact with characters.{/i}"
    "{i}Part of this interaction includes mini-games, which are the primary method of building relationships.{/i}"
    "{i}There are also unique events that can increase relationship with a character.{/i}"
    "{i}As your relationship grows, special scenes will become available for that character!{/i}"
    "{i}Each relationship level unlocks a new scene.{/i}"
    "{i}You are free to choose who you want to have relationships with!{/i}"
    "{i}Some situations will require \"Boldness.\"{/i}"
    "{i}Boldness is an important attribute to accumulate.{/i}"
    "{i}Boldness can be increased through certain scenes and mini-games.{/i}"
    "{i}Try to discover these scenes and mini-games!{/i}"
    "{i}As you level up your Boldness, you'll have the potential to perform new actions, or explore new locations.{/i}"
    "{i}Exclusive to this mod are two options.\n\"Browse\" the internet, to learn more about the strange events that await Sam...{/i}"
    "{i}And \"Stream Chat\" to see what's got the chat members of Sam's stream buzzing!{/i}"
    "{i}\"Browse\" is accessible at any time. \"Stream Chat\" is unlocked after the first time the stream goes live.{/i}"
    "{i}Both of these options are found in Sam's bedroom.\nBe sure to check these often after reaching certain points in the story!{/i}"
    "{i}\"FAQ\" and \"Changelog\" options are also available to read here as well.{/i}"
    "{i}Finally, feel free to explore to your heart's content, and enjoy playing \"Sam's Awakening!\"{/i}"

    call day_reset_locations_chars
    call day_start_after_location_reset

    return

label julia_arrival_leftovers_sam_mod:
#    $ renpy.pause(1)
    $ play_music("audio/music/Daily_Music_03.ogg", fadein = 2.0, fadeout = 1.0)

    $ sa.position = "left"
    $ n.position = "right"
    $ julia.position = "right"

    call process_scene_beginning(bg = "bg sam_room_daytime", char_tuple_array = [ (sa, "outfit clothes pose handface face embarrassed blush false"), (n, "outfit clothesjacket pose behindhead face concerned blush false position right") ])

    call process_character(sa, appearance = "outfit clothes pose handface face embarrassed blush false")
    sa.c "She's not going on the stream?!"

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "No."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "She said she doesn't like video games that much."

    call process_character(sa, appearance = "outfit clothes pose handsbehind face concerned blush false")
    sa.c "Aw man, and we had everything planned out!"

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Yeah, it's too bad."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "...{p}..."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "So she's not into video games at all huh?"

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "What does she like?"

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "Did she tell you?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "She just told me she was going to read a book."

    call process_character(sa, appearance = "outfit clothes pose handface face angry blush false")
    sa.c "Read a book?!"

    call process_character(sa, appearance = "outfit clothes pose handface face angry blush false")
    sa.c "Ugh!"

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "I guess she's different now than we remember."

    call process_character(sa, appearance = "outfit clothes pose handsbehind face angry blush false")
    sa.c "I'll say!"

    call process_character(sa, appearance = "outfit clothes pose handsbehind face angry blush false")
    sa.c "Since when did she like reading books?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "She dresses differently too."

    call process_character(sa, appearance = "outfit clothes pose handface face curious blush false")
    sa.c "..."

    call process_character(sa, appearance = "outfit clothes pose handface face curious blush false")
    sa.c "Dresses different?"

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "Well, I'd just go see for yourself."

    call process_character(sa, appearance = "outfit clothes pose handface face curious blush false")
    sa.c "..."

    call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false")
    sa.c "Sounds like she needs some more fun introduced into her schedule!"

    call process_character(sa, appearance = "outfit clothes pose leaning face happy blush false")
    sa.c "And I'm just the one to do it!"

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "(Good luck...)"

    call fade_to_black(1)

    python hide:
        for char in character_list():
            char.position = "right"

    call process_scene_beginning(bg = living_room)
    $ display_multiple_characters([ (sa, "outfit clothes pose handsbehind face concerned blush false position left") ])

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "...{p}..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "(Man, she really is reading a book)"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "(That's so unlike her!)"

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "(She used to pull a funny face when looking at them)"

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "(And she really is dressed differently too, just like [n.say_name] said)"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "(She hasn't noticed me yet)"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "(I know what will get her attention!)"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "Guess who?"

    call process_character(julia, appearance = "outfit clothes pose handup face angry blush false position right")
    julia.c "{cps=40}Ugh, I'm trying to-{/cps}{w=0.75}{nw}"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "Hellooo, [julia.say_name]!"

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "[sa.say_name]..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Hehe, long time no see!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I'm so happy to see you, [julia.say_name]!"

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "Did you just try to pull a prank on me?"

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "Sure did!"

    call process_character(julia, appearance = "pose handup face embarrassed blush false")
    julia.c "By covering my eyes with your hands?"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "Yup!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "([sa.say_name] hasn't changed one bit, I see)"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "So, how have you been?"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "Okay."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "What have you been up to?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Anything cool?"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "No."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Ooh, I like what you've done with yourself!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "You look really cool!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Thanks."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "You know, I've been looking forward to seeing you again this whole time!"

    call process_character(sa, appearance = "pose handface face embarrassed blush false")
    sa.c "I hardly slept!"

    call process_character(julia, appearance = "pose handface face curious blush false")
    julia.c "..."

    call process_character(sa, appearance = "pose handface face embarrassed blush false")
    sa.c "(Is she... {w=1.0}not happy to see me?)"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "Hey [julia.say_name], something about you seems... {w=1.0}different..."

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "No, everything about you is different!"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "Your hair, your makeup, your outfit, even the way you speak!"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "You never liked reading books."

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "What gives with that?"

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "What made you change your mind all of a sudden?"

    call process_character(julia, appearance = "pose handup face concerned blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose handup face concerned blush false")
    julia.c "[sa.say_name]..."

    call process_character(julia, appearance = "pose handup face concerned blush false")
    julia.c "I'm sorry, but..."

    call process_character(julia, appearance = "pose handup face concerned blush false")
    julia.c "I've changed a lot about myself since we last saw each other."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I want to come across as mature."

    call process_character(julia, appearance = "pose handface face concerned blush false")
    julia.c "I'm afraid I'm no longer the person you knew anymore."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "I see..."

    call process_character(julia, appearance = "pose handface face concerned blush false")
    julia.c "Yeah."

    call process_character(julia, appearance = "pose handface face concerned blush false")
    julia.c "(I knew this was going to be difficult)"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Well, I don't really mind either way!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "You don't need to act mature around me."

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "All that matters is that we have fun, right?"

    call process_character(julia, appearance = "pose handup face concerned blush false")
    julia.c "..."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "So what video games do you wanna play?"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "No, better yet, let's have a gaming marathon!"

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "{cps=40}Because it's all planned out for the stream, so whenever you're-{/cps}{w=0.75}{nw}"

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "I'm just not interested in video games, [sa.say_name]."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I prefer to read instead."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "And as I've already said to [n.say_name], I'd rather not appear on a stream."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "I've never been comfortable in front of cameras."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "We both know that."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "I also didn't want to disturb you up there, either."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I thought you were busy playing a game."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "Right, yeah..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "Sorry..."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Don't worry about it."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I told [n.say_name] I was down here in the living room anyways."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "..."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "It was good seeing you again, [sa.say_name]."

    call process_character(julia, appearance = "pose handface face happy blush false")
    julia.c "Even though we'll be seeing a lot of each other over the summer."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "Yeah..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "I-It's good to see you too, [julia.say_name]..."

    call character_leave_dissolve(sa)
    pause 0.5

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    sa.c "..."

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    sa.c "(I hope I didn't upset her)"

    call process_new_location(bg = sam_room)
    call process_character(sa, appearance = "outfit clothes pose handsbehind face concerned blush false")
    sa.c "(Wow, she really has changed)"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "([n.say_name] wasn't kidding when he said she's \"different now than we remember.\")"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "(I almost didn't recognise her when I first walked into the room)"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "Guess that means I need to get to know her again)"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "(The \"new\" [julia.say_name])"

    $ reset_all_characters()
    call day_reset_locations_chars
    call day_start_after_location_reset

    return

## Sam Kira Convos ##
label kira_convo_1_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes position left"), (k, "outfit clothes pose armsup face happy position right") ])

    call process_character(k, appearance = "pose armsup face happy")
    k.c "Keeping it real, sis!"

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "Huh?"

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "Keeping it.. {w=1.0}real?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Uh, it's a saying."

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "It's new to me."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "You pick up on a ton of new sayings when you're around others."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "I've learnt two just this past week!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Uh-huh..."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Anyway, the phrase is basically another way of saying you like to chill."

    call process_character(k, appearance = "pose armsup face happy")
    k.c "And who wouldn't want to hang out and chill with me?"

    call process_character(k, appearance = "pose armsup face happy")
    k.c "You're definitely \"keeping it real\" in that regard, ha!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Haha, yeah!"

    call process_end_of_bonus_scene("kira_convo_1_leftovers_sam_mod", k)

    return

label kira_convo_2_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes position left"), (k, "outfit clothes pose armcross position right") ])

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "So, how's it feel to have your own room now?"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "It's nice."

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "But it's weird not sharing the same room."

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "I really am missing [n.say_name] sleeping next to me."

    call process_character(k, appearance = "pose handhip face concerned")
    k.c "Yeah, I can imagine."

    call process_character(k, appearance = "pose handhip face concerned")
    k.c "When I was your age, I couldn't get used to sleeping on my own."

    call process_character(k, appearance = "pose handhip face concerned")
    k.c "Ended up sleeping in Mom's bed a lot."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Wow, I didn't know that."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Yeah, I was afraid of being on my own."

    call process_character(k, appearance = "pose handhip face embarrassed")
    k.c "Still kind of am, but, uh, don't tell anyone about that part."

    call process_character(k, appearance = "pose armsup face embarrassed")
    k.c "I prefer having company."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Your rooms are right next to each other, so you can pop in and see each other whenever you want."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "I heard you two are going to stream live to people or something like that?"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "Yup!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "We have our channel on [video_sharing_site], \"Twinsticks.\""

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Games, reviews, livestreaming, you name it!"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "{i}\"Twin\"{/i}sticks..."

    call process_character(k, appearance = "pose armsup face happy")
    k.c "Nice one, sis."

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "Hehe, it was my idea on that one!"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "I don't keep up much with technology like that anymore, though."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "We will!"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "I mostly just search for stuff online."

    call process_character(k, appearance = "pose armcross face neutral")
    $ k.c("Think you and " + n.say_name + " will get popular?")

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "I hope so!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "But we're still in the early days yet."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "We got plans [k.say_name]!"

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "Big plans!"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Oh yeah?"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "How big are we talking here?"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "We're gonna be really famous some day, I just know it!"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Wow."

    call process_character(k, appearance = "pose armcross face happy")
    k.c "That's certainly ambitious."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Well, I'm sure you'll get there someday."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "You two work off each other well."

    call process_character(k, appearance = "pose armsup face happy")
    k.c "And soon enough other people will see that!"

    call process_end_of_bonus_scene("kira_convo_2_leftovers_sam_mod", k)

    return

label kira_convo_3_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes position left"), (k, "outfit clothes pose handhip position right") ])

    call process_character(sa)
    sa.c "Do you miss your old school [k.say_name]?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Nah."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "I mean it was fun, don't get me wrong."

    call process_character(k, appearance = "pose handhip face happy")
    k.c "Wiping the floor against other school teams was glorious."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "But now I don't have to worry about school work anymore."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "I can focus on building a career."

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Oh yeah?"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "I do have plenty of sports experience."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "I could probably be qualified to be a football or basketball coach if I wanted."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Nah, you'd get bored and wanna play!"

    call process_character(k, appearance = "pose armcross face happy")
    k.c "Ha, yeah.{p=1.0}You're right on that one, sis."

    call process_character(k, appearance = "pose armcross face happy")
    k.c "Maybe I could be the first coach and active player in sports!"

    call process_end_of_bonus_scene("kira_convo_3_leftovers_sam_mod", k)

    return

label kira_convo_4_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handsbehind position left"), (k, "outfit clothes pose armcross position right") ])

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "What happens at work when it's quiet anyway?"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "What do you mean?"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "You know, when there's not many people exercising."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "What, you think the equipment goes to waste?{p=1.0}I sure as shit will make sure it doesn't!"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "I'll just exercise myself with the free equipment."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Wouldn't you get in trouble for that?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "With who?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Everyone who works there needs to keep fit."

    call process_character(sa, appearance = "pose handface face neutral")

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "We also trade advice on proper form and techniques for stretching and lifting weights."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "The last time we had a quiet day, I learned the proper exercise for your \"rotator cuff\"."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Rotator... {w=1.0}cuff?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Oh uh, it's a muscle on the back side of your shoulder."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "It's very important for baseball pitchers and shot putters!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Do you get a lot of customers [k.say_name]?"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "You bet."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Sometimes we have people come in and not use the equipment at all."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "They just want to \"observe\" my form."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "So they don't exercise themselves?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Oh, I'm sure they do exercises at home."

    call process_character(k, appearance = "pose handhip face happy")
    k.c "But they likely only train one {i}\"muscle\"{/i}... {w=1.0}many times over."

    call process_character(sa, appearance = "pose handsbehind face curious")

    $ renpy.pause(1)

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "...{p}..."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "I don't quite get it, but I'm happy for them either way!"

    call process_end_of_bonus_scene("kira_convo_4_leftovers_sam_mod", k)

    return

label kira_convo_5_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes position left"), (k, "outfit clothes pose armcross position right") ])

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "So this Reflux... {w=0.5}Vision... {w=1.0}Reflex..."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "[video_sharing_site]?"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Yeah... {w=1.0}that."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "What's it about, anyway?"

    call process_character(sa, appearance = "pose handface face neutral")

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "You talk about it all the time, but what's the attraction?"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "So it's really cool."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "You can share all sorts of stuff on there!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Funny videos, video game reviews..."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Reviews?"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Yeah, you get a \"critique\" of something!"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "You know, see if it's any good or not before you play it."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Can't you find that out for yourself though?"

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Well, I guess you could, but..."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "If everyone agrees something's bad and it gets bad reviews, then it's gotta be bad, right?"

    call process_character(k, appearance = "pose handhip face concerned")
    k.c "Eh, not always, sis."

    call process_character(k, appearance = "pose handhip face concerned")
    k.c "Maybe no one's giving it a fair chance."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "But I could care less about what everyone else thinks."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "I prefer to stand out from the crowd."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "If they go one way, I go the other."

    call process_character(k, appearance = "pose armcross face happy")
    k.c "Guess you could say I live... {w=0.5}dangerously!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "Haha! Kira {i}\"the Rebel\"{/i}!"

    call process_character(k, appearance = "pose armcross face happy")
    k.c "You know it!"

    call process_character(k, appearance = "pose armcross face happy")
    k.c "And don't you forget it!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "But yeah, it can also work the other way around."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "So if trustworthy reviewers says it's good..."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Then it's worth a look, isn't it?"

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "Yup!"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "It's all about that publicity."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "The more reviews, the better!"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Plus I just like hearing what others have to say."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "It creates engaging discussions."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "People trust reviews, after all."

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "And that brings in the views!"

    call process_character(k, appearance = "pose armsup face happy")
    k.c "Sounds like you've got your work cut out for you then."

    call process_end_of_bonus_scene("kira_convo_5_leftovers_sam_mod", k)

    return

label kira_convo_6_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes position left"), (k, "outfit clothes pose armsup position right") ])

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "So...{p=1.0}How did you like the squat challenge?"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Was it fun keeping count as I broke a milestone?"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Yeah!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "I can't believe you reached a hundred and fifty squats!"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "That's what happens when you keep pushing."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "You reach bigger milestones before you know it."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "You think I had good form?"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "It looked like \"good form\" to me!"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "I bet you would say that even if it wasn't."

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "I certainly would!"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Well, my legs were well spaced.{p=1.0}And my back was straightened too."

    $ renpy.pause(2)

    call process_character(k, appearance = "pose armsup face flirty")
    k.c "Butt was sticking out..."

    call process_character(sa, appearance = "pose leaning face embarrassed")
    sa.c "Haha, y-yeah..."

    call process_character(sa, appearance = "pose leaning face embarrassed")
    sa.c "It seemed good to me."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Maybe it wasn't sticking out far enough, though."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "I wasn't completely sure."

    call process_character(k, appearance = "pose handhip face flirty")
    k.c "I figured you'd be able to let me know, sis."

    call process_character(sa, appearance = "pose handface face embarrassed blush true")

    $ renpy.pause(1)

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "It was sticking out."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "So it was sticking out to the point where like,{w=1.0} the outline of my butt could be seen through my shorts?"

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "..."

    call process_character(k, appearance = "pose handhip face curious")
    k.c "This is important, sis."

    call process_character(k, appearance = "pose handhip face curious")
    k.c "I have to know that my squats have perfect form."

    call process_character(sa, appearance = "pose handface face curious blush true")
    sa.c "..."

    menu:
        "I could see your butt through your shorts.":
            call process_character(k, appearance = "pose armsup face neutral")
            sa.c "Like it was really nice and prominent and clear?"
        "Y-your butt looked like it was going to pop out of your shorts!":
#            call add_points(k, 1, tag = "kira_convo_6_squats")
            call process_character(k, appearance = "pose armsup face neutral")
            k.c "Oh yeah?"

            call process_character(k, appearance = "pose armsup face neutral")
            k.c "My shorts did feel rather tight."

            call process_character(k, appearance = "pose armsup face neutral")
            k.c "I almost thought they were going to break."

    call process_character(k, appearance = "pose armcross face neutral")
    $ renpy.pause(1)

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Good."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Just wanted to make sure."

    call process_character(k, appearance = "pose armsup face happy")
    k.c "Thanks for the {i}ass{/i}ist, sis!"

    call process_character(sa, appearance = "pose handface face neutral blush true")
    sa.c "..."

    call process_end_of_bonus_scene("kira_convo_6_leftovers_sam_mod", k)

    return

label kira_convo_7_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes position left"), (k, "outfit clothes pose handhip face happy position right") ])

    call process_character(k, appearance = "pose handhip face happy")
    k.c "Alright.{p=1.0}So how's the crack in the dam?"

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Huh?"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Give me the scoop."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Did your faucet trickle or did it blow out into a flood?"

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "I..."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "No need to hide it from me, sis."

    call process_character(k, appearance = "pose armcross face happy")
    k.c "I know when another girl has rubbed one out."

    call process_character(k, appearance = "pose armsup face happy")
    k.c "Your face was looking {i}very{/i} flushed, heh."

    call process_character(sa, appearance = "pose leaning face embarrassed blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose leaning face concerned blush true")
    sa.c "W-Well...{p=1.0}I did try it."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "And?"

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "Uh, nothing to report exactly..."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "[sa.say_name]..."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "We're both girls here.\nNothing isn't in the vocabulary where this is concerned."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "That rising feeling of intensity right when you're about to \"finish\"?"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Yup, I know all about it."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "I call it \"the wall\"."

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "The... {w=1.0}wall?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "How long did you last before you came?"

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "{w=0.5}D-Do you mean when the..."

    $ renpy.pause(1)

    call process_character(k, appearance = "pose armcross face happy")
    k.c "Ah yes, your juices, haha!"

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")

    $ renpy.pause(1)

    menu:
        "It didn't take me too long.":
            call process_character(k, appearance = "pose armsup face neutral")
            k.c "Ah, don't fret too hard about it."

            call process_character(k, appearance = "pose armsup face neutral")
            k.c "You're learning all the contours of your own body."

            call process_character(k, appearance = "pose handhip face neutral")
            k.c "That's a thing that takes time, and if you haven't thought to look before..."
        "I thought about a girl and that's when I got wet...":
#            call add_boldness(1, tag = "kira_convo_7_sam_femorgasm")
            call process_character(k, appearance = "pose handhip face neutral")
            k.c "A... {w=1.0}girl?"

            call process_character(k, appearance = "pose armsup face happy")
            k.c "Oh wow."

            call process_character(k, appearance = "pose armsup face happy")
            k.c "(I didn't expect that answer)"

            call process_character(k, appearance = "pose armsup face happy")
            k.c "(I bet it was me)"

            call process_character(k, appearance = "pose armcross face happy")
            k.c "(She's just too nervous to admit it)"

            call process_character(k, appearance = "pose armcross face happy")
            k.c "(To think, my own little sister likes...)"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Still, that's impressive, since Mom walked in on you."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "That would definitely be a mood killer to me."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "Y-you knew that happened?"

    call process_character(k, appearance = "pose armsup face happy")
    k.c "Well, it's certainly confirmed now, haha!"

    call process_character(sa, appearance = "pose leaning face concerned blush true")
    sa.c "..."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Mom didn't outright say it."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "But when her face turned red, that gave it away."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "And she didn't want to talk about it anymore."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "Y-Yeah..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "..."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Maybe your snatch scared her off."

    $ renpy.pause(2)

    call process_character(k, appearance = "pose armcross face happy")
    k.c "Very naughty of you, sis!"

    call process_character(sa, appearance = "pose leaning face embarrassed blush true")
    sa.c "W-what?!"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "I'm only kidding."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "But you should probably lock the door next time."

    $ renpy.pause(1)

    call process_character(k, appearance = "pose armsup face happy")
    k.c "(Though I wouldn't mind taking a peek)"

    call process_end_of_bonus_scene("kira_convo_7_leftovers_sam_mod", k)

    return

label kira_convo_8_leftovers_sam_mod:
    call process_new_location(bg = kira_room)

    call process_conversation_beginning([ (sa, "outfit clothes pose handface position left"), (k, "outfit clothes pose armsup position right") ])

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "I'm in better shape than ever!"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Yeah?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "I can dedicate more time to training."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Back at my previous school, I couldn't always do that."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "You know, homework and such."

    call process_character(k, appearance = "pose armsup face happy")
    k.c "Your favorite."

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "Ugg..."

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "Don't remind me..."

    $ renpy.pause(1)

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "You think you'll try out for the Olympics again, [k.say_name]?"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Hmm, hard to say."

    call process_character(sa, appearance = "pose handsbehind face neutral")

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Even though I've been training more than ever..."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "My tits never seem to get smaller."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Which you may know, stopped me from making the cut."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Why's boob size matter anyway?"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "..."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "It's... {w=1.0}a surprisingly {i}\"big\"{/i} topic."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "But basically the short answer is it's hard to stop them getting in the way."

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "I want to grow big boobs like yours, [k.say_name]!"

    call process_character(k, appearance = "pose armcross face happy")
    k.c "With my exercises you'll get there in no time, haha!"

    call process_character(k, appearance = "pose armcross face happy")
    k.c "Let's hope you're able to support their weight... {w=0.5}instead of, {w=0.5}you know, {w=1.0}immediately tipping over."

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Anyway, I'm thinking I should prove myself in local competitions first before I move on to the big leagues."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Gotta rebuild my reputation for this new town, y'know."

    call process_end_of_bonus_scene("kira_convo_8_leftovers_sam_mod", k)

    return

label kira_convo_9_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (k, "outfit underwear pose handhip face neutral position right") ])

    $ kira_convo_9_got_naked = False

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Hey [k.say_name]!"

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Well, look at you."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Someone's confidence is getting stronger."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "What do you mean?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "You're acting all cool and collected..."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Even though I'm in my bra and panties."

    menu:
        "I'm getting used to it.":
            call process_character(k, appearance = "pose armcross face neutral")
            k.c "Well, that makes sense."

            call process_character(k, appearance = "pose armcross face neutral")
            k.c "You've already seen me buck wild."

            call process_character(k, appearance = "pose armsup face flirty")
            k.c "Between us girls, we don't need to hide anything."
            pass
        "You should get naked [k.say_name]!":
#            call add_boldness(1, tag = "kira_convo_10_naked")
            call process_character(sa, appearance = "pose leaning face neutral")

            call process_character(k, appearance = "pose armsup face happy")
            k.c "Ho-ho-ho!"

            call process_character(k, appearance = "pose armsup face happy")
            k.c "Cutting right to the chase!"

            call character_leave_dissolve(k)
            $ renpy.pause(1)

            $ kira_convo_9_got_naked = True

            call process_character(k, appearance = "outfit nude pose armsup face flirty")
            k.c "How's that ya little perv?"

            call process_character(k, appearance = "outfit nude pose armsup face flirty")
            k.c "I swear, you're taking after me, sis!"

            call process_character(sa, appearance = "pose handsbehind face happy blush true")
            sa.c "..."

            call process_character(k, appearance = "pose handhip face happy")
            k.c "There's the blush I know well!"

            call process_character(k, appearance = "pose handhip face happy")
            k.c "Cheeks all flushed from the mammary memories."

            call process_character(sa, appearance = "pose handsbehind face curious blush true")
            sa.c "..."

            call process_character(sa, appearance = "pose handsbehind face curious blush true")
            sa.c "I..."

            call process_character(sa, appearance = "pose leaning face happy blush true")
            sa.c "I love seeing you naked, [k.say_name]!"

            call process_character(k, appearance = "pose armcross face happy")
            k.c "Oh, I bet you do."

            call process_character(k, appearance = "pose armcross face happy")
            k.c "If I were in your position, I would too."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "So by now I'm sure you know what this is all about."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Yeah!"

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "It's about trying out new exercises!"

    call process_character(k, appearance = "pose handhip face embarrassed")
    k.c "(Okay, maybe not...)"

    call process_character(k, appearance = "pose handhip face embarrassed")
    k.c "..."

    call process_character(k, appearance = "pose handhip face embarrassed")
    k.c "Oh yes, {w=1.0}exactly."

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "Oh, and spending quality time with my big sis!"

    call process_character(k, appearance = "pose handhip face happy")
    k.c "Hah, well there is that, of course."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "It's always really fun spending time with you, [k.say_name]!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "These exercises are new to me, and usually I feel all sore or super tired afterwards..."

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "But the ones you come up with aren't anything like that!"

    call process_character(k, appearance = "pose armcross face embarrassed")
    k.c "(I guess this is what happens when you're oblivious to what it really is...)"

    call process_character(k, appearance = "pose armcross face embarrassed")
    k.c "(Should I really keep stringing her along like this?)"

    call process_character(k, appearance = "pose armcross face embarrassed")
    k.c "(She {i}can{/i} be a bit... {w=1.0}naive at times...)"

    call process_character(k, appearance = "pose armcross face embarrassed")
    k.c "(Maybe I should just tell her I enjoy playing with her pussy...)"

    call process_character(k, appearance = "pose armcross face happy")
    k.c "..."

    call process_character(k, appearance = "pose handhip face curious")
    k.c "(Pull yourself together [k.say_name]!)"

    call process_character(k, appearance = "pose handhip face curious")
    k.c "(I can't just tell her that!)"

    call process_character(k, appearance = "pose handhip face embarrassed")
    k.c "(I can picture my little sis now, in her blissful ignorance...)"

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg white
    with Dissolve(1.0)
    $ renpy.pause(1.0)
    $ renpy.show_screen("dream_blur")

    show bg kitchen_daytime
    with Dissolve(1.0)

    $ si.position = "right"
    $ display_multiple_characters([ (sa, "outfit clothes pose handsbehind face neutral"), (si, "outfit clothes pose handsfront face neutral") ])
    $ quick_menu = True

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Hi, Mom!"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "Hi, sweetie."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "What have you been up to?"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "[k.say_name] said she had to have a taste of my pussy!"

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "She what?!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Yeah!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "You won't believe what she did to me, Mom!"

    call process_character(sa, appearance = "pose leaning face happy blush true")
    sa.c "Her tongue is really out of this world, hehe!"

    call process_character(si, appearance = "pose handsup face angry blush true")

    $ si.c(k.say_name.upper() + "!!!")

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg white
    with Dissolve(1.0)
    $ renpy.pause(1.0)
    $ renpy.scene('screens')

    if week.time == "day":
        show bg kira_room_daytime
        with Dissolve(1.0)
    else:
        show bg kira_room_evening
        with Dissolve(1.0)

    if kira_convo_10_got_naked:
        $ display_multiple_characters([ (sa, "outfit clothes pose handface face neutral blush false"), (k, "outfit nude pose armcross face embarrassed") ])
    else:
        $ display_multiple_characters([ (sa, "outfit clothes pose handface face neutral blush false"), (k, "outfit underwear pose armcross face embarrassed") ])

    $ quick_menu = True
    call process_character(k, appearance = "pose armcross face embarrassed")
    k.c "(Yeah, that wouldn't end well...)"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "(At least if she says they're just exercises, I can sneak my way out of that)"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "(\"Oh, that [sa.say_name] and her active imagination!\")"

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "Um... {w=1.0}Earth to [k.say_name]?"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Oh, sorry sis."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "I was just drumming up some new exercises in my head."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Gotta think it out, you know?"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Oh, okay!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Don't keep me waiting for too long!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "I really want to try out more exercises!"

    call process_end_of_bonus_scene("kira_convo_9_leftovers_sam_mod", k)

    return

label kira_convo_10_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handsbehind face neutral position left"), (k, "outfit clothes pose armsup face neutral position right") ])

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Whew, it's a hot one today!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Yeah!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "I've already gone in the pool a few times."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "I did too."

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Even though we have A/C, it's just barely able to keep up."

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "I had my fan blowing on me at full blast before."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "If we go running today, we'll have to hydrate a lot."

    call character_leave_dissolve(sa)
    call character_leave_dissolve(k)
    pause 0.5

    $ si.position = "right"

    call process_character(si, appearance = "outfit yoga pose handsfront face neutral")

    call process_character(si, appearance = "outfit yoga pose handsfront face neutral")
    si.c "Hey, kids."

    "[k.say_name] & [sa.say_name]" "Hey, Mom."

    call process_character(si, appearance = "outfit yoga pose handsup face neutral")
    si.c "I just checked on your brother."

    call process_character(si, appearance = "outfit yoga pose handsup face neutral")
    si.c "He's still in the pool trying to cool off."

    call process_character(si, appearance = "outfit yoga pose handsup face happy")
    si.c "I don't think he's going to come out until this weather passes!"

    $ k.position = "left"

    call process_character(k, appearance = "pose handhip face neutral")
    k.c "Can't blame him there."

    call process_character(si, appearance = "outfit yoga pose armunder face neutral")
    si.c "So what have you two been up to lately?"

    call process_character(k, appearance = "pose armsup face neutral")
    k.c "Eh, not too much."

    call character_leave_dissolve(k)

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "We've been doing lots of running!"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "We were thinking about doing some more today."

    call process_character(si, appearance = "outfit yoga pose armunder face curious")
    si.c "Well gosh, I'd really be careful in this heat."

    call process_character(si, appearance = "outfit yoga pose armunder face curious")
    si.c "I don't want either of you to get heat stroke."

    call character_leave_dissolve(sa)

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "Eh, it's still up in the air."

    call process_character(k, appearance = "pose armcross face neutral")
    k.c "We may just stay inside."

    call character_leave_dissolve(k)

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "We can always do some exercises inside!"

    call process_character(si, appearance = "outfit yoga pose handsup face happy")
    si.c "I've never seen you this excited about exercising before [sa.say_name]!"

    call process_character(si, appearance = "outfit yoga pose handsup face happy")
    si.c "A healthy break from all those video games is the right thing to do!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "[k.say_name] has some great routines we do!"

    call process_character(si, appearance = "outfit yoga pose handsup face happy")
    si.c "You are a miracle woman [k.say_name]!"

    call process_character(si, appearance = "outfit yoga pose handsup face happy")
    si.c "Getting your sister to happily exercise."

    call process_character(si, appearance = "outfit yoga pose handsfront face neutral")
    si.c "How did you manage to do it?"

    call character_leave_dissolve(sa)

    call process_character(k, appearance = "pose armsup face embarrassed")
    k.c "Oh well it uh..."

    call process_character(k, appearance = "pose armsup face embarrassed")
    k.c "..."

    call process_character(k, appearance = "pose armsup face embarrassed")
    k.c "It involved a lot of... {w=1.0}hand and leg exercises."

    call process_character(k, appearance = "pose armsup face embarrassed")
    k.c "A lot of hand and leg movements, right [sa.say_name]?"

    call character_leave_dissolve(k)

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Yes!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "They're really fun!"

    call process_character(si, appearance = "outfit yoga pose handsup face happy")
    si.c "Well, I say, keep it up!"

    call process_character(si, appearance = "outfit yoga pose handsup face happy")
    si.c "It is doing wonders on the both of you, it seems!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "[k.say_name] gave me a massage recently too!"

    call process_character(si, appearance = "outfit yoga pose handsup face neutral")
    si.c "Oh, your sister is a pro at those!"

    call process_character(si, appearance = "outfit yoga pose handsup face neutral")
    si.c "Whenever I have some neck or back pain, she's the one to go to for some relief!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Yeah, she did an awesome job on me!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "{cps=40}It was great when she massaged my p-{/cps}{w=0.75}{nw}"

    call character_leave_dissolve(sa)

    call process_character(k, appearance = "pose armcross face embarrassed blush true")
    k.c "No need to keep reminding me how great I am at it!"

    call process_character(si, appearance = "outfit yoga pose armunder face happy")
    si.c "[k.say_name]'s right."

    call process_character(si, appearance = "outfit yoga pose armunder face happy")
    si.c "I've told her countless times already!"

    call process_character(k, appearance = "pose armsup face embarrassed blush true")
    k.c "..."

    call process_character(si, appearance = "outfit yoga pose handsfront face neutral")
    si.c "Well, I'm going to sweat it out myself with some yoga."

    call process_character(si, appearance = "outfit yoga pose handsfront face neutral")
    si.c "Just make sure you drink lots of water today."

    call process_character(si, appearance = "outfit yoga pose handsfront face neutral")
    si.c "It's easy to get dehydrated!"

    call character_leave_dissolve(k)

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Okay, Mom!"

    call character_leave_dissolve(si)

    $ k.position = "right"

    call process_character(k, appearance = "pose handhip face embarrassed blush false")
    k.c "..."

    call process_character(k, appearance = "pose handhip face embarrassed blush false")
    k.c "(Holy shit was that close)"

    call process_character(k, appearance = "pose handhip face embarrassed blush false")
    k.c "..."

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "Hey, sis..."

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "Ease up on the details, will you?"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "..."

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "I can't have you sharing my... {w=0.5}super {w=0.5}secret {w=0.5}massage techniques."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Your secret massage techniques?"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "Uh..."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "Yeah, yeah, you know..."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "These massages and exercises are top secret."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "They gotta be kept under wraps."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Top secret?"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Wow!"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "That's right!"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "You're the only one I've tested them out on."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "And only you know about them."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "I... {w=1.0}want to create the greatest workout routine of all time!"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "But I need you to keep it between us sisters."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Seriously, we must swear absolute secrecy about it, you get me?"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "If anyone asks you, even Mom or [n.say_name]..."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "Just tell them you're simply doing exercises with me."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "But don't give out any details!"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "So, can you do it, [sa.say_name]?"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Can I trust that you'll honor the sisterly code?"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Keep our super secret massage techniques between us?"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "You can count on me, [k.say_name]!"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "Cool."

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "..."

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "(How did I pull that one off?)"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "..."

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "(I hope like shit she'll keep her word...)"

    call process_end_of_bonus_scene("kira_convo_10_leftovers_sam_mod", k)

    return

label kira_convo_11_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (k, "outfit clothes pose handhip face neutral blush false position right")])

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "That ReflexViz site you go on..."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yeah?"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Are there movie reviews too?"

    call process_character(k, appearance = "pose handhip face neutral  blush false")
    k.c "Cause the movie I watched a couple of nights ago was complete garbage."

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "I mean, {i}come on{/i} with that ending!"

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "And what was with the acting? {p=1.0}The lead actress couldn't act to save her life!"

    call process_character(k, appearance = "pose armcross face concerned blush false")
    k.c "Talk about a real disappointment, I was looking forward to that thing."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Yup, they have reviews for movies too!"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Good. {w=1.0}Because that movie sucked real ass."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Actually, there is one thing I do want to know."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Do they allow any type of video?"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "If it falls under their guidelines, then yes!"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "So you're saying I could upload vids of my fitness classes?"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "And people will watch them?"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Yup, that's completely fine!"

    call process_character(k, appearance = "pose armsup face happy blush false")
    k.c "(Heh, you just gave me a new idea, sis)"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Are you thinking of making an account on there, [k.say_name]?"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "I'll bet you'll be world-famous in no time!"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Now, hold on. {p=1.0}Let's not get too hasty here."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Was just curious about things, that's all."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "But now that you mention it, it doesn't sound like a bad idea."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "How many views do these videos get usually anyway?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "It's a really big platform, so a couple thousand views is super easy to reach!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "I've seen viewcounts that go up into the millions!"

    call process_character(k, appearance = "pose armsup face surprised blush false")
    k.c "Woah, hot damn!"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Seems like it's the talk of the town."

    call process_character(k, appearance = "pose armsup face happy blush false")
    k.c "No, the world!"

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "It is!"

    call process_end_of_bonus_scene("kira_convo_11_leftovers_sam_mod", k)

    return

label kira_convo_12_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (k, "outfit clothes pose handhip face neutral blush false position right")])

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "One day, I really want to go to the beach."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Yeah, me too!"

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "I wanna go windsurfing again!"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Maybe you and I could try to find some sea glass for Mom."

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "Sea glass?"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "You never heard of sea glass, sis?"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "It's actually pretty neat."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "It's this colorful, smooth glass you can occasionally find along the shoreline."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Where's it come from?"

    call process_character(k, appearance = "pose armsup face happy blush false")
    k.c "Probably from some frat boy tossing a beer bottle into the ocean."

    call process_character(k, appearance = "pose armsup face happy blush false")
    k.c "A bottle goes from holding alcohol, to becoming shiny paraphernalia."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Oooh, treasure hunt!"

    call process_character(k, appearance = "pose handhip face happy blush false")
    k.c "Now you're talking my language!"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "Maybe if we're lucky, we'll come across a necklace or ring."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yeah, yeah!"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Rare chance you'll just find something like that with the naked eye."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "But if you do..."

    call process_character(k, appearance = "pose armsup face happy blush false")
    k.c "Finders, keepers!"

    call process_end_of_bonus_scene("kira_convo_12_leftovers_sam_mod", k)

    return

label kira_convo_13_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (k, "outfit clothes pose handhip face curious blush false position right")])

    call process_character(k, appearance = "pose handhip face curious blush false")
    k.c "[sa.say_name], dude..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "What?"

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "If you're gonna flick your bean in the bathroom, at least clean up properly."

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "!"

    call process_character(k, appearance = "pose handhip face concerned blush false")
    k.c "I swear, I nearly slipped on it!"

    call process_character(k, appearance = "pose handhip face concerned blush false")
    k.c "Oh, and I could still smell it too."

    call process_character(k, appearance = "pose handhip face concerned blush false")
    k.c "I know it wasn't water. {p=1.0}Water doesn't smell like that."

    call process_character(sa, appearance = "pose leaning face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose leaning face concerned blush true")
    sa.c "S-Sorry about that."

    call process_character(sa, appearance = "pose leaning face concerned blush true")
    sa.c "I thought I cleaned it up..."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "I just use the shower head for that."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "No mess, no fuss."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "I-I could try that..."

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "On second thought..."

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "That may not be the best idea."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "Why?"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "Well, with how you've been going..."

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "I'll almost certainly need a second job to help cover the water bill."

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "..."

    call process_end_of_bonus_scene("kira_convo_13_leftovers_sam_mod", k)

    return

label kira_convo_14_leftovers_sam_mod:
    call process_new_location(bg = kira_room)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (k, "outfit clothes pose armcross face neutral blush false position right")])

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "It's funny how often my tits are stared at."

    call process_character(k, appearance = "pose armcross face happy blush false")
    k.c "And I don't mean just you."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "O-Oh?"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "When dudes stare it's cut and dry."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "They just ogle and are in a daze."

    call process_character(k, appearance = "pose armsup face happy blush false")
    k.c "It's the girls staring that are more amusing."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "So I'm not the only one?"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Nope."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Other girls don't stare as much as you do, but their eyes still wander."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "At the gym it's constant."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "My theory is girls probably don't think they're real."

    call process_character(k, appearance = "pose armcross face happy blush false")
    k.c "Or maybe it's titty envy."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "For me it was the latter!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Everyone else has really huge boobs but me."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "They probably want to squeeze them to see if they were legit."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "..."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "Well, wouldn't you, [sa.say_name]?"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "I know what you're like, sis."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "You love tits."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "There's no way you wouldn't take that opportunity."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "And I bet that brother of ours would do the same."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "He's a perv and he doesn't know it yet."

    call process_character(k, appearance = "pose armsup face happy blush false")
    k.c "Between us girls, he doesn't know what he's missing!"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "I mean, getting to squeeze a random girl's tits?"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Imagine just being allowed to do that out of the blue."

    call process_character(k, appearance = "pose handhip face happy blush false")
    k.c "I know I wouldn't pass it up!"

    call process_end_of_bonus_scene("kira_convo_14_leftovers_sam_mod", k)

    return

## Sam Simone Convos ##
label simone_convo_1_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose armunder face neutral position right") ])

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "I was wondering, [sa.say_name]..."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "Do you just like video games?"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "Or do you also like games in general?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "Because there's not just video games to play."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "There's card games too."

    call process_character(si, appearance = "pose handsfront face happy")
    si.c "And I've played plenty of board games myself!"

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "I don't think those sorts of games are for me, Mom."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "I understand, sweetie."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "The types of games I'm talking about are more tests of patience."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Your video games are very fast paced compared to them!"

    call process_character(sa, appearance = "pose handface face neutral")

    call process_character(si, appearance = "pose handsup face embarrassed")
    si.c "It's difficult to keep up with what's going on in them!"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "With card games and board games, it's not like that."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "You can't be quick with them."

    call process_character(si, appearance = "pose handsfront face curious")
    si.c "You have to take your time with it."

    call process_character(si, appearance = "pose handsfront face curious")
    si.c "Plan out what you have to do."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "I know, Mom."

    call process_character(si, appearance = "pose handsup face happy")
    si.c "One foul move could cost you, so watch out!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "..."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "I'm just saying that it's worth a try, honey."

    call process_character(si, appearance = "pose handsup face happy")
    si.c "I would love it if you and [n.say_name] joined me for a board game sometime!"

    call process_end_of_bonus_scene("simone_convo_1_leftovers_sam_mod", si)

    return

label simone_convo_2_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose armunder face neutral position right") ])

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "How do you like your room, [sa.say_name]?"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "It's good!"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "Is it comfortable?"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "Yeah!"

    call process_character(si, appearance = "pose handsfront face neutral")

    $ si.c("I wasn't sure how you and " + n.say_name + " would feel about being separated into two rooms.")

    call process_character(sa, appearance = "pose handface face concerned")
    sa.c "Yeah, it's gonna take some getting used to, I think."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "But [n.say_name] visits me all the time."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "We've got lots of free time while we're awake."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Sounds like you two keep each other company as much as you can!"

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "Yup, I have all the streaming stuff in my room!"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "Oh, that's right!{p=1.0}You two are putting videos on, what was it?"

    $ renpy.pause(2)

    call process_character(si, appearance = "pose armunder face embarrassed")
    si.c "\"[video_sharing_site_simone_wrong]?\""

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "[video_sharing_site]!"

    call process_character(si, appearance = "pose handsfront face happy")
    si.c "[video_sharing_site], that's right!"

    call process_character(si, appearance = "pose handsfront face happy")
    si.c "I'm pretty computer illiterate as you can tell."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "It's okay, Mom!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Our goal is to get as many people watching our videos as we can!"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Well, I think that's great you both are working hard together to succeed!"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Nothing better than teamwork!"

    call process_end_of_bonus_scene("simone_convo_2_leftovers_sam_mod", si)

    return

label simone_convo_3_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose handsfront face neutral position right") ])

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "I got a call from Mom."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Mom?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "Your grandmother."

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "Oooh!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "How's she doing?{p=1.0}What'd she call about?"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "She said she would like for us to come visit soon."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "I guess the house is being renovated."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "So it's tough to accommodate anyone there right now."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "We need to go to the beach as a family!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Her, us, everybody!"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "It has been a while since we've gone."

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "I bet [k.say_name]'s gonna stomp everybody at volleyball again!"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Oh yes, I remember that."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "She was beating every group that challenged her."

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "Bounced the ball right off that dude's face!"

    call process_character(si, appearance = "pose handsup face happy")
    si.c "That was so embarrassing!"

    call process_character(si, appearance = "pose handsup face happy")
    si.c "The poor guy's face was one big red mark."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "That's your sister though."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "She takes no prisoners in competitions."

    call process_end_of_bonus_scene("simone_convo_3_leftovers_sam_mod", si)

    return

label simone_convo_4_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose handsfront face neutral position right") ])

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "I was very impressed by your new school."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Oh, why?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "Your designated teacher called me."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "We had a very friendly chat."

    call process_character(sa, appearance = "pose handface face curious")

    $ renpy.pause(1)

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "The teacher called?{p=1.0}But we haven't started school yet."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Believe me, I was very surprised too!"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "But it was a good thing."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "It showed me they wanted to keep in touch with the parents."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "So does this mean I only have the one teacher at this new school?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "It's a very unique school."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "They like to have one teacher dedicated to a small group of students."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "So you become comfortable learning from one teacher."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Sounds cool to me!"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "I'm glad to hear that!"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "It allows the teacher to give more of their time to each student."

    call process_character(sa, appearance = "pose leaning face neutral")

    $ sa.c("Please tell me " + n.say_name + " and I will be in the same class!")

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Don't worry.{p=1.0}I made sure to request just that."

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "Yesss!"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "They normally like to break up siblings and put them into different classes because they fight."

    call process_character(si, appearance = "pose handsup face neutral")

    $ si.c("But I assured them you and " + n.say_name + " get along very well.")

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "I hope the teacher's really nice!"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "She seemed very polite over the phone."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "She sounded like a younger teacher."

    call process_character(si, appearance = "pose armunder face neutral")

    $ si.c("Probably only several years older than " + k.say_name + ".")

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "That's good!"

    call process_character(si, appearance = "pose handsfront face neutral")

    $ si.c("I think you and " + n.say_name + " will enjoy her teaching very much!")

    call process_end_of_bonus_scene("simone_convo_4_leftovers_sam_mod", si)

    return

label simone_convo_5_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose handsup face neutral position right") ])

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "I think it's great how well you get along with your brother and sister!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Were you worried I wouldn't be, Mom?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "I just think having a good relationship with your siblings is important."

    call process_character(sa, appearance = "pose handsbehind face neutral")

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "It's tougher to come by nowadays.{p=1.0}Or it feels that way..."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Don't you get along with Auntie?"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "Well...{p=1.0}We give each other space."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "I do care about my sister."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "But she can be very..."

    $ renpy.pause(2)

    call process_character(si, appearance = "pose armunder face concerned")
    si.c "Unfiltered."

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "Unfiltered?"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "She just lets you know what's on her mind."

    call process_character(si, appearance = "pose handsup face concerned")
    si.c "Whether it's good or bad."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Hmm..."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "So she's brutally honest?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "Yes. {p=1.0}It has it's ups and downs."

    call process_character(si, appearance = "pose handsfront face curious")
    si.c "While being honest is certainly a good quality to have..."

    call process_character(sa, appearance = "pose handface face curious")

    call process_character(si, appearance = "pose handsup face curious")
    si.c "I think it's just as important to be courteous and respectful to others."

    call process_character(si, appearance = "pose handsup face concerned")
    si.c "And unfortunately I think your Auntie misses the mark on that sometimes."

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "Auntie's always so nice to me!"

    call process_character(sa, appearance = "pose leaning face concerned")
    sa.c "But there was this one time where she told me \"video games are like junk\", though."

    call process_character(sa, appearance = "pose leaning face angry")
    sa.c "Video games are anything but junk!"

    call process_character(si, appearance = "pose armunder face embarrassed")
    si.c "She... {w=1.0}certainly does have her moments."

    call process_character(si, appearance = "pose armunder face angry")

    $ si.c("She also told me I was \"eating plenty\" while I was starving you and " + n.say_name + ", preventing you from growing...")

    call process_character(sa, appearance = "pose handface face concerned")
    sa.c "But you feed us just fine, Mom!"

    call process_character(si, appearance = "pose handsfront face concerned")
    si.c "I know. {w=1.0}I just wouldn't always trust everything your Auntie says about people, that's all."

    call process_end_of_bonus_scene("simone_convo_5_leftovers_sam_mod", si)

    return

label simone_convo_6_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face concerned position left"), (si, "outfit clothes pose handsfront face neutral position right") ])

    $ renpy.pause(1)

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "How has your day been so far?"

    call process_character(sa, appearance = "pose handsbehind face concerned")
    $ renpy.pause(1)

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "It's been okay, Mom."

    call process_character(si, appearance = "pose handsup face curious")

    $ si.c("I wanted to ask you " + sa.say_name + "...")

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "When you were in the bathroom, and I saw you."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    $ renpy.pause(1)

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "Y-yeah?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "I...{p=1.0}I just wanted to know if everything went okay."

    call process_character(sa, appearance = "pose leaning face concerned blush true")
    sa.c "O-Oh...{p=1.0}That..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "E-everything was okay, Mom."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "Promise."

    call process_character(si, appearance = "pose armunder face curious")
    si.c "Are you sure?"

    menu:
        "I-I'm okay Mom.":

            call process_character(sa, appearance = "pose handsbehind face concerned blush true")

            call process_character(si, appearance = "pose handsfront face neutral")
            si.c "Just wanted to make sure, sweetie."
        "W-well, something did come out after a while.":
#            call add_points(si, 1, tag = "simone_convo_6_you_sure_sam")
            call process_character(sa, appearance = "pose handface face concerned blush true")
            sa.c "I thought I was gonna pee at first, but it was something else."

            call process_character(sa, appearance = "pose handface face concerned blush true")
            sa.c "It just kept squirting out, like I was a fire hydrant or something."

            call process_character(sa, appearance = "pose handsbehind face concerned blush true")
            sa.c "My knees felt really weak afterwards..."

            call process_character(si, appearance = "pose handsup face neutral")
            si.c "That's perfectly normal, sweetie."

            call process_character(si, appearance = "pose handsup face neutral")
            si.c "You orgasmed."

            call process_character(sa, appearance = "pose handface face concerned blush true")
            sa.c "O-orgasmed?"
#            $ heard_of_ejaculate = True

            call process_character(si, appearance = "pose armunder face embarrassed")
            si.c "Pretty intensely too from the sounds of it."

            call process_character(sa, appearance = "pose handface face concerned blush true")
            sa.c "It... {w=0.5}was pretty intense, yeah."

            call process_character(si, appearance = "pose armunder face embarrassed")
            si.c "Ah well..."

            $ renpy.pause(2)

            call process_character(si, appearance = "pose armunder face curious")
            si.c "That's the word for what you experienced."

            call process_character(si, appearance = "pose handsfront face curious")
            si.c "It may seem weird at first, but I assure you it's nothing to worry about."

            call process_character(sa, appearance = "pose handsbehind face concerned blush true")
            $ renpy.pause(1)

            call process_character(sa, appearance = "pose handsbehind face concerned blush true")
            sa.c "Okay, Mom..."

            call process_character(sa, appearance = "pose handface face curious blush true")
            sa.c "But is it normal for all my muscles to ache?"

            call process_character(si, appearance = "pose armunder face embarrassed")
            si.c "..."

            call process_character(si, appearance = "pose armunder face curious")
            si.c "With... {w=0.5}intense... {w=0.5}orgasms like yours seems to have been, yes, I would say so."

    call character_leave_dissolve(sa)

    call process_character(si, appearance = "pose armunder face concerned")
    si.c "(It's clear she's confused about all of this...)"

    $ renpy.pause(1)

    call process_character(si, appearance = "pose armunder face concerned")
    si.c "(And it did sound like she was hurt in the bathroom)"

    call process_character(si, appearance = "pose handsup face concerned")
    si.c "(I tried to hold off exposing her to this)"

    call process_character(si, appearance = "pose handsup face concerned")
    si.c "(But I can't just tell her not to do it again)"

    call process_character(si, appearance = "pose handsup face concerned")
    si.c "(I hope she at least learns how to do it properly...)"

    $ renpy.pause(2)

    call process_character(si, appearance = "pose armunder face concerned")
    si.c "(But I'm not sure she will on her own...)"

    call process_end_of_bonus_scene("simone_convo_6_leftovers_sam_mod", si)

    return

label simone_convo_7_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face concerned blush true position left"), (si, "outfit clothes pose handsfront face embarrassed blush true position right") ])

    call process_character(si, appearance = "pose handsfront face embarrassed blush true")
    si.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "..."

    call process_character(si, appearance = "pose handsfront face embarrassed blush false")

    $ renpy.pause(1)

    call process_character(si, appearance = "pose handsfront face embarrassed blush false")
    si.c "Did you have a good night's rest, [sa.say_name]?"

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "I did, yeah."

    call process_character(si, appearance = "pose handsup face neutral")

    $ si.c("Don't feel bad about what happened, " + sa.say_name + ".")

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "..."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "You're getting to the point now where you are thinking more about..."

    call process_character(si, appearance = "pose armunder face curious")
    si.c "Well, other girls would be thinking about boys."

    call process_character(si, appearance = "pose armunder face curious")
    si.c "But it seems like you're thinking about girls instead."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "So it's not surprising when you saw my..."

    call process_character(si, appearance = "pose armunder face embarrassed")

    $ renpy.pause(2)

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "When you saw me that it...{p=1.0}Excited you."

    menu:
        "S-Sorry Mom, I'll make sure to tell you next time before I...":
#                call add_points(si, 1, tag = "simone_convo_7_excited_you_sam")
                call process_character(sa, appearance = "pose handface face concerned blush true")

                call process_character(si, appearance = "pose handsfront face neutral")
                si.c "I know."

                call process_character(si, appearance = "pose handsup face neutral")
                si.c "(I guess she does expect there to be a \"next time\")"

        "Y-you've got really huge boobs Mom!":
#                call add_boldness(1, tag = "simone_convo_7_excited_you_sam")
                call process_character(sa, appearance = "pose handface face happy blush true")

                call process_character(si, appearance = "pose armunder face embarrassed")

                $ renpy.pause(1)

                call process_character(si, appearance = "pose armunder face embarrassed")
                si.c "(That was rather blunt)"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "You're still learning about how to control and handle yourself."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")

    $ renpy.pause(1)

    call process_character(si, appearance = "pose handsup face embarrassed")
    si.c "(That came out wrong)"

    call process_character(si, appearance = "pose handsup face embarrassed")
    si.c "(And I'm still thinking about how intensely she...)"

    $ renpy.pause(2)

    call process_character(si, appearance = "pose handsup face embarrassed")
    si.c "(Orgasmed)"

    $ renpy.pause(2)

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "U-um, Mom..."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "For the record... {w=1.0}I am thinking about boys too."

    call process_character(si, appearance = "pose handsup face neutral blush true")
    si.c "..."

    call process_character(si, appearance = "pose handsfront face concerned blush true")
    si.c "We shouldn't talk about this out here."

    call process_character(si, appearance = "pose armunder face neutral blush true")
    si.c "W-would you like something to eat?"

    call process_character(si, appearance = "pose armunder face neutral blush true")
    si.c "I'll make you your favorite snack."

    call process_end_of_bonus_scene("simone_convo_7_leftovers_sam_mod", si)

    return

label simone_convo_8_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose armunder face neutral position right") ])

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "I'm thankful my company has let me work at home this long."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "I enjoy working at home a lot more."

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "That's so cool how they let you do that, Mom!"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "It truly is."

    call process_character(si, appearance = "pose handsfront face happy")
    si.c "it means I get to spend more time with the three of you!"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "I also didn't want you and [n.say_name] to be left alone all day if [k.say_name] was also working."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "[n.say_name] and I could easily handle being home alone, Mom!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "I bet we'd just play video games all day!"

    call process_character(sa, appearance = "pose handface face neutral")

    call process_character(si, appearance = "pose armunder face happy")
    si.c "I'm sure you would!"

    call process_character(si, appearance = "pose handsup face curious")
    si.c "I don't know this neighborhood yet."

    call process_character(si, appearance = "pose handsup face curious")
    si.c "But I'd rather be safe than sorry."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "The neighborhood seems good to me!"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "It's definitely safer than most."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "But it only takes one bad apple to change that."

    call process_end_of_bonus_scene("simone_convo_8_leftovers_sam_mod", si)

    return

label simone_convo_9_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose leaning face neutral position left"), (si, "outfit clothes pose armunder face neutral position right") ])

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "One of these days I'm going to make you come for a swim, Mom!"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "I'd have to politely decline then, sweetie."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Aww, why not?"

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "It's tough to explain."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "But if I go swimming..."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "It means I have to wear a bathing suit."

    call process_character(si, appearance = "pose handsfront face concerned")
    si.c "And I don't feel comfortable doing that."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "How come?"

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "Well..."

    call process_character(si, appearance = "pose armunder face neutral")
    si.c "How should I put this..."

    call process_character(si, appearance = "pose handsup face curious")
    si.c "Some women, myself included, can be very self-conscious."

    call process_character(si, appearance = "pose handsup face curious")
    si.c "You'll understand as you get older."

    call process_character(si, appearance = "pose handsup face curious")
    si.c "Especially when you're around my age."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "But to sum it up, it means that we care about how we look."

    call process_character(si, appearance = "pose handsfront face neutral")
    si.c "And how others judge how we look."

    call process_character(sa, appearance = "pose handface face concerned")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned")
    sa.c "But..."

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "How about just the pool then?"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "It's not like anyone can see in."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "It'll just be us."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "We'll all promise not to say a single word about it!"

    call process_character(sa, appearance = "pose leaning face happy")
    sa.c "Not even [k.say_name]!"

    call process_character(si, appearance = "pose armunder face concerned")
    si.c "I can't wear a bathing suit, [sa.say_name]."

    call process_character(si, appearance = "pose armunder face concerned")
    si.c "I'd be too concerned about how I look."

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "..."

    pause 0.5

    call process_character(sa, appearance = "pose handsbehind face concerned")
    sa.c "Bummer."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "I'm sure you'd love it!"

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "No need to worry about me, [sa.say_name]."

    call process_character(si, appearance = "pose handsup face neutral")
    si.c "You go enjoy yourself."

    call process_character(si, appearance = "pose handsup face happy")
    si.c "My garden keeps me plenty entertained!"

    call process_end_of_bonus_scene("simone_convo_9_leftovers_sam_mod", si)

    return

label simone_convo_10_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose handsup face neutral position right") ])

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "The park down the road looks lovely."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yeah, it's nice!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "I checked it out recently!"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Oh, you did?"

    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "You've been so preoccupied with videogames, I didn't think you even had time for the outdoors!"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "What did you like about it?"

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "There was this really huge fountain I wanted to climb!"

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "And the flowers there are really pretty."

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "That I would love to go see!"

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "Maybe I'll get some floral ideas for my garden."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "How's your garden doing, Mom?"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "I think it's getting by."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Our yard receives a lot of sun, so that's not an issue."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "But the plants need water constantly."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "They dry right up with the sun bearing down on them."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Will it become a farm, Mom?"

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "It's a small garden right now sweetie!"

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "If it gets big enough to feed us, then we can call it a farm."

    call process_character(sa, appearance = "pose handface face neutral blush false")

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "But I'm happy to report that the first vegetables I'm growing are looking healthy!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Ooh, what are they?"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "They are \"beginner friendly\"."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Tomatoes and lettuce."

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "The essential components of a salad!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "What about cherry tomatoes?"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "I heard those are really nice!"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "I'm not letting you just snack on all of them."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "You need to leave some for the rest of us."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "But that's a \"yes\" on them being cherry tomatoes, right?"

    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "Haha, we'll see, [sa.say_name]!"

    call process_end_of_bonus_scene("simone_convo_10_leftovers_sam_mod", si)

    return

label simone_convo_11_leftovers_sam_mod:
    call process_new_location(bg = simone_room)

    if week.time == "night":
        call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit nightgown pose handsfront face neutral position right") ])

        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "Hi, Mom!"

        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "What's with the nightgown?"

        call process_character(si, appearance = "pose handsfront face neutral blush false")
        si.c "I didn't sleep well last night."

        call process_character(si, appearance = "pose handsfront face neutral blush false")
        si.c "So I was tired most of the day."

        call process_character(si, appearance = "pose handsup face neutral blush false")
        si.c "I figured I should go to bed earlier to get some extra rest."
    else:
        call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose handsfront face happy position right") ])

        call process_character(si, appearance = "pose handsfront face happy blush false")
        si.c "{i}Yawn{/i}..."

        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "Hi, Mom!"

        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "You look a little sleepy."

        call process_character(si, appearance = "pose armunder face happy blush false")
        si.c "Haha, what gave it away?"

        call process_character(si, appearance = "pose armunder face neutral blush false")
        si.c "I had to do some business work late."

        call process_character(si, appearance = "pose armunder face neutral blush false")
        si.c "Lost track of time."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "(I hope Mom doesn't mention what I did)"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "(Maybe she forgot about it?)"

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "..."

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "(It doesn't look like [sa.say_name] wants to come clean)"

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "(She just seems so innocent, I didn't think she would...)"

    call process_character(si, appearance = "pose handsup face concerned blush false")
    si.c "[sa.say_name]?"

    call process_character(si, appearance = "pose handsup face concerned blush false")
    si.c "Is there something you want to tell me?"

    call process_character(sa, appearance = "pose leaning face embarrassed blush true")
    sa.c "(Uh oh...)"

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "..."

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "(She knows what I'm talking about)"

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "[sa.say_name]..."

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "Why were you outside my door watching me?"

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "U-um... {w=0.5}well..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "The thing is..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "..."

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "What were you doing [sa.say_name]?"

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "Tell me the truth..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "I-I..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "A-are you sure... {w=0.5}y-you want to know?"

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "I wouldn't be asking this otherwise."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "...{p}..."

    call process_character(sa, appearance = "pose leaning face embarrassed blush true")
    sa.c "Okay, I come clean!"

    call process_character(sa, appearance = "pose leaning face embarrassed blush true")
    sa.c "I was masturbating, Mom!"

    call process_character(si, appearance = "pose handsup face concerned blush false")

    pause 1.0

    call process_character(si, appearance = "pose handsup face concerned blush false")
    si.c "And why were you masturbating?"

    call process_character(sa, appearance = "pose leaning face embarrassed blush true")
    sa.c "U-um, I was masturbating... {w=0.5}b-because..."

    call process_character(sa, appearance = "pose leaning face embarrassed blush true")
    sa.c "My body felt really hot."

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "What made you feel that way, [sa.say_name]?"

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "I-I..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "I don't know."

    call process_character(si, appearance = "pose handsup face concerned blush false")
    si.c "I think you do know, [sa.say_name]."

    call process_character(si, appearance = "pose handsup face concerned blush false")
    si.c "Please tell me."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "T-the reason why I felt like that and started masturbating was...."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face neutral blush true")
    sa.c "I-I liked looking at you!"

    call process_character(sa, appearance = "pose handface face neutral blush true")
    sa.c "I'm really jealous of your boobs!"

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "They're really huge, and mine are really small..."

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "And t-then... {w=1.0}I just started masturbating, {w=0.5}and that's when I couldn't stop myself!"

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "I never felt anything like it!"

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "(Well, at least she's honest about how she's feeling)"

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "(She's gotten more ambitious)"

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "(And wants to see as much of me as she can)"

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "..."

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "I see..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "Please don't be mad at me, Mom..."

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "Well, you should not have been spying on me, [sa.say_name]."

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "You should have known better than to do something like that."

    call process_character(sa, appearance = "pose leaning face concerned blush true")
    sa.c "I'm really sorry, Mom!"

    call process_character(sa, appearance = "pose leaning face concerned blush true")
    sa.c "I should have stopped, but..."

    call process_character(si, appearance = "pose handsup face concerned blush false")
    si.c "..."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "I know you feel bad about it."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "And you told me the truth."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "So of course I'm not mad at you."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "You confessed to me, and you admitted it was wrong to do."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "It's good that you understood you made a mistake."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "Um, Mom?"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "Can I ask you a question about what you were doing?"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "That's..."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Of course you can, [sa.say_name]."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "What did you want to know?"

    menu:
        "Were you masturbating?":
            call process_character(si, appearance = "pose armunder face neutral blush true")
            si.c "..."

            call process_character(si, appearance = "pose armunder face neutral blush true")
            si.c "Yes..."

            call process_character(si, appearance = "pose armunder face neutral blush true")
            si.c "I was masturbating."
        "What were you thinking about when I saw you?":
#            call add_boldness(1, tag = "simone_convo_12_sam_thinking_about")
            call process_character(si, appearance = "pose armunder face embarrassed blush true")
            si.c "!"

            call process_character(si, appearance = "pose armunder face embarrassed blush true")
            si.c "..."

            call process_character(si, appearance = "pose armunder face embarrassed blush true")
            si.c "(Normally, I would want to tell [sa.say_name] the truth, {w=0.5}but...)"

            call process_character(si, appearance = "pose armunder face embarrassed blush true")
            si.c "(Telling her exactly what I was thinking about...)"

            call process_character(si, appearance = "pose armunder face embarrassed blush true")
            si.c "(That would lead to an awkward situation!)"

            call process_character(si, appearance = "pose armunder face embarrassed blush true")
            si.c "...{p}..."

            call process_character(si, appearance = "pose handsup face neutral blush false")
            si.c "(I'll just... {w=1.0}stretch the truth with her...)"

            call process_character(si, appearance = "pose handsup face neutral blush false")
            si.c "Well..."

            call process_character(si, appearance = "pose handsup face neutral blush false")
            si.c "Mommy was thinking about how good it felt."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "Did it feel good, Mom?"

    call process_character(si, appearance = "pose handsfront face neutral blush true")
    si.c "It felt very good."

    call process_character(si, appearance = "pose handsfront face neutral blush true")
    si.c "It's like how you feel when you masturbate."

    call process_character(si, appearance = "pose armunder face curious blush true")
    si.c "You feel all hot and bothered inside..."

    call process_character(si, appearance = "pose armunder face flirty blush true")
    si.c "And the heat inside you builds up to levels you can't control."

    call process_character(si, appearance = "pose armunder face flirty blush true")
    si.c "Your needs are so strong that you end up finding a way to release them..."

    $ renpy.pause(1.0)

    call process_character(si, appearance = "pose armunder face flirty blush true")
    si.c "{i}Sigh.{/i}.."

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "M-Mom..."

    call process_character(sa, appearance = "pose handsbehind face embarrassed blush true")
    sa.c "..."

    call process_character(si, appearance = "pose handsfront face embarrassed blush true")
    si.c "...{p}..."

    call process_character(si, appearance = "pose handsfront face embarrassed blush true")
    si.c "I'm sorry, [sa.say_name]. {p=1.0}That was a bit much."

    call process_character(sa, appearance = "pose leaning face neutral blush true")
    sa.c "No, it's cool actually!"

    call process_character(sa, appearance = "pose leaning face neutral blush true")
    sa.c "You're always so calm and gentle, that seeing you like that..."

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "...What were you thinking about in the bathroom?"

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "W-well..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "I was thinking of you."

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "!!!"

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "(What should I tell her?)"

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "..."

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "(If I say it's bad, then she'll feel guilty every time she masturbates)"

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "(But if I say it's okay...)"

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "(What kind of door am I opening?)"

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "(Will she get more curious?)"

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "..."

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "(It's impossible to know how she'll react)"

    call process_character(si, appearance = "pose armunder face embarrassed blush true")
    si.c "...{p}..."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "You are still growing, [sa.say_name]."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "There's still so much to learn."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "And before long, you will blossom into a lovely young woman."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "These feelings are new to you, after all."

    $ renpy.pause(1)

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "So I have no problem with what you are feeling towards me."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "So it's okay then?"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "It's perfectly fine."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "T-thanks so much, Mom!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "I feel so much better now!"

    call process_character(sa, appearance = "pose leaning face concerned blush false")
    sa.c "I was really worried that it was... {w=0.5}you know, {w=0.5}weird."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "There's nothing to worry about, [sa.say_name]."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "I'm glad you're feeling better about it."

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "Thanks again, Mom!"

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "Love you!"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "Love you too, [sa.say_name]."

    call character_leave_dissolve(sa)
    $ renpy.pause(1)

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "(I'm glad she's feeling better about the whole situation)"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face neutral blush true")
    si.c "(I wonder what she fantasizes about with me?)"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "(Are they the same as my fantasies?)"

    call process_end_of_bonus_scene("simone_convo_11_leftovers_sam_mod", si)

    return

label simone_convo_12_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose armunder face happy position right") ])

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "My arms feel like lead bricks today!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "You've been doing a lot of work in the garden, Mom!"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Yes, I have. {p=1.0}It's been tough work, but it's very fulfilling."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "How about you?"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "I'm all ready to go!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Sure, I'm still a little sore... {w=0.5}but I feel just fine!"

    call process_character(si, appearance = "pose handsfront face happy blush false")
    si.c "That's because you have new, well oiled parts!"

    call process_character(si, appearance = "pose handsfront face happy blush false")
    si.c "Whereas I've seen some mileage already!"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "..."

    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "That means I'm getting old, [sa.say_name]."

    call process_character(sa, appearance = "pose leaning face concerned blush false")
    sa.c "But you're not old at all, Mom!"

    call process_character(sa, appearance = "pose leaning face curious blush false")
    sa.c "Or at least... {w=0.5}you don't {i}look{/i} old."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "Are you practicing how to charm mature women, [sa.say_name]?"

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "Who knew my own daughter was such a charmer?"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Haha, no..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "That has me curious, [sa.say_name]."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Yeah?"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "I know you're probably not thinking about this much, especially at your age, but..."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "There comes a time where girls start thinking about boys."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "Is there any that caught your eye yet?"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Oh, tons!"

    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "Haha, I didn't mean friends, sweetie!"

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "Is there anyone you'd like to be... {w=1.0}{i}\"more than friends\"{/i} with?"

    menu:
        "Um, actually, t-there is one person...":
    #        if store.had_sam_vaginal_scene and "sam_scene_post_vaginal" in scenes_completed:
                call process_character(sa, appearance = "pose handface face concerned blush true")

                call process_character(si, appearance = "pose handsup face happy blush false")
                si.c "Oh? Do tell."

                call process_character(sa, appearance = "pose handsbehind face neutral blush true")
                sa.c "I can't share any details just yet!"

                call process_character(sa, appearance = "pose handsbehind face neutral blush true")
                sa.c "Just know that he's really sweet."

                call process_character(sa, appearance = "pose handsbehind face happy blush true")
                sa.c "And he's into the same things as me!"

                call process_character(si, appearance = "pose handsup face neutral blush false")
                si.c "I'm sure you two would make a very cute couple."

                call process_character(si, appearance = "pose handsup face happy blush false")
                si.c "(Ah, young love!)"

                call process_character(si, appearance = "pose handsup face happy blush false")
                si.c "(My [sa.say_name] is growing up so fast)"

#                call process_character(sa, appearance = "pose handface face concerned blush false")
#                sa.c "(Something tells me I shouldn't tell her about what me and [n.say_name] have been up to just yet...)"
        "M-Mom!":
            call process_character(sa, appearance = "pose leaning face embarrassed blush true")

            call process_character(si, appearance = "pose handsfront face neutral blush false")
            si.c "There's no need to be embarrassed, sweetie."

            call process_character(si, appearance = "pose handsfront face neutral blush false")
            si.c "I'm only being curious."

            call process_character(si, appearance = "pose handsfront face neutral blush false")
            si.c "There must be many cute boys at your school."

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "Perhaps one you met online?"

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "Or on that games console you play?"

            call process_character(si, appearance = "pose handsup face neutral blush false")
            si.c "Still, it would be nice if you brought a boy home."

            call process_character(si, appearance = "pose handsup face happy blush false")
            si.c "I think it'd be very sweet!"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "It would also be lovely if I had grandchildren one day too."

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "I would tell them they have their mother's smile while they're playing video games!"

    call process_character(sa, appearance = "pose handface face embarrassed blush true")
    sa.c "..."

    $ renpy.pause(1)

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "I'm only teasing you, dear."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "There's no rush whatsoever."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "You're still very young."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "I felt very much the same way you do when I was your age."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "Who you choose to be with is your decision."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "As you grow older you'll decide who is best for you."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Regardless, I think that having that \"special someone\" in your life makes it all worth it."

    $ renpy.pause(1.0)

    call process_character(sa, appearance = "pose handface face neutral blush false")

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Hmm..."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "While we're on the topic..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "What kind of boy, or girl even, would you like to date?"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "If you wanted to date, of course."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "For example..."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face flirt blush false")
    si.c "Our relationship has definitely seen some changes over the summer."

    call process_character(si, appearance = "pose armunder face flirt blush false")
    si.c "With that in mind, would I be someone you would date?"

    menu:
        "Yes!":
            call process_character(sa, appearance = "pose leaning face happy blush false")

            call process_character(si, appearance = "pose handsfront face neutral blush false")
            si.c "Why thank you, [sa.say_name]!"

            call process_character(si, appearance = "pose handsfront face neutral blush false")
            si.c "So you wouldn't mind dating an older person?"

            call process_character(sa, appearance = "pose leaning face neutral blush false")
            sa.c "Not at all!"

            call process_character(sa, appearance = "pose leaning face happy blush false")
            sa.c "Especially if they were as kind as you, Mom!"

            call process_character(si, appearance = "pose armunder face happy blush false")
            si.c "Oh my, I'm flattered, sweetie!"

            call process_character(si, appearance = "pose armunder face flirt blush false")
            si.c "I didn't know you were such a sweet talker."

            call process_character(si, appearance = "pose armunder face flirt blush false")
            si.c "Who knew you had that in you?"
        "You can be my girlfriend Mom!":
#            call add_boldness(1, tag = "simone_convo_13_sam_being_my_girlfriend")
            call process_character(sa, appearance = "pose handsbehind face happy blush true")

            call process_character(si, appearance = "pose armunder face happy blush true")
            si.c "Haha, oh my!"

            call process_character(si, appearance = "pose armunder face happy blush true")
            si.c "No first date?"

            call process_character(si, appearance = "pose armunder face happy blush true")
            si.c "Just cut straight to the chase and be in a relationship?"

            call process_character(sa, appearance = "pose handface face neutral blush false")
            sa.c "Yeah!"

            call process_character(sa, appearance = "pose handface face neutral blush false")
            sa.c "Who needs dates anyways?"

            call process_character(si, appearance = "pose handsfront face neutral blush false")
            si.c "The option is always there."

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "But usually a first date lets you know if you have a connection to the person."

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "Then from there, you could start a relationship."

            call process_character(sa, appearance = "pose handface face happy blush false")
            sa.c "Yeah, I get it!"

            call process_character(sa, appearance = "pose handface face happy blush false")
            sa.c "Man, it'd be so cool if you and I were together like that, Mom!"

            call process_character(si, appearance = "pose handsfront face flirt blush true")
            si.c "(I'd be her girlfriend?)"

            call process_character(si, appearance = "pose handsfront face flirt blush true")
            si.c "(Well, I don't think too many people would be bothered by the age difference)"

            call process_character(si, appearance = "pose armunder face embarrassed blush true")
            si.c "(But they'd have to get used to a mother and daughter relationship on {i}that{/i} level...)"

            call process_character(si, appearance = "pose armunder face embarrassed blush true")
            si.c "..."

            call process_character(si, appearance = "pose armunder face neutral blush true")
            si.c "(While it's not something I originally had in mind for [sa.say_name])"

            call process_character(si, appearance = "pose armunder face flirt blush true")
            si.c "(I'm not opposed to the idea of it)"

            call process_character(si, appearance = "pose armunder face flirt blush true")
            si.c "..."

    call process_character(sa, appearance = "pose handface face neutral blush false")

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "I was just curious..."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "No need to think too hard about it."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Do you know when you'll be working on the garden again, Mom?"

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "It's practically on a daily basis."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "But I'm going to take it easy today."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "So does that mean you won't be able to..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "T-touch me today?"

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "([k.say_name] and [n.say_name] are around)"

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "(Wouldn't exactly be smart to caress [sa.say_name] and risk being seen...)"

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "..."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Sorry, [sa.say_name], not today."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "Aww..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "But..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "I know you enjoy it."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "So you can always ask me when I'm available."

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "Nice!"

    call process_character(si, appearance = "pose armunder face curious blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face curious blush false")
    si.c "(Maybe I can find a way to convince [k.say_name] and [n.say_name] to go to the mall)"

    call process_character(si, appearance = "pose armunder face flirt blush false")
    si.c "(Then that gives [sa.say_name] and I plenty of time...)"

    call process_end_of_bonus_scene("simone_convo_12_leftovers_sam_mod", si)

    return

label simone_convo_13_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose handsup face happy position right") ])

    call process_character(si, appearance = "outfit clothes pose handsup face happy blush false")
    si.c "I've never seen the house so well organized!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "You look really happy about that, Mom!"

    call process_character(si, appearance = "pose handsfront face happy blush false")
    si.c "I am!"

    call process_character(si, appearance = "pose handsfront face happy blush false")
    si.c "I actually have free time in the day."

    call process_character(si, appearance = "pose handsfront face happy blush false")
    si.c "That's a first!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Anything planned?"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "You know, that is a good question!"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "I'd have to think about it..."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Ooh, I know!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "You could swim in the pool!"

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "I haven't had a chance to yet, that's true."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face happy blush false")
    si.c "You know what, I think I will do that!"

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "I'll go change into my bathing suit right now."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Mom?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Is it okay if I help you change?"

    call process_character(si, appearance = "pose handsfront face happy blush false")
    si.c "Is that what you really want to see?"

    call process_character(si, appearance = "pose handsfront face happy blush false")
    si.c "Me stripping rather than going into our pool?"

    call process_character(sa, appearance = "pose handface face neutral blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face neutral blush true")
    sa.c "Maybe..."

    call process_character(si, appearance = "pose handsup face neutral blush false")

    $ renpy.pause(0.5)
    call character_leave_dissolve(si)
    $ renpy.pause(1)

    call process_character(si, appearance = "outfit underwear pose handsup face flirt blush false")
    si.c "I'll have you pick [sa.say_name]."

    call process_character(si, appearance = "pose handsup face flirt blush false")
    si.c "Would you like to see me take my bra or my panties off first?"

    menu:
        "Show me your titties Mom!":
            call character_leave_dissolve(si)
            $ renpy.pause(1)
            call process_character(si, appearance = "outfit topless_underwear pose handsfront face happy blush false")
            si.c "Here they are, for exclusive viewing pleasure!"

            call process_character(sa, appearance = "pose handface face flirt blush true")
            sa.c "...{p}..."

            call process_character(si, appearance = "pose armunder face flirt blush false")
            si.c "..."

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "(I hope she knows she's not exactly being discreet when staring at another woman's chest)"

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "(She would be spotted a mile away with that look...)"

            $ renpy.pause(1)

            call process_character(si, appearance = "pose armunder face neutral blush true")
            si.c "(She really does envy my breasts)"

            call process_character(si, appearance = "pose armunder face neutral blush true")
            si.c "..."

            call process_character(si, appearance = "pose handsfront face neutral blush true")
            si.c "Let me remove my panties as well."

            call process_character(sa, appearance = "pose leaning face neutral blush true")
            sa.c "Go, Mom, go!"
        "I wanna see your vagina Mom!":
            call character_leave_dissolve(si)
            $ renpy.pause(1)
            call process_character(si, appearance = "outfit underwear_bottomless pose handsup face flirt blush false")
            $ renpy.pause(1)

            call process_character(si, appearance = "outfit underwear_bottomless pose handsup face flirt blush false")
            si.c "It's also called a pussy, snatch, or beaver."

            call process_character(sa, appearance = "pose handsbehind face neutral blush true")
            sa.c "Haha, beaver!"

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "I know, it's a ridiculous term."

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "It's used when a woman has hair around the crotch area."

            call process_character(sa, appearance = "pose leaning face happy blush true")
            sa.c "Because it's fuzzy and it eats wood!"

            call process_character(si, appearance = "pose handsup face happy blush false")
            si.c "Haha, maybe!"

            call process_character(si, appearance = "pose handsup face happy blush false")
            si.c "In that case, I hope I'm not too fuzzy down there!"

            call process_character(sa, appearance = "pose leaning face neutral blush true")
            sa.c "I like it, Mom!"

            call process_character(sa, appearance = "pose handsbehind face happy blush true")
            sa.c "I wish I had hair down there too!"

            call process_character(si, appearance = "pose armunder face neutral blush false")
            si.c "It'll appear as you get older, sweetie!"

            call process_character(sa, appearance = "pose handsbehind face happy blush true")
            sa.c "I can't wait!"

            call process_character(si, appearance = "pose armunder face flirt blush false")
            si.c "(I think she just likes seeing me naked)"

            call process_character(si, appearance = "pose armunder face flirt blush false")
            si.c "..."

            call process_character(si, appearance = "pose armunder face flirt blush false")
            si.c "(My [sa.say_name] has never been so mischievous before)"

            call process_character(si, appearance = "pose armunder face flirt blush true")
            si.c "(She's definitely tapped into her \"adventurous\" side)"

            call process_character(si, appearance = "pose armunder face flirt blush true")
            si.c "..."

            call process_character(si, appearance = "pose handsfront face neutral blush true")
            si.c "Let me remove my bra as well."

            call process_character(sa, appearance = "pose leaning face neutral blush true")
            sa.c "Go, Mom, go!"

    call character_leave_dissolve(si)
    $ renpy.pause(1)

    call process_character(si, appearance = "outfit nude")
    call process_character(sa, appearance = "pose handsbehind face flirty blush true")

    call process_character(si, appearance = "pose armunder face flirt blush true")
    si.c "Do you need a few moments [sa.say_name]?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "You should be naked all the time, Mom!"

    call process_character(sa, appearance = "pose handface face happy blush true")
    sa.c "We could be naked buddies!"

    call process_character(si, appearance = "pose handsup face happy blush true")
    si.c "[sa.say_name]! You are so naughty!"

    call process_character(si, appearance = "pose handsup face happy blush true")
    si.c "You'd want your Mom to walk around bare all the time?"

    call process_character(sa, appearance = "pose leaning face happy blush true")
    sa.c "That'd be so cool!"

    call process_character(si, appearance = "pose armunder face happy blush true")
    si.c "Haha, [sa.say_name]!"

    call process_character(si, appearance = "pose armunder face happy blush true")
    si.c "Very naughty!"

    call process_character(sa, appearance = "pose handface face neutral blush false")

    call character_leave_dissolve(si)
    $ renpy.pause(1)

    call process_character(si, appearance = "outfit swimsuit pose handsfront face neutral blush false")
    si.c "Are you going to be joining me, [sa.say_name]?"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yeah!"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "I never pass up pool time!"

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "Just try and keep yourself composed, sweetie."

    call process_character(si, appearance = "pose handsup face happy blush true")
    si.c "Or else [k.say_name] catches onto that \"womanly charm\" you have!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "..."

    call process_end_of_bonus_scene("simone_convo_13_leftovers_sam_mod", si)

    return

label simone_convo_14_leftovers_sam_mod:
    call process_new_location(bg = simone_room)
    call process_conversation_beginning([ (sa, "outfit clothes pose handface face neutral position left"), (si, "outfit clothes pose handsfront face neutral position right") ])

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "Hi, sweetie."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Hi, Mom!"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "Where's [n.say_name]?"

    if store.had_julia_arrived_scene and "julia_scene_post_vaginal" not in scenes_completed:
        call process_character(sa, appearance = "pose handface face neutral blush false")
        sa.c "He's showing [julia.say_name] the video game collection in my room!"

        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "I think she wants to play Temples & Hydras with us!"

        call process_character(si, appearance = "pose armunder face happy blush false")
        si.c "I hope that goes well for her!"

        call process_character(si, appearance = "pose armunder face neutral blush false")
        si.c "[julia.say_name] used to love playing it with you two."

        call process_character(si, appearance = "pose handsup face neutral blush false")
        si.c "Are you going to join them?"

        call process_character(sa, appearance = "pose leaning face neutral blush false")
        sa.c "In a bit, yeah!"

        call process_character(sa, appearance = "pose leaning face neutral blush false")
        sa.c "[n.say_name]'s going over the rules again with [julia.say_name] cause she forgot."

        call process_character(si, appearance = "pose handsup face neutral blush false")
        si.c "Oh I see."

        call process_character(si, appearance = "pose handsup face happy blush false")
        si.c "My brain would melt trying to read that rulebook of yours!"
    else:
        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "I think he wants to play Temples & Hydras with me!"

        call process_character(si, appearance = "pose armunder face happy blush false")
        si.c "You two love playing that game, don't you?"

        call process_character(sa, appearance = "pose leaning face happy blush false")
        sa.c "Yeah!"

        call process_character(sa, appearance = "pose leaning face happy blush false")
        sa.c "We get to write up our own characters each time."

        call process_character(sa, appearance = "pose leaning face happy blush false")
        sa.c "I'm going to be a wererabbit this time around!"

        call process_character(si, appearance = "pose armunder face curious blush false")
        si.c "Wererabbit?"

        call process_character(sa, appearance = "pose leaning face neutral blush false")
        sa.c "[n.say_name] sometimes likes to be a werewolf, so I wanted to be something a bit cuter!"

        call process_character(sa, appearance = "pose leaning face neutral blush false")
        sa.c "It's like a werewolf, but a rabbit instead."

        call process_character(si, appearance = "pose handsup face happy blush false")
        si.c "Oh, how cute!"

        call process_character(si, appearance = "pose handsup face happy blush false")
        si.c "Rabbits suit you well!"

        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "I'm pretending to be her in the game!"

        call process_character(si, appearance = "pose handsfront face neutral blush false")
        si.c "Oh, I see."

        call process_character(si, appearance = "pose handsfront face neutral blush false")
        si.c "So you become the character."

        call process_character(sa, appearance = "pose handface face neutral blush false")
        sa.c "Yeah!"

    $ k.position = "right"
    call character_leave_dissolve(sa)

    call process_character(k, appearance = "outfit naked pose armsup face neutral blush false")
    k.c "{i}Whew!{/i}"

    call process_character(k, appearance = "outfit naked pose armsup face neutral blush false")
    k.c "It is warm in my room!"

    $ k.position = "left"

    call process_character(k, appearance = "outfit naked pose armsup face neutral blush false position left")

    call process_character(si, appearance = "pose armunder face shock blush false")
    si.c "[k.say_name]!"

    call process_character(si, appearance = "pose armunder face shock blush false")
    si.c "Where are your clothes?!"

    call process_character(k, appearance = "outfit naked pose handhip face neutral blush false")
    k.c "I was hot, so I took them off."

    call process_character(si, appearance = "pose handsup face shock blush false")
    si.c "So you're just walking around the house bare?!"

    call process_character(k, appearance = "outfit naked pose handhip face neutral blush false")
    k.c "I walk around in my underwear all the time."

    call process_character(k, appearance = "outfit naked pose handhip face neutral blush false")
    k.c "This isn't much different."

    call process_character(si, appearance = "pose handsup face embarrassed blush false")
    si.c "It's a lot different!"

    call process_character(k, appearance = "outfit naked pose armcross face curious blush false")
    k.c "Mom, what's the issue here?"

    call process_character(k, appearance = "outfit naked pose armcross face curious blush false")
    k.c "[sa.say_name] never seen another woman naked before?"

    call process_character(k, appearance = "outfit naked pose armcross face curious blush false")
    k.c "Come on, she's gotta be more used to it by now."

    call process_character(k, appearance = "outfit naked pose armsup face neutral blush false")
    k.c "We all have the same equipment here."

    call character_leave_dissolve(k)

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "..."

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "Well..."

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "Even so..."

    call character_leave_dissolve(sa)

    call process_character(k, appearance = "outfit naked pose handhip face concerned blush false")
    k.c "I don't know how you're able to tolerate wearing your clothes in this heat, Mom!"

    call process_character(k, appearance = "outfit naked pose handhip face neutral blush false")
    k.c "You should just be naked like me."

    call process_character(si, appearance = "pose armunder face shock blush false")
    si.c "W-What?!"

    call process_character(k, appearance = "outfit naked pose armsup face neutral blush false")
    k.c "[sa.say_name], you too!"

    call process_character(k, appearance = "outfit naked pose armsup face happy blush false")
    k.c "We're all gonna have our titties bounce as we walk around!"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "Woo! Wait for me!"

    call character_leave_dissolve(sa)

    call process_character(si, appearance = "pose handsup face embarrassed blush true")
    si.c "That is perverse, [k.say_name]!"

    call process_character(k, appearance = "outfit naked pose armcross face neutral blush false")
    k.c "Afraid you spoke too soon, Mom."

    call process_character(k, appearance = "outfit naked pose armcross face neutral blush false")
    k.c "Look at [sa.say_name]..."

    call character_leave_dissolve(k)

    call process_character(sa, appearance = "outfit naked pose handsbehind face happy blush false")
    sa.c "...{p}..."

    call process_character(si, appearance = "pose handsfront face shock blush true")
    si.c "[sa.say_name]!"

    call process_character(si, appearance = "pose handsfront face shock blush true")
    si.c "Don't join in on [k.say_name]'s antics!"

    call process_character(si, appearance = "pose handsfront face shock blush true")
    si.c "And how did you get your clothes off that quickly, anyway?"

    call process_character(k, appearance = "outfit naked pose armcross face neutral blush false")
    k.c "Practice, Mom."

    call process_character(k, appearance = "outfit naked pose armcross face neutral blush false")
    k.c "As soon as I mentioned our titties bouncing..."

    call process_character(k, appearance = "outfit naked pose armsup face happy blush false")
    k.c "She was raring to go!"

    call process_character(sa, appearance = "outfit naked pose handsbehind face flirt blush true")
    sa.c "..."

    call process_character(si, appearance = "pose handsfront face embarrassed blush false")
    si.c "...{p}..."

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "[sa.say_name], you're glistening."

    call process_character(k, appearance = "outfit naked pose handhip face flirt blush false")
    k.c "She's flushed red!"

    call process_character(k, appearance = "outfit naked pose handhip face flirt blush false")
    k.c "I can't believe my little sis is in heat over a certain someone!"

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "...{p}..."

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "I'm sorry, [sa.say_name], but I can't."

    call process_character(si, appearance = "pose handsfront face concerned blush false")
    si.c "What if [julia.say_name] or [n.say_name] were to see all of us naked?"

    call process_character(sa, appearance = "outfit naked pose leaning face happy blush false")
    sa.c "Then [k.say_name] would tell them to get naked too!"

    call process_character(k, appearance = "outfit naked pose armsup face happy blush false")
    k.c "Hah! Damn right, sis!"

    call process_character(si, appearance = "pose handsup face angry blush false")
    si.c "That's enough, you two!"

    call process_character(si, appearance = "pose handsup face angry blush false")
    si.c "Please at least put on your bikinis, {w=0.5}o-or something!"

    call process_character(k, appearance = "outfit naked pose handhip face neutral blush false")
    k.c "Alright, alright."

    call process_character(k, appearance = "outfit naked pose handhip face neutral blush false")
    k.c "We didn't meant to upset you, Mom."

    call process_character(k, appearance = "outfit naked pose handhip face neutral blush false")
    k.c "We were only having a bit of fun."

    call character_leave_dissolve(k)

    call process_character(sa, appearance = "outfit naked pose handface face neutral blush true")
    sa.c "..."

    call process_character(k, appearance = "outfit naked pose armcross face neutral blush false")
    k.c "But hey, are you gonna take care of [sa.say_name]'s little problem there?"

    call process_character(k, appearance = "outfit naked pose armcross face flirt blush false")
    k.c "Or do you want me to carry her up to my room?"

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "O-Oh..."

    call process_character(si, appearance = "pose armunder face embarrassed blush false")
    si.c "..."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "I'll..."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "I'll take care of it."

    call process_character(k, appearance = "outfit naked pose armsup face neutral blush false")
    k.c "Wish I could watch, but I gotta put something on before [n.say_name] or [julia.say_name] sees me!"

    call process_character(k, appearance = "outfit naked pose armsup face neutral blush false")
    k.c "Oh, one more thing, Mom..."

    call process_character(k, appearance = "outfit naked pose armsup face happy blush false")
    k.c "If you use your fingers, start with the ring finger, she really likes it!"

    call process_character(k, appearance = "outfit naked pose armsup face happy blush false")
    k.c "You two have fun!"

    call character_leave_dissolve(k)
    pause 0.5

    call process_character(sa, appearance = "outfit naked pose handface face neutral blush true")

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "...{p}..."

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "Your sister really knows how to blow up a conversation."

    call process_character(si, appearance = "pose armunder face concerned blush false")
    si.c "I would expect no less from her."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "..."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "But since you're already nude..."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "Would you like me to use my fingers, sweetie?"

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "I'll be sure to do what [k.say_name] said you liked."

    call process_character(sa, appearance = "outfit naked pose handsbehind face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "outfit naked pose handsbehind face concerned blush true")
    sa.c "Y-yes please, Mom..."

    call fade_to_black(0.5)
    "{i}Mom fingered me, and I ended up squirting on her hand.{/i}"

    $ reset_all_characters()

    call process_end_of_bonus_scene("simone_convo_14_leftovers_sam_mod", si)

    return

## Sam Julia Convos ##
label julia_convo_1_leftovers_sam_mod:
    call process_new_location(bg = living_room)
    call process_conversation_beginning([(sa, "outfit clothes pose handsbehind face neutral blush false position left"), (julia, "outfit clothes pose handup face neutral blush false position right")])

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "You should come join us in the pool, [julia.say_name]!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "[k.say_name] and [n.say_name] are around the pool nearly all the time now."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Oh, I'm not big into swimming."

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "Why not?"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "It's just not my thing."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "Pools especially."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "I'm very picky about my hair."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "Chlorine water messes it up."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "Aww, man..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "And I don't really like the heat to be honest."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I tend to burn easy."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "During summer I stay indoors practically twenty four seven."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "But even then, the heat gets to me in there."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yeah, that's why you hop into the pool!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Mom says it can get really hot around this time of year."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "She always tells me to put on sun-cream."

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "So just say if you need it, [julia.say_name]."

    call process_character(julia, appearance = "pose armcross face curious blush false")
    julia.c "I... {w=1.0}may consider it."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "But on one condition..."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yeah?"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "I'd sit around outside the pool."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "Maybe read a book while I'm at it."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "The weather's a lot more cool here than it is at my house."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "It's hard to read at home sometimes because of the heat."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "All I have in my room is a tiny fan, and no air conditioning."

    $ renpy.pause(1)

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "It's brutal."

    call process_end_of_bonus_scene("julia_convo_1_leftovers_sam_mod", julia)

    return

label julia_convo_2_leftovers_sam_mod:
    call process_new_location(bg = living_room)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (julia, "outfit clothes pose armcross face angry blush false position right")])

    call process_character(julia, appearance = "pose armcross face angry blush false")
    julia.c "Ugh, your brother is hopeless in the hair department!"

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "[n.say_name]?"

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "How so?"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "He couldn't give me a straight answer on how long your hair was."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "But I could have easily told you that, [julia.say_name]!"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "You were busy at the time."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I didn't want to disturb you."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "Oh, and he had no idea on what my bangs were."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "He just called them \"hair thingies\"."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "But while you're here..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "How do you manage it? {p=1.0}Your hair, I mean."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I think I manage just fine."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Your hair's much longer than mine, [julia.say_name]!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Yeah, I'm letting it grow."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I've been growing this for years at this point."

    call process_character(sa, appearance = "pose handface face embarrassed blush false")
    sa.c "Years!?"

    call process_character(julia, appearance = "pose armcross face curious blush false")
    julia.c "Ya..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "But like I said already to [n.say_name], it's getting tougher to manage."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "By how long it took to grow hair this length..."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "It takes forever to dry."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I have to comb it every day to prevent knots."

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "Knots?"

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "I don't think I've ever had a problem like that."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "So your hair never gets twisted and mangled?"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "Um, maybe? {p=1.0}I'm not too sure."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "But Mom's been helping me with stuff like that, anyway!"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "She always said I had messy hair, haha!"

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "My mom's always too busy to help me with things like hair..."

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Then I'd be happy to help you anytime!"

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "I really should be doing this myself..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "It's perfectly fine to ask for help when you need it, [julia.say_name]!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "We all need some help from time to time after all!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "In any case, I'm happy with my hair despite my complaints."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "I can style it all kinds of ways."

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "(Oooh, I wonder what'll she look like with hair like mine!)"

    call process_end_of_bonus_scene("julia_convo_2_leftovers_sam_mod", julia)

    return

label julia_convo_3_leftovers_sam_mod:
    call process_new_location(bg = living_room)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (julia, "outfit clothes pose handup face neutral blush false position right")])

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I really do envy your hair."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I'm still having a lot of problems managing mine."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I'd be happy to give you tips, then!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I was curious and looked up the best tips online."

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "Tip number one... {w=1.0}Comb!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Let your hair loose, comb your bangs and fringe, and use a mirror while you're doing it!"

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "I already do that, [sa.say_name]."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Moving on, then... {w=1.0}tip number two!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Scrunchies! {p=1.0}Mom uses them when she puts my hair up."

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "I think you'd look really cute with a ponytail, [julia.say_name]!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Oh, and sometimes we get these special oils!"

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "Coco... {w=1.0}Coconut oil, I think it's called."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Mom helps me put it on every now and then."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "So tip number three is to put that on your hair, and use special conditioner afterwards!"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "Yeah, I hate when my hair feels sticky to touch."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "[k.say_name] doesn't really care about her hair like we do, so she just skips the oil part entirely."

    call process_character(julia, appearance = "pose handface face curious blush false")
    julia.c "..."

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "But I swear, it makes my hair look silky smooth and smell super nice!"

    call process_character(julia, appearance = "pose handface face happy blush false")
    julia.c "It really does look nice."

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "And tip number four was to stick to a routine, but I think you know that already!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Yeah, that one was obvious."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "You can use anything that's in the bathroom, [julia.say_name]!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "My stuff is on the right usually."

    call process_character(julia, appearance = "pose handup face happy blush false")
    julia.c "Thanks."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I wish I had brought the rest of what we use at home here, though."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I've already used up a bit of what was in the bottom cabinet since I got here."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I preferred the smell to what your sister and your Mom uses."

    call process_character(julia, appearance = "pose armcross face embarrassed blush false")
    julia.c "Sorry about that."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Don't worry about it!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "What's mine is yours, right?"

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "Help yourself to whatever you need!"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "I guess you're free to use anything I have, too."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "Although it's not much."

    call process_end_of_bonus_scene("julia_convo_3_leftovers_sam_mod", julia)

    return

label julia_convo_4_leftovers_sam_mod:
    call process_new_location(bg = living_room)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (julia, "outfit clothes pose handup face angry blush false position right")])

    call process_character(julia, appearance = "pose handup face angry blush false")
    julia.c "Your brother has no sense of privacy!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "What do you mean?"

    call process_character(julia, appearance = "pose handup face angry blush false")
    julia.c "The other day he just whipped open the door!"

    call process_character(julia, appearance = "pose handup face angry blush false")
    julia.c "What kind of person does that?"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "It was when I was sitting outside the pool, and I got soaked."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Yeah, I remember."

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "The look on your face!"

    call process_character(julia, appearance = "pose handface face embarrassed blush false")
    julia.c "I was getting changed in your room, so he saw my..."

    call process_character(julia, appearance = "pose handface face neutral blush true")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face angry blush true")
    julia.c "Anyway, who does that?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "We do that all the time!"

    call process_character(julia, appearance = "pose armcross face embarrassed blush false")
    julia.c "Huh!?"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yeah, sorry about that! {p=1.0}I should have told you."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "We don't tend to knock."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I'm fine with [n.say_name] just coming into my room whenever."

    call process_character(julia, appearance = "pose handup face concerned blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "Well, I don't think you should be."

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "I mean, what if you're getting dressed?"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Oh, it doesn't bother me!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "We were already used to that in the old house."

    call process_character(julia, appearance = "pose armcross face embarrassed blush false")
    julia.c "You were used to seeing each other get dressed!?"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yeah, we shared the same room."

    call process_character(julia, appearance = "pose armcross face embarrassed blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face concerned blush false")
    julia.c "I guess, but..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "Still, I'd be careful if I were you."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "If you're not, he'll end up seeing things you don't want him to see."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "And that'll be embarrassing for the both of you."

    $ renpy.pause(1)

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Just something to consider, that's all."

    call process_end_of_bonus_scene("julia_convo_4_leftovers_sam_mod", julia)

    return

# Sam Bonus Conversations #
label janet_convo_leftovers_sam_mod:
    $ play_music("audio/music/Fashion.ogg", fadein = 2.0, fadeout = 1.0)

    call process_new_location(bg = janet_house)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (janet, "outfit clothes pose handface face neutral blush false position right")])

    call process_character(janet, appearance = "pose handface face neutral blush false")
    janet.c "I have to ask, [sa.say_name]..."

    call process_character(janet, appearance = "pose handface face neutral blush false")
    janet.c "What do you think of modelling?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "It's really cool!"

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "I really admire what you do, Auntie Janet!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Why are you asking, though?"

    call process_character(janet, appearance = "pose handchest face embarrassed blush false")
    janet.c "I tried to get [julia.say_name] to take an interest in my work too, but she wouldn't have it."

    call process_character(janet, appearance = "pose handchest face embarrassed blush false")
    janet.c "She kept telling me her and I are very different."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Yup, sounds like [julia.say_name]!"

    call process_character(janet, appearance = "pose handface face happy blush false")
    janet.c "Actually, [sa.say_name], I think you'd make a star model!"

    call process_character(janet, appearance = "pose handface face happy blush false")
    janet.c "You're very well put together!"

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "You really think so?"

    call process_character(janet, appearance = "pose handchest face happy blush false")
    janet.c "Of course!"

    call process_character(janet, appearance = "pose handhips face happy blush false")
    janet.c "On my watch, no niece of mine could get away with looking like a mess!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "..."

    call process_character(janet, appearance = "pose handhips face neutral blush false")
    janet.c "And besides..."

    call process_character(janet, appearance = "pose handchest face neutral blush false")
    janet.c "Cuteness is the craze right now."

    call process_character(janet, appearance = "pose handchest face neutral blush false")
    janet.c "You'd fit right in!"

    call process_character(janet, appearance = "pose handface face embarrassed blush false")
    janet.c "It's a shame [julia.say_name] isn't interested, though."

    call process_character(janet, appearance = "pose handface face embarrassed blush false")
    janet.c "She'd make a great model too."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "She would!"

    call process_character(janet, appearance = "pose handchest face happy blush false")
    janet.c "Haha, don't tell her I told you that!"

    call process_character(janet, appearance = "pose handchest face happy blush false")
    janet.c "She'd go ballistic!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "..."

    call process_end_of_bonus_scene("janet_convo_leftovers_sam_mod", janet)

    return

label edna_convo_leftovers_sam_mod:
    $ play_music("audio/music/Funking the Streets.ogg", fadein = 2.0, fadeout = 1.0)

    call process_new_location(bg = edna_house)
    call process_conversation_beginning([(sa, "outfit clothes pose handface face neutral blush false position left"), (edna, "outfit clothes pose handhip face neutral blush false mouth red position right")])

    call process_character(edna, appearance = "pose handhip face neutral blush false")
    edna.c "I've always wondered why grandkids loved cookies."

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "It's because you bake them, Grandma!"

    call process_character(edna, appearance = "pose handhip face happy blush false")
    edna.c "Oh?"

    call process_character(edna, appearance = "pose handhip face happy blush false")
    edna.c "Well, thank you, [sa.say_name]!"

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "You make them so tasty!"

    call process_character(edna, appearance = "pose fisthip face happy blush false")
    edna.c "Yes, you and your brother have always enjoyed the cookies I baked for you."

    call process_character(edna, appearance = "pose handclasp face neutral blush false")
    edna.c "Unfortunately I've never been one for that crunchy aftertaste."

    call process_character(edna, appearance = "pose handclasp face neutral blush false")
    edna.c "Sweet and sour is just the way I like things."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Do you like chocolate, Grandma?"

    call process_character(edna, appearance = "pose handclasp face happy blush false")
    edna.c "Hot chocolate, definitely!"

    call process_character(edna, appearance = "pose handclasp face neutral blush false")
    edna.c "I simply cannot get enough of the beans they use to mix it."

    call process_character(edna, appearance = "pose fisthip face neutral blush false")
    edna.c "Cocoa, I believe?"

    call process_character(edna, appearance = "pose fisthip face neutral blush false")
    edna.c "It creates a rich aftertaste, that's for sure."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Next time you bake us a cookie, you should have one too!"

    call process_character(edna, appearance = "pose handhip face surprised blush false")
    edna.c "Oh, I couldn't do that!"

    call process_character(edna, appearance = "pose handhip face neutral blush false")
    edna.c "I make them specifically for you and [n.say_name]."

    call process_character(edna, appearance = "pose handhip face neutral blush false")
    edna.c "I just love watching your faces light up when you chow down on one."

    call process_character(edna, appearance = "pose handclasp face happy blush false")
    edna.c "It makes my day!"

    call process_end_of_bonus_scene("edna_convo_leftovers_sam_mod", edna)

    return

# Stream Talk #
label stream_talk_1_sam_mod_leftovers:
    call process_scene_beginning(bg = "bg sam_room_evening", char_tuple_array = [ (sa, "outfit underwear pose handface face neutral") ], force_bg_change = True)
    $ play_music("audio/music/Lounge5.ogg", fadein = 2.0, fadeout = 1.0)

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Yup, Complete Steel Conjurer was fun!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "My favorite part was when the enchantress took down an entire army with just one spell!"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "That was so cool!"

    "DronyCascade" "That was my favorite part too!"
    "DronyCascade" "It was straight out of a movie!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Yeah!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Who knew she had it in her?"

    "DronyCascade" "The Potion of Iron must have enhanced her abilities."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Yeah, Indignant Ian was saying the same thing!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "I doubt she could have pulled that off otherwise!"

    call process_end_of_bonus_scene("stream_talk_1_sam_mod_leftovers", sa)

    return

label stream_talk_2_sam_mod_leftovers:
    call process_scene_beginning(bg = "bg sam_room_evening", char_tuple_array = [ (sa, "outfit underwear pose handface face neutral") ], force_bg_change = True)
    $ play_music("audio/music/Lounge5.ogg", fadein = 2.0, fadeout = 1.0)

    "SummersTwo" "It's a good idea you're doing reviews!"
    "SummersTwo" "Channel Impressive and Christie Ramstaff are my go-to for that sort of thing."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "They're good at what they do, aren't they?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "They have neat editing styles, too!"

    "SummersTwo" "I've seen quite a few creators make both movie and game reviews."

    call process_character(sa, appearance = "pose handsbehind face curious blush false")
    sa.c "How do they find the time to do it?"

    "SummersTwo" "Haha!"
    "SummersTwo" "It's their job!"
    "SummersTwo" "They get paid to do it."
    "SummersTwo" "Oh! Speaking of which, you could do it too!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "You think so?"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "I don't know much about movies compared to video games..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I'd be treading unfamiliar territory there!"

    "SummersTwo" "It's worth a shot at least, right?"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "Hmm..."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "I'll ask [n.say_name] about it next chance I get."

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "Thanks for the suggestion!"

    call process_end_of_bonus_scene("stream_talk_2_sam_mod_leftovers", sa)

    return

label stream_talk_3_sam_mod_leftovers:
    call process_scene_beginning(bg = "bg sam_room_evening", char_tuple_array = [ (sa, "outfit underwear pose handface face neutral") ], force_bg_change = True)
    $ play_music("audio/music/Lounge5.ogg", fadein = 2.0, fadeout = 1.0)

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Yeah, my big sis knows all about muscle!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "She says the trick to keeping the \"guns\" loaded, as she calls them, is a healthy diet, and a big dose of protein!"

    "StarLake" "Haha, she sounds awesome!"
    "StarLake" "What's her name?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "[k.say_name]."

    "StarLake" "Wow, even her name sounds tough!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Yeah!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "I know, right?"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "I bet she could carry me on her shoulder with no issues at all!"

    "StarLake" "Oh, no doubt there!"

    call process_end_of_bonus_scene("stream_talk_3_sam_mod_leftovers", sa)

    return

label stream_talk_4_sam_mod_leftovers:
    call process_scene_beginning(bg = "bg sam_room_evening", char_tuple_array = [ (sa, "outfit underwear pose handface face neutral") ], force_bg_change = True)
    $ play_music("audio/music/Lounge5.ogg", fadein = 2.0, fadeout = 1.0)

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "What's my favorite meal?"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Oh!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "That's easy, omelettes!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "That and OJ is the way to go, I think!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "But I'm not really too fussy about what I eat."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Except things that are sour, though!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "It always ends up leaving a bad aftertaste in my mouth..."

    call process_character(sa, appearance = "pose handface face angry blush false")
    sa.c "Yuck!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "My big sis [k.say_name] wolfs down anything you put in front of her, though!"

    call process_end_of_bonus_scene("stream_talk_4_sam_mod_leftovers", sa)

    return

label stream_talk_5_sam_mod_leftovers:
    call process_scene_beginning(bg = "bg sam_room_evening", char_tuple_array = [ (sa, "outfit underwear pose handface face concerned") ], force_bg_change = True)
    $ play_music("audio/music/Lounge5.ogg", fadein = 2.0, fadeout = 1.0)

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "How am I doing?"

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I-I'm fine!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Thanks for watching the stream."

    call process_character(sa, appearance = "pose leaning face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose leaning face concerned blush false")
    sa.c "A-actually..."

    call process_character(sa, appearance = "pose leaning face concerned blush false")
    sa.c "Something's been on my mind recently."

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "When you've shared the same room with your brother for so long, I can't shake this strange feeling I have."

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "Sometimes I don't realize he's not there, and in the other room now..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "I know I can see him whenever I want, but it still feels a little lonely, you know?"

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "I liked when we shared the same room."

    call process_character(sa, appearance = "pose handface face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose leaning face concerned blush false")
    sa.c "(Sorry, just wanted to put that out there)"

    call process_character(sa, appearance = "pose leaning face concerned blush false")
    sa.c "(It felt good to get it off my chest, at least)"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Again, thanks for tuning in to the stream, everybody!"

    call process_end_of_bonus_scene("stream_talk_5_sam_mod_leftovers", sa)

    return

label stream_talk_6_sam_mod_leftovers:
    call process_scene_beginning(bg = "bg sam_room_evening", char_tuple_array = [ (sa, "outfit underwear pose handface face neutral") ], force_bg_change = True)
    $ play_music("audio/music/Lounge5.ogg", fadein = 2.0, fadeout = 1.0)

    "DronyCascade" "That was a great stream, Twinsticks!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Thanks, DronyCascade!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "We had a lot of fun too."

    "PartyGirl" "I keep watching parts of it over and over."
    "PartyGirl" "Looks like [n.say_name] had a lot of fun too. <3"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "He most certainly did!"

    "VivaLos" "Don't know if you saw, but there was a crack in the wall on the second stage."
    "VivaLos" "I heard if you break it with a spell, you unlock a new outfit."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Oooh... Viva, that's really neat!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I'll definitely have to try that out next stream."

    "DronyCascade" "Something I did notice though..."
    "DronyCascade" "Towards the end of the stream, you two started looking at each other."

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "{w=1.0}We did?"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "Hmm, I don't remember that..."

    "DronyCascade" "Both of you were smiling, but you weren't saying anything."

    "PartyGirl" "Oh, now that you mention it, yeah!"
    "PartyGirl" "I thought it was really cute!"

    "DronyCascade" "You must have zoned out without realizing it."

    "PartyGirl" "They were having fun, and that's all that matters!"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "You said it, PartyGirl!"

    call process_end_of_bonus_scene("stream_talk_6_sam_mod_leftovers", sa)

    return

label stream_talk_7_sam_mod_leftovers:
    call process_scene_beginning(bg = "bg sam_room_evening", char_tuple_array = [ (sa, "outfit underwear pose handface face neutral") ], force_bg_change = True)
    $ play_music("audio/music/Lounge5.ogg", fadein = 2.0, fadeout = 1.0)

    "PartyGirl" "Oooh, I've been to that area before!"
    "PartyGirl" "The waves there are enormous!"
    "PartyGirl" "I went surfing with my sister there one time, and the waves almost got us!"
    "PartyGirl" "Went straight over our heads!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Wow! That sounds crazy!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "I hope no one got hurt!"

    "PartyGirl" "Thankfully everything turned out fine."
    "PartyGirl" "It gave us a real shock though, haha!"

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "I'll bet!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "[n.say_name] had a run-in with some crazy waves too."

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Mom ran as fast as the wind when she saw what happened!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Remind me to tell you the full story at some point."

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "It's really funny!"

    call process_end_of_bonus_scene("stream_talk_7_sam_mod_leftovers", sa)

    return
