## For those wondering what this file is.. ##
## This serves as a way of fixing existing bugs or smaller issues seen in the last versions of the game (v1.2) ##
## It mainly covers bug-fixing, but it also makes small tweaks to some scenes such as including conditionals to dialogue where it previously wasn't before. ##
## See the list below for more info. ##

## This file is already included in Leftovers, so please do not have this file twice!! ##

## List ##
#1 Ability to rename Julia during her intro, as well as Kacey and Vicky (currently cant do this in the base game)
#2 Janet's intro should take place downstairs and not in Nate's room so everyone's not in Nate's room (lol)
#3 Conditional for if you've done the racing minigame with Kira during Janet's intro
#4 Fix Nate changing back his clothes (for instance if he's naked) when you reached the "scene limit"/revisit scene limit for the day with a character, such as Nate saying "Maybe I can do that tomorrow?". Also applies to a check with Nate not having enough Boldness, i.e. "I don't know if I'm ready for that yet"
#5 Conditional for Kira's convo where she mentions people training one "muscle" over and over.
#6 The stream with Sam/Nate will now give money the second time they stream.
#7 Fixed Nate sleeping in his underwear still if the player has fucked everyone at home.

# Will be covered by DrX in a future update for IA:
# Extended list for triggering the first masturbation.
# Much more conditionals!

init 300 python:
    config.label_overrides["julia_arrival"] = "julia_arrival_rename"
    config.label_overrides["gloryhole_handjob_scene_sex"] = "gloryhole_handjob_scene_sex_rename"
    config.label_overrides["vicky_intro"] = "vicky_intro_rename"
    config.label_overrides["janet_intro"] = "janet_intro_misc"

## Julia Rename ##
label julia_arrival_rename:
    $ nate_room.decide_and_play_daily_music_queue()

    python hide:
        for char in character_list():
            char.position = "right"

    call process_scene_beginning(bg = "bg hallway_daytime")
    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "(I wonder if [julia.say_name] has arrived yet...)"
    si.c "[n.say_name]!"
    si.c "Come on downstairs!"

    call process_new_location(bg = living_room)

    call process_character(si, appearance = "pose handsup face neutral blush false position right")
    si.c "[julia.say_name] is here!"

    call character_leave_dissolve(si)
    pause 0.5

    call process_character(julia, appearance = "pose handface face neutral blush false", show_bust = False)
    $ refresh_character(julia, force_transition = Dissolve(0.75))
    pause 0.75
    call change_character_name(julia, prompt = _("Cousin's name"))

    $ display_multiple_characters([ (julia, "outfit clothes pose handface face neutral blush false"), (n, "outfit clothes pose handpocket face neutral blush false") ])

    call process_character(n, appearance = "pose handpocket face happy blush false position right")
    n.c "Hey [julia.say_name]!"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "Hey."

    call character_leave_dissolve(n)
    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "So you'll have the couch to sleep on while you stay here [julia.say_name]."

    call process_character(si, appearance = "pose handsfront face neutral blush false")
    si.c "I've provided some pillows and blankets for you."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "..."

    call process_character(si, appearance = "pose handsup face neutral blush false")
    si.c "I actually have to head out."

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "[n.say_name], why don't you show [julia.say_name] around the house?"

    call process_character(si, appearance = "pose armunder face neutral blush false")
    si.c "Help her get familiar with things."

    call character_leave_dissolve(si)
    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Okay Mom!"

    call character_leave_dissolve(n)
    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "I'll see you two later!"

    $ clear_characters()

    $ display_multiple_characters([ (julia, "pose handface face neutral blush false"), (n, "pose handpocket face neutral blush false position right") ])

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "..."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Okay, so let me give you a tour!"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "..."

    call process_new_location(bg = kitchen, char_tuple_array = [ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (julia, "outfit clothes pose handup face neutral blush false")] )

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "So here's the kitchen!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "There's plenty of snacks in the cabinets."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "..."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "My Mom grows and stores a lot of vegetables for us."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "I'm personally more of a fan of fruits."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "..."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "I keep some of my favorite cereals in the back."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "If [k.say_name] finds them, she'll eat all of it."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Shouldn't she buy her own cereal to eat?"

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "That's a good point..."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Well, we buy cereal frequently."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "So usually there's some available."

    call process_new_location(bg = backyard, char_tuple_array = [(julia, "pose handface face neutral blush false"), (n, "pose twohandfist face neutral blush false")] )

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Now this..."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "This is the best part of the house in my opinion!"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "We got a big pool we can swim in all the time."

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "Provided it's warm enough outside."

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "So you could be out here the whole day practically!"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I burn easily."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "We got plenty of sunscreen on hand."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "My Mom always tells me to put it on."

    call process_character(n, appearance = "pose behindhead face happy blush false")
    n.c "I haven't gotten burned yet!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "..."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Alright, let's go back inside, and I'll show you the rest of the house."

    call process_new_location(bg = hallway, char_tuple_array = [(julia, "pose armcross face neutral blush false"), (n, "pose handpocket face neutral blush false")] )

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Up here is where my room is, along with [sa.say_name] and..."

    call character_leave_dissolve(n)
    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false position right")
    k.c "Sup [n.say_name]."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Oh hey [julia.say_name]!"

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "Did you just get here?"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "Yeah."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "[n.say_name]'s showing you around I take it?"

    call character_leave_dissolve(k)
    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Yep!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "I'm giving her the tour of the house."

    call character_leave_dissolve(n)
    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "What do you think so far [julia.say_name]?"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "It's nice."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "You should check out our bathroom when you get a chance."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "It's got all the bells and whistles you can think of!"

    call character_leave_dissolve(k)
    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Yeah!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "I like using it."

    if "simone_scene_1_seq_1" in scenes_completed:
        call character_leave_dissolve(n)
        k.c "[n.say_name] likes spending extra time in there."

        call process_character(k, appearance = "pose armcross face happy blush false")
        k.c "It's why we need a lot of tissue paper."

        call character_leave_dissolve(k)
        call process_character(n, appearance = "pose behindhead face embarrassed blush false")
        n.c "..."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "..."

    call character_leave_dissolve(n)
    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "I'll let [n.say_name] finish showing you around the house."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "I have to clean up after my cardio routine."

    call character_leave_dissolve(k)
    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "[k.say_name] does a lot of exercises."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "That's why she's in really good shape."

    call character_leave_dissolve(n)
    call process_character(k, appearance = "pose armsup face happy blush false")
    k.c "These muscles won't build themselves!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "..."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "Anyway, I'll chat with you two later."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "See ya."

    call character_leave_dissolve(k)
    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Alright, it's on to my room!"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "..."

    call process_new_location(bg = nate_room, char_tuple_array = [(julia, "pose handface face neutral blush false"), (n, "pose handfist face happy blush false")] )

    call process_character(julia, appearance = "pose handface face neutral blush false")
    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "And here it is!"

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Before this house, [sa.say_name] and I shared a room."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "Yeah, I remember."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "I usually hang out in [sa.say_name]'s room a lot to be honest."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "All the video games are in there."

    call process_character(n, appearance = "pose behindhead face happy blush false")
    n.c "Oh!"

    call process_character(n, appearance = "pose behindhead face happy blush false")
    n.c "Speaking of which!"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "[sa.say_name] and I have our own streaming channel!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "And we also review video games and shows."

    call process_character(julia, appearance = "pose handface face happy blush false")
    julia.c "That's cool."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "We were thinking you could join us as a guest on our next stream!"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "[sa.say_name] and I went through our game collection..."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "{cps=40}And we found some great choices so all of us could-{/cps}{w=0.75}{nw}"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I'm not really into video games."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Oh..."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "And I'd rather not appear on a stream."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "That's okay."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "{cps=40}You can always watch us when we're live to see how it-{/cps}{w=0.75}{nw}"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I'm good."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "Thanks for showing me around the house."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "No problem!"

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "So what would you like to do then?"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "[sa.say_name] and I have the whole day free!"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "Actually, I was just gonna go downstairs and read for a while."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Oh..."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "Alright."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "You gonna read some comic books?"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "No, I'm reading a novel."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "Oh yeah?"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "We could take turns narrating it!"

    call process_character(julia, appearance = "pose handface face curious blush false")
    julia.c "I think that would take a while."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "Can't be too bad."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "How long is the novel?"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Six hundred pages."

    call process_character(n, appearance = "pose behindhead face embarrassed blush false")
    n.c "Six hundred pages?!"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Yeah."

    call process_character(n, appearance = "pose handpocket face embarrassed blush false")
    n.c "That would take me forever to read!"

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "It's not that bad."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "I'll probably complete it in a couple days."

    call process_character(n, appearance = "pose handpocket face curious blush false")
    n.c "...{p}..."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "Anyway, I'll be downstairs."

    call process_character(n, appearance = "pose twohandfist face concerned blush false")
    n.c "Wait!"

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "Don't you want to say hi to [sa.say_name]?"

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "She's right in her room."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "I don't want to disturb her."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "{cps=40}Oh it's fine, she's actually been waiting for-{/cps}{w=0.75}{nw}"

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "I'll see her soon enough."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "You can tell her I'm in the living room."

    call character_leave_dissolve(julia)
    pause 0.5

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "...{p}..."

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "(Guess I gotta tell [sa.say_name] [julia.say_name] won't be joining us...)"


    call process_new_location(bg = sam_room, char_tuple_array = [(sa, "outfit clothes pose handface face embarrassed blush false"), (n, "pose behindhead face concerned blush false")] )

    call process_character(n, appearance = "pose behindhead face concerned blush false")

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

    $ reset_all_characters()
    if started_main_game:
        $ had_julia_arrived_scene = True
        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        jump debug_menu

    return

