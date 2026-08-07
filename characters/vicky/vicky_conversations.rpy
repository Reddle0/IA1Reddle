label vicky_convo_default:
    call process_conversation_beginning([ (n, ""), (vicky, "") ])
    vicky.c "Hi [n.say_name]!"

    call process_end_of_conversation("vicky_convo_default", vicky, priority = False, default = True)

    return

label vicky_scene_minigame_intro(dream = False):
    call vicky_scene_minigame_intro_sex(dream)
    return

label vicky_scene_minigame_intro_sex(dream = False):
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
        call process_scene_beginning(bg = "bg apartment_evening", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg apartment_daytime", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "I see you eyeing those papers on my desk."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "That's a lot..."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "It certainly is."

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "You must have a really important job if you have all of that on your desk!"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Oh, I wouldn't say that."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Busy would be a more accurate term."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "..."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "My work as a ReflexViz.HD affiliate involves {i}a lot{/i} of moving parts."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Like what?"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Creator reports, partnership updates, payment details, audience trends..."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "And in your case, keeping an eye on how Twinsticks is performing, of course!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "Oh!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "So some of those papers are about me and [sa.say_name]?"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Some of them, yes."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Your channel has been doing well, so I need to make sure it gets the proper attention."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "That sounds important..."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "Yes, although the difficult part is knowing when to step away from it."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "What do you do when you're not working, [vicky.say_name]?"

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "That's a bit of a tough question to answer."

    call process_character(vicky, appearance = "pose handhip face sad blush false")
    vicky.c "Unfortunately, I don't leave much room for personal time."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Because there's always more work to do?"

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "In a sense, yes."

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "When something starts gaining traction, I feel responsible for keeping it moving."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "If you step away at the wrong time, people can move on before you notice."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "That's why I have a hard time telling myself the work can wait."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "So even when you're not working, you're still thinking about work?"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Yes, more often than I'd like."

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "There are very few moments when I can truly relax."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "You can't just stop?"

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "I'm afraid it doesn't work that way, [n.say_name]."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "Once I set a target for myself, it's difficult to step away from it."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "Part of me keeps thinking about what still needs to be done."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "It's tough, but my work is still rewarding at the end of the day."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "How so?"

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "People depend on me."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "For instance, you!"

    call process_character(vicky, appearance = "pose fisthip face surprised blush false")
    vicky.c "Creators trust me to help them succeed."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "So when that work pays off, knowing I did the job properly is its own reward."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "My Mom is like that too!"

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "She always spends her time looking after us, but never has any time to herself."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Your mother would understand where I'm coming from, then."

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
        vicky.c "She sounds like a wonderful woman!"


    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "Raising children takes a lot of work, and it's certainly not something you should take lightly!"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "But if you never rest, won't you get tired?"

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "Eventually, yes."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "Maybe you could put dedicated break times in your schedule."

    call process_character(vicky, appearance = "pose fisthip face curious blush false")
    vicky.c "Break times?"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Yeah!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Like times where you're not allowed to work."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Hmm..."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Scheduled rest..."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "When you put it that way, that does sound less like I'm just slacking off."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "I don't know if I'll be good at sticking to it, but I'll give it a try!"

    $ vicky_disable_talk_intro = True

    call process_end_of_conversation("vicky_convo_1", vicky, priority = False, default = False)

    return

label vicky_convo_2:
    if store.week.time == "night":
        call process_scene_beginning(bg = "bg apartment_evening", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])
    else:
        call process_scene_beginning(bg = "bg apartment_daytime", char_tuple_array = [(n, ""), (vicky, "pose handhip face neutral blush false")])

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "I've been curious about the rest of your family, [n.say_name]."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "You spend a lot of time with them, don't you?"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Yeah!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Especially [sa.say_name]!"

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "That part I already knew."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "You two have a very natural rhythm together."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Most people don't notice their own appeal."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "That's what makes outside perspective useful."

