label julia_scene_swimsuit(after_buy_label = False, dream = False):
    call julia_scene_swimsuit_sex(dream = dream)

    return

label julia_scene_swimsuit_sex(dream = False):
    call process_scene_beginning(bg = "bg nate_room_daytime", dream = dream)
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    n.c "(Alright, the swimsuit is purchased)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "(I hope I'm not making a mistake here)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "(I just really want [julia.say_name] to try out the pool!)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "(I don't think she has a bathing suit yet)"

    call process_character(n, appearance = "pose twohandfist face neutral")
    n.c "(Well now she will!)"

    call process_scene_beginning(bg = "bg living_room_daytime", char_tuple_array = [ (julia, "outfit clothes pose handface face neutral") ], dream = dream, force_bg_change = True)

    call process_character(julia, appearance = "pose handface face curious blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face curious blush false")
    julia.c "(This is tougher than I thought)"

    call process_character(julia, appearance = "pose armcross face curious blush false")
    julia.c "(Usually writing isn't a problem for me, but I'm really struggling here)"

    call process_character(julia, appearance = "pose armcross face curious blush false")
    julia.c "(The main character just isn't interesting enough)"

    call process_character(julia, appearance = "pose armcross face curious blush false")
    julia.c "(Despite everything I'm doing to change that up)"

    call process_character(julia, appearance = "pose armcross face curious blush false")
    julia.c "(And the worldbuilding needs to be fleshed out more)"

    call process_character(julia, appearance = "pose handface face curious blush false")
    julia.c "{cps=40}(Because right now you have-{/cps}{w=0.75}{nw})"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face happy")
    n.c "Hey [julia.say_name]!"

    call process_character(julia, appearance = "pose handup face embarrassed position left")
    julia.c "Oh, hey."

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "(Is she okay?)"

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "(Looked like she was staring off into space for a second there)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "Did I catch you at a bad time?"

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "No, was just lost in my thoughts."

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "I'm busy brainstorming for a story, but I'm thinking what I have needs more work."

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "Oh yeah?"

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "What's the story about?"

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "A sorcerer tinkering with a new spell."

    call process_character(n, appearance = "pose handfist face neutral")
    n.c "Cool."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "But things take a turn for the worse when it backfires on him."

    call process_character(n, appearance = "pose handpocket face neutral")
    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "And he ends up having to work with the main villain at some point."

    pause 1.0
    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "Like I said, still trying to iron out the details."

    call process_character(julia, appearance = "pose handface face curious")
    julia.c "...Anyway, did you need something?"

    call process_character(julia, appearance = "pose handup face curious")
    julia.c "And what's with that bag you're carrying?"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "Actually [julia.say_name], I.."

    call process_character(julia, appearance = "pose handface face concerned")
    julia.c "What?"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "Um..."

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "How do you feel about surprises?"

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "Depends on what the surprise is."

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "I like to know things beforehand instead of being surprised, but..."

    call process_character(n, appearance = "pose handpocket face concerned")
    n.c "So you don't mind them?"

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "I guess not."

    call process_character(julia, appearance = "pose armcross face curious")
    julia.c "But you're being awfully vague here, [n.say_name]..."

    call process_character(julia, appearance = "pose armcross face curious")
    julia.c "Is there something I should know?"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "The thing is..."

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "I-I got something for you."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "(That would explain the bag)"

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "What did you get me?"

    call process_character(n, appearance = "pose handpocket face curious")
    n.c "Here."

    call process_character(n, appearance = "pose handpocket face curious")
    n.c "It's a new swimsuit."

    call process_character(julia, appearance = "pose armcross face curious")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face curious")
    julia.c "You got this for me?"

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "Y-yeah."

    pause 1.0
    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "...{p}..."

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "(...)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "([julia.say_name]'s gone quiet)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "(I hope I didn't upset her)"

    call process_character(n, appearance = "pose handpocket face curious")
    n.c "So what do you think?"

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face angry")
    julia.c "What do I think?"

    call process_character(julia, appearance = "pose armcross face angry")
    julia.c "What would {i}you{/i} think when your cousin gets you a swimsuit out of the blue?"

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "Um, well..."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "Because I'd be questioning what their motives are."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "Judging by your recent actions, I'm inclined to think you're up to something."

    pause 1.0
    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "Perverted intentions, perhaps."

    call process_character(julia, appearance = "pose armcross face curious")
    julia.c "You {i}do{/i} know what I'm talking about, right?"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "I'm not up to anything [julia.say_name]!"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "I saw you lounging by the pool the other day, but you were in your normal clothes!"

    call process_character(julia, appearance = "pose armcross face curious")
    julia.c "Uh-huh..."

    call process_character(n, appearance = "pose handpocket face embarrassed")
    n.c "I just didn't think you had a swimsuit yet!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "And I also thought it'd be cool if you swam in the pool with us!"

    call process_character(julia, appearance = "pose handface face curious")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "I guess no one's told you I don't actually swim [n.say_name]."

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "Oh..."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "Yeah."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "Swimming just isn't my thing."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "My Mom keeps trying to get me to swim, but I just don't want to."

    pause 1.0
    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "But that's not the only reason."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "Any swimsuits she picks out for me just end up being too small."

    call process_character(julia, appearance = "pose handup face embarrassed")
    julia.c "(Or too big)"

    call process_character(julia, appearance = "pose handup face embarrassed")
    julia.c "..."

    pause 1.0
    call process_character(julia, appearance = "pose armcross face embarrassed")
    julia.c "But don't tell anybody I told you that!"

    call process_character(julia, appearance = "pose armcross face angry")
    julia.c "I mean it."

    call process_character(julia, appearance = "pose armcross face angry")
    julia.c "I'm very sensitive about that!"

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "...Noted..."

    call process_character(n, appearance = "pose handpocket face curious")
    n.c "But you don't have to wear it if you don't want to."

    call process_character(n, appearance = "pose handpocket face curious")
    n.c "And maybe you don't have to swim with it on."

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "You could just use it as a bathing suit instead."

    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "[k.say_name] wears her swimsuit for sunbathing too."

    call process_character(n, appearance = "pose handfist face neutral")
    n.c "It'll be good for when you go outside to read!"

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "If I go outside to read."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "You already know I burn easily [n.say_name]."

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "Right..."

    pause 1.0

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "{w=0.5}Do you want me to return it, then?"

    call process_character(julia, appearance = "pose armcross face concerned")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face concerned")
    julia.c "(My first response would usually be yes, but...)"

    call process_character(julia, appearance = "pose armcross face concerned")
    julia.c "([n.say_name] did go out of his way to get this for me)"

    call process_character(julia, appearance = "pose armcross face concerned")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "(That's more than I can say for other boys who didn't bother to get me anything at all)"

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "(Maybe I'm being a bit selfish here?)"

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "(And like he said, it'd be good for reading outside in the heat)"


