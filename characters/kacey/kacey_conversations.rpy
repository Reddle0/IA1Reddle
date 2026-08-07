label gloryhole_girl_convo_default:
    call process_conversation_beginning([ (n, ""), (gloryhole_girl, "") ])
    gloryhole_girl.c "Hi [n.say_name]!"

    call process_end_of_conversation("gloryhole_girl_convo_default", gloryhole_girl, priority = False, default = True)

    return

# apartment intro
label kacey_apartment_intro(dream = False):
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
    n.c "\"I finally got settled into my new apartment, and I 'd love for you to come see it!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"It's a couple blocks away, but I've sent you directions on your phone to easily get here.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"When you're on the right block, look for the big white building.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"You can't miss it!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"I'll be waving at you from my window, so don't keep me waiting! <3\""

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

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "It looks really nice!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Apart from the last box or two in the corner there, I'm all set here!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Come on, I'll give you the tour!"

    pause 0.25
    
    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "While we're already here, this is the living room."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I have a few games consoles tucked away under the TV."

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
        n.c "Secret plan?"

        call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
        gloryhole_girl.c "Mm-hm!"

        call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
        gloryhole_girl.c "You'll learn all about it soon enough."

        call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
        gloryhole_girl.c "I'm not spilling any secrets just yet!"

        call process_character(n, appearance = "pose behindhead face curious blush false")
        n.c "..."

        call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
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

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "How does a hefty amount of snacks sound?"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "I'm not picky about what I eat, so I like to stock up."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I'd love if you could join me for a meal sometime!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "Sounds good!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I'm no master cook, but I'm sure I could whip you up something good!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
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
    gloryhole_girl.c "Yeah, it's older than the one in the living room, but it still works like a charm!"

    pause 1.0

    $ renpy.pause(1)

    call process_character(n, appearance = "pose behindhead face flirty blush true")
    n.c "..."


    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "I see you eyeing the bed."

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "Getting ideas already?"

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
    gloryhole_girl.c "Well, I think we both know our sessions together can get a little... (w=1.0)messy."

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
    gloryhole_girl.c "Yup!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "It's our own special spot."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "We've already gotten used to it, so let's not give it up just yet!"

    $ renpy.pause(1)

    pause 1.0

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Come on, let's get back to the living room."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I'll get you something to drink."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "Will orange juice do you just fine?"


    call process_new_location("bg kacey_apartment_daytime")

    python hide:
        for char in character_list():
            char.position = "right"
            char.outfit = "clothes"

    pause 0.25
    $ display_multiple_characters([ (gloryhole_girl, "outfit clothes pose handsfront face neutral blush false position left"), (n, "outfit clothesjacket pose handpocket face neutral blush false") ])
    pause 0.25

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You know, I used to live on the other side of town before I rented this new apartment."

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
    gloryhole_girl.c "I thought it'd be better and easier for us to see each other."

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "And that's just what I ended up doing!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "That's really nice of you."

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
    n.c "\"I'm usually in around then.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"Just don't come in with any naughty intentions!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"Or else my landlord will be angry with me.\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"And we wouldn't want that!\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"As for where I am in the evenings...\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "\"Well...\""

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush true")
    n.c "\"You know where to find me! <3\""

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

