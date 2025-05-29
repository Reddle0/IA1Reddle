# Edits existing scenes to have the phone UI show up instead of the characters reading it out, i.e. "Ding!"
# Overrides other mod files like impreg_override and leftovers_override

# This affects:
# 1. Pool party prelude, when Kacey and Vicky texts Nate
# 2. Vicky's vaginal and anal scenes
# 3. Kacey's apartment intro (Leftovers-Mod)

init 201 python:
    config.label_overrides.update( { "finale_scene_leftovers_sex" : "finale_scene_leftovers_1" } )
    config.label_overrides.update( { "vicky_scene_vaginal_sex" : "vicky_scene_vaginal_sex_leftovers" } )
    config.label_overrides.update( { "vicky_scene_anal_sex" : "vicky_scene_anal_sex_leftovers" } )

label finale_scene_leftovers_1(dream = False):
# now in finale_scene_leftovers_3
#    $ renpy.start_predict("edna_titfuck_nude_anim")

# now in finale_scene_leftovers_5
#    call finale_scene_initialize

#    if finale_julia_sam:
#        $ finale_fucked_amount_goal = 8
#    else:
#        $ finale_fucked_amount_goal = 6

    call process_scene_beginning(bg = "bg kira_room_evening", char_tuple_array = [], dream = dream)

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(Tonight's ideal for a jog!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(The temperatures are starting to get cooler)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(I should get [n.say_name] to join me)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(It'll give him a change of pace from the running track)"

    call process_new_location(bg = "bg nate_room_evening", dream = dream)

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "Hey [n.say_name]!"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "{cps=40}You wanna go-{/cps}{w=0.75}{nw}"

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "(Where the hell is he?)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(I know he's not fucking Mom, she's downstairs cleaning the kitchen)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(I didn't see him in [sa.say_name]'s room either)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(I'll try calling him)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(If he doesn't answer, then I'll just go by myself)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "..."

    call play_phone_ring
#    "{i}Ring-Ring-Ring!{/i}"

    # pause to have a delayed recation
    pause 2

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "..."

    call play_phone_ring

    # another pause
    pause 1

#    "{i}Ring-Ring-Ring!{/i}"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(What the...)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(Seriously [n.say_name]?)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(You left your phone in your room?)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "{i}Sigh.{/i}.."

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "(My brother can be a flake sometimes...)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "(One of these days his phone will get lost or stolen, it's inevitable)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(I bet he doesn't even have a password on his phone)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "..."

    # pause to have a slightly delayed recation