## Kacey Rename ##
label gloryhole_handjob_scene_sex_rename(dream = False):
    $ renpy.scene('screens')
    if dream:
        show screen dream_blur

    $ no_bust_art = False
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    n.c "(I recall there is a park nearby our house)"

    call process_character(n, appearance = "outfit clothesjacket pose handfist face happy")
    n.c "(It would be cool to go there!)"


    if store.week.time != "night":
        $ store.week.time = "night"
        call process_character(n, appearance = "outfit clothesjacket pose handfist face happy")
        n.c "(I'll head out there tonight!)"

    else:
        call process_character(n, appearance = "outfit clothesjacket pose handfist face happy")
        n.c "(I think I'll head out right now!)"

    call process_scene_beginning(bg = park, char_tuple_array = [ (n, "outfit clothesjacket pose twohandfist face happy") ], dream = dream )

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy")
    n.c "(I practically have the park to myself!)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    n.c "(It's quiet and peaceful)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    n.c "(All I can hear are the bugs chirping)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    n.c "{i}Sigh{/i}..."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral")
    n.c "(This park is pretty big)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    n.c "(But all these paths are well lit)"

    call process_character(n, appearance = "outfit clothesjacket pose handfist face neutral")
    n.c "(And all the signs make it real easy to find my way around)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious")
    n.c "Hm?"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious")
    n.c "(Looks like a bathroom building up ahead)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face concerned")
    n.c "(Now that I think about it, I gotta go pretty bad...)"

    call fade_to_black(1.0, do_not_show_quick_menu = True)
    show bg public_bathroom_evening
    with Dissolve(0.5)
    $ no_bust_art = False
    pause 0.5
    $ quick_menu = True
    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral")
    n.c "(This bathroom is not half bad!)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious")
    n.c "(Though it looks like some of the toilets aren't working)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face happy")
    n.c "(The stall at the end looks like it's open!)"

    window hide
    $ quick_menu = False
    $ clear_characters()
    show bg black
    with Dissolve(0.5)
    pause 1.0
    call static_still_ctc("bg gloryhole")
    n.c "(Ah, that felt good!)"
    n.c "(I had to go pretty bad)"
    n.c "..."
    n.c "What's this hole doing here?"


    "{color=#FDDF7D}Female Voice{/color}" "Would you like to know?"
    n.c "..."
    n.c "Who said that?"

    "{color=#FDDF7D}Female Voice{/color}" "Hey there!"
    "{color=#FDDF7D}Female Voice{/color}" "I'm in the stall next to you."
    n.c "Uh..."
    n.c "Hi."

    "{color=#FDDF7D}Female Voice{/color}" "I haven't heard your cute voice before."
    "{color=#FDDF7D}Female Voice{/color}" "You new?"
    n.c "..."
    n.c "Yeah..."
    n.c "I moved nearby here not too long ago."

    "{color=#FDDF7D}Female Voice{/color}" "Oh nice!"
    "{color=#FDDF7D}Female Voice{/color}" "Have you been checking out the park?"
    n.c "Er, yeah..."

    "{color=#FDDF7D}Female Voice{/color}" "It's a great park to be in."
    "{color=#FDDF7D}Female Voice{/color}" "But not many people are around at night."
    n.c "..."
    n.c "You sound like you're a girl."

    "{color=#FDDF7D}Female Voice{/color}" "I am."
    n.c "But..."
    n.c "Isn't this the boy's bathroom?"

    "{color=#FDDF7D}Female Voice{/color}" "It is?"
    "{color=#FDDF7D}Female Voice{/color}" "Woops!"
    "{color=#FDDF7D}Female Voice{/color}" "I must have misread the sign."
    n.c "Oh..."
    n.c "...{p}..."

    "{color=#FDDF7D}Female Voice{/color}" "So you were curious about this hole?"
    n.c "It is odd."

    "{color=#FDDF7D}Female Voice{/color}" "You know what it's used for?"
    n.c "No idea."

    "{color=#FDDF7D}Female Voice{/color}" "You don't?"
    "{color=#FDDF7D}Female Voice{/color}" "Oh, you're missing out!"
    "{color=#FDDF7D}Female Voice{/color}" "You should try it!"
    n.c "Try it?"
    n.c "How do I try it?"

    "{color=#FDDF7D}Female Voice{/color}" "Easy!"
    "{color=#FDDF7D}Female Voice{/color}" "Just put your penis through it!"
    n.c "M-My penis?!"
    n.c "..."
    n.c "W-What happens if I do that?"

    "{color=#FDDF7D}Female Voice{/color}" "Well..."
    "{color=#FDDF7D}Female Voice{/color}" "Something fun happens!"
    n.c "..."
    n.c "I don't know."

    "{color=#FDDF7D}Female Voice{/color}" "You'll never know unless you try..."
    n.c "...{p}..."
    n.c "(It's a little weird doing this...)"
    n.c "..."
    n.c "If I don't like it, can I pull my penis out?"

    "{color=#FDDF7D}Female Voice{/color}" "Sure."
    "{color=#FDDF7D}Female Voice{/color}" "(I doubt you'll want to though)"
    n.c "...{p}..."
    n.c "O-Okay, I'll put my penis through."


    call static_still_ctc("bg gloryhole_sticks_dick_through")

    "{color=#FDDF7D}Female Voice{/color}" "..."
    "{color=#FDDF7D}Female Voice{/color}" "{i}Gasp!{/i}"
    n.c "W-What?"

    "{color=#FDDF7D}Female Voice{/color}" "You have such a nice penis!"
    n.c "Oh..."
    n.c "T-thanks."

    "{color=#FDDF7D}Female Voice{/color}" "(I have struck gold!)"
    "{color=#FDDF7D}Female Voice{/color}" "(This is the youngest penis I've seen!)"
    "{color=#FDDF7D}Female Voice{/color}" "(I hope I'm not imagining it!)"

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg gloryhole_touches_dick")
    n.c "Ah, w-what are you doing?"

    "{color=#FDDF7D}Female Voice{/color}" "(Looks completely untouched!)"
    "{color=#FDDF7D}Female Voice{/color}" "(And feels so smooth)"
    "{color=#FDDF7D}Female Voice{/color}" "..."
    "{color=#FDDF7D}Female Voice{/color}" "(Is it already getting hard?)"
    "{color=#FDDF7D}Female Voice{/color}" "(Oh the potential with this kid...)"
    n.c "Ah..."
    n.c "(It feels like her fingers are moving along my penis!)"
    n.c "(I-I can feel it getting...)"


    call static_still_ctc("bg gloryhole_handjob")

    "{color=#FDDF7D}Female Voice{/color}" "!!!"
    "{color=#FDDF7D}Female Voice{/color}" "(Look at that reaction!)"
    "{color=#FDDF7D}Female Voice{/color}" "(He knows what feels good!)"
    "{color=#FDDF7D}Female Voice{/color}" "Well, well..."
    n.c "Hah..."
    n.c "M-My penis..."
    n.c "I-It got hard."

    "{color=#FDDF7D}Female Voice{/color}" "Indeed it did."
    "{color=#FDDF7D}Female Voice{/color}" "And it happened so quick!"
    "{color=#FDDF7D}Female Voice{/color}" "That means you're liking this, aren't you?"
    n.c "I-It does feel nice..."

    "{color=#FDDF7D}Female Voice{/color}" "(Well if he thinks that feels nice...)"
    "{color=#FDDF7D}Female Voice{/color}" "(Wait till he feels this!)"

    call static_still_ctc("bg gloryhole_handjob_stall_opaque")

    $ gloryhole_handjob_xray_on = False
    show screen gloryhole_handjob_xray

    "{color=#FDDF7D}Female Voice{/color}" "Yeah-ha-ha!"
    n.c "Ah, ah, ah!"
    n.c "W-what are you laughing about?"

    "{color=#FDDF7D}Female Voice{/color}" "Ha, well I just..."
    "{color=#FDDF7D}Female Voice{/color}" "Your penis is bouncing all over the place!"
    "{color=#FDDF7D}Female Voice{/color}" "..."
    "{color=#FDDF7D}Female Voice{/color}" "(This kid is getting one hell of a whacking)"
    "{color=#FDDF7D}Female Voice{/color}" "(But I can't help it!)"
    "{color=#FDDF7D}Female Voice{/color}" "(How often would I get an innocent cock to slap around?)"
    n.c "Hah! Ngh..."
    n.c "(S-She's being a little rough!)"
    n.c "(B-But it's not too bad)"

    "{color=#FDDF7D}Female Voice{/color}" "How you doing in there?"
    n.c "Ah, mm..."
    n.c "I, ah..."
    n.c "I-I think I'll keep it in a little longer."

    "{color=#FDDF7D}Female Voice{/color}" "(I've got him now!)"
    "{color=#FDDF7D}Female Voice{/color}" "...{p}..."
    "{color=#FDDF7D}Female Voice{/color}" "(He's hanging in there, I'm surprised)"
    "{color=#FDDF7D}Female Voice{/color}" "(I thought for sure by now he would-)"
    n.c "Ah, oh..."
    n.c "Ahn..."
    n.c "Ahhh!"

    hide screen gloryhole_handjob_xray

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc("bg gloryhole_handjob_cum")

    "{color=#FDDF7D}Female Voice{/color}" "(Oh, spoke too soon)"
    "{color=#FDDF7D}Female Voice{/color}" "..."
    "{color=#FDDF7D}Female Voice{/color}" "(Holy crap!)"
    "{color=#FDDF7D}Female Voice{/color}" "(How much can I squeeze out of him?)"
    "{color=#FDDF7D}Female Voice{/color}" "(Just get every {w=0.5}last {w=0.5}drop)"
    n.c "Y-You're squeezing pretty hard!"

    "{color=#FDDF7D}Female Voice{/color}" "My bad."
    "{color=#FDDF7D}Female Voice{/color}" "You just had some lingering drops I had to get out."
    "{color=#FDDF7D}Female Voice{/color}" "..."
    "{color=#FDDF7D}Female Voice{/color}" "So..."
    "{color=#FDDF7D}Female Voice{/color}" "Did you like that?"
    n.c "Y-Yeah."

    "{color=#FDDF7D}Female Voice{/color}" "This hole is fun isn't it?"
    n.c "I-I didn't know it was gonna be like that."
    n.c "But I did like it."

    "{color=#FDDF7D}Female Voice{/color}" "(I'd say so based on how much my hand is covered)"
    "{color=#FDDF7D}Female Voice{/color}" "..."
    "{color=#FDDF7D}Female Voice{/color}" "Well hey..."
    "{color=#FDDF7D}Female Voice{/color}" "I hope to see you stop by here again."
    n.c "Right here you mean?"

    "{color=#FDDF7D}Female Voice{/color}" "Why not?"
    "{color=#FDDF7D}Female Voice{/color}" "No one's around to bother us, and we can have a good time together!"
    n.c "How will I know when you're around?"

    "{color=#FDDF7D}Female Voice{/color}" "Easy!"
    "{color=#FDDF7D}Female Voice{/color}" "Just call out my name."

    call change_character_name(gloryhole_girl, prompt = _("Gloryhole girl's name"))
    gloryhole_girl.c "[gloryhole_girl.say_name]!"
    gloryhole_girl.c "..."
    gloryhole_girl.c "Speaking of names, what's yours?"

    n.c "Oh..."
    n.c "M-My name's [n.say_name]."
    gloryhole_girl.c "[n.say_name]..."
    gloryhole_girl.c "I like that name."
    gloryhole_girl.c "Alright [n.say_name]."
    gloryhole_girl.c "I'll see you again real soon!"
    gloryhole_girl.c "Next time I may have a new surprise for you..."

    python:
        gloryhole_girl.revistable_scenes.add("gloryhole_handjob_scene_revisit")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_received_handjob", 1)
            stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene("gloryhole_handjob_scene", char = gloryhole_girl, dream = dream)

    return