label kacey_scene_minigame_intro_sex(dream = False):
    call process_scene_beginning(bg = kacey_apartment, char_tuple_array = [ (n, "outfit clothesjacket pose handpocket face happy blush false"), (gloryhole_girl, "outfit clothes pose handsfront face neutral blush false") ], dream = dream )

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "Did you hear?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "About what?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "There's a new arcade in town that opened up last week!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "It's all retro-themed!"

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
    gloryhole_girl.c "I have some video games she might like."

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
    gloryhole_girl.c "I like \"Pentindow\" games since the company always makes good stuff."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "But I also really like the games \"ALTES\" makes."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "\"ALTES\"?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Yup, they're known mostly for the \"New Goddess Revival\" and \"Anima\" series."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Oh, I think I've heard of those!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "What I like about them is how you build up relationships with the characters."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "You fight alongside them, hang out with them on certain days..."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "And eventually you end up spoiling them rotten!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Spoil them?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You know..."
    
    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Gifts, dates, special scenes..."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "It's so rewarding to see that relationship pay off in the end."

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "It's a slice of life, made into a video game!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Maybe that's why I like visual novels too."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "\"Visual novels\"?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face surprised blush false")
    gloryhole_girl.c "Oh, don't tell me you've never played one before!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I haven't..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face surprised blush false")
    gloryhole_girl.c "Then you are seriously missing out!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What makes them different from a regular novel?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Well, the \"visual\" part is the obvious difference."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You get to watch the story play out instead of just reading about it."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c ""

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "So it's like reading a book with pictures?"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "Close!"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "But there's a key difference."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Yeah?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "A regular novel usually keeps you on one path."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "But with visual novels, they tend to spice things up."

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "The fun ones let you make choices that affect the story!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Oh, I've played other video games that do the same!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Your choices can even change your relationship with the characters."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "So one character's path can turn out completely different from someone else's."

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "That's cool!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "So you get to pick where the story goes?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Yup!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Then one little choice comes back later and makes you wonder if you ruined everything!"

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "That can happen?"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Oh, absolutely!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "But that's part of the fun!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You get attached to people, and then suddenly every choice feels important."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "That sounds kind of nice."

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "Maybe I'll show you my favorites sometime."

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

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Some even took out their handhelds and started to play games with each other."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Others started to join in, and soon enough nearly everybody in line was doing it!"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
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

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "But you got everyone in that line playing together..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "That's different, [n.say_name]."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "It was easier when everyone had something else to focus on."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Talking to people normally was a lot harder for me."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Aww..."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "I would have been your friend, [gloryhole_girl.say_name]!"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "That's very sweet of you to say!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "You're cool, you like video games, and you're really fun to talk to..."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "And you have all these cool stories!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "You'll make me blush at this rate, [n.say_name]!"

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

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Hmm..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Is everything okay, [gloryhole_girl.say_name]?"

    call process_character(gloryhole_girl, appearance = "pose handface face embarrassed blush false")
    gloryhole_girl.c "Yup!"

    call process_character(gloryhole_girl, appearance = "pose handface face embarrassed blush false")
    gloryhole_girl.c "I was just thinking about something."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Yeah?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face embarrassed blush false")
    gloryhole_girl.c "I was just thinking about how we started."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Oh, right."

    call process_character(gloryhole_girl, appearance = "pose handsfront face embarrassed blush false")
    gloryhole_girl.c "Yeah..."

    call processw_character(gloryhole_girl, appearance = "pose handsfront face embarrassed blush false")
    gloryhole_girl.c "I just realized I never really told you why I started doing the whole gloryhole thing."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "I was wondering about that..."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I figured you might be."

    call process_character(gloryhole_girl, appearance = "pose handface face embarrassed blush false")
    gloryhole_girl.c "It's not exactly the kind of thing that explains itself."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Did something make you want to try it?"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Sort of."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "It's a long story."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "I may not look it..."

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "But I'm actually pretty adventurous."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "I think I already knew that..."

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "Hehe."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I think the mystery was what got me interested."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Because you didn't know who would be there?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Exactly."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Not knowing who might be on the other side made it feel exciting."

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "And then I met you."

    call process_character(n, appearance = "pose behindhead face embarrassed blush false")
    n.c "..."

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "So I'd say things worked out pretty well!"

    call process_character(n, appearance = "pose behindhead face embarrassed blush false")
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
    n.c "So it was pretty recent?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I installed it as soon as summer arrived."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Were you nervous?"

    call process_character(gloryhole_girl, appearance = "pose handface face embarrassed blush false")
    gloryhole_girl.c "A little."

    call process_character(gloryhole_girl, appearance = "pose handface face flirty blush false")
    gloryhole_girl.c "But that was part of the fun."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "The funny thing is..."

    call process_character(gloryhole_girl, appearance = "pose handface face concerned blush false")
    gloryhole_girl.c "I haven't seen a lot of men around this neighborhood."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "It does seem that way..."

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "Maybe they all got spooked and thought I was a ghost!"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "But I got lucky and ran into you instead!"

    call process_character(n, appearance = "pose behindhead face embarrassed blush false")
    n.c "Lucky?"

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "Very lucky!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Not many are around after dark, after all."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Were you just waiting for somebody to show up?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Pretty much, yes."

    call process_character(gloryhole_girl, appearance = "pose handface face embarrassed blush false")
    gloryhole_girl.c "It sounds a little silly when you say it out loud..."

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "But the waiting was part of the excitement."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "And what if nobody showed up?"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "Then I'd just try another day!"

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "Didn't you get tired of waiting?"

    call process_character(gloryhole_girl, appearance = "pose leaning face neutral blush false")
    gloryhole_girl.c "I'm only there for a couple hours, so the waiting doesn't bother me."

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "I also had... (w=1.0)plenty of other ways to keep myself occupied."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Like what?"

    call process_character(gloryhole_girl, appearance = "pose leaning face flirty blush false")
    gloryhole_girl.c "Wouldn't you like to know?"

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
    n.c "It does feel like we've known each other for a while, though."

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
    gloryhole_girl.c "We got into things backwards from how you're {i}supposed{/i} to do it, right?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What do you mean?"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Well, most people get to know each other first."

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "Then, eventually, things get more... (w=1.0)intimate."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "But for us, it was sex first, talk later!"

    call process_character(n, appearance = "pose behindhead face embarrassed blush false")
    n.c "I guess we really did do things backwards..."

    call process_character(gloryhole_girl, appearance = "pose handsfront face happy blush false")
    gloryhole_girl.c "Very backwards!"

    call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
    gloryhole_girl.c "I guess I shouldn't have expected anything normal from us!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "We've learned so much about each other through sex!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "That sounds kind of funny when you say it like that..."

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "But it's true!"

    call process_character(gloryhole_girl, appearance = "pose handface face surprised blush false")
    gloryhole_girl.c "It's bound us together!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I wouldn't really know about how things are supposed to be..."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "I just know I really like being with you, [gloryhole_girl.say_name]!"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "I'm glad to hear that!"

    call process_character(gloryhole_girl, appearance = "pose leaning face happy blush false")
    gloryhole_girl.c "The feeling is definitely mutual!"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "I also really like spending time with you, [n.say_name]."

    call process_character(n, appearance = "pose handpocket face happy blush false")
    n.c "I'm glad I met you too, [gloryhole_girl.say_name]!"

    call process_character(gloryhole_girl, appearance = "pose handface face neutral blush false")
    gloryhole_girl.c "Who knew a bathroom wall could be such a good matchmaker?"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "It's been a highlight of my summer!"

    call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
    gloryhole_girl.c "So... (w=1.0)thank you for that!"

    $ kacey_disable_talk_intro = True

    call process_end_of_conversation("gloryhole_girl_convo_4", gloryhole_girl, priority = False, default = False)

    return