## conditional
    if "finale_scene" in scenes_completed:
        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "Who lives at your household besides [sa.say_name]?"

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "[k.say_name] and your Mom?"

        call process_character(n, appearance = "pose handpocket face neutral blush false")
        n.c "That's right."

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "I'm still putting together how everyone in your family is connected, you see."

        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "There's also [julia.say_name]."

        call process_character(vicky, appearance = "pose fisthip face curious blush false")
        vicky.c "[julia.say_name]?"

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "Oh, the girl with the violet hair!"

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "I believe she said she was your cousin, correct?"

        call process_character(n, appearance = "pose twohandfist face happy blush false")
        n.c "Yeah!"

        call process_character(vicky, appearance = "pose handhip face happy blush false")
        vicky.c "I liked her fashion style."

        call process_character(vicky, appearance = "pose handhip face happy blush false")
        vicky.c "That sort of distinct look can be useful on camera, if someone knows how to present it."

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "And of course, I met the rest of your family at the pool party we had."

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "Do you all live near each other?"

        call process_character(n, appearance = "pose handpocket face neutral blush false")
        n.c "Grandma lives near the beach, and Aunt Janet's place is close enough that we can head there from her house too."

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
        n.c "There's my Mom, and my big sister, [k.say_name]."

        call process_character(vicky, appearance = "pose handhip face neutral blush false")
        vicky.c "[k.say_name]..."

        call process_character(vicky, appearance = "pose handhip face happy blush false")
        vicky.c "Now there's a strong sounding name if I've ever heard one!"

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
        vicky.c "And for helping you with them!"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Things like that are beyond me, I'm afraid."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Why?"

    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "Let's just say my last attempt at aerobic exercise... (w=1.0)didn't exactly go well."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What happened?"

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "I ended up twisting my ankle."

    call process_character(vicky, appearance = "pose handup face sad blush false")
    vicky.c "Somehow..."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Oh..."

    call process_character(vicky, appearance = "pose fisthip face embarrassed blush false")
    vicky.c "It was not my finest professional performance..."

    call process_character(vicky, appearance = "pose fisthip face embarrassed blush false")
    vicky.c "..."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "In any case..."
    
    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Even if exercise turned out not to be my area of expertise, I appreciate someone who helps others improve."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "It's valuable to have someone who can push you toward becoming a better version of yourself."

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "[k.say_name] does that for me a lot."

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "I'd say you're lucky to have her, then!"

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
    vicky.c "I'm afraid it's not going to happen with that little camera."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "Aww..."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Though I do admire your enthusiasm!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Did you have anything in particular in mind?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Uh, not exactly..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I thought it would be cool to do."
    
    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "You have lots of equipment here."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Movies require a lot more thought than simply picking up a camera and speaking lines."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Anyone can record footage, but turning that footage into a real production is another matter."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "What's the difference?"

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "You need a script, performers, lighting, sound, locations, editing..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "That sounds like a lot..."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "It is."

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "While we don't have that kind of setup right now..."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "If we keep at it, we could expand into bigger projects."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "For now, let's stick to what we're good at."

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "But I won't object to any potential future ideas!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "I know who we could get for a writer!"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Oh?"

    ## conditional
    if "finale_scene" in scenes_completed:
        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "[julia.say_name] reads a lot of novels, and she's writing her own book!"

    else:
        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "My cousin [julia.say_name] reads a lot of novels, and she's writing her own book!"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "That sounds promising!"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "A writer understands structure, and structure matters before a camera ever turns on."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "I could advertise her book on stream when she's done!"

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "That is exactly the sort of support a new creator needs!"

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
    vicky.c "You know, I wasn't always focused on video work."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "I actually moved into video through audio work."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Audio?"

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "I know, it's hard to believe."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "I pictured myself behind a sound desk more than behind a camera."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Not quite as flashy as being behind a camera, but still crucial."

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Really?"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "You could have fooled me!"

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "That was a long time ago now!"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Eventually, I found myself more drawn to camera work and editing."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "But audio and video are still connected more often than people realize."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "They overlap often, but they aren't the same skill."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Someone can be good with a camera and still have no idea how to fix bad sound."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "So audio and video usually go together?"

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "Quite often."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Like... (w=1.0)music videos?"

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "That's a good example!"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "The song matters, obviously."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "But the visuals have to support it, or the whole thing feels off."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "So is audio harder than video?"

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "In some ways."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Audio can be... (w=1.0)sneakier."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "What do you mean?"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Well, a voice can be slightly too quiet, or too muffled..."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Or you get the opposite problem, and the voice comes through too loud."

    call process_character(vicky, appearance = "pose handup face curious blush false")
    vicky.c "Someone watching may not know exactly what's wrong."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "They'll only know it sounds off, and that can be enough to make them stop watching."

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "That sounds bad."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Audiences can forgive imperfect visuals for a while."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Unpleasant audio is what really drives them away, though."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "[sa.say_name] always complains when other streams have bad microphones."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "She's right to do so."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "It takes a good ear to catch things like volume balance and mixing."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Small problems can slip by until the whole video feels worse."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "And video doesn't have that problem?"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Video has plenty of problems too."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "But bad lighting or awkward framing tends to announce itself right away."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I never thought about sound that much."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Most people tend not to, since they focus more on the visuals."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Sound is something they only notice when it goes wrong."

    ## conditional
    if "finale_scene" in scenes_completed and finale_julia_sam:
        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "For what it's worth, you and [sa.say_name] already do a good job with your streams!"

        call process_character(vicky, appearance = "pose handup face happy blush false")
        vicky.c "I do watch the channel, after all."

        call process_character(n, appearance = "pose handfist face happy blush false")
        n.c "You do?"

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "I believe I mentioned that during the pool party."
    
    else:
        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "For what it's worth, you and [sa.say_name] already seem to have a decent handle on things."

        call process_character(n, appearance = "pose handpocket face happy blush false")
        n.c "Really?"

        call process_character(vicky, appearance = "pose fisthip face happy blush false")
        vicky.c "Of course!"

        call process_character(vicky, appearance = "pose handup face neutral blush false")
        vicky.c "Your channel has a natural charm to it."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Even then, there are always small ways to improve."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Make sure the microphone isn't too far away from either of you."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Does that make a big difference?"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Yes, a much bigger one than people expect."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "You also don't want fans, keyboards, or background noise fighting with your voices."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "And if one of you sounds much louder than the other, be sure to adjust it before you start streaming."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "That sounds like something we could do."

    call process_character(vicky, appearance = "pose handhip face happy blush false")
    vicky.c "Small improvements can make a channel feel much more professional."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "I guess sound is harder than I thought..."

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "It can be."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Does that mean video is easier?"

    call process_character(vicky, appearance = "pose handup face embarrassed blush false")
    vicky.c "Oh, I wouldn't say that..."

    call process_character(vicky, appearance = "pose handup face embarrassed blush false")
    vicky.c "It has its moments."

    call process_character(vicky, appearance = "pose handup face angry blush false")
    vicky.c "Moments where you might pull out a few hairs getting things just right..."

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
    vicky.c "Well, for starters, I used to go by \"Vicky Vixen\"."

    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "It was the name I used when I was... (w=1.0)a cam-girl, so to speak."

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "I like that name!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "That was such a long time ago now!"
    
    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "I was inexperienced back then, so I didn't know what I was doing most of the time."

    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "The first time I was on camera, I was extremely nervous."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "That sounds scary..."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "All I had was a cheap webcam."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Luckily, the poor video quality masked my nervousness a bit."

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
    vicky.c "Honestly, I think it's for the best."

    call process_character(vicky, appearance = "pose handhip face embarrassed blush false")
    vicky.c "If I saw my old self, I'd die of embarrassment!"

    call process_character(vicky, appearance = "pose handhip face curious blush false")
    vicky.c "..."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "In any case, I'm proud of the kind of career I'm in now."

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "Back then, I was just a young woman trying to make a name for herself."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "After those early cam-girl days, I moved into the business side of things."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Like your old marketing job?"

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "Exactly."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "Imagine if the producers there had found out about my old \"Vicky Vixen\" days..."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "..."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "That sort of history would have been very easy for them to package."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "First that studio job, then ReflexViz.HD..."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "I suppose I was always drawn to the business side of adult entertainment."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "So you went from making videos by yourself to running the whole thing?"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "In a sense, yes."

    call process_character(vicky, appearance = "pose fisthip face neutral blush false")
    vicky.c "The equipment we have here is a huge step up from what I had when I shot those videos."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Instead of a crummy bedroom, I now have a lovely office!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "And instead of a low-quality webcam, I have a professional camera, ready to catch the best shots at a moment's notice!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "And now you have Vicky's Empornium too!"

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "Exactly!"

    call process_character(vicky, appearance = "pose handup face neutral blush false")
    vicky.c "While the old webcam days taught me I could make it on my own..."

    call process_character(vicky, appearance = "pose handhip face neutral blush false")
    vicky.c "It was my studio job that taught me how the adult business really worked from behind the scenes."

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "And now I have a website and a growing library of content that I can proudly call my own!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "I'd say you made it, [vicky.say_name]!"

    call process_character(vicky, appearance = "pose fisthip face happy blush false")
    vicky.c "Yes, I guess I did!"

    call process_character(vicky, appearance = "pose handup face happy blush false")
    vicky.c "Though I certainly don't plan on stopping any time soon!"

    $ vicky_disable_talk_intro = True

    call process_end_of_conversation("vicky_convo_5", vicky, priority = False, default = False)

    return
