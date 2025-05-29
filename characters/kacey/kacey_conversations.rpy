label gloryhole_girl_convo_default:
    call process_conversation_beginning([ (n, ""), (gloryhole_girl, "") ])
    gloryhole_girl.c "Hi [n.say_name]!"

    call process_end_of_conversation("gloryhole_girl_convo_default", gloryhole_girl, priority = False, default = True)

    return

# apartment intro
label kacey_apartment_intro:
    $ replace_position = True

    $ nate_room.decide_and_play_daily_music_queue()
    call process_scene_beginning(bg = "bg nate_room_daytime")

#    call process_scene_beginning(bg = "bg kacey_apartment_daytime")
#    $ kacey_apartment.decide_and_play_daily_music_queue()

#    python hide:
#        for char in character_list():
#            char.position = "right"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious blush false")
    n.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "Hey bro."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "Planning anything today?"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned blush false")
    n.c "Not really..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "Not gonna play video games with [sa.say_name]?"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned blush false")
    n.c "Not today."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned blush false")
    n.c "She said the controllers were having issues."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "Shame."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "Well, don't let me keep you!"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "Oh!"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "I almost forgot."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "Saw your phone light up on your desk just now."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "I think it was a text message?"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "Didn't see who it was from, though."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "Hm?"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "Oh..."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "I'll take a look at it."

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false")
    k.c "I'll leave you to it, then."


    call character_leave_dissolve(k)
    pause 0.5

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious blush false")
    n.c "(I wonder who's texting me right now)"


    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious blush false")
    n.c "...{p}..."

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(It's from [gloryhole_girl.say_name]!)"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(What's it say...)"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "..."


    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"Hi [n.say_name]! Hope you're doing well!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"I've recently got a new apartment, and I'd love for you to come see it!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"It's a couple blocks away, but I've sent you directions on your phone to easily get here.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"When you're on the right block, it'll be the big white building right in front of you.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"You can't miss it!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"I'll be waving at you from my apartment window.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"Don't keep me waiting! <3\""


    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(She sounds really excited about this!)"

    call process_character(n, appearance = "outfit clothesjacket pose handfist face happy blush false")
    n.c "\"I'll be there in a few minutes [gloryhole_girl.say_name]!\""


    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(There!)"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(Better head over as soon as I can!)"

    call process_new_location("bg kacey_apartment_daytime")
    $ replace_position = True
    $ kacey_apartment.decide_and_play_daily_music_queue()

    python hide:
        for char in character_list():
            char.position = "right"

    pause 0.25
    $ display_multiple_characters([ (gloryhole_girl, "outfit clothes pose handsfront face happy blush false position left"), (n, "outfit clothesjacket pose handpocket face neutral blush false") ])
    pause 0.25

    window show

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "You're here!"

    call process_character(n, appearance = "pose handpocket face happy blush false")
    n.c "Hi [gloryhole_girl.say_name]!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "I'm very glad you could make it, [n.say_name]!"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "I'll be renting this apartment from now on, and I'd like to get your thoughts on it!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "I like it!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Apart from the last box or two in the corner there, I'm all set here!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Let me give you a quick tour around!"

    pause 0.25
    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "While we're already here, this is the living room."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Underneath the TV, I have some games consoles tucked away there."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "So any time you want, feel free to use them!"


