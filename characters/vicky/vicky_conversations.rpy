label vicky_convo_default:
    call process_conversation_beginning([ (n, ""), (vicky, "") ])
    vicky.c "Hi [n.say_name]!"

    call process_end_of_conversation("vicky_convo_default", vicky, priority = False, default = True)

    return

label vicky_scene_minigame_intro(dream = False):
    call vicky_scene_minigame_intro_sex(dream)
    return

label vicky_scene_minigame_intro_sex(dream = dream):
    call process_scene_beginning(bg = edna_house, char_tuple_array = [ (n, "outfit clothesjacket pose behindhead face neutral blush false"), (vicky, "outfit clothes pose handhip face neutral blush false") ], dream = dream )

#"Ah, Nate!"
#"Excellent timing."
#"You caught me in my off-time."
#"What do you have in your hand, Vicky?"
#"Oh, these?"
#"Well, one of the ways I like to wind down is this..."
#"A deck of cards?"
#"Yup!"
#"The rules are simple."
#"The object of the game is to beat the dealer's hand without going over twenty-one."
#"Without?"
#"That's right."
#"If you end up with twenty-two points or higher, you'll lose automatically."
#"But if you get twenty-one points exactly.."
#"That's called a \"blackjack.\""
#"But if you can't manage to reach twenty-one with the cards you have..."
#"I guess we'll end up basing your score on the total value of those cards."
#"Hmm..."
#"I'm sure you'll get the hang of it in no time."
#"So, what do you say?"
#"Want to give it a shot?"

#"Oh, and one more thing..."
#"I'm willing to put in some extra pocket change."
#"{b}Consider it a lttle bonus on top of our existing partnership."



#"I'll be filling the role of the dealer."

    window hide
    menu:
        "Play Tennis Minigame":
            call process_end_of_scene("edna_scene_minigame_intro", char = edna, dream = dream, force_no_boldness = True, force_not_replayable = True, do_not_jump = True)
            call minigame_table_tennis(partner = edna)
        "Don't Tennis Minigame":
            call process_end_of_scene("edna_scene_minigame_intro", char = edna, dream = dream, force_no_boldness = True, force_not_replayable = True, do_not_jump = started_main_game)
            if started_main_game:
                $ edna.scene = ""
                $ edna_house.start()

    return


label vicky_convo_1:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg apartment_evening", char_tuple_array = [(n, ""), (vicky, "pose fisthip face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg apartment_daytime", char_tuple_array = [(n, ""), (vicky, "pose fisthip face neutral blush false")])

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Don't think I see you eyeing those papers on my desk!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "That's a lot..."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "It certainly is."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "So what's it like?"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Hmm?"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "You must be a really powerful businesswoman if you have all of that on your desk!"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Oh, I wouldn't say that exactly."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "I do believe I've already answered this question before, though..."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "Perhaps in too roundabout a way."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "..."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Well, to answer your question..."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "My job as a ReflexViz.HD associate involves {i}a lot{/i} of work."

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "I don't think there's a limit to it."

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "There's almost never a time I can ever truly relax."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What do you do when you're not working?"

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "That's a bit of a tough question to answer."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "Unfortunately, there's not much I {i}can{/i} do when I'm not working."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "It takes up so much of my time that I find it difficult to slot in personal hours."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "You can't just stop?"

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "I'm afraid it doesn't work that way, [n.say_name]."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "Once you set yourself to goals, it's hard getting out of it."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "I don't feel happy with myself when I'm not working."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "It feels as if I'm wasting valuable time."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "It's tough, but my work is still rewarding at the end of the day."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "How so?"

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "People depend on me."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "For instance, you!"

    call process_character(vicky, appearance = "pose fisthip face surprised blush false")
    vicky.c "What kind of a person would I be if I started slacking off, I'd be leaving them twisting in the wind!"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "That's why I believe that working my hardest every time, all the time is fulfilling."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "It leaves me with a very satisfied feeling."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "My Mom is like that too!"

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "She always spends our time looking after us, but never has any time to herself."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Then I believe that you and her may already know where I'm coming from, then."

## conditional
    if "finale_scene" in scenes_completed:
        call process_character(vicky, appearance = "pose handup face happy blush false")
        vicky.c "And now that I've met her in person, I see that she certainly raised you well!"

        call process_character(vicky, appearance = "pose handup face happy blush false")
        vicky.c "You've grown to be a fine young man!"

    else:
        call process_character(vicky, appearance = "pose handup face happy blush false")
        vicky.c "In any case, I'd love to meet your mother someday!"

        call process_character(vicky, appearance = "pose handup face happy blush false")
        vicky.c "She sounds like a wonderful person!"


    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "Raising kids requires a lot of work, and certainly something you shouldn't slouch on!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Maybe you could put in dedicated break times in your schedule where you're not allowed to work."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "I don't know if my schedule will allow it, but I could give it a shot."

    $ vicky_disable_talk_intro = True

    call process_end_of_conversation("vicky_convo_1", vicky, priority = False, default = False)

    return