## conditional
    if "julia_scene_topless" in scenes_completed:
        call process_character(julia, appearance = "pose handface face angry")
        julia.c "(Last time my clothes got soaked by his sister's cannon bomb...)"

        call process_character(julia, appearance = "pose handface face embarrassed")
        julia.c "(And that's when [n.say_name] saw me in [sa.say_name]'s room... {w=0.5}topless)"

        call process_character(julia, appearance = "pose handface face embarrassed")
        julia.c "(I guess I wouldn't have ended up in that situation if I was wearing a swimsuit)"

        call process_character(julia, appearance = "pose handface face angry")
        julia.c "(Especially if they pull a stunt like that again)"

    else:
        call process_character(julia, appearance = "pose handface face neutral")
        julia.c "(Might be better than being cooped up inside all the time)"

        call process_character(julia, appearance = "pose handface face neutral")
        julia.c "(And it'd save me from getting my clothes wet if I'm sat next to the pool)"

        call process_character(julia, appearance = "pose handface face embarrassed")
        julia.c "(Ugh, that would be a nightmare!)"

        call process_character(julia, appearance = "pose handface face angry")
        julia.c "(Gotta watch out for that sister of his)"


    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "..."

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "Normally I'm not one for swimsuits."

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "If you told me to wear one, I would say no."

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "But I could make this an exception."

    call add_points(julia, 2, tag = "julia_scene_swimsuit_try_it_on")
    call process_character(julia, appearance = "pose handup face happy")
    julia.c "I'll try it on."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "(And at least that way if you {i}are{/i} trying to perv on me again with buying me this, I can prove it)"

    call process_character(julia, appearance = "pose armcross face happy")
    julia.c "Looks like you win this time [n.say_name]."

    call process_character(julia, appearance = "pose armcross face happy")
    julia.c "Let's hope you got the right size for me."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "And the right color."

    call process_character(julia, appearance = "pose armcross face angry")
    julia.c "Because I swear [n.say_name], if you got me pink, I'll..."

    call process_character(n, appearance = "pose behindhead face embarrassed")
    n.c "{i}Gulp!{/i}"

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "Meet me outside at the pool."

    call process_character(n, appearance = "pose twohandfist face happy")
    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "I'll be there in a bit."

    call fade_to_black(1)

    call process_scene_beginning(bg = "bg backyard_daytime", char_tuple_array = [ (n, "outfit swimsuit pose behindhead face curious")])

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "([julia.say_name] told me she'd meet me out here)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "(But she's taking a while)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "...{p}..."

    call process_character(n, appearance = "pose twohandfist face happy")
    n.c "(Oh, here she comes now!)"

    call process_character(julia, appearance = "outfit swimsuit pose handface face embarrassed")
    julia.c "Okay, it's..."

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "You don't like it?"

    call process_character(julia, appearance = "pose handup face happy blush false")
    julia.c "Actually, quite the opposite."

    call process_character(julia, appearance = "pose handup face happy")
    julia.c "Where did you get this?"

    call process_character(n, appearance = "pose handfist face neutral")
    n.c "I bought it online!"

    call process_character(n, appearance = "pose handfist face neutral")
    n.c "The store website said it was a \"exclusive run.\""

    call process_character(n, appearance = "pose twohandfist face neutral")
    n.c "\"Exclusive\" sounds like the kind of thing you'd like, right?"

    call process_character(julia, appearance = "pose handface face curious")
    julia.c "Well, not quite..."

    call process_character(julia, appearance = "pose armcross face angry")
    julia.c "Okay, maybe a little, but that's beside the point!"

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "I'm asking because it's different."

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "Different? How?"

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "For starters, it {i}feels{/i} different."

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "It's surprisingly light."

    call process_character(n, appearance = "pose handsdown face curious")
    call process_character(julia, appearance = "pose handface face curious")
    julia.c "And fluffy, I think?"

    call process_character(julia, appearance = "pose handface face curious")
    julia.c "I'm honestly surprised this thing fits me as well as it does."

    call process_character(julia, appearance = "pose handface face embarrassed")
    julia.c "I mean, just look at all of these straps!"

    call process_character(julia, appearance = "pose handface face embarrassed")
    julia.c "At first I felt like I was putting on a harness, not a swimsuit!"

    call process_character(n, appearance = "pose behindhead face concerned")
    n.c "Sorry about that..."

    call process_character(julia, appearance = "pose handup face curious")
    julia.c "Hold on, what'd the tag say..."

    call process_character(julia, appearance = "pose handup face curious")
    julia.c "{w=0.5}Nylon and elastine..."

    call process_character(julia, appearance = "pose handup face embarrassed")
    julia.c "Stretch velvet!?"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "Are swimsuits not supposed to have stretch velvet in it?"

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "Velvet is a weave, not a material."

    call process_character(n, appearance = "pose handsdown face curious")
    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "A very complicated weave."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "Whoever made this certainly knew their stuff."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face happy")
    julia.c "Honestly, I'm impressed [n.say_name]..."

    call process_character(julia, appearance = "pose handface face happy")
    julia.c "You actually did get a decent size."

    call process_character(julia, appearance = "pose handface face happy")
    julia.c "You really lucked out there."

    pause 1.0
    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "...{p}..."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "So, how do I look?"

    call process_character(n, appearance = "pose twohandfist face happy")
    n.c "It suits you really well!"

    call process_character(julia, appearance = "pose handface face happy")
    julia.c "Yeah, I like the color you picked out."

    call process_character(julia, appearance = "pose handface face happy")
    julia.c "It's a good color."

    call process_character(n, appearance = "pose handfist face neutral")
    n.c "I bet anything in that color suits you."

    call process_character(julia, appearance = "pose handup face happy")
    julia.c "Mm, maybe."

    call process_character(julia, appearance = "pose handup face happy")
    julia.c "Black is a good color for anything."

    call process_character(julia, appearance = "pose handup face happy")
    julia.c "But I'm a fan of dark purple too."

    call process_character(n, appearance = "pose twohandfist face neutral")
    n.c "You should come out here more often [julia.say_name]!"

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "Hm, we'll see."

    call process_character(julia, appearance = "pose handup face neutral")
    julia.c "I still prefer to be indoors, but..."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "I guess being out here's not so bad."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "There's a nice breeze blowing through, and you have plenty of shade from the trees and umbrellas."

    call process_character(julia, appearance = "pose armcross face neutral")
    julia.c "It's certainly a lot better than what we have back home."

    call process_character(julia, appearance = "pose armcross face angry")
    julia.c "Reading inside can prove to be challenging when your sister's stomping around."

    call process_character(n, appearance = "pose behindhead face neutral")
    n.c "You mean [k.say_name]?"

    call process_character(julia, appearance = "pose armcross face curious")
    julia.c "Yes, her."

    call process_character(julia, appearance = "pose armcross face embarrassed")
    julia.c "You can practically hear her footsteps all across the house!"

    call process_character(julia, appearance = "pose armcross face curious")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "Hey, [n.say_name]..."

    call process_character(julia, appearance = "pose handface face neutral")
    julia.c "I don't say this often, but..."

    call process_character(julia, appearance = "pose handface face happy")
    julia.c "Thanks."

    call process_character(julia, appearance = "pose handface face happy")
    julia.c "I really do like this swimsuit."

    call process_character(julia, appearance = "pose handface face happy")
    julia.c "It's nice."

    python:
        julia.revistable_scenes.add("julia_scene_swimsuit_revisit")

        if not dream:
            stats.add_stat("times_seen_bikini", 1)

    call process_end_of_scene("julia_scene_swimsuit", char = julia, dream = dream, reset_prompted_scene = False )

    return

label julia_scene_swimsuit_revisit:
    if store.week.time == "night" and "julia_scene_swimsuit_revisit_first_time_vaginal" in scenes_completed:
        n.c "(It's late)"
        n.c "(I'll ask [julia.say_name] tomorrow if she wants to fuck by the pool again)"

    elif store.week.time == "night":
        n.c "(It's late)"
        n.c "(I'll ask [julia.say_name] tomorrow if she wants to relax by the pool)"

        $ julia.select()

        return

    if "julia_scene_swimsuit_revisit" not in scenes_completed:
        $ no_bust_art = False
        call process_character(n, appearance = "pose handfist face neutral blush false")
        call process_character(julia, appearance = "pose handface face neutral blush false")
        julia.c "I'll be out there in a bit."

        call process_character(julia, appearance = "pose handface face happy blush false")
        julia.c "Just let me get ready first."


    if "julia_scene_vaginal" and "julia_scene_swimsuit_revisit_first_time_normal" in scenes_completed:
        if "julia_scene_swimsuit_revisit_first_time_vaginal" in scenes_completed:
            call julia_scene_swimsuit_revisit_second_time_vaginal
        else:
            call julia_scene_swimsuit_revisit_first_time_vaginal
    elif "julia_scene_4" in scenes_completed:
        if "julia_scene_swimsuit_revisit_first_time_blowjob" in scenes_completed:
            call julia_scene_swimsuit_revisit_second_time_blowjob
        else:
            call julia_scene_swimsuit_revisit_first_time_blowjob
    else:
        if "julia_scene_swimsuit_revisit" in scenes_completed:
            call julia_scene_swimsuit_revisit_second_time_normal
        else:
            call julia_scene_swimsuit_revisit_first_time_normal
    return

label julia_scene_swimsuit_revisit_first_time_vaginal:
    call process_scene_beginning(bg = backyard, char_tuple_array = [(n, "outfit swimsuit pose twohandfist face happy blush false")])

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "([julia.say_name] got out here before I did again)"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "(I think she's found a new-found passion for reading by the pool!)"

    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
    n.c "What book are you reading this time, [julia.say_name]?"


    call static_still_ctc("bg julia_swimsuit_read")

    call process_character(julia, appearance = "outfit swimsuit pose handface face happy blush false")
    julia.c "I'm almost finished with the book I was reading before."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "The one about the magical swashbuckler?"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "That's the one."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "It's crazy how you can read so quick like that."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "It's not that hard to grasp."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "Once you've set your mind to something, you can get it done quickly."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "It just takes a bit of concentration."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "Has reading by the pool helped?"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "Surprisingly, yes it has."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "It's calm and quiet out here, which is just the way I like it."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "I think I'm starting to see the appeal."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "Even when you're out in the sun?"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "Yeah, I can't stay out here too long."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "I know I'll end up get sunburnt, since my skin's sensitive."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "And what about the pool?"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "Oh, yeah, that's not changing."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "I don't want to swim, and I'm staying firm on that."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "But I guess it wouldn't hurt if I dipped my feet in water every now and then."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "Maybe the hot tub will be good for that."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "That's good to hear!"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "It's also helped me come up with some new ideas for stories I want to write."

    call process_character(julia, appearance = "outfit swimsuit pose handface face happy blush false")
    julia.c "There's one idea I've taken to..."

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face aroused blush false")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face aroused blush false")
    n.c "([julia.say_name] looks good in that bathing suit)"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face aroused blush false")
    n.c "(It doesn't cover much though)"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face aroused blush false")
    n.c "(I think I'm able to see her...)"

    call fade_to_black(1)

    call bust_art_background(backyard)

    call process_character(n, appearance = "outfit swimsuit_hard pose twohandfist face aroused blush true", show_bust = False)
    $ refresh_character(n, force_transition = Dissolve(1.5))

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face aroused blush true")
    n.c "...{p}..."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "And that's the gist of it."

    call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
    julia.c "I know it sounds a bit much to understand right now, but..."

    call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
    julia.c "{cps=40}I'm still working on the finer details, but I'd like to get your opinion on-{/cps}{w=0.75}{nw}"

    call process_character(julia, appearance = "outfit swimsuit pose handface face curious blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit swimsuit pose handface face curious blush false")
    julia.c "[n.say_name]?"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face curious blush false")
    julia.c "(...)"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face curious blush false")
    julia.c "(Is he... staring at my swimsuit?)"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "(...)"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "(I can see his dick bulge)"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "(This must be why he bought this for me)"

    call process_character(julia, appearance = "outfit swimsuit pose handface face curious blush false")
    julia.c "(Has he never seen a girl in a swimsuit before?)"

    call process_character(julia, appearance = "outfit swimsuit pose handface face curious blush false")
    julia.c "(Or maybe he has, and just likes looking at them)"

    pause 1.0
    call process_character(julia, appearance = "outfit swimsuit pose armcross face curious blush false")
    julia.c "(...)"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face curious blush false")
    julia.c "(He's really zoned out)"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face angry blush false")
    julia.c "(God, what a pervert!)"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face angry blush false")
    julia.c "[n.say_name]!"

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face embarrassed blush true")
    n.c "Y-yeah?"

    call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
    julia.c "I wanted to get your opinion on my story idea."

    call process_character(julia, appearance = "outfit swimsuit pose handup face angry blush false")
    julia.c "It was certainly {i}not{/i} an invitation to stare!"

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face curious blush true")
    n.c "O-Oh..."

    call process_character(julia, appearance = "outfit swimsuit pose handup face angry blush true")
    julia.c "And don't think I noticed your little {i}\"situation\"{/i} down there!"

    call process_character(n, appearance = "outfit swimsuit_hard pose twohandfist face curious blush true")
    n.c "I..."

    call process_character(n, appearance = "outfit swimsuit_hard pose twohandfist face embarrassed blush true")
    n.c "(Uh oh...)"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face angry blush true")
    julia.c "You're a real pervert, you know that?"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face angry blush true")
    julia.c "So what, you got a thing for girls in swimsuits or something?"

    call process_character(n, appearance = "outfit swimsuit_hard pose twohandfist face curious blush true")
    n.c "..."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face angry blush true")
    julia.c "Is that a yes or a no?"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face angry blush false")
    julia.c "On second thought, don't answer that."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face angry blush false")
    julia.c "I can already see your dick bulging out from your swim shorts."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face angry blush false")
    julia.c "I think I already know what the answer is."

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face embarrassed blush true")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face embarrassed blush true")
    n.c "Sorry, [julia.say_name]..."

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face embarrassed blush true")
    n.c "You just look really good in that swimsuit."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face curious blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face curious blush false")
    julia.c "I do?"

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face embarrassed blush true")
    n.c "Y-Yeah."

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face embarrassed blush true")
    n.c "I like seeing you wear it."

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face embarrassed blush true")
    n.c "It's something different compared to what you usually wear."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face curious blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit swimsuit pose handface face happy blush false")
    julia.c "Let's take advantage of that, then."

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face curious blush false")
    n.c "Huh?"

    call fade_to_black(1)
    julia.c "Tell me [n.say_name], is anyone watching?"
    n.c "N-Not that I can see."
    julia.c "Good."
    julia.c "Then you won't mind if I just do this..."
    n.c "Hold on [julia.say_name], what about-"

    python hide:
        play_music("audio/music/Summer Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg julia_swimsuit_vaginal_reveal")
    julia.c "And there we go."
    n.c "(!!!)"
    n.c "(I-I can see her...)"
    julia.c "So, do I look better with the swimsuit on, or without?"
    julia.c "This is what you wanted, right?"
    julia.c "To fuck me while I wear this, right?"
    julia.c "Right here on this deck chair?"
    n.c "..."
    n.c "Y-Yeah..."
    n.c "I do, [julia.say_name]."
    julia.c "Say it like you mean it."
    n.c "I wanna fuck you right here and now [julia.say_name]!"
    julia.c "..."
    julia.c "That's more like it."
    julia.c "Well, I also want that to happen too."
    julia.c "Get those shorts off."
    julia.c "You won't be needing them."
    julia.c "I'll be keeping my bathing suit on for this, although I doubt you'd object to it."
    julia.c "You said I look good in it, so let's put that to the test."
    julia.c "Are you ready, [n.say_name]?"
    n.c "I-I'm ready [julia.say_name]!"
    julia.c "In that case..."


    call static_still_ctc("bg julia_swimsuit_vaginal_spread")
    julia.c "What are we waiting for?"
    julia.c "Get to it, [n.say_name]."
    n.c "Won't someone see us?"
    julia.c "Nah, they've gone out."
    julia.c "I saw them leave earlier."
    julia.c "There's no one around but us."
    julia.c "You picked a good time to pull this one."
    julia.c "Whenever you're ready, [n.say_name]."
    julia.c "I'm ready for you."

    call static_still_ctc("bg julia_swimsuit_fuck_nude" if julia_scene_swimsuit_revisit_nude else "bg julia_swimsuit_fuck")
    julia.c "Y-yeah, like that..."
    n.c "Ah! Ah!"
    n.c "(My dick slid in easy!)"
    julia.c "Oh..."
    julia.c "You should consider yourself lucky, [n.say_name]..."
    julia.c "I've never fucked in places like this before."
    julia.c "It's usually far too risky to fuck outside."
    n.c "Maybe the risk is part of the fun!"
    julia.c "Heh, maybe."
    julia.c "..."
    julia.c "You're harder than usual."
    julia.c "(I guess he really does have a thing for swimsuits)"
    julia.c "Ah, ah!"
    julia.c "(He's also a bit faster than usual too)"
    julia.c "(Maybe I should wear this suit more often if I'm looking for a good fuck from [n.say_name])"

    call static_still_ctc("bg julia_swimsuit_fuck_blur" if julia_scene_swimsuit_revisit_nude else "bg julia_swimsuit_fuck_blur")
    n.c "Ah, Ahn!"
    n.c "(Her pussy is tightening around m-my penis)"
    n.c "(It feels so good!)"
    n.c "(Fucking outside makes me more excited than usual too)"
    n.c "(Maybe the risk really is part of the fun!)"
    n.c "(Even if there's no one around to see this right now)"
    julia.c "Ah, Mmn..."
    julia.c "Keep going, [n.say_name]!"

    pause 1.0
    julia.c "I think..."
    julia.c "I-I'm..."
    n.c "You're.. what?"
    julia.c "Keep drilling your cock in me."
    n.c "Mm! Mmn!"
    julia.c "F-faster, [n.say_name]..."
    julia.c "..."
    n.c "I-I think..."
    julia.c "Seems like you're ready to cum [n.say_name]."
    julia.c "In that case, don't hold back!"

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Cum!")
    $ quick_menu = True
    julia.c "Y-You're moving faster!"
    n.c "Ah, oh!"
    n.c "Mhm..."
    n.c "I'm coming!"

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc("bg julia_swimsuit_cum_blur")
    n.c "[julia.say_name]!"
    julia.c "Aa... Ahhh-hn.!"


    call static_still_ctc("bg julia_swimsuit_aftercum")
    n.c "{i}Pant,{/i} {i}pant.{/i}.."
    n.c "..."
    julia.c "...{p}..."
    julia.c "Are you finished [n.say_name]?"
    n.c "I-I think so."
    n.c "..."
    n.c "(That was amazing...)"
    julia.c "Look at the mess you made."
    julia.c "It went all over my top."
    julia.c "Let's hope it doesn't end up on the deck chair."
    julia.c "Those balls of yours must have been backed up."
    julia.c "..."
    julia.c "(It kinda feels nice though)"

    pause 1.0
    julia.c "Well."
    julia.c "That was certainly an interesting experience."
    julia.c "Judging by the amount of cum, it was exactly what you were hoping for."
    n.c "..."
    n.c "Y-yeah, it was."
    n.c "We should do this again [julia.say_name]!"
    julia.c "Yes, we should."
    julia.c "But next time, make sure you cum inside me."
    julia.c "No pulling out at the last minute!"
    n.c "..."

    python:
#        stats.add_stat("times_seen_breasts", 1)
#        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_had_incestual_situation", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    $ scenes_completed.add("julia_scene_swimsuit_revisit_first_time_vaginal")

    call julia_scene_swimsuit_revisit_end
    return

label julia_scene_swimsuit_revisit_second_time_vaginal:
    $ julia_scene_swimsuit_revisit_nude = False

    $ no_bust_art = False
    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "You're being very ballsy recently [n.say_name]..."

    call process_character(julia, appearance = "pose armcross face happy blush false")
    julia.c "Keep it up."

    call static_still_ctc("bg julia_swimsuit_fuck_nude" if julia_scene_swimsuit_revisit_nude else "bg julia_swimsuit_fuck")

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    julia.c "([n.say_name]'s starting to get used to outside fucking)"
    julia.c "(At this rate, there'll be no need to fuck indoors)"
    julia.c "(I can just picture him saying he wants to keep fucking out here instead, because it's fun)"
    julia.c "(...)"
    julia.c "(Well, he's right)"
    julia.c "(Despite any risks we may face while out here, I'd be lying if I said I wasn't having fun too)"
    julia.c "(I have to be careful, though)"
    julia.c "(Doing it outside might be too much for me to handle)"
    julia.c "(If I stay out here for too long, I'd burn up for sure)"
    julia.c "(But when I look up and see [n.say_name]...)"
    julia.c "(It's like I never want to stop)"
    n.c "(So good...)"
    n.c "(Having sex with [julia.say_name] feels so good...)"
    julia.c "I want to see if you can top your last performance."
    n.c "Performance?"
    julia.c "Your sexual performance, [n.say_name]."
    julia.c "Fucking out here is a different experience compared to what we're both used to."
    julia.c "But that doesn't mean the sex is different.\nThe goal still remains the same."
    n.c "Pleasure for both of u-us?"
    julia.c "That's right."
    julia.c "You delivered last time, and I hope you keep it up."

    n.c "..."
    n.c "Hey, [julia.say_name]..."
    julia.c "Yeah?"
    n.c "We could do this without our bathing suits."
    julia.c "That's an interesting idea, [n.say_name]."
    julia.c "We absolutely could."
    julia.c "But it's your choice."

    menu:
        "We should get naked!":
            $ julia_scene_swimsuit_revisit_nude = True
            julia.c "I'll put my top next to your shorts."
            julia.c "Hopefully we don't burn up in this heat."


            call fade_to_black(1.0)
            call static_still_ctc("bg julia_swimsuit_fuck_blur_nude" if julia_scene_swimsuit_revisit_nude else "bg julia_swimsuit_fuck_blur")

        "Actually, we're fine as is.":
            julia.c "Sure, if you say so."
            julia.c "What we're doing is already risky enough."
            julia.c "Might be {i}too{/i} risky if we got naked as well."

    julia.c "(Shit...)"
    julia.c "(Did he just get harder?)"
    julia.c "F-Faster, [n.say_name]."
    julia.c "Fuck me harder."
    n.c "..."
    n.c "O-Okay."
    n.c "Ah!"
    n.c "Doing this outside..."
    n.c "Feels like, ah, we could be caught at any moment."
    julia.c "Let's try to finish up before someone sees us, then."
    julia.c "Would you stop if they did?"
    n.c "I don't think I could if I-I wanted to."
    julia.c "Me neither."

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Cum!")
    $ quick_menu = True
    julia.c "Ah! Ah! Fuck..."
    n.c "[julia.say_name], I'm gonna..."
    julia.c "(Me too)"
    julia.c "I'm close too, [n.say_name]."
    julia.c "Let it out!"
    n.c "Here it comes!"

    if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc("bg julia_swimsuit_cum_blur_nude" if julia_scene_swimsuit_revisit_nude else "bg julia_swimsuit_cum_blur")
    n.c "[julia.say_name]!"
    julia.c "Mhm... Aah!"

    call static_still_ctc("bg julia_swimsuit_cum_nude" if julia_scene_swimsuit_revisit_nude else "bg julia_swimsuit_cum")
    n.c "{i}Sigh...{/i}"
    n.c "..."
    n.c "That was..."
    julia.c "Yeah..."
    julia.c "(The feeling of his cum on my skin...)"
    julia.c "(Why do I love it so much?)"

    call static_still_ctc("bg julia_swimsuit_aftercum_nude" if julia_scene_swimsuit_revisit_nude else "bg julia_swimsuit_aftercum")
    julia.c "You should let me know in advance when you want to fuck out here so I can put on more sunscreen."
    julia.c "I think I just got a sunburn."

    python:
        if julia_scene_swimsuit_revisit_nude:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_had_incestual_situation", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    $ scenes_completed.add("julia_scene_swimsuit_revisit_second_time_vaginal")
    $ julia_scene_swimsuit_revisit_nude = False
    call julia_scene_swimsuit_revisit_end
    return