#    pause 1

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(Yep, knew it!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(I can just open his phone with no effort!)"

    #Comment: Texting SFX
    call play_new_chat

    # pause to have a slightly delayed recation
    pause 1

#    "{i}Ding!{/i}"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(And of course a text comes in)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(Whoever sent it will have to wait a while for a response from my brother)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "...{p}..."

    pause 1

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "([gloryhole_girl.say_name]?)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(I've never heard [n.say_name] mention a girl named [gloryhole_girl.say_name]...)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "..."

    call character_leave_dissolve(k)

    call texting_preparation(gloryhole_girl)
    window auto hide

    kacey_nvl "I'll be at the park in a few minutes [n.say_name]!"
    $ phone_slide_up = False
    kacey_nvl "Can't wait for us to have some more fun together! {❤️}"

    call texting_hide_phone(hide_window = False, clear_nvl = True)

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "(Well I'll be...)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "([n.say_name]'s got himself a girlfriend!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(Seems like she's fond of him too)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(Bro must want to keep this under the radar, meeting her in the park at night)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(I'm real curious to see what kind of girl [n.say_name] has hooked up with!)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(I know where I'm going for my jog!)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(If [n.say_name] happens to spot me, I'll just say it's pure coincidence that I'm jogging around the same park)"

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false")
    k.c "(Yeah, pure coincidence...)"

    call finale_scene_leftovers_2(dream = dream)

    return

label finale_scene_leftovers_2(dream = False):
    call fade_to_black(1)

    call process_new_location("bg park_evening", dream = dream)

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(Alright, where is he, where is he...)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(A-ha!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(I see [n.say_name]!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(He's over near one of the bathrooms)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "(I've got a bead on you now bro!)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(No girlfriend in sight...{w=1.0}yet)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(I bet they meet up near the bathroom, since it's an obvious landmark)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(Further investigation is required!)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "([n.say_name]'s going into the bathroom)"

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false")
    k.c "(While he's in there, I'll keep watch for his girl...)"

    call fade_to_black(1)

    call process_new_location("bg park_evening", dream = dream)

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(How long is [n.say_name] going to be in there for?)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(Is he crapping his brains out or something?)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "(And I haven't seen anyone around here since he first went in)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "(No other text messages from [gloryhole_girl.say_name] either...)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "...{p}..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(Finally, he's emerged!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armsup face curious blush false")
    k.c "(Why does [n.say_name] look sweaty?)"

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "(Only time he sweats that much is when he's...)"

    call process_character(k, appearance = "outfit clothes pose handhip face shocked blush false")
    k.c "!"

    call process_character(k, appearance = "outfit clothes pose handhip face shocked blush false")
    k.c "(Whoa, whoa, what the fuck?!)"

    call process_character(k, appearance = "outfit clothes pose armcross face shocked blush false")
    k.c "(A girl just came out of the same bathroom as [n.say_name]!)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(And she's talking to him too...)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face embarrassed blush false")
    k.c "(Could that be...{w=1.0}[gloryhole_girl.say_name]?)"

    call process_character(k, appearance = "outfit clothes pose handhip face embarrassed blush false")
    k.c "(She appears to be sweating as well)"

    call process_character(k, appearance = "outfit clothes pose handhip face shocked blush false")
    k.c "(Was bro doing what I think he was doing in there with her?)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "...{p}..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(They're hugging)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "([n.say_name]'s grabbing a good amount of her ass too...{w=0.5}nice one bro)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(There's no doubt in my mind that's [gloryhole_girl.say_name])" # fixed custom name not being present here

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(Looks like they're parting ways)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(I need to take a quick look inside that bathroom)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(If any dirty deed was done in there, I'll know pretty quick...)"

    call fade_to_black(1)

    call process_new_location("bg public_bathroom_evening", dream = dream)

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(There is a strong, familiar odor in here)"

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false")
    k.c "(And it's not the usual smell associated with a bathroom)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(But I need more evidence...)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "...{p}..."

    call static_still_ctc("bg gloryhole")

    k.c "(Well, can't get more obvious than this...)"
    k.c "(A gloryhole!)"
    k.c "(Wow, look at the floor just below it!)"
    k.c "(Those are fresh cum stains)"
    k.c "(Some jizz strands are still sliding down the stall door)"
    k.c "(That's all I need to see!)"
    k.c "([n.say_name]'s been banging this [gloryhole_girl.say_name] girl!)"
    k.c "(And from the looks of things, it's been way more than once!)"
    k.c "..."
    k.c "(How did these two manage to meet each other?)"
    k.c "(And why hasn't [n.say_name] invited her over to our place yet?)"
    k.c "(She seems like a girl I'd want to get to know!)"
    k.c "..."
    k.c "(Wait a second... {w=1.0}[n.say_name]'s phone...)"
    k.c "([gloryhole_girl.say_name] would assume it's [n.say_name] who's texting her from this number)"
    k.c "..."
    k.c "(I think I'll set up a meet and greet with this [gloryhole_girl.say_name])"
    k.c "(Then I can learn more about all the juicy, sticky details between her and [n.say_name], hehe...)"

    call finale_scene_leftovers_3(dream = dream)

    return

label finale_scene_leftovers_3(dream = False):
    $ renpy.start_predict("edna_titfuck_nude_anim")

    call fade_to_black(1)

    call process_new_location("bg kitchen_daytime", dream = dream)

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face aroused blush false")
    n.c "{i}Yawn.{/i}.."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "Late night, eh?"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "Yeah."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "You won't be able to stay up as late with school starting soon."

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "Unless your plan is to take naps during class!"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face concerned blush false")
    n.c "Can't believe summer's almost over..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "There's still some time left."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "You just have to make the most out of it!"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral blush false")
    n.c "Yeah, I should..."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "Personally, I want to get a few more beach days in!"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "Me too!"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "Why don't we go there today?"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "I'm hankering for another volleyball match!"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "Can we ask Grandma if she'd like to join us?"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "Sure."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "I doubt she'd turn down a beach invite."

    call fade_to_black(1)

    call process_new_location("bg beach_daytime", dream = dream)

    $ replace_position = True
    $ k.position = "right"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I'm happy you two were able to get to the beach today!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "Yeah, we are too!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Won't be long before we'll need jackets if we want to be out here."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Fall is fast approaching."

    call process_character(n, appearance = "outfit swimsuit pose handsdown face concerned blush false")
    n.c "And so is school..."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face curious blush false mouth red")
    edna.c "Is it really that close to school starting up for you again [n.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "Feels like summer just started a few days ago!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")

    call process_character(k, appearance = "outfit bikini pose armcross face concerned blush false")
    k.c "Worst part is how long the wait is for the next summer to arrive."

    call process_character(k, appearance = "outfit bikini pose armcross face concerned blush false")
    k.c "Winter drags on for too long."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "I know exactly how you feel [k.say_name]!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face embarrassed blush false mouth red")
    edna.c "My joints do not appreciate the cold weather!"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "Well, before those cold fronts start rolling in, I'm gonna crush it at volleyball some more!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "[n.say_name], you want to pair up so we can dominate?"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "Hmm..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Can [n.say_name] join you a little later [k.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I want to talk with him about what's going to be happening at his new school, and what he'll be learning!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "That's fine Grandma."

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "While I wait, I'll help tilt a team that needs an extra player!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Go get em granddaughter!"

    call character_leave_dissolve(k)
    pause 0.5

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "Once you're back in school, I won't get to see you as often."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "You'll be busy studying, taking tests..."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face concerned blush false")
    n.c "And writing papers..."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "[k.say_name] will be occupied for a while."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face flirt blush false mouth red")
    edna.c "Did you want to head up to my condo?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face flirt blush false mouth red")
    edna.c "There are certain things we can do while we're up there..."

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face neutral blush false")
    n.c "There sure is Grandma..."

    call fade_to_black(1)

    call process_new_location("bg beach_daytime", dream = dream)

    call process_character(k, appearance = "outfit bikini pose armcross face angry blush false")
    k.c "I don't think I've played with a shittier team before!"

    call process_character(k, appearance = "outfit bikini pose armcross face angry blush false")
    k.c "They could hardly hit the ball over the net!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "[n.say_name], you and I would wipe the floor against them!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Let's go back over there, and show them who are the masters of..."

    call process_character(k, appearance = "outfit bikini pose armsup face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Where'd [n.say_name] and Grandma go?)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Their stuff is still here)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "(I bet they're making some sandwiches back at the condo)"

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "(I need to grab some extra water bottles, so I'll head back up there real quick)"

    call fade_to_black(1)

    call process_new_location("bg edna_house_daytime", dream = dream)

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Damn, did I just miss them?)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Nah, I couldn't have)"

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "(I would have spotted them in the hallway or the lobby)"

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "(There's no sandwiches or anything on the kitchen counter)"

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "(What did they come back here for then?)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Did [n.say_name] get stung by a jellyfish or something?)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(Oh, there they are!)"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(They're out on the balcony)"

    call process_character(k, appearance = "outfit bikini pose armsup face curious blush false")
    k.c "(Wait...{w=1.0}are they naked out there?)"

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "{cps=40}(And why is Grandma kneeling down-){/cps}{w=0.75}{nw}"

    call process_character(k, appearance = "outfit bikini pose armcross face shocked blush false")
    k.c "!!"

    $ set_main_animation_speed(1.0)
    $ edna_titfuck_had_slow_speed_message = False
    $ edna_titfuck_had_normal_speed_message = False
    $ edna_titfuck_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    show anim_nothing_image at main_animation_transform(IA_Animation_Edna_Titfuck_Nude_Info()) as main_animation
    with Dissolve(1.15)
    show bg white

    pause
    $ quick_menu = True
    $ no_bust_art = True

    k.c "(What the fucking shit?!)"
    k.c "(Am I suffering from heat stroke hallucinations?!)"
    k.c "..."
    k.c "(This...{w=1.0}this is real right now)"
    k.c "(Grandma and [n.say_name]...)"
    k.c "(Grandma...{w=1.0}and [n.say_name]!)"
    k.c "(Even for me, I can't wrap my head around this!)"
    k.c "..."
    k.c "(Although...{w=1.0}I recall Grandma acting a bit flirty towards [n.say_name] recently)"
    k.c "(But I thought she was just having fun!)"
    k.c "(I didn't think she wanted some real hardcore action with bro's dick!)"
    k.c "(I figured she was past that point at her age)"
    k.c "(I got that wrong!)"

    window hide
    call edna_titfuck_set_speed(edna_titfuck_fastest_speed_multiplier)
    pause
    window auto
    k.c "(Grandma is having a ball!)"
    k.c "(She's been smiling the whole time [n.say_name] has had his dick between her tits!)"
    k.c "(And [n.say_name] is showing no signs of hesitation!)"
    k.c "(Gone is the nervous and reluctant brother staring at my ass!)"
    k.c "(Now he's a verified mother, and grandmother fucker!)"
    n.c "Oh, oh yeah..."
    n.c "Here I come Grandma!"
    k.c "..."

    $ quick_menu = False
    window hide
    hide main_animation
    with Dissolve(1.5)
    $ play_sex_sounds = False

    pause 0.5

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    $ quick_menu = False
    window hide
    show bg edna_nude_titfuck_cumshot_surprise
    with Dissolve(1.5)

    pause
    $ quick_menu = True
    n.c "Hnngaa!"
    k.c "(Damn, what a fat nut!)"

    call static_still_ctc("bg edna_nude_titfuck_aftercum_smile")
    k.c "([n.say_name] just blasted Grandma's tits with cum!)"
    k.c "(He spurted like a fountain!)"
    k.c "(And look at the wide grin on Grandma!)"
    k.c "(I don't think I've seen anybody show that much glee about a titty fuck...{w=0.5}other than me!)"
    edna.c "Feel better [n.say_name]?"
    edna.c "Now you'll be set for playing volleyball with your big sister!"
    n.c "Yeah, I will Grandma!"
    edna.c "Let's head back down to the beach."
    edna.c "[k.say_name] is probably wondering where we are right now."
    k.c "(Shit, I have to get out of here!)"
    k.c "(I'll just play it cool for the remainder of the day)"

    call fade_to_black(1)

    $ renpy.stop_predict("edna_titfuck_nude_anim")
    call process_new_location(bg = "bg edna_house_evening", dream = dream)

    $ k.position = "right"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "That was one of the longest times I've stayed at the beach in one day!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "But the temperature was too perfect to waste!"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "I think that was the best beach day yet Grandma!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I think it was too!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "It wasn't crowded, the waves were rolling in smooth..."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face happy blush false mouth red")
    edna.c "And you and [k.say_name] went undefeated together in volleyball!"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "Thanks to my trusty spike I like to call, deep impact!"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "I got sand all down my suit from playing."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "All those diving saves I made put plenty of the beach up my ass crack."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Use the shower to clean yourself up."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "After being on the beach for that long, you do start to get a bit grimy."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "You go in first bro."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "I'll chat with Grandma while I wait."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "That's nice of you [k.say_name]."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Don't hog all the hot water though!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "I won't."

    call character_leave_dissolve(n)
    pause 0.5

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "...{p}..."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "I know you saw me on the balcony with [n.say_name], [k.say_name]."

    call process_character(k, appearance = "outfit bikini pose armcross face embarrassed blush false")
    k.c "!"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "I caught your bright green bikini out of the corner of my eye."

    call process_character(k, appearance = "outfit bikini pose armcross face embarrassed blush false")
    k.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "You were going to ask me about it, I could tell."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "So I'm admitting to you now that yes, I do have sex with [n.say_name]."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "You're being surprisingly chill about telling me all of this Grandma."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Well, your reaction to it is rather subdued."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face curious blush false mouth red")
    edna.c "Isn't that unusual as well?"

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "What does my reaction have to do with this?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "You've also had sexual experiences with [n.say_name]."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "It started this summer."

    call process_character(k, appearance = "outfit bikini pose armsup face embarrassed blush false")
    k.c "Huh?!"

    call process_character(k, appearance = "outfit bikini pose armsup face embarrassed blush false")
    k.c "How do you..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "How do I know?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "[n.say_name] loves talking about you."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "He tells me you give great titfucks to him back at home."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face curious blush false mouth red")
    edna.c "And you both practice these...{w=0.5}kamasutra positions with each other?"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face happy blush false mouth red")
    edna.c "They're out of my range of flexibility!"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "So [n.say_name]'s just been blabbering all of this to you?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "Now don't get mad at [n.say_name], [k.say_name]."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "He only tells me these things because he knows I support it."

    call process_character(k, appearance = "outfit bikini pose armcross face embarrassed blush false")
    k.c "You support [n.say_name] and I fucking Grandma?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Of course I do!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I think it's great!"

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "I...{w=1.0}didn't know you were so enthusiastic about it."

    if "family_foursome_scene" in scenes_completed or finale_julia_sam:
        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "[n.say_name] couldn't stop talking about the foursome he had with you, [sa.say_name], and [si.say_name] the other day!"

        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "I wish I could have been there to see it!"

    else:
        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "[n.say_name] couldn't stop talking about the threesome he had with you and [si.say_name] the other day!"

        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "I wish I could have been there to see it!"

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "Are you like...{w=1.0}a nymphomaniac Grandma?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "Haha!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "At one point in time, that would have been a very accurate word to associate with me!"

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "So now you're just a nympho?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Very funny [k.say_name]!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Man, [n.say_name] has been getting around this summer!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "He's using that free time he has effectively!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "It's why I wanted to be with him today."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "School will be squeezing his schedule."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "He already occupies most of his time rotating among all of us!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "One day it may be me, next day it may be [si.say_name], then [janet.say_name], then..."

    call process_character(k, appearance = "outfit bikini pose armcross face shocked blush false")
    k.c "Wait, what?"

    call process_character(k, appearance = "outfit bikini pose armcross face shocked blush false")
    k.c "Aunt [janet.say_name]?!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face curious blush false mouth red")
    edna.c "You didn't know about [janet.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "Yes, she's been active with [n.say_name] as well."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "I've spotted them a couple times, fucking on the beach."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "It's very clever how they hide between the lounge chairs!"

    if finale_julia_sam:
        call process_character(k, appearance = "pose armsup face embarrassed blush false")
        k.c "He's practically banging the entire family!"

        call process_character(k, appearance = "pose armsup face embarrassed blush false")
        k.c "I don't know how [julia.say_name] hasn't found out about this yet."

        call process_character(edna, appearance = "pose handclasp face neutral blush false")
        edna.c "Mm...{w=1.0}well..."

        call process_character(k, appearance = "pose armcross face shocked blush false")
        k.c "..."

        call process_character(k, appearance = "pose armcross face shocked blush false")
        k.c "You've got to be shitting me."

        call process_character(edna, appearance = "pose handclasp face neutral blush false")
        edna.c "He's fucking [julia.say_name] too."

    else:
        call process_character(k, appearance = "pose armsup face embarrassed blush false")
        k.c "..."

        call process_character(k, appearance = "pose armsup face embarrassed blush false")
        k.c "You've got to be shitting me."

    call process_character(k, appearance = "outfit bikini pose handhip face embarrassed blush false")
    k.c "How is that even possible for [n.say_name] to accomplish?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "I don't know, but [n.say_name] makes it work."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "I think it helps that everyone is in close proximity."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Did he also tell you about [gloryhole_girl.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face curious blush false mouth red")
    edna.c "[gloryhole_girl.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "[gloryhole_girl.say_name]...{w=0.5}[gloryhole_girl.say_name]..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Yeah."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Bro's been having a big fling with her at the local park."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "I learned about his involvement with her purely by accident."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "I did not know about that."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "So [n.say_name] has had sexual adventures outside the family as well."

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "[n.say_name] literally has a girl for every day of the week."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "A full itinerary!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "It's just constant sex for him."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "Bro's not just a sex addict...{w=1.0}he's a sex maniac!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "I don't know how much longer [n.say_name] will be able to keep this under wraps."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "My feeling is each girl will eventually learn everything we currently know."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "I think you're spot on Grandma."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Sooner or later, it will all come bursting out."

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "Just like what [n.say_name] did earlier today, bursting on your tits!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Haha!"

    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false")
    n.c "Okay, I'm done in the shower."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "..."

    call process_character(n, appearance = "outfit underwear pose behindhead face neutral blush false")
    n.c "What were you two laughing about?"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "Oh, we were just laughing about..."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "How I bonked that one dude off the head with one of my spikes!"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face happy blush false mouth red")
    edna.c "Yes!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "Oh yeah!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "That was hilarious!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "He spun around after he got hit!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "My turn for the shower."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Grandma, we'll talk again later."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "There's a lot we need to catch up on..."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "I can't wait [k.say_name]!"

    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false")
    n.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Now, [n.say_name]..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Would you like to help me prepare a meal in the kitchen?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I've got a recipe for sweet and sour meatballs that I know you'll love!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "That sounds insanely good Grandma!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "Yeah, I want to help make it!"

    call finale_scene_leftovers_4(dream = dream)

    return

label finale_scene_leftovers_4(dream = False):
    call fade_to_black(1)

    call process_new_location(bg = "bg kira_room_daytime", dream = dream)

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(So this is how far you've come bro)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(One day you're wedging your dick between my butt cheeks, eager to see what it feels like...)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "(And the next, your dick is going into the pussy of every girl you meet!)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "(Quite a drastic leap)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(Imagine the number of fuck buddies he'll make at school!)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(It will be like a small army!)"

    #Comment: Texting SFX
    call play_new_chat

    # pause to have a slightly delayed recation
    pause 1

#    "{i}Ding!{/i}"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "(Who'd I get a text from?)"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "(The number isn't familiar)"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose handhip face curious blush false")
    k.c "([vicky.say_name]?)"

    call process_character(k, appearance = "pose handhip face curious blush false")
    k.c "(No idea who this is)"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "(Yikes, she sent me a wall of text!)"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "(Let's see here...)"

    call character_leave_dissolve(k)

    call texting_preparation(vicky)
    window auto hide

    vicky_nvl "Greetings [k.say_name] [last_name]."
    $ phone_slide_up = False
    vicky_nvl "My name is [vicky.say_name] Hardy, and I run an adult video production company, \"[vicky.say_name]'s Empornium\"." # added Vicky's last name and quotation marks around the Empornium name

    call process_character(k, appearance = "pose armcross face happy blush false")
    k.c "(Empornium...{w=1.0}clever)"

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "(But why am I being contacted by someone like that?)"

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "..."

    vicky_nvl "I was referred to you by your brother, [n.say_name] [last_name]."

    call process_character(k, appearance = "pose handhip face shocked blush false")
    k.c "(What?)"

    call process_character(k, appearance = "pose handhip face shocked blush false")
    k.c "(An owner of a porn company knows [n.say_name]?)"

    call process_character(k, appearance = "pose handhip face embarrassed blush false")
    k.c "(And he referred me?)"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "(This has to be a joke...)"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "..."

    vicky_nvl "I would very much like to arrange a meeting with you."
    vicky_nvl "There is a great opportunity for you that we can discuss!"
    vicky_nvl "If you're interested, please respond to this text."
    vicky_nvl "I look forward to hearing from you!"

    call texting_hide_phone(hide_window = False, clear_nvl = True)

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "(Great opportunity?)"

    call process_character(k, appearance = "pose handhip face embarrassed blush false")
    k.c "(What crazy scheme did [n.say_name] get himself into?)"

    call process_character(k, appearance = "pose handhip face happy blush false")
    k.c "(Still... {w=1.0}my curiosity is through the roof right now!)"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "(I want to know if this chick is legit or not...)"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "..."

    kira_nvl "Hey [vicky.say_name]" # fixed custom name not being present here
    kira_nvl "Where are you at, and what times are you available?"

    call fade_to_black(1)

    show bg vicky_sit_smile
    with Dissolve(0.5)

    k.c "You're [vicky.say_name], I presume?"
    vicky.c "And you must be [k.say_name]!"
    vicky.c "I finally get to meet [n.say_name]'s big sister in the flesh!"
    k.c "Yeah so...{w=1.0}how did my little brother come to know you anyway?"
    k.c "I can't imagine he encountered a porn company owner by accident."

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    vicky.c "I previously worked as an affiliate for ReflexViz.HD."
    vicky.c "Are you familiar with the company?"
    k.c "That's the streaming thing online, right?"
    k.c "[n.say_name] and [sa.say_name] couldn't stop talking about it at the beginning of the summer."
    k.c "They were making a show or something called Twinsticks."
    vicky.c "That's right."
    vicky.c "I contacted [n.say_name] after he and his sister [sa.say_name] began building a sizable audience."
    vicky.c "Their channel had a lot of potential, and so I met with [n.say_name] to help maximize his growth."
    k.c "So [n.say_name] & [sa.say_name] must have been rocking it with their stream to be contacted by someone like you."

    show bg vicky_sit_smile
    with Dissolve(0.5)
    vicky.c "They're well on their way to becoming one of the top channels on the ReflexViz.HD platform!"
    k.c "So, where then does the whole porn thing come into play?"
    vicky.c "I found that [n.say_name] had a rather...{w=1.0}special talent when it came to adult content."
    vicky.c "Right from our first meeting, it was clear to me that [n.say_name] had all the makings of the next great porn star."
    k.c "Porn star?!"
    k.c "My little bro [n.say_name], a porn star?"
    k.c "Hahaha!"
    vicky.c "I can attest to [n.say_name]'s impressive capabilities."
    vicky.c "He never fails to deliver!"
    k.c "..."
    k.c "Are you trying to tell me that...{w=1.0}you and [n.say_name]..."
    vicky.c "This very office has been the sight of more than a few of our...{w=1.0}sessions."
    k.c "(I thought I smelled the faint scent of cum in here...)"
    vicky.c "Soon after, I established [vicky.say_name]'s Empornium, with [n.say_name] playing a pivotal role in production."
    k.c "A pivotal role, huh?"
    vicky.c "Have you seen our videos yet?"
    k.c "You and [n.say_name] made a video?!"
    vicky.c "Several at this point."
    vicky.c "It's content exclusive to the [vicky.say_name]'s Empornium website."

    show bg vicky_sit_turn
    with Dissolve(0.5)

    vicky.c "Here, let me pull up one of our recent ones for you."
    k.c "..."
    k.c "Holy shit, there's [n.say_name]!"
    k.c "And that's you!"
    vicky.c "Indeed it is."
    k.c "Nice camera work there."
    k.c "I see you let him go up your back passage, hehe."
    k.c "I approve."
    vicky.c "We try to do every possible scenario we can."
    k.c "([n.say_name]'s turned fucking into a profession!)"
    k.c "(He's literally making dough by having his dick do the work!)"

    show bg vicky_sit_smile
    with Dissolve(0.5)
    vicky.c "So, what do you think?"
    k.c "I think...{w=1.0}[n.say_name] is one lucky bastard."
    k.c "I wish I was doing the same thing."
    vicky.c "Then you'll want to hear my offer [k.say_name]."
    k.c "..."
    k.c "Go on."
    vicky.c "I'd like you to be the main adult actress that works with [n.say_name]."
    vicky.c "You could have your own dedicated series!"
    vicky.c "And, you'll get to keep seventy percent of the royalties from sales and subscriptions."
    k.c "Hmm!"
    k.c "I'm liking the sound of that!"
    k.c "If it becomes successful, I won't have to work at the fitness center anymore!"
    vicky.c "I'm certain it will be successful."
    vicky.c "The market is ripe for this sort of content right now."

    show bg vicky_sit_neutral
    with Dissolve(0.5)
    vicky.c "But you don't have to rush your decision."
    vicky.c "I want to make sure you feel certain about it."
    vicky.c "Before you leave today, I'll give you some documents and outlines as to what would be expected of you."
    vicky.c "Read it over carefully, and let me know what you think."

    show bg vicky_sit_smile
    with Dissolve(0.5)

    vicky.c "I'm open to revisions and negotiations, so all of what you read is subject to change."
    k.c "I don't think it will take me that long to make a decision!"
    vicky.c "That's great to hear you have enthusiasm for the offer!"
    vicky.c "I'm glad you were able to stop by and talk to me today!"
    k.c "Hey, thank you for dropping this once in a lifetime opportunity in my lap!"
    vicky.c "No need to thank me."
    vicky.c "It was your brother [n.say_name] that informed me about you, after all."
    vicky.c "He's the one you should be thanking."
    k.c "Oh trust me, I will..."
    vicky.c "You have my contact information and business card, so give me a buzz whenever you'd like to talk."
    k.c "Sounds good [vicky.say_name]!"

    call fade_to_black(1)

    call process_new_location(bg = "bg backyard_daytime", dream = dream)

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(Imagine...{w=0.5}me being a porn star with [n.say_name])"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "(My favorite pastime of fucking can now be a career!)"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "(I'll have to come up with a good porn star name)"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "(I wonder if [n.say_name] has one yet...)"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "(Bro is the only person I've known where thinking with his dick turned out to be a good thing!)"

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "(Now he has a whole line-up of girls willing to go down on him)"

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(Imagine if every girl [n.say_name] had been with gathered together in one spot?)"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(It would be chaos...{w=1.0}for [n.say_name]!)"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "(Talk about too much of a good thing!)"

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "(Would his cock and balls even survive such an ordeal?)"

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Hmm..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "Hehe..."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(Given the way this summer has been for [n.say_name], it would only be fitting if it went out with a huge bang)"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "(A gangbang that is...)"

    call finale_scene_leftovers_5(dream = dream)

    return

label finale_scene_leftovers_5(dream = False):
    call finale_scene_initialize

    if finale_julia_sam:
        $ finale_fucked_amount_goal = 8
    else:
        $ finale_fucked_amount_goal = 6

    call fade_to_black(1)

    "{i}Several days later...{/i}"

    call process_new_location(bg = "bg nate_room_daytime", dream = dream)

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned blush false")
    n.c "(Not much longer until school starts...)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(Wish I could time travel and go through the summer again)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned blush false")
    n.c "{i}Sigh.{/i}.."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "(Well, like [k.say_name] said, I need to make the most of my remaining summer vacation)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious blush false")
    n.c "Hm?"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(I hear a lot of talking outside at the pool)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(Did Mom invite company over?)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "(It is pretty warm out today)"

    call process_character(n, appearance = "outfit clothesjacket pose handfist face neutral blush false")
    n.c "(I think a swim in the pool is in order!)"

    call character_leave_dissolve(n)

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "(I'm ready for a cannonball!)"

    call fade_to_black(1)

    call process_new_location(bg = "bg backyard_daytime", dream = dream)

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "..."

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose armunder face happy blush false")
        si.c "There he is!"
    else:
        call process_character(si, appearance = "outfit clothes pose armunder face happy blush false")
        si.c "There he is!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Bout time bro!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Everyone's been waiting for you."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "What do you mean everyone?"

    if finale_julia_sam and "sam_scene_swimsuit" in store.scenes_completed:
        call process_character(sa, appearance = "outfit swimsuit pose leaning face neutral blush false")
        sa.c "Just look at who's here [n.say_name]!"
    else:
        call process_character(sa, appearance = "outfit clothes pose leaning face neutral blush false")
        sa.c "Just look at who's here [n.say_name]!"

    call process_character(janet, appearance = "outfit swimsuit pose handhips face neutral blush false")
    janet.c "I love this pool [n.say_name]!"

    call process_character(janet, appearance = "outfit swimsuit pose handhips face neutral blush false")
    janet.c "It's perfect for hosting a party like this!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face happy blush false")
    n.c "Aunt [janet.say_name]!"

    if finale_julia_sam and "julia_scene_swimsuit" in store.scenes_completed:
        call process_character(julia, appearance = "outfit swimsuit pose armcross face concerned blush false")
        julia.c "..."

        call process_character(n, appearance = "outfit swimsuit pose handsdown face happy blush false")
        n.c "Hey [julia.say_name]!"

        call process_character(n, appearance = "outfit swimsuit pose handfist face happy blush false")
        n.c "Oh, you're wearing the swimsuit I got you!"

        call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
        julia.c "..."

        call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
        julia.c "Yeah..."

        call process_character(janet, appearance = "outfit swimsuit pose handface face happy blush false")
        janet.c "Ah, ha!"

        call process_character(janet, appearance = "outfit swimsuit pose handface face happy blush false")
        janet.c "So it was you who got her that, [n.say_name]!"

        call process_character(janet, appearance = "outfit swimsuit pose handchest face neutral blush false")
        janet.c "This is the first time in a long time that I've seen her wear a swimsuit."

        call process_character(janet, appearance = "outfit swimsuit pose handchest face happy blush false")
        janet.c "I guess I have you to thank for that!"

        call process_character(julia, appearance = "outfit swimsuit pose handup face concerned blush false")
        julia.c "..."

        call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
        n.c "Um, is everything okay, [julia.say_name]?"

        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handface face neutral blush false")
            sa.c "She's fine!"
        else:
            call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false")
            sa.c "She's fine!"

        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handsbehind face neutral blush false")
            sa.c "She's just a little embarrassed about wearing her swimsuit in front of everybody, I think."
        else:
            call process_character(sa, appearance = "outfit clothes pose handsbehind face neutral blush false")
            sa.c "She's just a little embarrassed about wearing her swimsuit in front of everybody, I think."

        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handsbehind face neutral blush false")
            sa.c "But I'm helping her ease into it!"

            call process_character(julia, appearance = "outfit swimsuit pose armcross face embarrassed blush false")
            julia.c "Yes, she's very... {w=0.5}persistent about it."

            call process_character(sa, appearance = "outfit swimsuit pose leaning face neutral blush false")
            sa.c "I gave her some inspiring words of encouragement earlier too."

            call process_character(sa, appearance = "outfit swimsuit pose leaning face happy blush false")
            sa.c "Everybody gets to wear a swimsuit today!"

        else:
            call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false")
            sa.c "Oh man, I wish I had a swimsuit too!"

            call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false")
            sa.c "Maybe I could get one just like yours, [julia.say_name]!"

            call process_character(sa, appearance = "outfit clothes pose leaning face happy blush false")
            sa.c "Then we could have matching swimsuits!"

        call process_character(janet, appearance = "outfit swimsuit pose handchest face neutral blush false")
        janet.c "I know you're no fan of swimming, [julia.say_name], but it suits you very well!"