## Vicky Rename ##
label vicky_intro_rename:
    $ nate_room.decide_and_play_daily_music_queue()
    call process_scene_beginning(bg = nate_room)

    call process_character(n, appearance = "outfit clothes pose behindhead face aroused blush false")
    n.c "(Looks like I woke up a little early...)"

    call process_character(n, appearance = "outfit clothes pose behindhead face aroused blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothes pose behindhead face happy blush false")
    n.c "(Oh! I should check how the latest review is doing!)"

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "...{p}..."

    call process_character(n, appearance = "outfit clothes pose handfist face happy blush false")
    n.c "(All right!)"

    call process_character(n, appearance = "outfit clothes pose handfist face happy blush false")
    n.c "(This one's doing better than the last!)"

    call process_character(n, appearance = "outfit clothes pose handfist face happy blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothes pose handsdown face curious blush false")
    n.c "(Hm?)"

    call process_character(n, appearance = "outfit clothes pose handsdown face curious blush false")
    n.c "(I got a private message...)"

    call process_character(n, appearance = "outfit clothes pose handsdown face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "{i}Gasp!{/i}"

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "(It's from ReflexViz.HD!)"

    call process_character(n, appearance = "outfit clothes pose behindhead face neutral blush false")
    n.c "(What's it say...)"

    call process_character(n, appearance = "outfit clothes pose behindhead face neutral blush false")
    n.c "..."


    call change_character_name(vicky, prompt = _("ReflexViz.HD Affiliate's name"))

    "\"Hello, my name is [vicky.say_name] Hardy, and I work as a local affiliate for ReflexViz.HD.\""

    "\"Your reviews have been getting a lot of shares on our site, and I wanted to discuss with you the possibility of establishing a partnership program with us.\""

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "(Oh my gosh, oh my gosh!)"

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "(This is it!)"

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "(What else does it say...)"


    "\"I'd like to chat with you the next time you are available.\""
    "\"You can contact me via a private chatroom using the link I've provided.\""
    "\"I look forward to hearing from you.\""

    call process_character(n, appearance = "outfit clothes pose handfist face happy blush false")
    n.c "(No way!)"

    call process_character(n, appearance = "outfit clothes pose handfist face happy blush false")
    n.c "(This could be huge!)"

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "(Getting a partnership offer this early is a great sign!)"

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "(I don't want to miss this opportunity!)"

    call process_character(n, appearance = "outfit clothes pose handfist face happy blush false")
    n.c "(I'll go into the chatroom right now!)"


    call process_new_location(bg = nate_room, force_bg_change = True)

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "(It's connecting...)"

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothes pose twohandfist face neutral blush false")
    n.c "(Alright, I'm in!)"

    call process_character(n, appearance = "outfit clothes pose twohandfist face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothes pose behindhead face curious blush false")
    n.c "(I guess I should type something to see if [vicky.say_name] is there...)"

    call process_character(n, appearance = "outfit clothes pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothes pose behindhead face curious blush false")
    n.c "\"Hello.\""

    call process_character(n, appearance = "outfit clothes pose behindhead face curious blush false")
    n.c "\"I clicked the link to join the private chat.\""
    vicky.c "\"Hello!\""
    vicky.c "\"How are you today?\""

    call process_character(n, appearance = "outfit clothes pose handsdown face happy blush false")
    n.c "(Yes, she's there!)"

    call process_character(n, appearance = "outfit clothes pose handsdown face happy blush false")
    n.c "\"I'm doing good!\""
    vicky.c "\"That's great to hear!\""
    vicky.c "\"Are you the owner of the channel \"Twinsticks?\""

    call process_character(n, appearance = "outfit clothes pose handfist face happy blush false")
    n.c "\"I am!\""

    call process_character(n, appearance = "outfit clothes pose handfist face happy blush false")
    n.c "\"My sister owns it too.\""
    vicky.c "\"Do you control decisions on the channel?\""

    call process_character(n, appearance = "outfit clothes pose behindhead face neutral blush false")
    n.c "\"Uum...\""

    call process_character(n, appearance = "outfit clothes pose behindhead face neutral blush false")
    n.c "\"I guess I do, yeah.\""
    vicky.c "\"Okay, great!\""
    vicky.c "\"I just wanted to make sure you were one of the authorities for it.\""

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "\"Gotcha.\""
    vicky.c "\"I didn't happen to get your name.\""
    vicky.c "\"Could you give it to me for my file?\""

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "\"My name is [n.say_name] [last_name].\""
    vicky.c "\"Thank you.\""
    vicky.c "\"Well Mr. [last_name], I'm to assume you're interested in a partnership with ReflexViz.HD?\""

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "\"I sure am!\""
    vicky.c "\"Excellent!\""

    call process_character(n, appearance = "outfit clothes pose handfist face neutral blush false")
    n.c "\"So, how do I become a partner?\""
    vicky.c "\"I'm glad you asked!\""
    vicky.c "\"In order to become partnered with us, you have to sign and agree to a contract.\""

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "\"Okay!\""

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "\"Can you email it to me?\""
    vicky.c "\"Actually, this contract has to be signed in person.\""
    vicky.c "\"I need to have a legal signature confirming the partnership.\""

    call process_character(n, appearance = "outfit clothes pose behindhead face concerned blush false")
    n.c "\"Oh...\""

    call process_character(n, appearance = "outfit clothes pose behindhead face concerned blush false")
    n.c "\"How will I be able to do that though?\""
    vicky.c "\"No worries!\""
    vicky.c "\"I'm actually close to your area!\""
    vicky.c "\"ReflexViz has localized agents, such as myself, so meeting up requires minimal travel!\""

    call process_character(n, appearance = "outfit clothes pose handsdown face neutral blush false")
    n.c "\"Where exactly are you?\""
    vicky.c "\"I can send you the directions via email.\""
    vicky.c "\"I have an office in my apartment.\""

    call process_character(n, appearance = "outfit clothes pose twohandfist face neutral blush false")
    n.c "\"Awesome!\""

    call process_character(n, appearance = "outfit clothes pose twohandfist face neutral blush false")
    n.c "\"When can we meet?\""
    vicky.c "\"Whenever is convenient for you!\""
    vicky.c "\"Just let me know ahead of time, and I'll fit you into my schedule!\""

    call process_character(n, appearance = "outfit clothes pose handsdown face happy blush false")
    n.c "\"I can't wait!\""
    vicky.c "\"I sent the directions just now.\""
    vicky.c "\"I look forward to meeting you Mr. [last_name]!\""

    call process_character(n, appearance = "outfit clothes pose handsdown face happy blush false")
    n.c "\"Same!\""


    "{i}Chat Disconnected.{/i}"

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "(This is so great!)"

    call process_character(n, appearance = "outfit clothes pose twohandfist face happy blush false")
    n.c "(I'll head over there as soon as I can!)"

    "{i}You can now travel to [vicky.say_name]'s apartment.{/i}"

    $ reset_all_characters()
    if started_main_game:
        $ had_vicky_intro_scene = True
        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        jump debug_menu

    return

# Janet Intro Fix, now takes place downstairs instead of in Nate's bedroom
label janet_intro_misc:
    $ nate_room.decide_and_play_daily_music_queue()
    call process_scene_beginning(bg = nate_room, char_tuple_array = [ (n, ""), (si, "outfit clothes pose handsup face happy blush false") ])

    call process_character(si, appearance = "outfit clothes pose handsup face happy blush false")
    si.c "Today is gorgeous!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Yeah, it is!"

    call process_character(si, appearance = "outfit clothes pose handsup face neutral blush false")
    si.c "You should get outside."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    call process_character(si, appearance = "outfit clothes pose handsfront face neutral blush false")
    si.c "Summer won't last forever!"

    call process_character(si, appearance = "outfit clothes pose handsfront face neutral blush false")
    si.c "Take advantage of every nice day you can."

    call process_character(n, appearance = "pose handpocket face neutral blush false")
    n.c "That's true."

    call process_character(si, appearance = "outfit clothes pose handsup face neutral blush false")
    si.c "You should get your sister to come out as well."

    call process_character(si, appearance = "outfit clothes pose handsup face neutral blush false")
    si.c "She needs to take a break from all those video games."

    "{i}Knock-Knock-Knock{/i}"

    call process_character(si, appearance = "outfit clothes pose handsfront face curious blush false")
    si.c "(Who could that be?)"

    call process_character(si, appearance = "outfit clothes pose handsfront face curious blush false")
    si.c "(I didn't think we were expecting any visitors today)"

    "{color=[janet.color]}Woman's Voice{/color}" "Hello, hello!"

    call process_character(si, appearance = "outfit clothes pose armunder face embarrassed blush false")
    si.c "(!!!)"

    call process_character(si, appearance = "outfit clothes pose armunder face embarrassed blush false")
    si.c "(Oh dear...)"

    call process_character(si, appearance = "outfit clothes pose armunder face embarrassed blush false")
    si.c "(I'd recognize that voice anywhere)"

    call process_character(si, appearance = "outfit clothes pose handsfront face embarrassed blush false")
    si.c "Quick, we better head downstairs right away!"

    call process_character(si, appearance = "outfit clothes pose handsfront face embarrassed blush false")
    si.c "I think I just heard her come in!"

    call process_scene_beginning(bg = "bg kitchen_daytime")

    $ clear_characters()
    python hide:
        for char in character_list():
            char.position = "right"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false", replace = True)
    "{color=[janet.color]}Woman{/color}" "Hey!"
    "{color=[janet.color]}Woman{/color}" "How is everybody?"

    call change_character_name(janet, prompt = _("Aunt's name"))
    call process_character(si, appearance = "pose handsup face shocked blush false",  replace = True)
    si.c "[janet.say_name]?!"

    call process_character(si, appearance = "pose handsup face shocked blush false",  replace = True)
    si.c "I didn't know you were stopping by!"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "It's a heck of a lot easier to visit now that you're so close!"

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "I figured, why not come say hello to everyone!"

    call process_character(janet, appearance = "outfit clothes pose handface face happy blush false",  replace = True)
    janet.c "{i}Gasp...{/i}"

    call process_character(janet, appearance = "outfit clothes pose handface face happy blush false",  replace = True)
    janet.c "Is that you [n.say_name]?"

    call process_character(n, appearance = "pose handfist face happy blush false",  replace = True)
    n.c "Hi Aunt [janet.say_name]!"

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "You look taller than the last time I saw you!"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "But you're still so skinny!"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "You're practically all bone!"

    call process_character(n, appearance = "pose handpocket face curious blush false",  replace = True)
    n.c "..."

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "But that's better than being overweight!"

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "It's easy to put on the pounds, but it's hard to lose them!"

    call process_character(janet, appearance = "outfit clothes pose handface face happy blush false",  replace = True)
    janet.c "For our family that's especially true!"

    call process_character(si, appearance = "pose handsfront face concerned blush false",  replace = True)
    si.c "..."

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "So where are your two sisters [n.say_name]?"

    call process_character(n, appearance = "pose behindhead face neutral blush false",  replace = True)
    n.c "[sa.say_name] is upstairs."

    call process_character(n, appearance = "pose behindhead face neutral blush false",  replace = True)
    n.c "And [k.say_name] went out for a run."

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "Ah yes, your big sis is staying committed to her exercise!"

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "I got her into that whole workout routine you know."

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "She was born to be an athlete!"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false",  replace = True)
    k.c "..."

    call process_character(janet, appearance = "outfit clothes pose handchest face happy blush false",  replace = True)
    janet.c "And here she is!"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false",  replace = True)
    k.c "No way!"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false",  replace = True)
    k.c "Aunt [janet.say_name]!"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false",  replace = True)
    k.c "When did you get here?"

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "Just before you did."

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "Our times lined up almost perfectly!"

    call process_character(janet, appearance = "outfit clothes pose handface face happy blush false",  replace = True)
    janet.c "And look at you!"

    call process_character(janet, appearance = "outfit clothes pose handface face happy blush false",  replace = True)
    janet.c "You've buffed up!"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false",  replace = True)
    k.c "I added weightlifting to my regiment."

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "You look like you could lift [n.say_name] up with one arm!"

    call process_character(n, appearance = "pose behindhead face curious blush false",  replace = True)
    n.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false",  replace = True)
    k.c "Haha!"

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false",  replace = True)
    k.c "I bet I could!"


    if "minigame_racing_first_time_intro" in scenes_completed:
        call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false",  replace = True)
        k.c "He's actually been working out with me."

        call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false",  replace = True)
        k.c "We go to the running track and race each other."

        call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
        janet.c "You have your work cut out for you racing against your sister [n.say_name]!"


    else:
        call process_character(k, appearance = "outfit clothes pose armsup face happy blush false",  replace = True)
        k.c "He can happily sit on my arm while I do push-ups with the other!"

        call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
        janet.c "He'll be cheering you on all the way, [k.say_name]!"

        call process_character(n, appearance = "pose behindhead face curious blush false",  replace = True)
        n.c "..."


    call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    sa.c "{i}Yawn...{/i}"

    call process_character(si, appearance = "pose handsup face neutral blush false",  replace = True)
    si.c "Morning sweetie!"

    call process_character(janet, appearance = "outfit clothes pose handface face curious blush false",  replace = True)
    janet.c "Morning?"

    call process_character(janet, appearance = "outfit clothes pose handface face curious blush false",  replace = True)
    janet.c "It's almost eleven thirty!"

    call process_character(sa, appearance = "outfit clothes pose handsbehind face happy blush false",  replace = True)
    sa.c "Aunt [janet.say_name]!"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "Hey there kiddo!"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "Hope you're not staying up too late!"

    call process_character(sa, appearance = "outfit clothes pose handsbehind face happy blush false",  replace = True)
    sa.c "Hehe, I lose track of time when I'm playing online at night."

    call process_character(si, appearance = "pose armunder face neutral blush false",  replace = True)
    si.c "Don't mess up your sleep pattern too much okay?"

    call process_character(si, appearance = "pose armunder face neutral blush false",  replace = True)
    si.c "You'll be dead tired when school starts up!"

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "Your Mom is right about that."

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "[julia.say_name]'s got the same problem."

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "She stays up late, and then I practically have to drag her out of bed in the morning."

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "Where is she by the way?"

    call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    sa.c "She just got in the shower."

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "Oh she'll be in there forever."

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "I just wanted to know how she's been doing."

    call process_character(janet, appearance = "outfit clothes pose handchest face curious blush false",  replace = True)
    janet.c "Has she been behaving herself?"

    call process_character(si, appearance = "pose handsup face happy blush false",  replace = True)
    si.c "Oh [julia.say_name]'s been excellent!"

    call process_character(si, appearance = "pose handsup face happy blush false",  replace = True)
    si.c "She's quite the reader!"

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "Yeah she is."

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "Years ago I bought her some book with dragons on the cover and that was it."

    call process_character(janet, appearance = "outfit clothes pose handface face happy blush false",  replace = True)
    janet.c "She rarely goes a day without reading now!"

    call process_character(n, appearance = "pose handpocket face neutral blush false",  replace = True)
    n.c "[sa.say_name] and I asked if she wanted to play video games, but she wasn't interested."

    call process_character(n, appearance = "pose handpocket face curious blush false",  replace = True)
    n.c "At first we thought we did something wrong..."

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "That's just the way she is."

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "She doesn't always like being dragged into things."

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "She wants to be the one that decides if she'll do something."

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "It was her that asked to stay over here during the summer."

    call process_character(n, appearance = "pose behindhead face neutral blush false",  replace = True)
    n.c "She was?"

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "I think [julia.say_name] was going a bit stir crazy at our house."

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "It's too big for us."

    call process_character(janet, appearance = "outfit clothes pose handchest face happy blush false",  replace = True)
    janet.c "It's great for hosting parties and get togethers!"

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "But the majority of the time a lot of the rooms go unused."

    call process_character(si, appearance = "pose armunder face neutral blush false",  replace = True)
    si.c "It is a lovely home you have."

    call process_character(si, appearance = "pose armunder face neutral blush false",  replace = True)
    si.c "But I prefer a smaller home as well."

    call process_character(si, appearance = "pose armunder face happy blush false",  replace = True)
    si.c "Less upkeep and cleaning required!"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "You guys are welcome to stop by at any time!"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "It would be great to have company!"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false",  replace = True)
    k.c "That sounds cool."

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "We could head off to the beach near Grandma's house from my place too."

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "I love going there!"

    call process_character(sa, appearance = "outfit clothes pose handface face happy blush false",  replace = True)
    sa.c "Aww, the beach!"

    call process_character(n, appearance = "pose twohandfist face happy blush false",  replace = True)
    n.c "Yeah!"

    call process_character(si, appearance = "pose handsup face neutral blush false",  replace = True)
    si.c "We have been meaning to go to the beach this summer."

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "The water is at a perfect temperature right now."

    call process_character(si, appearance = "pose armunder face happy blush false",  replace = True)
    si.c "I know [sa.say_name] and [n.say_name] really want to ride the waves!"

    call process_character(sa, appearance = "outfit clothes pose leaning face happy blush false",  replace = True)
    sa.c "Yes, yes, yes!"

    call process_character(janet, appearance = "outfit clothes pose handhips face neutral blush false",  replace = True)
    janet.c "Oh yeah, I bodysurf myself."

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "I can show [sa.say_name] and [n.say_name] how to catch some big ones!"

    call process_character(janet, appearance = "outfit clothes pose handhips face happy blush false",  replace = True)
    janet.c "..."

    call process_character(janet, appearance = "outfit clothes pose handface face neutral blush false",  replace = True)
    janet.c "Anyway, I have to head out to do some errands."

    call process_character(janet, appearance = "outfit clothes pose handface face happy blush false",  replace = True)
    janet.c "But it was great to see everybody!"

    call process_character(n, appearance = "pose handpocket face neutral blush false",  replace = True)
    n.c "It was great to see you too Aunt [janet.say_name]!"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false",  replace = True)
    k.c "We'll talk to you again soon!"

    call process_character(janet, appearance = "outfit clothes pose handchest face neutral blush false",  replace = True)
    janet.c "Just give me a buzz when you'd like to come over."

    call process_character(janet, appearance = "outfit clothes pose handchest face happy blush false",  replace = True)
    janet.c "If just one of you wants to stop by feel free!"

    call process_character(janet, appearance = "outfit clothes pose handchest face happy blush false",  replace = True)
    janet.c "See ya later!"

    call process_character(si, appearance = "pose handsfront face neutral blush false",  replace = True)
    si.c "..."

    call process_character(si, appearance = "pose handsfront face neutral blush false",  replace = True)
    si.c "{i}Phew...{/i}"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false",  replace = True)
    k.c "Aunt [janet.say_name] sure has a lot of energy."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false",  replace = True)
    k.c "I hope I can remain that lively when I'm her age!"

    call process_character(si, appearance = "pose armunder face concerned blush false",  replace = True)
    si.c "Just don't get as impulsive as she does..."

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false",  replace = True)
    k.c "Oh, did she barge in unannounced as always?"

    call process_character(si, appearance = "pose handsup face shocked blush false",  replace = True)
    si.c "She knocked on the door, then just walks in!"

    call process_character(si, appearance = "pose handsup face shocked blush false",  replace = True)
    si.c "I had no idea she was even coming!"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false",  replace = True)
    k.c "Just the way she likes it Mom!"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false",  replace = True)
    k.c "Arriving out of nowhere, and at the most awkward times!"

    call process_character(si, appearance = "pose armunder face neutral blush false",  replace = True)
    si.c "Yes, but before she couldn't do it as much since we lived far away."

    call process_character(si, appearance = "pose armunder face embarrassed blush false",  replace = True)
    si.c "But now we're so close..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false",  replace = True)
    k.c "I wouldn't worry too much about it Mom."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false",  replace = True)
    k.c "It sounds like she wants us to visit her more than the other way around."

    call process_character(sa, appearance = "outfit clothes pose leaning face neutral blush false",  replace = True)
    sa.c "I want to go to the beach so bad!"

    call process_character(si, appearance = "pose handsfront face neutral blush false",  replace = True)
    si.c "I know you do sweetie!"

    call process_character(si, appearance = "pose handsfront face neutral blush false",  replace = True)
    si.c "I'm hoping we'll all be able to go together soon."

    call process_character(si, appearance = "pose handsfront face happy blush false",  replace = True)
    si.c "But you can go with Aunt [janet.say_name] if you get impatient!"

    call process_character(sa, appearance = "outfit clothes pose handsbehind face happy blush false",  replace = True)
    sa.c "Yay!"

    call process_character(sa, appearance = "outfit clothes pose handsbehind face happy blush false",  replace = True)
    sa.c "I bet she's a master wave rider!"

    call process_character(si, appearance = "pose handsfront face neutral blush false",  replace = True)
    si.c "Same goes for you [n.say_name]."

    call process_character(si, appearance = "pose armunder face curious blush false",  replace = True)
    si.c "Even though she can be tactless at times...{w=1.0}she does love seeing you guys."

    call process_character(si, appearance = "pose armunder face happy blush false",  replace = True)
    si.c "But if you sleep over there, be prepared to wake up with the chickens!"

    call process_character(si, appearance = "pose armunder face happy blush false",  replace = True)
    si.c "She's the true definition of a morning person!"

    call process_character(n, appearance = "pose handfist face happy blush false",  replace = True)
    n.c "It will be cool to see her more often!"

    $ reset_all_characters()
    if started_main_game:
        $ had_janet_intro_scene = True
        $ reset_all_characters()
        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        jump debug_menu

    return