label julia_scene_swimsuit_revisit_first_time_blowjob:
    call process_scene_beginning(bg = backyard, char_tuple_array = [(n, "outfit swimsuit pose twohandfist face happy blush false")])

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "(Hm?)"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "(Where's [julia.say_name]?)"

    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
    n.c "(Isn't she meant to be out here?)"

    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
    n.c "(Where could she be?)"

    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
    n.c "(She can't be in the pool, so maybe she's by the hot tub?)"

    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
    n.c "(Oh, there she is!)"

    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
    n.c "{cps=40}(Maybe I should ask her if-){/cps}{w=0.75}{nw}"


    call static_still_ctc("bg julia_swimsuit_read_nude")

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    n.c "[julia.say_name[0]]-[julia.say_name]!"
    n.c "Y-you're..."
    julia.c "Naked?"
    julia.c "Yes, I am."
    julia.c "..."
    julia.c "What are you so concerned about?"
    julia.c "It's not like anyone else is around."
    julia.c "You've seen me naked before."
    julia.c "I know it's not a problem for you anymore."
    julia.c "Right?"
    n.c "..."
    n.c "T-There's no problem at all..."
    n.c "But I thought you didn't like the heat?"
    julia.c "I don't."
    n.c "And won't being n-naked make that worse?"
    julia.c "When it's brutal hot temperatures, sure."
    julia.c "But I also remember saying your yard has a surprisingly nice breeze."
    julia.c "I'm taking advantage of the difference in temperature however I can."
    n.c "By reading naked?"
    julia.c "Yes."
    julia.c "I've even done it at my house a couple times."
    julia.c "Oddly enough it's made me a better reader, even."
    n.c "W-What did your Mom say?"
    julia.c "Considering the lack of air conditioners in my room, it came as no surprise to her."
    julia.c "She's even done it herself too."
    julia.c "Even wearing just underwear was too much for my tiny fan to keep me cool."
    n.c "..."

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)

    $ scenes_completed.add("julia_scene_swimsuit_revisit_first_time_blowjob")
    call julia_scene_swimsuit_revisit_end
    return