label vicky_convo_2:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg apartment_evening", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg apartment_daytime", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "I'm intrigued about the other members in your family, [n.say_name]."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Do you like to spend time with them?"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Yeah!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Especially [sa.say_name]!"

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "You two are inseparable, after all."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "But what about the rest of your family?"

## conditional
    if "finale_scene" in scenes_completed:
        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "Who lives at your household besides [sa.say_name]?"

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "[k.say_name] and your Mom?"

        call process_character(n, appearance = "pose handpocket face neutral blush false")
        n.c "That's right."

        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "There's also [julia.say_name]."

        call process_character(vicky, appearance = "pose fisthip face curious blush false")
        vicky.c "[julia.say_name]?"

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "Oh, the girl with the purple-ish hair!"

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "I believe she said she was your cousin, correct?"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "Yeah!"

        call process_character(vicky, appearance = "pose handhip face happy blush false")
        vicky.c "I liked her fashion style."

        call process_character(vicky, appearance = "pose handhip face happy blush false")
        vicky.c "She'd fit in well with some other business ventures I've been planning."

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "And of course, I met the rest of your family at the pool party we had."

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "Do you all live near each other?"

        call process_character(n, appearance = "pose handpocket face neutral blush false")
        n.c "Yeah, but my Aunt and Grandma live next to the beach."

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "Impressive."

        call process_character(n, appearance = "pose handpocket face neutral blush false")
        n.c "[julia.say_name] lives with my Aunt, but she's been staying over at our house for the summer."

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "I'm sure you must have been happy when she turned up!"

        call process_character(n, appearance = "pose behindhead face happy blush false")
        n.c "Yeah, I hadn't seen her in a long time before that."

        call process_character(vicky, appearance = "pose handhip face happy blush false")
        vicky.c "Your sister [k.say_name] got us all together for a party you won't be forgetting any time soon!"

        call process_character(vicky, appearance = "pose handhip face neutral blush false")
        vicky.c "Be sure to thank her next time you see her."

        call process_character(vicky, appearance = "pose handhip face flirty blush false")
        vicky.c "But I hope she doesn't end up running you dry!"

        call process_character(n, appearance = "pose handpocket face embarrassed blush true")
        n.c "..."

        call process_character(vicky, appearance = "pose handup face happy blush false")
        vicky.c "Just kidding!"

        call process_character(vicky, appearance = "pose handup face happy blush false")
        vicky.c "Although I won't lie, I envy her."

        call process_character(vicky, appearance = "pose handup face happy blush false")
        vicky.c "Having a body like that..."

    else:
        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "Who lives at your household besides [sa.say_name]?"

        call process_character(n, appearance = "pose handpocket face neutral blush false")
        n.c "There's Mom, and my older sister, [k.say_name]."

        call process_character(vicky, appearance = "pose handhip face neutral blush false")
        vicky.c "[k.say_name]..."

        call process_character(vicky, appearance = "pose handhip face happy blush false")
        vicky.c "Now there's a strong-sounding name if I've heard one!"

        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "Yeah, she's really strong."

        call process_character(vicky, appearance = "pose handhip face neutral blush false")
        vicky.c "I hope I get to meet her one day."

        call process_character(n, appearance = "pose handpocket face neutral blush false")
        n.c "I'm pretty sure I'm only able to do pushups at all because of my big sister."

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "Oh, is she into fitness?"

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "I commend her for that!"

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "And for her teaching you how to do pushups!"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Things like that are beyond me, I'm afraid."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Why?"

    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "Let's just say my last attempt at aerobic exercises... didn't exactly go well."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What happened?"

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "I ended up twisting my ankle."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "Somehow..."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Oh..."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "But even if it's not for me, I can still appreciate those who work hard exercising."

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "Especially if they help others along the way!"

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "It's always nice to have someone to help you strive towards becoming a better version of you."

    $ vicky_disable_talk_intro = True

    call process_end_of_conversation("vicky_convo_2", vicky, priority = False, default = False)

    return

label vicky_convo_3:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg apartment_evening", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg apartment_daytime", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "Maybe we could film a movie some time!"

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "A movie?"

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Yeah, it'd be fun!"

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "About that..."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "While it's certainly an interesting idea..."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "I'm afraid it's not going to happen in front of that little camera."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Aww..."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Though I do admire your enthusiasm!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Did you have anything particular in mind?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Uh, not exactly..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I thought it would be cool to do, considering the equipment here."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Movies require a lot more thought than simply picking up a camera and speaking lines."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "It's an ambitious endeavor, after all..."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "You need actors, locations, script writers, musicians..."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "We unfortunately do not have those luxuries, but..."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "If we keep at it, we could expand our horizons."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "For now, let's stick to what we're good at."

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "But I won't object to any potential future ideas!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "I know who we could get for a writer!"

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "Oh?"


    ## conditional
    if "finale_scene" in scenes_completed:
        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "I know [julia.say_name] really likes her novels, and is writing her own book."

    else:
        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "My cousin [julia.say_name] really likes her novels, and is writing her own book."


    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "I could advertise her book on stream when she's done!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "I'm sure she would appreciate that greatly!"


    $ vicky_disable_talk_intro = True

    call process_end_of_conversation("vicky_convo_3", vicky, priority = False, default = False)

    return