## conditional
    if "finale_scene" in store.scenes_completed:
        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "This room will be my secret base for my teaching studies!"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "Oh yeah!"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "I remember you saying you wanted to get into teaching."

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "You could be my teacher!"

        call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
        gloryhole_girl.c "In due time, [n.say_name]!"

        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "It's still a ways off yet, I think."

        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "I'm nowhere near ready to begin teaching just yet."

        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "But I'm confident I'll get there eventually!"

    else:
        call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
        gloryhole_girl.c "I'll also be using this room for a secret plan of mine."

        call process_character(n, appearance = "pose behindhead face curious blush false")
        n.c "Oh?"

        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "You'll learn all about it soon enough."

        call process_character(gloryhole_girl, appearance = "pose handface face flirty blush false")
        gloryhole_girl.c "I'm not spilling any secrets just yet!"

        call process_character(n, appearance = "pose behindhead face curious blush false")
        n.c "..."

        call process_character(gloryhole_girl, appearance = "pose handface face flirty blush false")
        gloryhole_girl.c "Just know that if I'm lucky and keep working hard at it, it'll involve you in it!"

    call process_new_location("bg kacey_apartment_kitchen")

    python hide:
        for char in character_list():
            char.position = "right"
            char.outfit = "clothes"

    pause 0.25
    $ display_multiple_characters([ (gloryhole_girl, "outfit clothes pose handsfront face neutral blush false position left"), (n, "outfit clothesjacket pose handpocket face neutral blush false") ])
    pause 0.25

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Moving on..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "This is my kitchen."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Well, it's more than a kitchen, actually."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "It's a kitchen and dining room, all in one!"

    call process_character(n, appearance = "pose twohandfist face embarrassed blush false")
    n.c "Wow, your fridge is huge!"

    call process_character(n, appearance = "pose handpocket face happy blush false")
    n.c "What do you have in there?"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Oh, all kinds of stuff!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I'm not picky about what I eat, so I like to stock up."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I'd love if you could join me for a meal sometime!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "Sounds good!"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "I'm no master cook, but I'm sure I could whip you up something good!"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "You need simply ask!"

    call process_new_location("bg kacey_apartment_room_daytime")

    python hide:
        for char in character_list():
            char.position = "right"
            char.outfit = "clothes"

    pause 0.25
    $ display_multiple_characters([ (gloryhole_girl, "outfit clothes pose handsfront face neutral blush false position left"), (n, "outfit clothesjacket pose handpocket face neutral blush false") ])
    pause 0.25

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "And this is where I sleep."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Nothing fancy, haha!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "You have a TV in here too?"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Yeah, it's slightly older than the one in the living room, but it still works like a charm!"


    pause 1.0

    $ renpy.pause(1)

    call process_character(n, appearance = "pose behindhead face flirty blush true")
    n.c "..."


    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "I see you eyeing the bed!"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "I hope you aren't getting any funny ideas!"


    call process_character(n, appearance = "pose behindhead face flirty blush true")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face flirty blush true")
    n.c "Maybe we could..."

    call process_character(n, appearance = "pose behindhead face flirty blush true")
    n.c "..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face flirty blush true")
    gloryhole_girl.c "Have sex on the bed?"

    call process_character(n, appearance = "pose behindhead face flirty blush true")
    n.c "Y-yeah..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face flirty blush true")
    gloryhole_girl.c "Oh, I would love nothing more!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face sad blush false")
    gloryhole_girl.c "But unfortunately I don't think things are meant to be."

    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "What do you mean?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Well, I think we both know our sessions together can get a little... messy."

    call process_character(n, appearance = "pose handpocket face curious blush true")
    n.c "..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face embarrassed blush false")
    gloryhole_girl.c "I mean, what if your cum ends up soaking the bedsheets?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face embarrassed blush false")
    gloryhole_girl.c "Or ends up on a wall?"

    call process_character(gloryhole_girl, appearance = "pose handface face embarrassed blush false")
    gloryhole_girl.c "It would be very difficult explaining that to my landlord!"

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "She just had the paint done last week!"

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "And cleaning it up would be easier said than done!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "So I guess we're sticking to the park bathrooms for our \"meetups\"?"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "Yup! It's our own special spot!"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "We've already gotten used to it, so let's not give it up just yet!"


    $ renpy.pause(1)

    pause 1.0

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Come on, let's get back to the living room."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I'll fetch you some orange juice."


    call process_new_location("bg kacey_apartment_daytime")

    python hide:
        for char in character_list():
            char.position = "right"
            char.outfit = "clothes"

    pause 0.25
    $ display_multiple_characters([ (gloryhole_girl, "outfit clothes pose handsfront face neutral blush false position left"), (n, "outfit clothesjacket pose handpocket face neutral blush false") ])
    pause 0.25

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You know, I used to live on the other side of town before I rented out this new apartment."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "What made you move here?"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "You!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "You moved because of me?"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "That's right!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Believe it or not, I thought it'd be better for the both of us if we lived closer to each other."

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "And that's just what I ended up doing!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "I also really liked being closer to the park."

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "I think you already know the reason for that one..."


    pause 1.0
    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "Hehe."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "..."


    $ replace_position = True

    call fade_to_black(1)
    "{i}Several hours later...{/i}"

    $ stop_music(fadeout=3)
    call process_scene_beginning(nate_room)

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(That was a lot of fun!)"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "([gloryhole_girl.say_name]'s apartment is so cool!)"


    "{i}Ding!{/i}"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(Hm?)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(Another text?)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(Let me see...)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "..."


    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"One more thing I forgot to mention!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"You can visit my apartment any time you want during the day.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"I'll always be in.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"Just don't come in with any naughty intentions!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"Or else my landlord will be angry with me.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"And we wouldn't want that!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"As for where I am in the evenings...\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\Well...\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush true")
    n.c "You know where to find me! <3\""

    call character_leave_dissolve(n)

    call fade_to_black(1)
    $ had_kacey_apartment_intro = True
    "{i}You can now travel to [gloryhole_girl.say_name]'s apartment during the day.{/i}"
    "{i}You now have the option to \"Talk\" with her, as well as play minigames!{/i}"

    call process_end_of_scene("kacey_apartment_intro", char = gloryhole_girl, dream = dream)

    return