label julia_scene_swimsuit_revisit_second_time_blowjob:
    $ no_bust_art = False
    call process_character(n, appearance = "pose behindhead face curious blush false")
    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "(...)"

    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "([julia.say_name]'s naked again)"

    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "(This time I didn't even need to ask her to come out here)"

    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "(Maybe reading naked outside really does make her read better)"


    call static_still_ctc("bg julia_scene_swimsuit_read_nude")
    julia.c "Care to join me [n.say_name]?"


    menu:
        "Yes!":
            call add_boldness(1, tag = "julia_scene_swimsuit_revisit_second_time_blowjob_naked_join")
            julia.c "I knew you couldn't resist."
            julia.c "Let me finish up on this book, and I'll lend it to you for a bit."
            julia.c "It's just us around, so we'll be fine."
            julia.c "Get those shorts off, and focus all your attention on the book."
            julia.c "No perving on me, got it?"

        "Uh, not right now.":
            julia.c "Alright, I'll keep reading then."
            julia.c "I won't be staying out here long, anyways."


    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)

    $ scenes_completed.add("julia_scene_swimsuit_revisit_second_time_blowjob")

    call julia_scene_swimsuit_revisit_end
    return

label julia_scene_swimsuit_revisit_first_time_normal:
    call process_scene_beginning(bg = backyard, char_tuple_array = [ (n, "outfit swimsuit pose twohandfist face happy blush false")])

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "(Today's great weather to be by the pool!)"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "(I think [julia.say_name] thinks so too!)"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face neutral blush false")
    n.c "(She got out here before I did)"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face neutral blush false")
    n.c "(She's already lounging on one of the deck chairs, reading a book)"

    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
    n.c "What are you reading, [julia.say_name]?"


    call static_still_ctc("bg julia_swimsuit_read")

    call process_character(julia, appearance = "outfit swimsuit pose handface face happy blush false")
    julia.c "Something about being by water put me in the mood for a story with pirates."

    call process_character(julia, appearance = "outfit swimsuit pose handface face happy blush false")
    julia.c "It's about a magical swashbuckler, crewing an entire ship on his own."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "Swash... what now?"

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "Swashbuckler."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "It's another term for \"pirate\"."

    call process_character(n, appearance = "outfit swimsuit pose handsdown face curious blush false")
    n.c "Oh..."

    call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
    julia.c "He's embarked on a quest to find his missing crewmates."

    call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
    julia.c "There's thirty chapters, and I'm already halfway through."

    call process_character(julia, appearance = "outfit swimsuit pose handup face embarrassed blush false")
    julia.c "It's not a bad read."

    call process_character(julia, appearance = "outfit swimsuit pose handup face embarrassed blush false")
    julia.c "Maybe I can lend it to you after I'm done, if you're interested."

    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
    n.c "Sure!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "I'd like that."

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "But reading out here isn't like you, [julia.say_name]."

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "I thought you would be reading indoors, away from the sun."

    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false")
    julia.c "I've had just as much difficulty reading indoors too lately."

    call process_character(julia, appearance = "outfit swimsuit pose handup face embarrassed blush false")
    julia.c "Today the sun's decided it wants to seep through all the windows."

    call process_character(julia, appearance = "outfit swimsuit pose handup face embarrassed blush false")
    julia.c "So I decided to just come out here instead."

    call process_character(julia, appearance = "outfit swimsuit pose handup face embarrassed blush false")
    julia.c "Needed some fresh air after it got too stuffy in there."

    call process_character(julia, appearance = "outfit swimsuit pose handup face embarrassed blush false", text = "")
    call process_character(julia, appearance = "outfit swimsuit pose handface face neutral blush false")
    julia.c "But if things still get too bad even under the umbrella, I've got sunglasses next to me."

    call process_character(julia, appearance = "outfit swimsuit pose handface face neutral blush false")
    julia.c "That might be also be an easy way to get eye strain, though."

    pause 1.0
    call process_character(julia, appearance = "outfit swimsuit pose handface face angry blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit swimsuit pose handface face angry blush false")
    julia.c "Don't hold me to that one."


    $ scenes_completed.add("julia_scene_swimsuit_revisit_first_time_normal")

    call julia_scene_swimsuit_revisit_end

    return