label vicky_convo_4:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg apartment_evening", char_tuple_array = [(n, ""), (vicky, "pose handup face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg apartment_daytime", char_tuple_array = [(n, ""), (vicky, "pose handup face neutral blush false")])

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "You know, I wasn't always into video work."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "I just so happened to fall into video from work I did on audio."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Audio?"

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "I know, it's hard to believe."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "I saw myself more as being behind a sound desk rather than a camera."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "Really?"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "You could have fooled me!"

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "That was a {i}long{/i} time ago now!"

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "I think that was well before I first picked up a webcam!"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "I figured camera-work and video editing were my true callings."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "It's not really that different from each other though, when you get down to basics."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Most audio work you do will usually be for videos anyway."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "Unless you're doing music of course, but even then..."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "What about music videos?"

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "Then you combine both talents into one."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "But separated, they're both very different skillsets."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Audio sometimes was too subtle."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What do you mean?"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "I couldn't quite hear what was wrong with it even if I knew something was up."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "And video doesn't have that problem?"

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Nope!"

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "If you don't know what you're doing, audio can get deceptive at times."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "You need a good ear to pick up on issues like audio balancing, mixing..."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Things that would otherwise fly under the radar if you're not paying attention."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "So you don't have to do that with video?"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "If you want audio to sound right in your videos, you do."

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "While I have some concerns with video I won't get into, at least it doesn't try to lie to you like audio does."

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "It's slightly more easier in that regard."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "If it's wrong, it's front and centre."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Everyone gets to see it."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "So it's easier to fix mistakes, then."

    call process_character(vicky, appearance = "pose handup face embarrassed blush false")
    vicky.c "Oh, I wouldn't say that..."

    call process_character(vicky, appearance = "pose handup face embarrassed blush false")
    vicky.c "It has it's moments."

    call process_character(vicky, appearance = "pose handup face angry blush false")
    vicky.c "Moments in which you might pull out a few hairs getting things just right."

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "..."


    $ vicky_disable_talk_intro = True

    call process_end_of_conversation("vicky_convo_4", vicky, priority = False, default = False)

    return

label vicky_convo_5:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg apartment_evening", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg apartment_daytime", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "What were you like when you were younger, [vicky.say_name]?"

    call process_character(vicky, appearance = "pose handup face embarrassed blush false")
    vicky.c "Oh boy..."

    call process_character(vicky, appearance = "pose handup face embarrassed blush false")
    vicky.c "What {i}wasn't{/i} I like back then?"

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Hm?"

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Well, for starters, I was known as \"Vicky Vixen\"."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Or at least, that was my name when I used to be a cam-girl."

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "I like that name!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "That was such a long time ago now!"

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "I was inexperienced back then, so I didn't know what I was doing most of the time."

    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "The first time I was on camera, I was extremely nervous."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "I only ever had a cheap webcam to use."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Luckily the quality of the video masked my nervousness a bit."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "But when I got my first request, I was practically over the moon!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "What kind of videos did you do?"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "I was a one-woman team, so I stuck to doing solo videos."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Solo videos?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Like, it was just you?"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "That's right."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "I was my own boss, basically."

    call process_character(vicky, appearance = "pose handhip face sad blush false")
    vicky.c "I really don't think I would have handled it well if someone else was there back then."

    call process_character(vicky, appearance = "pose handhip face sad blush false")
    vicky.c "And, unfortunately, I think those videos are lost to time too..."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "I wasn't exactly good at managing things back then, so I didn't think to make any backups."

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "..."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "In truth, I think it is for the best though."

    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "If I saw my old self, I'd die of embarrassment!"

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "..."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "In any case, I'm proud of the kind of career I'm in now."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Back then, I was just some naive teenage girl with stars in her eyes."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "The producers at my old market directing role would have been all over that."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Really?"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "They were already obsessed with me to begin with while I was there."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "So imagine if a teen version of me entered that scene."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "I guess in some way, I was always destined to make a career out of pornography."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "..."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "The equipment we have here is a huge step up from what I had when I shot those videos."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Instead of a crummy bedroom, I now have a lovely office!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "And instead of a low-quality webcam, I have a professional camera, able to catch the best shots!"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "I'd say you made it, [vicky.say_name]!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Yes, I guess I did!"

    $ vicky_disable_talk_intro = True

    call process_end_of_conversation("vicky_convo_5", vicky, priority = False, default = False)

    return