#        call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
#        n.c "Yeah!"

        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handsbehind face happy blush false")
            sa.c "Mhm!"

            call process_character(sa, appearance = "outfit swimsuit pose handsbehind face happy blush false")
            sa.c "You look really cute in that swimsuit!"
        else:
            call process_character(sa, appearance = "outfit clothes pose handsbehind face happy blush false")
            sa.c "Mhm!"

            call process_character(sa, appearance = "outfit clothes pose handsbehind face happy blush false")
            sa.c "You look really cute in that swimsuit!"

        call process_character(julia, appearance = "outfit swimsuit pose armcross face embarrassed blush true")
        julia.c "(Cute?)"

        call process_character(julia, appearance = "outfit swimsuit pose armcross face embarrassed blush true")
        julia.c "T-thanks..."

    elif finale_julia_sam and "julia_scene_swimsuit" not in store.scenes_completed:
        call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
        julia.c "I don't have a suit to put on for swimming, not that I would anyway."

        call process_character(julia, appearance = "outfit clothes pose armcross face happy blush false")
        julia.c "But, I like dipping my feet into the hot tub."

        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "Hey [julia.say_name]!"

        call process_character(julia, appearance = "outfit clothes pose handup face happy blush false")
        julia.c "Hey."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Help yourself to the snacks [n.say_name]!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Try out the chips and dip!"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "You're here too Grandma?!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose handsup face neutral blush false")
        si.c "This was all [k.say_name]'s planning!"
    else:
        call process_character(si, appearance = "outfit clothes pose handsup face neutral blush false")
        si.c "This was all [k.say_name]'s planning!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose handsup face happy blush false")
        si.c "She said we should have an end of summer get together, and I very much agreed with the idea!"
    else:
        call process_character(si, appearance = "outfit clothes pose handsup face happy blush false")
        si.c "She said we should have an end of summer get together, and I very much agreed with the idea!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "It wasn't easy working around the schedules."

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "But I wasn't going to give up!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face happy blush false")
    n.c "I'm glad you didn't [k.say_name]!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face happy blush false")
    n.c "This is so cool having everybody here!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Well, it's not quite everyone yet."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "There's still two more guests yet to arrive."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "Really?"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "More?"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Yes..."

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "Your park friend [gloryhole_girl.say_name], and business partner [vicky.say_name]."

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face embarrassed blush false")
    n.c "[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name] and [vicky.say_name] are coming?!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose handsfront face neutral blush false")
        si.c "You should have told us about them earlier sweetie!"
    else:
        call process_character(si, appearance = "outfit clothes pose handsfront face neutral blush false")
        si.c "You should have told us about them earlier sweetie!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose handsfront face neutral blush false")
        si.c "They both sound like lovely girls, based on what [k.say_name] told me."
    else:
        call process_character(si, appearance = "outfit clothes pose handsfront face neutral blush false")
        si.c "They both sound like lovely girls, based on what [k.say_name] told me."

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose armunder face happy blush false")
        si.c "I would have invited them over for supper!"
    else:
        call process_character(si, appearance = "outfit clothes pose armunder face happy blush false")
        si.c "I would have invited them over for supper!"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "H-How did you learn about..."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Attention everyone!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Attention!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face concerned blush false")
    n.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Now that [n.say_name] is finally here...{w=1.0}it's about time we revealed to him what this party is really about."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "Each of you should know exactly what I mean, based on what was discussed previously."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "What was discussed?"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "I don't think you talked to me about it..."

    call character_leave_dissolve(k)
    pause 0.5

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call process_character(k, appearance = "outfit nude pose armsup face happy blush false")
    pause 0.5

    call process_character(k, appearance = "outfit nude pose armsup face happy blush false")
    k.c "..."

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face embarrassed blush false")
    n.c "!!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose armunder face flirt blush false")
    else:
        call process_character(si, appearance = "outfit clothes pose armunder face flirt blush false")

    pause 0.5
    call character_leave_dissolve(si)
    pause 0.5
    call process_character(si, appearance = "outfit nude pose armunder face flirt blush false")
    pause 0.5

    call process_character(si, appearance = "outfit nude pose armunder face flirt blush false")
    si.c "..."

    call process_character(n, appearance = "outfit swimsuit pose handsdown face embarrassed blush true")
    n.c "(H-Huh?!)"

    if finale_julia_sam:
        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handface face happy blush false")
        else:
            call process_character(sa, appearance = "outfit clothes pose handface face happy blush false")
        pause 0.5
        call character_leave_dissolve(sa)
        pause 0.5
        call process_character(sa, appearance = "outfit nude pose handface face happy blush false")
        pause 0.5

        call process_character(sa, appearance = "outfit nude pose handface face happy blush false")
        sa.c "Aw yeah, it begins!"

        if "julia_scene_swimsuit" in store.scenes_completed:
            call process_character(julia, appearance = "outfit swimsuit pose handup face aroused blush false")
        else:
            call process_character(julia, appearance = "outfit clothes pose handup face aroused blush false")
        pause 0.5
        call character_leave_dissolve(julia)
        pause 0.5
        call process_character(julia, appearance = "outfit nude pose handup face aroused blush false")
        pause 0.5
        call process_character(julia, appearance = "outfit nude pose handup face aroused blush false")
        julia.c "..."

    call process_character(janet, appearance = "outfit swimsuit pose handface face neutral blush false")
    pause 0.5
    call character_leave_dissolve(janet)
    pause 0.5
    call process_character(janet, appearance = "outfit nude pose handface face neutral blush false")
    pause 0.5

    call process_character(janet, appearance = "outfit nude pose handface face neutral blush false")
    janet.c "Your face is bright red [n.say_name]!"

    call process_character(janet, appearance = "outfit nude pose handface face happy blush false")
    janet.c "Are there too many cute girls around you?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    pause 0.5
    call character_leave_dissolve(edna)
    pause 0.5
    call process_character(edna, appearance = "outfit nude pose handhip face happy blush false mouth red")
    pause 0.5

    call process_character(edna, appearance = "outfit nude pose handhip face happy blush false mouth red")
    edna.c "There's a lot to look at, isn't there [n.say_name]?"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face embarrassed blush true")
    n.c "(T-They're all naked...)"

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face aroused blush true")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit_hard pose twohandfist face aroused blush true")
    n.c "(My whole family is naked in front of me!)"

    call process_character(k, appearance = "outfit nude pose handhip face flirt blush false")
    k.c "Are you connecting the dots in your head yet bro?"

    call process_character(k, appearance = "outfit nude pose handhip face flirt blush false")
    k.c "Your other head has figured it out already!"

    call process_character(n, appearance = "outfit swimsuit_hard pose handsdown face aroused blush true")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit_hard pose handsdown face aroused blush true")
    n.c "(What's going to happen with everyone here?)"

    call process_character(k, appearance = "outfit nude pose armsup face happy blush false")
    k.c "Quit ogling the tits and ass [n.say_name], and get that suit off!"

    call process_character(n, appearance = "outfit nudehard pose twohandfist face aroused blush true", show_bust = False)
    $ refresh_character(n, force_transition = Dissolve(1.0))
    call process_character(n, appearance = "outfit nudehard pose twohandfist face aroused blush true")
    n.c "Ah!"

    call process_character(k, appearance = "pose armcross face flirt blush false")
    k.c "Alright, who wants first dibs?"

    if finale_julia_sam:
        call process_character(sa, appearance = "pose leaning face neutral blush false")
        sa.c "Me, me, me!"

        call process_character(sa, appearance = "pose leaning face neutral blush false")
        sa.c "I want first dibs!"

    call process_character(edna, appearance = "pose handclasp face happy blush false")
    edna.c "Is seniority factored in to who goes first?"

    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "What about if you're head of the household?"

    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "Haha!"

    call process_character(janet, appearance = "pose handface face happy blush false")
    janet.c "Shall we draw straws?"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "W-Wait!"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "Do I get a say in this?"

    call process_character(k, appearance = "pose handhip face happy blush false")
    k.c "You want to choose yourself bro?"

    call process_character(k, appearance = "pose handhip face flirt blush false")
    k.c "I should have known, since you like to do that."

    call process_character(n, appearance = "pose behindhead face curious blush true")

    call process_character(edna, appearance = "pose handhip face neutral blush false")
    edna.c "That's fine with me."

    call process_character(edna, appearance = "pose handhip face happy blush false")
    edna.c "As long as I get my time in with my grandson!"

    if finale_julia_sam:
        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "Same!"

    call process_character(janet, appearance = "pose handchest face neutral blush false")
    janet.c "Whatever's easiest!"

    if finale_julia_sam:
        call process_character(julia, appearance = "pose handface face neutral blush false")
        julia.c "I don't care, either way."

    call process_character(si, appearance = "pose armunder face flirt blush false")
    si.c "Seems like there's a general agreement that you'll make the choice sweetie!"

    call process_character(k, appearance = "pose armsup face flirt blush false")
    k.c "Okay bro, you got a lot of options."

    call process_character(k, appearance = "pose armsup face flirt blush false")
    k.c "Hope you can pace yourself!"

    call process_character(n, appearance = "pose handsdown face curious blush true")
    n.c "..."

    call finale_scene_choices_impreg_override(dream = dream)

    return