label kacey_scene_minigame_intro(dream = False):
    call kacey_scene_minigame_intro_sex(dream)
    return

label kacey_scene_minigame_intro_sex(dream = dream):
    call process_scene_beginning(bg = kacey_apartment, char_tuple_array = [ (n, "outfit clothesjacket pose handpocket face happy blush false"), (gloryhole_girl, "outfit clothes pose handsfront face neutral blush false") ], dream = dream )

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "Did you hear?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "About what?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "There's a new arcade in town that opened up last week!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "The theme is very retro-styled!"

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "I went there yesterday, and it was huge!"

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "There were so many games there I lost count!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Have you been to it yet?"


## conditional ##
    if "edna_scene_intro_2" in store.scenes_completed:
        call process_character(n, appearance = "pose handfist face happy blush false")
        n.c "I have!"

        call process_character(n, appearance = "pose handfist face happy blush false")
        n.c "In the strip mall, right?"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "I went there with Grandma recently!"

        call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
        gloryhole_girl.c "Oh, you did?"

        call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
        gloryhole_girl.c "That's great to hear!"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "It had fifty different arcade games to play!"

        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "Yup! That's the one!"

        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "In that case, you know what to expect!"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "Oh, are you going to take me there too [gloryhole_girl.say_name]?"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "Please?"

    else:
        call process_character(n, appearance = "pose handpocket face neutral blush false")
        n.c "I haven't."

        call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
        gloryhole_girl.c "Oh, you're missing out!"

        call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
        gloryhole_girl.c "I've been to plenty of arcades already, but that one easily takes the cake!"

        call process_character(n, appearance = "pose handpocket face curious blush false")
        n.c "Where is it?"

        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "It's supposed to be in the strip mall a dozen blocks away."

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "Oh, can we head there?"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "Please?"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "Of course!"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "How could I refuse a cute request like that?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I'll take you any time."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "In fact, we could try out this one co-op game there you might like."

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "But you'll just have to see when we get there!"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "{b}I'll make sure we have plenty of quarters to use!{/b}"

    window hide
    menu:
        "Play Pong Minigame":
            call process_end_of_scene("kacey_scene_minigame_intro", char = gloryhole_girl, dream = dream, force_no_boldness = True, force_not_replayable = True, do_not_jump = True)
            call minigame_table_tennis(partner = gloryhole_girl)
        "Leave":
            call process_end_of_scene("kacey_scene_minigame_intro", char = gloryhole_girl, dream = dream, force_no_boldness = True, force_not_replayable = True, do_not_jump = started_main_game)
            if started_main_game:
                $ gloryhole_girl.scene = ""
                $ kacey_apartment.start()

    return