label julia_scene_swimsuit_revisit_second_time_normal:
    $ no_bust_art = False
    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    call process_character(julia, appearance = "pose handface face happy blush false", text = "I'll be out in a bit. Wait for me.")

    call fade_to_black(1)

    call process_scene_beginning(bg = "bg backyard_daytime", char_tuple_array = [ (n, "outfit swimsuit pose handsdown face neutral")])

    call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false", text = "Hm, looks like it's just us again.")
    call process_character(julia, appearance = "outfit swimsuit pose armcross face neutral blush false", text = "Is it usually like this when you're out here?")
    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false", text = "Sometimes, yeah.")
    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false", text = "[sa.say_name] likes to come out here too.")
    call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false", text = "She loves making up new challenges we can do while we're in the water.")
    call process_character(julia, appearance = "outfit swimsuit pose handface face curious blush false", text = "Challenges?")
    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false", text = "Like creating the biggest splash we can.")

    if "sam_scene_swimsuit_revisit_first_time_normal" in store.scenes_completed:
        call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false", text = "Or planning our plan of entry...")

    call static_still_ctc("bg julia_swimsuit_read")

    call process_character(julia, appearance = "", text = "You know, I'm starting to get used to this.")
    call process_character(julia, appearance = "", text = "It's really not so bad out here.")
    call process_character(julia, appearance = "", text = "Good thing there's plenty of shade too.")
    call process_character(julia, appearance = "", text = "Makes reading a breeze.")

    $ scenes_completed.add("julia_scene_swimsuit_revisit_second_time_normal")
    call julia_scene_swimsuit_revisit_end

    return

label julia_scene_swimsuit_revisit_end:
    call process_end_of_scene("julia_scene_swimsuit_revisit", char = julia, force_no_boldness = True, reset_prompted_scene = False, force_not_replayable = True, revisit = True)
    return