## Scene Limit/Boldness Failure ##
init 300 python:
    config.label_overrides["retry_prompt_boldness_failure"] = "retry_prompt_boldness_failure_misc"
    config.label_overrides["scene_limit_notice"] = "scene_limit_notice_misc"

label retry_prompt_boldness_failure_misc(retry_prompt_boldness_failure_char):
    call process_character(n, appearance = "pose handpocket face concerned")
    n.c "(I don't know if I'm ready for that yet)"

    call process_character(n, appearance = "pose handpocket face concerned")
    n.c "(Maybe if I was more {b}bold{/b}...)"

    $ retry_prompt_boldness_failure_char.display_menu()
    return

label scene_limit_notice_misc(scene_limit_char):
    call process_character(n, appearance = "pose handpocket face neutral")
    n.c "Maybe I can do that tomorrow?"

    $ scene_limit_char.display_menu()
    return

## Wake/Sleep Lines Nudefix ##
init 300 python:
    config.label_overrides["morning_wake_lines"] = "morning_wake_lines_misc"
    config.label_overrides["sleep_lines"] = "sleep_lines_misc"

label morning_wake_lines_misc:
    $ n.reset_appearance(show_bust = False)
    if store.has_fucked_everyone_in_home:
        $ n.outfit = "nudesoft"
    else:
        $ n.outfit = "underwear"

    python:
        random_line_array = []
        random_line_array.append( {"char": n, "appearance": "yea", "text": "{i}Yawn{/i}...A new day begins!" } )
        random_line_array.append( {"char": n, "appearance": "yea", "text": "Time to be up and about!" } )
        random_line_array.append( {"char": n, "appearance": "yea", "text": "Wonder what I should do today?" } )
        random_line_array.append( {"char": n, "appearance": "yea", "text": "Rested and ready to go for the day!" } )

    call random_line(random_line_array)
    $ clear_characters(Dissolve(0.3))

    return