label gloryhole_girl_convo_1:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg kacey_apartment_evening", char_tuple_array = [(gloryhole_girl, "pose handsfront face neutral blush false"), (n, "pose handpocket face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg kacey_apartment_daytime", char_tuple_array = [(gloryhole_girl, "pose handsfront face neutral blush false"), (n, "pose handpocket face neutral blush false")])

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You should invite your sister over some time!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I have games she may like."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "That would be cool!"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "You two do have a lot in common."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Except [sa.say_name] doesn't wear glasses like you do."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "What games do you have here anyway?"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Oh, plenty!"

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "What would you say your favorite game is?"

    call process_character(gloryhole_girl, appearance = "pose handface face curious blush false")
    gloryhole_girl.c "That's hard to say!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I don't have a favorite, exactly."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I like \"Pentindow\" games since the company that makes them always make good products."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "But I also really like the games \"ALTES\" makes."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "\"ALTES\"?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Yup, they're known mostly for the \"New Goddess Revival\" and \"Anima\" series."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Oh, I think I've heard of those!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "What I like about them is how you're able to build up relationships with the cast of characters."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "You fight alongside them, hang out with them on certain days..."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "And eventually you end up going on dates with them!"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "It's so rewarding to see that relationship pay off in the end."

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "It's a slice of life, made into a video game!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Maybe that's why I like visual novels so much."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "\"Visual novels\"?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face surprised blush false")
    gloryhole_girl.c "Don't tell me you've never seen one before!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I haven't..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face surprised blush false")
    gloryhole_girl.c "Then you are certainly missing out!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What makes it different from a regular novel?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Well, the \"visual\" part is the obvious difference."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Everything appears on a screen.\nYou're able to see the artwork."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Characters, backgrounds..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You get the idea."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "But there's another key difference that separates the two."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Yeah?"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Novel stories are almost always set in stone."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "But with visual novels, it's not like that."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Some are, but most aren't."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You make your own choices throughout the story that can change your relationship with the characters."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "So, for example, going with one character's path will turn out completely different compared to if you ended up going with somebody else."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "That's cool!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "So you can make your own adventure?"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "Yup!"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "Maybe I'll show you my favourites sometime."

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "I'd love that!"

    $ kacey_disable_talk_intro = True

    call process_end_of_conversation("gloryhole_girl_convo_1", gloryhole_girl, priority = False, default = False)

    return

label gloryhole_girl_convo_2:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg kacey_apartment_evening", char_tuple_array = [(gloryhole_girl, "pose handsfront face neutral blush false"), (n, "pose handpocket face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg kacey_apartment_daytime", char_tuple_array = [(gloryhole_girl, "pose handsfront face neutral blush false"), (n, "pose handpocket face neutral blush false")])

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I heard they're ending production of \"Demon Can Laugh\" soon."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Aw, but that game was so cool!"

    call process_character(gloryhole_girl, appearance = "pose handface face sad blush false")
    gloryhole_girl.c "I know, right?"

    call process_character(gloryhole_girl, appearance = "pose handface face sad blush false")
    gloryhole_girl.c "What a shame!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I remember being at the launch party for that game."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Really?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Yup!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "It wasn't much of a \"party\", though."

    call process_character(gloryhole_girl, appearance = "pose handsfront face concerned blush false")
    gloryhole_girl.c "I'd say it was more of a frustrated line of people who hadn't slept enough."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Oh..."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "I wouldn't say it was all bad though."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "We all had fun in our own way!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What do you mean?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Plenty of people were finding ways to socialize."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Some even took out their handhelds and started to play games with each other."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Others started to join in and soon enough nearly everybody in the line were doing it!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Guess who started that?"

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "You?"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "Yep, yours truly!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "That's cool!"

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Now I'm kinda sad I didn't get to know you when you were my age."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "You sounded awesome!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I'm surprised to hear that!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I was actually a bit of a loner."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I usually kept to my own devices."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Aww..."

    call process_character(n, appearance = "pose twohandfist face concerned blush false")
    n.c "I would have been your friend [gloryhole_girl.say_name]!"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "That's very kind of you to say!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "You're cool, you like videogames, you're really fun to talk to..."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "And you have all these cool stories!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You'll make me blush at this rate [n.say_name]!"

    call process_character(n, appearance = "pose twohandfist face happy blush true")
    n.c "Oh, and you feel really good on my penis!"

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush true")
    gloryhole_girl.c "We certainly can't forget that part!"

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush true")
    gloryhole_girl.c "Hehe."

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush true")
    gloryhole_girl.c "You really know the way to a woman's heart, don't you?"

    $ kacey_disable_talk_intro = True

    call process_end_of_conversation("gloryhole_girl_convo_2", gloryhole_girl, priority = False, default = False)

    return