# Vicky #
label vicky_scene_vaginal_sex_leftovers(dream = False):
    $ renpy.scene('screens')
    window hide
    show bg black
    with Dissolve(0.5)
    pause 0.5

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "...{p}...")
    call process_character(vicky, appearance = "", text = "(Developing a website is a lot more challenging than I realized)")
    call process_character(vicky, appearance = "", text = "(These pre-built layouts aren't what I'm looking for...)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(I may just have to learn how to design one myself)")
    call process_character(vicky, appearance = "", text = "(That's likely going to take a long time)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(I could hire someone to do the work for me...)")
    call process_character(vicky, appearance = "", text = "(That can get pricey though...)")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "{i}Sigh.{/i}..")
    call process_character(vicky, appearance = "", text = "(All of this planning and designing is overtaxing me)")
    call process_character(vicky, appearance = "", text = "(I need to decompress...)")
    call process_character(vicky, appearance = "", text = "...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "(I've been feeling horny since mid morning)")
    call process_character(vicky, appearance = "", text = "(It's been building up throughout the day)")
    call process_character(vicky, appearance = "", text = "...{p}...")
    call process_character(vicky, appearance = "", text = "(I think I should give [n.say_name] a call...)")

    $ store.current_background = ""
    call process_new_location(bg = nate_room)

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false", text = "...{p}...")

    "{i}Ding!{/i}"

    call process_character(n, appearance = "pose behindhead face neutral blush false", text = "(Sounds like I got a text...)")
    call process_character(n, appearance = "pose behindhead face happy blush false", text = "(It's from [vicky.say_name]!)")
    call process_character(vicky, appearance = "", text = "\"It would be great if you could stop by my place today.\"")
    call process_character(vicky, appearance = "", text = "\"We'll have a great time!\"")
    call process_character(n, appearance = "pose handpocket face neutral blush false", text = "...")
    call process_character(n, appearance = "pose handpocket face neutral blush false", text = "(We'll have a great time...)")
    call process_character(n, appearance = "pose handpocket face neutral blush false", text = "...")
    call process_character(n, appearance = "pose handpocket face happy blush false", text = "(I wonder if we're celebrating a milestone on the channel!)")
    call process_character(n, appearance = "pose twohandfist face happy blush false", text = "(I wouldn't want to miss out on that!)")
    call process_character(n, appearance = "pose twohandfist face happy blush false", text = "(I should let her know I'll be over)")
    call process_character(n, appearance = "pose twohandfist face happy blush false", text = "\"Cool!\"")
    call process_character(n, appearance = "pose twohandfist face happy blush false", text = "\"I'll be over in a few!\"")

    call fade_to_black(1)

    $ no_bust_art = True

    "{i}A little while later...{/i}"

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "Well, that was fast!")
    call process_character(vicky, appearance = "", text = "I must have timed my text message perfectly!")
    call process_character(n, appearance = "blush false", text = "You got me at just the right time!")
    call process_character(n, appearance = "blush false", text = "I was hanging around in my room back home.")
    call process_character(vicky, appearance = "", text = "Planning to play video games I presume?")
    call process_character(n, appearance = "blush false", text = "I was debating it, yeah.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "So you said we'll have a great time if I came over!")
    call process_character(n, appearance = "blush false", text = "Are we celebrating a milestone on the Twinsticks channel?")
    call process_character(n, appearance = "blush false", text = "Or are we going to make a porn video?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "I know normally whenever I ask you to come over it's business related one way or another.")
    call process_character(vicky, appearance = "", text = "You and I have been working our tails off recently.")
    call process_character(n, appearance = "blush false", text = "We sure have!")
    call process_character(n, appearance = "blush false", text = "I've never had such a busy summer before!")
    call process_character(vicky, appearance = "", text = "I could say the same myself.")
    call process_character(vicky, appearance = "", text = "I've worked quite a few late nights.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "Which is why I think we deserve a break for once.")
    call process_character(n, appearance = "blush false", text = "Yeah?")
    call process_character(vicky, appearance = "", text = "No one works as hard as we do [n.say_name].")
    call process_character(vicky, appearance = "", text = "We go above and beyond the average workload, because we want to succeed.")
    call process_character(vicky, appearance = "", text = "But even we need to unwind and relax once in a while.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "I do like the sound of that.")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "The mind and body does need its rest.")
    call process_character(vicky, appearance = "", text = "It's unhealthy to always be in work mode.")
    call process_character(vicky, appearance = "", text = "I mean think about how often we are in my office!")
    call process_character(n, appearance = "blush false", text = "We're in here pretty much all the time...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "Exactly!")
    call process_character(vicky, appearance = "", text = "So let's change things up!")
    call process_character(n, appearance = "blush false", text = "How?")
    call process_character(vicky, appearance = "", text = "Let's go to my bedroom.")
    call process_character(vicky, appearance = "", text = "I find it easy to relax and get comfortable in there.")
    call process_character(n, appearance = "blush false", text = "I've never even seen your bedroom.")
    call process_character(vicky, appearance = "", text = "All the more reason to go there then!")

    window hide
    show bg black
    with Dissolve(0.5)
    pause 0.5

    call process_character(vicky, appearance = "", text = "...")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(vicky, appearance = "", text = "Here it is!")
    call process_character(n, appearance = "blush false", text = "This is really nice [vicky.say_name]!")
    call process_character(n, appearance = "blush false", text = "It does feel relaxing in here!")
    call process_character(vicky, appearance = "", text = "See what I mean?")
    call process_character(vicky, appearance = "", text = "I needed a bedroom that could help me fall asleep quickly after long nights of working.")
    call process_character(n, appearance = "blush false", text = "I like the view you have too!")
    call process_character(n, appearance = "blush false", text = "I forgot how high up we are!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Why don't you try out my bed?")
    call process_character(vicky, appearance = "", text = "It's got a memory foam mattress.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "Ooh, this is nice!")
    call process_character(n, appearance = "blush false", text = "Super comfy!")
    call process_character(vicky, appearance = "", text = "They're expensive, but worth it if you want to sleep soundly.")
    call process_character(n, appearance = "blush false", text = "I should ask my Mom if she can get me one of these for my bed!")
    call process_character(vicky, appearance = "", text = "At the rate you're channel is going [n.say_name], you'll be able to buy one out of your own pocket!")
    call process_character(n, appearance = "blush false", text = "Hey, I probably could yeah!")
    call process_character(vicky, appearance = "", text = "...{p}...")
    call process_character(vicky, appearance = "", text = "(I can feel my nipples getting hard...)")
    call process_character(vicky, appearance = "", text = "(And I'm getting wet...)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(There hasn't been any action on this bed before)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(I figured it was going to stay that way before [n.say_name] came along...)")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "(Vicky's bed is way better than mine)")
    call process_character(n, appearance = "blush false", text = "(It makes me want to close my eyes for a while...)")
    call process_character(n, appearance = "blush false", text = "...{p}...")
    call process_character(n, appearance = "blush false", text = "{i}Oof!{/i}")
    call process_character(n, appearance = "blush false", text = "(Something heavy is on top of me...)")
    call process_character(vicky, appearance = "", text = "This bed is made for two you know.")
    call process_character(n, appearance = "blush false", text = "Why are you sitting on me Vicky?")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "A-Are you taking off my pants?")
    call process_character(vicky, appearance = "", text = "You won't need them.")
    call process_character(n, appearance = "blush false", text = "...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg vicky_onbed_clothed_soft")

    call process_character(vicky, appearance = "", text = "Very nice.")
    call process_character(vicky, appearance = "", text = "Now we're all set to fuck!")
    call process_character(n, appearance = "blush false", text = "F-Fuck?")
    call process_character(vicky, appearance = "", text = "Mhm, I'm going to sit on your cock!")
    call process_character(vicky, appearance = "", text = "I've been wondering what you would feel like in my pussy, and I'm ready to find out!")

    if stats.stat_value("times_had_vaginal_sex") > 0:
        call process_character(n, appearance = "blush false", text = "It should feel pretty good...")
        call process_character(vicky, appearance = "", text = "Ah, are you saying you know how to please a woman with your dick?")
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(n, appearance = "blush false", text = "I-I just know I've enjoyed it a lot before.")
    else:
        call process_character(n, appearance = "blush false", text = "T-That's what you mean by fuck?")
        call process_character(vicky, appearance = "", text = "It's alright if you don't know how to do it properly [n.say_name].")
        call process_character(vicky, appearance = "", text = "You'll catch on fast!")

    if "sam_scene_vaginal" in scenes_completed:
        call process_character(vicky, appearance = "", text = "Was it your sister [sa.say_name] that liked your cock?")
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(vicky, appearance = "", text = "I remember watching her facial expressions as you pounded her pussy.")
        call process_character(vicky, appearance = "", text = "She was enjoying every moment of it!")
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(n, appearance = "blush false", text = "[sa.say_name] never had experienced anything like that before.")
        call process_character(vicky, appearance = "", text = "She helped build my anticipation for your dick!")
        call process_character(vicky, appearance = "", text = "I hope it's more than just hype!")

    call static_still_ctc("bg_vicky_onbed_clothed_hard")

    call process_character(n, appearance = "blush false", text = "...")
    call process_character(vicky, appearance = "", text = "Do you feel my panties rubbing against your cock?")
    call process_character(vicky, appearance = "", text = "How is it [n.say_name]?")
    call process_character(n, appearance = "blush false", text = "Ooh...")
    call process_character(vicky, appearance = "", text = "Mmm, this is feeling good!")
    call process_character(vicky, appearance = "", text = "This is guaranteed to calm our nerves!")
    call process_character(vicky, appearance = "", text = "Already I'm feeling relief from the stress of today!")
    call process_character(n, appearance = "blush false", text = "That's good to hear.")
    call process_character(vicky, appearance = "", text = "Don't worry about writing a new review, or when your next livestream is...")
    call process_character(vicky, appearance = "", text = "Just enjoy this moment and clear your head.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(vicky, appearance = "", text = "Only think about my pussy lowering on your cock...")

    call static_still_ctc("bg vicky_onbed_clothed_pen")

    call process_character(vicky, appearance = "", text = "Yes, yes!")
    call process_character(vicky, appearance = "", text = "Your cock wanted to be in my pussy!")
    call process_character(n, appearance = "blush false", text = "Ah, [vicky.say_name]!")
    call process_character(n, appearance = "blush false", text = "You're so warm [vicky.say_name]!")
    call process_character(vicky, appearance = "", text = "It's just starting [n.say_name]!")
    call process_character(vicky, appearance = "", text = "We'll both be hot and sweaty before it's all over!")
    call process_character(n, appearance = "blush false", text = "Mmn!")
    call process_character(vicky, appearance = "", text = "It's...{w=1.0}it's so good!")
    call process_character(vicky, appearance = "", text = "Ooh!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "I need to adjust my stance...")
    call process_character(vicky, appearance = "", text = "Then I'll be able to get more motion going!")

    call static_still_ctc("bg vicky_vaginal_clothed")

    call process_character(n, appearance = "blush false", text = "Ah, ah!")
    call process_character(vicky, appearance = "", text = "Now I can ride your cock properly [n.say_name]!")
    call process_character(vicky, appearance = "", text = "I've got more balance this way!")
    call process_character(n, appearance = "blush false", text = "I-I see what you mean!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(It's incredible to think about the events leading up to this...)")
    call process_character(vicky, appearance = "", text = "(At first I really thought [n.say_name] was just some horny kid obsessed with big tits)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(Well, he is definitely obsessed with big tits...{w=1.0}but I didn't think he would be anything more than that)")
    call process_character(vicky, appearance = "", text = "(I figured he'd cop a feel and that may motivate him to develop a modest channel)")
    call process_character(vicky, appearance = "", text = "(But he continues to do a remarkable job with his channel)")
    call process_character(vicky, appearance = "", text = "(And he's doing remarkable things with me...)")
    call process_character(n, appearance = "blush false", text = "Ahn, {i}pant.{/i}..")
    call process_character(vicky, appearance = "", text = "(He's smart, intuitive, and already has great business sense)")
    call process_character(vicky, appearance = "", text = "(But he also has this charming innocence about him)")
    call process_character(vicky, appearance = "", text = "(And damn he's a good fuck!)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(I didn't think anyone could keep up with my lifestyle, but [n.say_name] does it in stride)")
    call process_character(vicky, appearance = "", text = "(He's making me question if I should stay single or not...)")
    call process_character(n, appearance = "blush false", text = "Haa!")
    call process_character(n, appearance = "blush false", text = "Hrm!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(I think [n.say_name] is one in a million, no...{w=0.5} one in a billion!")
    call process_character(vicky, appearance = "", text = "(I'll never meet someone who loves sexual pleasure as much as he does!)")
    call process_character(vicky, appearance = "", text = "...{p}...")
    call process_character(vicky, appearance = "", text = "How are you doing [n.say_name]?")
    call process_character(n, appearance = "blush false", text = "I-I'm doing great.")
    call process_character(vicky, appearance = "", text = "I wouldn't have tried this position unless we were on the bed.")
    call process_character(n, appearance = "blush false", text = "Ah, why's that?")
    call process_character(vicky, appearance = "", text = "Well for one, I'm putting a lot of weight on you.")
    call process_character(vicky, appearance = "", text = "On a soft bed, it's no problem because the mattress absorbs the impact.")
    call process_character(vicky, appearance = "", text = "If we were on a hard floor however...")
    call process_character(vicky, appearance = "", text = "I'd be knocking the wind out of you right now!")
    call process_character(n, appearance = "blush false", text = "I don't think I would have liked that...")
    call process_character(vicky, appearance = "", text = "No, definitely not.")
    call process_character(vicky, appearance = "", text = "Aah, yeah...")
    call process_character(n, appearance = "blush false", text = "Mm!")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "H-How's your website coming along?")
    call process_character(vicky, appearance = "", text = "Thanks for asking.")
    call process_character(vicky, appearance = "", text = "It's been coming along, but slower than I would like.")
    call process_character(n, appearance = "blush false", text = "How come?")
    call process_character(vicky, appearance = "", text = "I think I've just been looking at the big picture too much, and it makes me hit a brick wall.")
    call process_character(vicky, appearance = "", text = "It's better to turn a big project into small, bite size segments.")
    call process_character(vicky, appearance = "", text = "That's how I need to approach this website.")
    call process_character(n, appearance = "blush false", text = "I handle my reviews in a similar way.")
    call process_character(n, appearance = "blush false", text = "I split it up into smaller sections, and it becomes way easier to write!")
    call process_character(vicky, appearance = "", text = "It's a very good mindset to keep.")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Ah, yes, yes!")
    call process_character(vicky, appearance = "", text = "Haha, listen to us!")
    call process_character(vicky, appearance = "", text = "We're supposed to be fucking, and yet we're talking about project management!")
    call process_character(vicky, appearance = "", text = "But you know...")
    call process_character(vicky, appearance = "", text = "Having sex has made me re-think my work method.")
    call process_character(vicky, appearance = "", text = "I feel like I can tackle that website much more effectively now!")
    call process_character(n, appearance = "blush false", text = "That's awesome [vicky.say_name]!")
    call process_character(n, appearance = "blush false", text = "You always figure that kind of stuff out!")
    call process_character(vicky, appearance = "", text = "I'm able to discover solutions faster when you're around [n.say_name].")
    call process_character(vicky, appearance = "", text = "You just have that aura of motivation.")
    call process_character(n, appearance = "blush false", text = "My aura of what now?")
    call process_character(vicky, appearance = "", text = "We can talk about those things later...")
    call process_character(vicky, appearance = "", text = "What I want to do right now, is make us have a dual orgasm.")
    call process_character(n, appearance = "blush false", text = "A dual orgasm?")
    call process_character(vicky, appearance = "", text = "Meaning we both come at the same time.")
    call process_character(n, appearance = "blush false", text = "Oh, nice.")
    call process_character(n, appearance = "blush false", text = "Are we gonna try to get it via the way we're fucking now?")
    call process_character(vicky, appearance = "", text = "We need to do something more potent to trigger a dual orgasm.")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "I think I know what we can try.")
    call process_character(n, appearance = "blush false", text = "What have you thought of?")
    call process_character(vicky, appearance = "", text = "Let me see here...")

    call fade_to_black(1)

    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Alright, I'll move down this way...")
    call process_character(vicky, appearance = "", text = "And you go like this...")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(vicky, appearance = "", text = "Alright, now you have to move your legs back...")
    call process_character(n, appearance = "blush false", text = "W-Whoa!")
    call process_character(n, appearance = "blush false", text = "I have to bend them back this far?")
    call process_character(vicky, appearance = "", text = "It'll be worth it [n.say_name]!")

    call static_still_ctc("bg vicky_matingpress_clothed")

    call process_character(n, appearance = "blush false", text = "Haaahn!")
    call process_character(vicky, appearance = "", text = "Ooh! It's working!")
    call process_character(vicky, appearance = "", text = "It's working fantastic [n.say_name]!")
    call process_character(n, appearance = "blush false", text = "Gah, ah!")
    call process_character(n, appearance = "blush false", text = "M-My feet are practically up at my head!")
    call process_character(vicky, appearance = "", text = "But can you feel the ecstasy from this?!")
    call process_character(vicky, appearance = "", text = "The way your cock fits into my pussy is, {i}gasp!{/i}")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "(I never knew my legs could bend back this far!)")
    call process_character(n, appearance = "blush false", text = "(I hope they don't get stuck like this!)")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "(It's true what [vicky.say_name] is saying though...)")
    call process_character(n, appearance = "blush false", text = "Gaah!")
    call process_character(n, appearance = "blush false", text = "(My dick feels a super strong sensation from this!)")
    call process_character(n, appearance = "blush false", text = "(It's like my penis is burning, but it doesn't hurt)")
    call process_character(n, appearance = "blush false", text = "(Instead it just feels amazing!)")
    call process_character(n, appearance = "blush false", text = "Hrm!")
    call process_character(vicky, appearance = "", text = "Mmn!")
    call process_character(vicky, appearance = "", text = "([n.say_name]'s cock is bumping my g-spot every few seconds!)")
    call process_character(vicky, appearance = "", text = "{i}Gasp!{/i}")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(I consider my sex endurance to be above average but...)")
    call process_character(vicky, appearance = "", text = "(This is testing my limits!)")
    call process_character(vicky, appearance = "", text = "(I can't imagine what [n.say_name] is feeling)")
    call process_character(vicky, appearance = "", text = "(It's inevitable he will come)")
    call process_character(n, appearance = "blush false", text = "Haa, aah...")
    call process_character(n, appearance = "blush false", text = "[vicky.say_name]...")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "I can't keep going.")
    call process_character(n, appearance = "blush false", text = "I'm ready to explode!")
    call process_character(vicky, appearance = "", text = "I share the same sentiment!")
    call process_character(vicky, appearance = "", text = "We're both pushed to our extremes!")
    call process_character(n, appearance = "blush false", text = "Mm, Mmm!")
    call process_character(vicky, appearance = "", text = "I'm coming [n.say_name]!")
    call process_character(vicky, appearance = "", text = "Let's mix our bodily fluids!")
    "[n.say_name] & Vicky" "Aaah!!"

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc("bg vicky_matingpress_clothed_cum")

    call process_character(n, appearance = "blush false", text = "Nng, Nng!")
    call process_character(vicky, appearance = "", text = "(Oh shit, what an orgasm!)")
    call process_character(vicky, appearance = "", text = "(That coupled with [n.say_name]'s ejaculation...)")
    call process_character(n, appearance = "blush false", text = "{i}Sigh.{/i}..")

    call static_still_ctc("bg vicky_matingpress_clothed_cum_impreg")

    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Wasn't that position worth it [n.say_name]?")
    call process_character(vicky, appearance = "", text = "You must feel good about stopping by today huh?")
    call process_character(n, appearance = "blush false", text = "Mm...")
    call process_character(n, appearance = "blush false", text = "Mhm...")
    call process_character(vicky, appearance = "", text = "We both needed this.")
    call process_character(vicky, appearance = "", text = "Having an orgasm like that flushes away anxiety.")
    call process_character(vicky, appearance = "", text = "I feel I can focus much more now than I've been able to!")
    call process_character(vicky, appearance = "", text = "You feel the same way [n.say_name]?")
    call process_character(n, appearance = "blush false", text = "Hm?")
    call process_character(n, appearance = "blush false", text = "Yeah...")
    call process_character(n, appearance = "blush false", text = "I feel focused...{w=1.0}too...")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "Zzz...")
    call process_character(vicky, appearance = "", text = "(He conked right out...)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "{i}Yawn.{/i}..")
    call process_character(vicky, appearance = "", text = "(I could use a power nap myself...)")

    python:
        vicky.revistable_scenes.add("vicky_scene_vaginal_revisit")

        if not dream:
            minigame_typing_money_earned_since_last_vicky_meeting = 0
            minigame_typing_times_succeeded_since_last_vicky_meeting = 0

            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene("vicky_scene_vaginal", char = vicky, dream = dream)

    return

label vicky_scene_anal_sex_leftovers(dream = False):
    call process_scene_beginning(bg = "bg nate_room_daytime", dream = dream)
    call process_character(n, appearance = "outfit underwear pose handsdown face aroused blush false", text = "...{p}...")
    call process_character(n, appearance = "outfit underwear pose behindhead face curious blush false", text = "(Hm?)")
    call process_character(n, appearance = "outfit underwear pose behindhead face curious blush false", text = "(I got text messages this early in the morning?)")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "(The only person I know who would do that is...)")
    call process_character(n, appearance = "outfit underwear pose handfist face happy blush false", text = "([vicky.say_name], I thought so!)")
    call process_character(n, appearance = "outfit underwear pose handfist face happy blush false", text = "...")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "\"[n.say_name] I have fantastic news!\"")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "\"My website is now complete, and is nearly ready for launch!\"")
    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false", text = "(She finally got her website done!)")
    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false", text = "([vicky.say_name]'s been working on that for a long time)")
    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false", text = "...")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "(Looks like she sent me a few more messages...)")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "\"I'd like you and I to record a welcome message for the website\"")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "\"I want to intrigue visitors to join, and a welcome message is a perfect way to attract interest!\"")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "\"If you can stop by very soon that would be great.\"")
    call process_character(n, appearance = "outfit underwear pose behindhead face happy blush false", text = "(That's a smart idea recording a video that introduces what's on the website!)")
    call process_character(n, appearance = "outfit underwear pose behindhead face happy blush false", text = "([sa.say_name] and I should do the same thing for our ReflexViz channel!)")
    call process_character(n, appearance = "outfit underwear pose handfist face neutral blush false", text = "(I bet we could nab extra subscribers by doing that!)")
    call process_character(n, appearance = "outfit underwear pose handfist face neutral blush false", text = "...")

    call character_leave_dissolve(n)
    pause 0.5

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face happy blush false", text = "(I'll let [vicky.say_name] know I can go to her office today!)")
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face happy blush false", text = "\"Hi [vicky.say_name], that's awesome to hear about the website!\"")
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face happy blush false", text = "\"I can come over today if you want.\"")
    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false", text = "(And sent!)")
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false", text = "...{p}...")
    "{i}Ding!{/i}"
    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false", text = "(Wow, that's a fast response...)")
    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false", text = "...")
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false", text = "\"Excellent!\"")
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false", text = "\"I'm setting up the camera for the recording right now.\"")
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face happy blush false", text = "\"Everything will be ready by the time you get here!\"")

    call fade_to_black(1)
    $ no_bust_art = True

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "I've been looking forward to this day [n.say_name].")
    call process_character(vicky, appearance = "", text = "Getting this website completed is a big step forward.")
    call process_character(n, appearance = "blush false", text = "You were able to do it all on your own too!")
    call process_character(n, appearance = "blush false", text = "I wouldn't know the first thing about website design.")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "It's not so bad if you have the time to learn it.")
    call process_character(vicky, appearance = "", text = "Fortunately since I work primarily at home, I was able to compile numerous resources on website design and management.")
    call process_character(vicky, appearance = "", text = "It's a constant challenge to maintain an expanding website like mine, but I like that there is always a way to make improvements.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "The payoff for a well designed website is massive.")
    call process_character(vicky, appearance = "", text = "Giving visitors an all in one portal for high quality pornography is a big draw.")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        call process_character(n, appearance = "blush false", text = "I know my sister [sa.say_name] will really like that!")
        call process_character(vicky, appearance = "", text = "I'm sure she will!")
        call process_character(vicky, appearance = "", text = "No need for her to waste time trying to browse everywhere, because it will all be right here!")
    else:
        call process_character(n, appearance = "blush false", text = "I'm sure people will really like that!")
        call process_character(vicky, appearance = "", text = "I know they will!")
        call process_character(vicky, appearance = "", text = "No need for them to waste time trying to find the right video, because it will all be right here!")

    call process_character(n, appearance = "blush false", text = "I can't wait to record this welcome message for the website!")
    call process_character(n, appearance = "blush false", text = "Are you going to post it everywhere?")
    call process_character(vicky, appearance = "", text = "It's going to be distributed to every major social media platform, yes.")
    call process_character(vicky, appearance = "", text = "All it will take is a little bit of a interest to grow, and it will snowball from there!")
    call process_character(n, appearance = "blush false", text = "Where are we going to record the video?")
    call process_character(vicky, appearance = "", text = "Right here in the office.")
    call process_character(vicky, appearance = "", text = "I've got all the camera angles in place!")
    call process_character(n, appearance = "blush false", text = "There's more than one camera?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "It will be necessary for the video.")
    call process_character(vicky, appearance = "", text = "There needs to be a professional look.")
    call process_character(vicky, appearance = "", text = "Having one viewing angle is rather bland.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "It's vital whoever watches the video doesn't miss any of the action!")
    call process_character(n, appearance = "blush false", text = "Action?")
    call process_character(n, appearance = "blush false", text = "But I thought we were just going to introduce the website and talk about it.")
    call process_character(vicky, appearance = "", text = "Oh, we are.")
    call process_character(vicky, appearance = "", text = "But we need to keep their attention for the duration of the video.")

    call static_still_ctc("bg vicky_sit_tease")

    call process_character(vicky, appearance = "", text = "And given the subject matter of our website...")
    call process_character(vicky, appearance = "", text = "I think our course of action is obvious.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "We're going to fuck and talk about the website at the same time?")
    call process_character(vicky, appearance = "", text = "I'll handle most of the talking.")
    call process_character(vicky, appearance = "", text = "But feel free if you want to chime in during it.")
    call process_character(vicky, appearance = "", text = "In your case however, actions will speak louder than words, hehe...")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(n, appearance = "blush false", text = "(Good thing I've gotten used to fucking [sa.say_name] while other people watch online...)")
        call process_character(n, appearance = "blush false", text = "(This is essentially the same thing)")
    else:
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(n, appearance = "blush false", text = "(So a lot of people might watch this video online)")
        call process_character(n, appearance = "blush false", text = "(I hope I don't get too nervous while recording...)")

    call process_character(vicky, appearance = "", text = "You all set to begin?")
    call process_character(vicky, appearance = "", text = "We'll have to do this in one take, but I can always edit out any mistakes.")
    call process_character(vicky, appearance = "", text = "Or maybe it would make the video more authentic to keep them...")
    call process_character(n, appearance = "blush false", text = "Yeah, I'm ready to start the recording!")
    call process_character(vicky, appearance = "", text = "Let me make sure all the cameras are recording!")

    call fade_to_black(1)

    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "That camera is set...")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "This one is too...")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Okay, cameras are rolling!")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "Why are you clearing off your desk [vicky.say_name]?")
    call process_character(vicky, appearance = "", text = "To make room for us.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "Does that mean...")
    call process_character(vicky, appearance = "", text = "It's time to show your stuff [n.say_name]!")
    call process_character(vicky, appearance = "", text = "I'm bent over and prepped for your cock!")
    call process_character(n, appearance = "blush false", text = "But I can't quite reach...")
    call process_character(n, appearance = "blush false", text = "You're taller than me.")
    call process_character(vicky, appearance = "", text = "Roll my office chair behind me so you can prop yourself up!")
    call process_character(n, appearance = "blush false", text = "Oh yeah!")
    call process_character(n, appearance = "blush false", text = "Good idea.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "There, now you're at the perfect height!")
    call process_character(n, appearance = "blush false", text = "I'm actually a little too high up.")
    call process_character(n, appearance = "blush false", text = "I'd have to bend down to fuck your pussy.")
    call process_character(n, appearance = "blush false", text = "Should I lower the chair or...")
    call process_character(vicky, appearance = "", text = "What about my asshole?")
    call process_character(vicky, appearance = "", text = "Are you at the right height for that?")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "Yeah...{w=1.0} my penis is pointing directly at it.")
    call process_character(vicky, appearance = "", text = "Then I think that's where you should go!")

    call static_still_ctc("bg vicky_anal_probe")

    if stats.stat_value("times_given_anal_sex") > 0:
        call process_character(n, appearance = "blush false", text = "Really, I can?")
        call process_character(vicky, appearance = "", text = "My ass is all yours.")
        call process_character(vicky, appearance = "", text = "Unless you feel you wouldn't like it...")
        call process_character(n, appearance = "blush false", text = "No, I'd like to do it!")
        call process_character(n, appearance = "blush false", text = "I haven't had the chance to fuck your ass [vicky.say_name]!")
        call process_character(vicky, appearance = "", text = "You sound excited by how firm that decision was!")
        call process_character(vicky, appearance = "", text = "Now I'm intrigued!")
        call process_character(vicky, appearance = "", text = "Show my ass a good time [n.say_name]!")
    else:
        call process_character(n, appearance = "blush false", text = "R-Really?")
        call process_character(vicky, appearance = "", text = "My ass is all yours.")
        call process_character(vicky, appearance = "", text = "Unless you feel you wouldn't like it...")
        call process_character(n, appearance = "blush false", text = "I've never fucked there before...")
        call process_character(vicky, appearance = "", text = "Well now you can give it a try!")
        call process_character(vicky, appearance = "", text = "In my opinion, you'll have a good time.")
        call process_character(vicky, appearance = "", text = "It may be a little tight, but the feeling from it is...")
        call process_character(vicky, appearance = "", text = "You'll know the moment you push in!")


    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "Okay, here I go!")
    call process_character(vicky, appearance = "", text = "Make sure you can get it in all the way!")
    call process_character(vicky, appearance = "", text = "Mount me if that will help!")
    call process_character(n, appearance = "blush false", text = "Ah...")
    call process_character(n, appearance = "blush false", text = "It's sliding into your ass [vicky.say_name]!")

    call static_still_ctc("bg vicky_anal_behind")

    call process_character(vicky, appearance = "", text = "Oh yeah [n.say_name]!")
    call process_character(vicky, appearance = "", text = "My ass is taking all of your dick!")
    call process_character(vicky, appearance = "", text = "Start thrusting your body!")
    call process_character(n, appearance = "blush false", text = "Alright!")
    call process_character(n, appearance = "blush false", text = "Mm, Mmn!")
    call process_character(n, appearance = "blush false", text = "How's that [vicky.say_name]?")
    call process_character(vicky, appearance = "", text = "Yes!")
    call process_character(vicky, appearance = "", text = "That's what I want [n.say_name]!")
    call process_character(vicky, appearance = "", text = "Drive your cock into me!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(Now I'm wondering if I can keep my composure for my website introduction!)")
    call process_character(vicky, appearance = "", text = "([n.say_name] isn't going to stop pounding my ass anytime soon...)")
    call process_character(vicky, appearance = "", text = "(And I don't want him to!)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(I don't think I'll be able to follow my rehearsed script)")
    call process_character(vicky, appearance = "", text = "(I'll just go off the cuff, and do the best I can!)")

    call static_still_ctc("bg vicky_anal_shirt")

    call process_character(n, appearance = "blush false", text = "{i}Pant.{/i}..")
    call process_character(n, appearance = "blush false", text = "Hoo, ah...")
    call process_character(vicky, appearance = "", text = "I'm going to start the welcome message [n.say_name].")
    call process_character(n, appearance = "blush false", text = "G-Got it.")
    call process_character(vicky, appearance = "", text = "{i}Ahem.{/i}..")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Hi there, and welcome to...{w=0.5}ah, [vicky.say_name]'s Empornium!")
    call process_character(n, appearance = "blush false", text = "I like that!")
    call process_character(n, appearance = "blush false", text = "Empornium!")
    call process_character(vicky, appearance = "", text = "Haha, [n.say_name] {i}shh!{/i}")
    call process_character(vicky, appearance = "", text = "Keep the candid comments to a minimum for now.")
    call process_character(vicky, appearance = "", text = "I'll let you know when you can speak.")
    call process_character(n, appearance = "blush false", text = "Oh, right!")
    call process_character(n, appearance = "blush false", text = "Sorry [vicky.say_name]!")
    call process_character(n, appearance = "blush false", text = "Why don't you start again?")
    call process_character(n, appearance = "blush false", text = "I'll stay quiet.")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Hi there, and welcome to my website, [vicky.say_name]'s Empornium!")
    call process_character(vicky, appearance = "", text = "You're very lucky to have...{w=1.0}oh, stopped by!")
    call process_character(vicky, appearance = "", text = "I'm building a vast video library containing only the very best adult content for your viewing pleasure!")
    call process_character(n, appearance = "blush false", text = "([vicky.say_name]'s doing a great job promoting the site!)")
    call process_character(vicky, appearance = "", text = "On top of that you'll get to see me, [vicky.say_name], and the original content I'll produce exclusively for the Empornium!")
    call process_character(vicky, appearance = "", text = "Aah...{w=1.0} as a special preview, you're watching one of my videos right now!")
    call process_character(vicky, appearance = "", text = "The young man taking me from behind is the very talented [n.say_name]!")
    call process_character(n, appearance = "blush false", text = "Hrm, ah...")
    call process_character(vicky, appearance = "", text = "Together, [n.say_name] and I will be delivering the kind of porn you want to watch!")
    call process_character(vicky, appearance = "", text = "Register now as an early adopter, and receive a special discount for a lifetime membership!")
    call process_character(vicky, appearance = "", text = "[n.say_name], would you like to say anything?")

    call static_still_ctc("bg vicky_anal_shirtpull")

    call process_character(n, appearance = "blush false", text = "{i}Pant,{/i} {i}pant.{/i}..")
    call process_character(n, appearance = "blush false", text = "I love fucking [vicky.say_name]!")
    call process_character(vicky, appearance = "", text = "[n.say_name] sure does...")
    call process_character(vicky, appearance = "", text = "And you watching will fucking love [vicky.say_name]'s Empornium!")
    call process_character(vicky, appearance = "", text = "Mmn!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "And cut!")
    call process_character(n, appearance = "blush false", text = "The message is done?")
    call process_character(vicky, appearance = "", text = "It's all done!")
    call process_character(vicky, appearance = "", text = "Did I make sense when I was talking?")
    call process_character(n, appearance = "blush false", text = "I-I thought you did great!")
    call process_character(vicky, appearance = "", text = "That's encouraging!")
    call process_character(vicky, appearance = "", text = "It's tough to concentrate when your...{w=0.5}ah, ass is getting plowed!")
    call process_character(n, appearance = "blush false", text = "Y-yeah...{w=1.0}I can barely focus when I'm doing this.")
    call process_character(n, appearance = "blush false", text = "That's why I couldn't think of much to say.")
    call process_character(vicky, appearance = "", text = "It's all good.")
    call process_character(vicky, appearance = "", text = "This will be a strong welcome message video to launch with the site!")
    call process_character(n, appearance = "blush false", text = "D-Do we have to stop fucking now since you've said everything?")
    call process_character(vicky, appearance = "", text = "No way!")
    call process_character(vicky, appearance = "", text = "I'd never stop cold turkey, that's just mean!")
    call process_character(vicky, appearance = "", text = "We're going all the way to the climax!")
    call process_character(vicky, appearance = "", text = "It will make for some great b-roll and extra footage!")
    call process_character(n, appearance = "blush false", text = "(Yes!)")
    call process_character(n, appearance = "blush false", text = "(We'll keep going!)")

    call static_still_ctc("bg vicky_anal_fuck")

    call process_character(vicky, appearance = "", text = "Oh, oh!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "([n.say_name]'s getting into it now!)")
    call process_character(vicky, appearance = "", text = "(He's very happy we're continuing!)")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(His hips are slamming against my butt)")
    call process_character(vicky, appearance = "", text = "Yes, ah!")
    call process_character(vicky, appearance = "", text = "(My desk is shaking back and forth!)")
    call process_character(n, appearance = "blush false", text = "Mmf...")
    call process_character(n, appearance = "blush false", text = "(I can't help but fuck [vicky.say_name] as fast as I can!)")
    call process_character(n, appearance = "blush false", text = "(Her ass is tightening on my dick!)")
    call process_character(n, appearance = "blush false", text = "(The squeezing is intense!)")
    call process_character(vicky, appearance = "", text = "Aah yeah, [n.say_name]...")
    call process_character(vicky, appearance = "", text = "We're going to make great videos together.")
    call process_character(vicky, appearance = "", text = "[vicky.say_name]'s Empornium will be a huge success, I just know it!")
    call process_character(vicky, appearance = "", text = "We'll reach a level of quality that no competitor will be able to rival.")
    call process_character(vicky, appearance = "", text = "There's a bright business future ahead of you [n.say_name].")
    call process_character(vicky, appearance = "", text = "You'll get to fuck and earn a buck...")
    call process_character(vicky, appearance = "", text = "It's the perfect job for you [n.say_name]!")
    call process_character(n, appearance = "blush false", text = "T-That does sound perfect...")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "I can't wait to do more of this [vicky.say_name].")
    call process_character(vicky, appearance = "", text = "There's plenty for us to work on.")
    call process_character(vicky, appearance = "", text = "We'll be at this for a long time.")
    call process_character(n, appearance = "blush false", text = "{i}Pant,{/i} {i}pant.{/i}..")
    call process_character(n, appearance = "blush false", text = "I want to try everything!")
    call process_character(n, appearance = "blush false", text = "As long as it feels like this!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(He's letting the sex dictate most of his thoughts right now...)")
    call process_character(vicky, appearance = "", text = "(But I don't doubt he's being sincere)")
    call process_character(n, appearance = "blush false", text = "Haah!")
    call process_character(n, appearance = "blush false", text = "I'm gonna come [vicky.say_name], I'm gonna come!")
    call process_character(vicky, appearance = "", text = "That's the all important money shot [n.say_name]!")
    call process_character(vicky, appearance = "", text = "The spotlight is on you!")
    call process_character(n, appearance = "blush false", text = "Hrrm!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc("bg vicky_anal_behind_cum")

    call process_character(vicky, appearance = "", text = "Oooh!")
    call process_character(vicky, appearance = "", text = "(My fingers are curling!)")
    call process_character(vicky, appearance = "", text = "(And my legs are shaking!)")
    call process_character(n, appearance = "blush false", text = "Uh, uhn!")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "{i}Sigh.{/i}..")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Only you can cause me to orgasm like that [n.say_name].")
    call process_character(vicky, appearance = "", text = "I don't know how you do it, but you can really give it to a woman.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "I'm not sure I know either...")
    call process_character(vicky, appearance = "", text = "All that's important is the end result.")
    call process_character(n, appearance = "blush false", text = "How do you feel about the video?")
    call process_character(vicky, appearance = "", text = "We couldn't have done it better.")
    call process_character(vicky, appearance = "", text = "I'm very confident this will be a home run for the website!")
    call process_character(vicky, appearance = "", text = "The video needs a bit of editing and polish, and after that it will be finalized!")
    call process_character(n, appearance = "blush false", text = "Sweet!")
    call process_character(n, appearance = "blush false", text = "Can you send it to me once it's done?")
    call process_character(vicky, appearance = "", text = "I'll be more than happy to!")
    call process_character(vicky, appearance = "", text = "I can't wait to see how we look on camera from all the perspectives!")

    python:
        vicky.revistable_scenes.add("vicky_scene_anal_revisit")

        if not dream:
            minigame_typing_money_earned_since_last_vicky_meeting = 0
            minigame_typing_times_succeeded_since_last_vicky_meeting = 0

            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_butt", 1)
            stats.add_stat("times_seen_butthole", 1)
            stats.add_stat("times_given_anal_sex", 1)
            stats.add_stat("times_given_anal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene("vicky_scene_anal", char = vicky, dream = dream)

    return