label sleep_lines_misc:
    $ n.reset_appearance(show_bust = False)
    python:
        if store.has_fucked_everyone_in_home:
            sleep_lines_outfit = "nudesoft"
        else:
            sleep_lines_outfit = "underwear"
        random_line_array = []
        random_line_array.append( {"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Sleeep..." } )
        random_line_array.append( {"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Gotta get some rest..." } )
        random_line_array.append( {"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Alright, time for bed." } )
        random_line_array.append( {"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "My bed sure looks comfortable..." } )

    call random_line(random_line_array)

    return

## Kira Convo 4 Conditional ##
init 300 python:
    config.label_overrides["kira_convo_4"] = "kira_convo_4_misc"

label kira_convo_4_misc:
    call process_conversation_beginning([ (n, ""), (k, "") ])
    n.c "What happens at work if not many people stop by for exercising?"

    call process_character(k, appearance = "pose armsup face neutral",  )
    k.c "What do ya think?{p=1.0}I'm taking advantage of that shit."

    call process_character(k, appearance = "pose armsup face neutral",  )
    k.c "I'll just exercise myself with the free equipment."

    call process_character(n, appearance = "pose handpocket face concerned")
    n.c "You don't get in trouble for that?"

    call process_character(k, appearance = "pose handhip face neutral",  )
    k.c "Nah."

    call process_character(k, appearance = "pose handhip face neutral",  )
    k.c "Other employees usually ask me for tips on proper techniques for stretching and lifting weights."

    call process_character(n, appearance = "pose handpocket face neutral")
    call process_character(k, appearance = "pose armcross face neutral",  )
    k.c "Some customers come in and don't even exercise."

    call process_character(k, appearance = "pose armcross face neutral",  )
    k.c "They just want to \"observe\" my form."

    call process_character(n, appearance = "pose handpocket face curious")
    n.c "That seems weird."

    call process_character(n, appearance = "pose handpocket face curious")
    n.c "Coming in just to watch you exercise, but not do it themselves."

    call process_character(k, appearance = "pose handhip face neutral",  )
    k.c "I'm sure they do exercises themselves at home."

    call process_character(k, appearance = "pose handhip face concerned",  )
    k.c "They likely only train one \"muscle\"... many times over."

    if "simone_scene_1_seq_1" in scenes_completed or stats.stat_value('times_fapped') > 0:
        call process_character(k, appearance = "pose armsup face flirty",  )
        k.c "Reminds me of a certain {i}someone{/i} I know."

        call process_character(k, appearance = "pose armsup face flirty",  )
        k.c "Hehe."

        call process_character(n, appearance = "pose behindhead face embarrassed blush false")
        n.c "..."

    else:
        call process_character(n, appearance = "pose behindhead face curious")
        $ renpy.pause(1)
        call process_character(n, appearance = "pose behindhead face curious")
        n.c "Some people are weird."

    call process_end_of_conversation("kira_convo_4", k, priority = False)

    return

# Sam Donation Revisit Fix #
init 300 python:
    config.label_overrides["sam_scene_3_revisit"] = "sam_scene_3_revisit_donation_fix"

label sam_scene_3_revisit_donation_fix:
    call process_character(n, appearance = "pose twohandfist face neutral")
    call process_character(sa, appearance = "pose handface face happy")
    sa.c "I hear that!"

    call process_scene_beginning(sam_room, char_tuple_array = [ (n, "outfit underwear pose behindhead face neutral"), (sa, "outfit underwear pose handsbehind face neutral") ], force_bg_change = True)

    call process_character(n, appearance = "pose behindhead face neutral")
    n.c "Alright, I did that pose as requested!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "And there it is!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Another donation to the Twinsticks stream!"

    call process_character(n, appearance = "pose handfist face happy")
    n.c "You guys are awesome!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "So awesome in fact..."

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "We'll be able to put these donations towards brand new streaming equipment!"

    call process_character(n, appearance = "pose twohandfist face neutral")
    n.c "Anything is possible with the help of our awesome subscribers!"

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Incoming request..."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Whoah..."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Fifty dollars awaiting if we do this!"

    call process_character(n, appearance = "pose handsdown face happy")
    n.c "Holy cow!"

    call process_character(n, appearance = "pose handsdown face happy")
    n.c "A fifty dollar donation!?"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "This is no ordinary request or donation, that's for sure!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "We have to do several things!"

    call process_character(n, appearance = "pose handfist face neutral")
    n.c "Bring em on!"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "First..."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "You have to show off your penis!"

    call process_character(n, appearance = "pose behindhead face neutral")
    n.c "S-sure, no problem..."

    call character_leave_dissolve(n)
    $ renpy.pause(1)

    call process_character(n, appearance = "outfit nudesoft pose handsdown face neutral")
    n.c "Done!"

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "Good, good!"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Now, I have to remove my bra..."


    call character_leave_dissolve(sa)
    $ renpy.pause(1)

    call process_character(sa, appearance = "outfit topless pose handsbehind face neutral")
    sa.c "There we are!"

    call process_character(n, appearance = "pose twohandfist face neutral")
    n.c "Are we good?"

    call process_character(n, appearance = "pose twohandfist face neutral")
    n.c "Is that it?"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Not quite, not quite!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "There's one last part!"

    call process_character(n, appearance = "pose handsdown face neutral")
    n.c "..."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "You have tooo..."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "R-remove my underwear."

    call process_character(n, appearance = "pose handsdown face curious blush true")
    n.c "..."

    call process_character(n, appearance = "pose handsdown face curious blush true")
    n.c "A-and that's it?"

    call process_character(sa, appearance = "pose handface face neutral blush true")
    sa.c "T-the request will be done, yep!"

    call process_character(n, appearance = "pose handsdown face curious blush true")
    n.c "..."

    call static_still_ctc("bg sam_2_pulls_down_sam_underwear")

    sa.c "A-and there they go!"
    sa.c "..."
    sa.c "(We're doing this live, with many viewers watching!)"
    sa.c "(I hope [n.say_name] doesn't mind it)"
    sa.c "(I...)"
    sa.c "(I kinda like doing this in front of viewers...)"


    call fade_to_black(1)
    call bust_art_background(sam_room)
    $ display_multiple_characters([ (n, "outfit nudehard pose handsdown face curious blush true"), (sa, "outfit nude pose handsbehind face neutral blush false") ])

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "And there you have it!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "Both of us are now naked!"

    call process_character(sa, appearance = "pose handsbehind face neutral")
    sa.c "..."

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "And look!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "As a bonus, [n.say_name]'s penis is hard!"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "R-right, a bonus."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Oh, oh!"

    $ inventory.add_money(50, tag = "sam_3_revisit_donation")
    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Here's our donation!"

    call process_character(n, appearance = "pose behindhead face curious blush true")
    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "And it's got a message with it!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "\"Thanks for doing my request...\""

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "\"Here's a bonus, for the bonus boner.\""

    $ inventory.add_money(5, tag = "sam_3_revisit_donation_bonus")
    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "Sweet!"

    call process_character(sa, appearance = "pose handsbehind face happy")
    sa.c "[n.say_name], we got five dollars extra on top of the fifty!"

    call process_character(sa, appearance = "pose handsbehind face curious")
    sa.c "For something called a \"boner.\""

    call process_character(n, appearance = "pose handsdown face curious blush false")
    n.c "..."

    call process_character(n, appearance = "pose handsdown face curious")
    n.c "Did you ask the chat what it means?"

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "Hmm..."

    call process_character(sa, appearance = "pose handface face curious")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "Oooh..."

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "Haha, I see!"

    call process_character(n, appearance = "pose behindhead face neutral")
    n.c "What?"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "A boner is when your penis gets hard!"

    call process_character(sa, appearance = "pose handface face neutral")
    sa.c "I guess cause it's hard like bone?"

    call process_character(sa, appearance = "pose handface face happy")
    sa.c "Who cares, it's hilarious!"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "(So my penis is...)"

    call process_character(n, appearance = "pose behindhead face curious")
    n.c "(A boner?)"

    python:
        store.heard_of_boner = True
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene("sam_scene_3_revisit", char = sa, force_no_boldness = True, reset_prompted_scene = False, force_not_replayable = True, revisit = True)

    return