label gloryhole_girl_convo_3:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg kacey_apartment_evening", char_tuple_array = [(gloryhole_girl, "pose handsfront face neutral blush false"), (n, "pose behindhead face curious blush false")])
    else:
        call process_scene_beginning(bg = "bg kacey_apartment_daytime", char_tuple_array = [(gloryhole_girl, "pose handsfront face neutral blush false"), (n, "pose behindhead face curious blush false")])

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I'm curious..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "About what?"

    call process_character(n, appearance = "pose behindhead face embarrassed blush false")
    n.c "Why the gloryhole?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face embarrassed blush false")
    gloryhole_girl.c "Um, well..."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "It's a long story."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I may not look it..."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "But I'm actually pretty adventurous."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I heard a story of a girl back when I was at school that set up a gloryhole."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "She liked not knowing who was on the other side."

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "It was more fun that way!"

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "So you wanted to try it out too?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Yes!"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "The girl really liked to play with penises."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "The cuter, the better."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "And it turns out I'm no different!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I even joined in on some of her \"sessions\", and the boys had to guess who was who."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I'm definitely no stranger to gloryhole fun!"

    call process_character(n, appearance = "pose handpocket face embarrassed blush false")
    n.c "..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face flirty blush false")
    gloryhole_girl.c "I love to experiment."

    call process_character(gloryhole_girl, appearance = "pose handsfront face flirty blush false")
    gloryhole_girl.c "And have fun while doing it."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Did you install the gloryhole?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face embarrassed blush true")
    gloryhole_girl.c "..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face sad blush true")
    gloryhole_girl.c "Do you promise not to laugh?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Promise..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face sad blush true")
    gloryhole_girl.c "Pinky promise?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face sad blush true")
    gloryhole_girl.c "Okay then..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Y-yes. I did."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "It hasn't been there for long, though."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I installed it as soon as summer arrived."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Speaking of which..."

    call process_character(gloryhole_girl, appearance = "pose handface face concerned blush false")
    gloryhole_girl.c "I haven't seen a lot of men around this neighborhood."

    call process_character(gloryhole_girl, appearance = "pose handface face concerned blush false")
    gloryhole_girl.c "I wonder why that is."

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "Maybe they all got spooked and thought I was a ghost!"

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "It does seem that way..."

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "But I'm considering myself lucky that I ran into you instead!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Not many are around after dark after all."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I guess I shouldn't be too surprised there."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Were you just waiting for somebody to show up?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Pretty much, yes."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "And what if nobody showed up?"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "Then I'd just try another day!"

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "Did you not get tired of waiting?"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "I'm only there for a couple hours, so the waiting doesn't bother me."

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "I also had... plenty of other ways to keep myself occupied."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    $ kacey_disable_talk_intro = True

    call process_end_of_conversation("gloryhole_girl_convo_3", gloryhole_girl, priority = False, default = False)

    return

label gloryhole_girl_convo_4:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg kacey_apartment_evening", char_tuple_array = [(gloryhole_girl, "pose handsfront face neutral blush false"), (n, "pose handpocket face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg kacey_apartment_daytime", char_tuple_array = [(gloryhole_girl, "pose handsfront face neutral blush false"), (n, "pose handpocket face neutral blush false")])

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Just look at us."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "We're getting along like old friends!"

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Yeah?"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "It's just weird to think about, that's all."

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "Especially given how we..."

    call process_character(n, appearance = "pose behindhead face flirty blush true")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face flirty blush true")
    n.c "I think I know what you mean..."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "It does feels like we have known each other a while though."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "It wasn't even that long ago that I met you."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "We jumped into the deep end, didn't we?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "(Hehe, deep)"

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Have you been thinking about this for a while?"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Actually, I was just about to ask you the same thing."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "It's just..."

    call process_character(gloryhole_girl, appearance = "pose handface face concerned blush false")
    gloryhole_girl.c "We got into things backwards to how you're 'supposed' to do it, right?"

    call process_character(gloryhole_girl, appearance = "pose handface face concerned blush false")
    gloryhole_girl.c "We did things slightly differently."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What do you mean?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Well, you get to know each other first."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You usually start with these kinds of conversations and then it leads to sex."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "But for us, it's sex first, talk later!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "It's a bit funny to think about how it all works out in the end."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I guess I shouldn't have expected anything different from our relationship!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "We've practically learnt all we can about each other through sex!"

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "It's binded us together!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I wouldn't really know about how things are supposed to be..."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "I just know I really like being with you [gloryhole_girl.say_name]!"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "I'm glad to hear that!"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "The feeling is definitely mutual!"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "I also really like spending time with you, [n.say_name]."

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "It's been a highlight of my summer!"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "So... thank you for that!"

    call process_end_of_conversation("gloryhole_girl_convo_4", gloryhole_girl, priority = False, default = False)

    $ kacey_disable_talk_intro = True

    return
