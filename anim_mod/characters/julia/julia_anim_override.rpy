default julia_anal_revisit_2nd_time = False

# Debug #
init 999 python:
    config.label_overrides["debug_julia"] = "debug_julia_anim_mod"

label debug_julia_anim_mod:
    menu:
        "Julia Conversations":
            call debug_character_conversations(julia, living_room)
        "Julia Scenes":
            call debug_julia_scenes
        "Julia Anal First Scene":
            call julia_scene_anal_sex
        "Julia Anal Revisit Test":
            call julia_scene_anal_revisit
        "Julia Anal First Revisit":
            call julia_scene_anal_revisit_1st_time
        "Julia Anal Second Revisit":
            call julia_scene_anal_revisit_2nd_time
    return

# Animates Julia's anal scene #
init python:
    def julia_anal_set_speed(label, is_revisit, dream = False):
        renpy.call(label, is_revisit, dream = dream)

        return

image julia_anal_anim:
    "julia_anal_anim_0"
    pause 0.07
    "julia_anal_anim_1"
    pause 0.07
    "julia_anal_anim_2"
    pause 0.07
    "julia_anal_anim_3"
    pause 0.07
    "julia_anal_anim_4"
    pause 0.07
    "julia_anal_anim_5"
    pause 0.07
    "julia_anal_anim_6"
    pause 0.07
    "julia_anal_anim_7"
    pause 0.07
    "julia_anal_anim_8"
    pause 0.07
    "julia_anal_anim_9"
    pause 0.07
    "julia_anal_anim_10"
    pause 0.07
    "julia_anal_anim_11"
    pause 0.07
    "julia_anal_anim_12"
    pause 0.07
    "julia_anal_anim_13"
    pause 0.07
    "julia_anal_anim_14"
    repeat

# Overrides Scenes #
init 999 python:
    config.label_overrides["julia_scene_anal"] = "julia_scene_anal_anim_mod"
    config.label_overrides["julia_scene_anal_sex"] = "julia_scene_anal_sex_anim_mod"
    config.label_overrides["julia_scene_anal_revisit"] = "julia_scene_anal_revisit_anim_mod"
    config.label_overrides["julia_scene_anal_revisit_1st_time"] = "julia_scene_anal_revisit_1st_time_anim_mod"
    config.label_overrides["julia_scene_anal_revisit_2nd_time"] = "julia_scene_anal_revisit_2nd_time_anim_mod"
    config.label_overrides["julia_scene_anal_revisit_end"] = "julia_scene_anal_revisit_end_anim_mod"

init 300 python:
    anim_mod_julia_anal_old_gallery_images = Julia.gallery_images

    def anim_mod_julia_anal_gallery_images(self):
        images = anim_mod_julia_anal_old_gallery_images(self)

        if "julia_scene_anal" in scenes_completed:
            images.append("mods/leftovers_mod/images/anim_mod/animations/julia anal/julia_anal_anim_0.png")

        return images

    Julia.gallery_images = anim_mod_julia_anal_gallery_images

# Animation Class Info #
init 100 python:
    class IA_Animation_Julia_Anal_Info(IA_Animation_Info):
        def image_base_path(self):
            return "mods/leftovers_mod/images/anim_mod/animations/julia anal/"

        def image_name(self):
            return "julia_anal_anim"

        def section_data(self):
            return [ ( 0 , 14 ) ]

        def last_frame(self):
            return 14

        def frame_durations(self):
            return [0.07]

        def frame_duration_multiplier(self):
            return store.main_animation_speed

        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            if store.play_sex_sounds:
                return [["audio/sounds/smack1.ogg", "audio/sounds/smack2.ogg", "audio/sounds/smack3.ogg"]]
            return []

# Sets Animation Speeds #
init python:
    julia_anal_slow_speed_multiplier = 1.10
    julia_anal_fast_speed_multiplier = 0.75
    julia_anal_fastest_speed_multiplier = 0.5

label julia_scene_anal_anim_mod:
    call julia_scene_anal_sex_anim_mod

    return

label julia_scene_anal_sex_anim_mod(dream = False):
    $ renpy.start_predict("julia_anal_anim")
    call process_scene_beginning(hallway, char_tuple_array = [ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (julia, "outfit clothes pose handface face neutral blush false") ], dream = dream)

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "Hey [julia.say_name]."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "Whatcha up to?"

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "...{p}..."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral blush false")
    n.c "Are you thinking about something?"

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "Yeah..."

    call process_character(n, appearance = "outfit clothesjacket pose handfist face neutral blush false")
    n.c "Is it a new story idea?"

    call process_character(julia, appearance = "outfit clothes pose armcross face happy blush false")
    julia.c "Good guess..."

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "But no, that's not it."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious blush false")
    n.c "That's not it?"

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "It's...{w=1.0}not something we can discuss out here."

    call process_character(julia, appearance = "outfit clothes pose handup face neutral blush false")
    julia.c "I can tell you in your room."

    call process_character(julia, appearance = "outfit clothes pose handup face curious blush false")
    julia.c "That is, if you really want to find out."

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face neutral blush false")
    n.c "I'm too curious now!"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "Yeah, I want to know!"


    call process_new_location(nate_room, dream = dream)

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")

    call process_character(julia, appearance = "outfit clothes pose handup face neutral blush false")
    julia.c "Make sure the door is closed."

    call process_character(n, appearance = "outfit clothesjacket pose handfist face neutral blush false")
    n.c "Got it!"

    call process_character(n, appearance = "outfit clothesjacket pose handfist face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handfist face neutral blush false")
    n.c "Now can you tell me?"

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "I was tallying up all the times we've had sex this summer so far."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral blush false")
    n.c "Yeah?"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral blush false")
    n.c "I bet it was a lot."

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "That's an understatement..."

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "When I came up with the initial number, I recalculated several more times."

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "Because I truly couldn't believe it."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "What was it?"

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "The number isn't as important as what I concluded from it."

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "[n.say_name]..."

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "We've fucked me more times in the summer than all my previous times combined!"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "Is that...{w=0.5}a lot?"

    call process_character(julia, appearance = "outfit clothes pose armcross face curious blush false")
    julia.c "\"Is that a lot?\""

    call process_character(julia, appearance = "outfit clothes pose armcross face curious blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "Let me put it this way..."

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "All of the sex I've had over the past couple years, you matched during the time I've been here."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face happy blush false")
    n.c "Wooow..."

    call process_character(julia, appearance = "outfit clothes pose handup face neutral blush false")
    julia.c "Yeah..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "I like how much we've been doing it!"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "It's great!"

    call process_character(julia, appearance = "outfit clothes pose handface face happy blush false")
    julia.c "Oh, I agree."

    call process_character(julia, appearance = "outfit clothes pose handface face happy blush false")
    julia.c "I was pointing out my genuine surprise at the feat we accomplished."

    call process_character(n, appearance = "outfit clothesjacket pose handfist face happy blush false")
    n.c "You think there are awards for this sort of thing?"

    call process_character(julia, appearance = "outfit clothes pose armcross face happy blush false")
    julia.c "Ha, I doubt it."

    call process_character(julia, appearance = "outfit clothes pose armcross face happy blush false")
    julia.c "Why would we need an award?"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral blush false")
    n.c "Well, I don't know..."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral blush false")
    n.c "Just to show how impressive we are at it!"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "Imagine if there were medals, or even crowns!"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "We could be called the king and queen of fucking!"

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "The queen of fucking huh?"

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit clothes pose handface face happy blush false")
    julia.c "Not a title I'd be against receiving..."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral blush false")
    n.c "I figured there was no award or achievement for it."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face happy blush false")
    n.c "I still like pretending there is though!"

    call process_character(julia, appearance = "outfit clothes pose handup face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit clothes pose handup face neutral blush false")
    julia.c "While we're on this topic [n.say_name]..."

    call process_character(julia, appearance = "outfit clothes pose handup face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit clothes pose handup face neutral blush false")
    julia.c "There's a type of sex I've never actually tried before."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned blush false")
    n.c "There is?"

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "I've never allowed anyone to do it to me."

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "I didn't have enough confidence in them."

    call process_character(julia, appearance = "outfit clothes pose armcross face concerned blush false")
    julia.c "Plus I...{w=1.0}was nervous about doing it."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "What kind of sex is it?"

    call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit clothes pose handup face neutral blush false")
    julia.c "Anal."

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face concerned blush false")
    n.c "..."

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "Instead of a dick going into my pussy, it would go into my asshole."

    call process_character(julia, appearance = "outfit clothes pose handface face curious blush false")
    julia.c "You ever heard of it?"


    $ heard_of_anal = True

    if stats.stat_value("times_given_anal_sex") > 0:
        call process_character(n, appearance = "pose twohandfist face neutral blush false")
        n.c "Oh yeah, yeah!"

        call process_character(n, appearance = "pose twohandfist face neutral blush false")
        n.c "I've heard of it before."

        call process_character(julia, appearance = "pose armcross face curious blush false")
        julia.c "You sound a little too confident with the way you answered that."

        call process_character(julia, appearance = "pose armcross face curious blush false")
        julia.c "You're sure you've only heard of it?"

        call process_character(n, appearance = "pose handpocket face curious blush false")
        n.c "..."

        call process_character(julia, appearance = "pose armcross face neutral blush false")
        julia.c "I've heard it's tighter feeling, compared to fucking a pussy."

    else:
        call process_character(n, appearance = "pose behindhead face curious blush false")
        n.c "..."

        call process_character(n, appearance = "pose behindhead face curious blush false")
        n.c "No, I've never heard about anal..."

        call process_character(n, appearance = "pose behindhead face curious blush false")
        n.c "..."

        call process_character(n, appearance = "pose behindhead face concerned blush false")
        n.c "So it's no different than sticking my penis into your pussy?"

        call process_character(julia, appearance = "pose armcross face neutral blush false")
        julia.c "There is one major difference, from what I've been told..."

        call process_character(julia, appearance = "pose armcross face neutral blush false")
        julia.c "It's way tighter."

        call process_character(n, appearance = "pose handpocket face curious blush false")
        n.c "Tighter?"

        call process_character(julia, appearance = "pose handup face neutral blush false")
        julia.c "It means you'll have to push your dick into my ass more than you would my cunt."

        call process_character(n, appearance = "pose handpocket face concerned blush false")
        n.c "O-Oh..."


    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "Anyway..."

    call process_character(n, appearance = "pose behindhead face concerned blush false")
    n.c "So, you've never done that before?"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "No, but..."

    call process_character(julia, appearance = "pose handface face happy blush false")
    julia.c "I think I can change that."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "Like I was saying before..."

    call process_character(julia, appearance = "pose handup face neutral blush false")
    julia.c "You and I have rapidly accumulated sexual encounters."

    call process_character(julia, appearance = "pose handup face aroused blush false")
    julia.c "I've felt more and more comfortable with you when we fuck."

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "You helped me become more confident when fucking [julia.say_name]!"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "That's true."

    call process_character(julia, appearance = "pose handface face happy blush false")
    julia.c "You were clueless at first."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "..."

    call process_character(n, appearance = "pose handpocket face concerned blush false")
    n.c "I can't deny that..."

    call process_character(julia, appearance = "pose armcross face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face embarrassed blush false")
    julia.c "It's embarrassing to say this, but..."


    call process_character(n, appearance = "pose handpocket face neutral blush false")

    call process_character(julia, appearance = "pose armcross face embarrassed blush false")
    julia.c "..."

    call process_character(julia, appearance = "pose armcross face embarrassed blush false")
    julia.c "I've reached the point where...{w=1.0}I trust in your sexual ability [n.say_name]."

    call process_character(julia, appearance = "pose handface face embarrassed blush false")
    julia.c "So I want you to be the one to...{w=1.0}try it out with me."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "Are you saying..."

    call process_character(n, appearance = "pose behindhead face curious blush false")
    n.c "You want to do anal with me?"

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "I don't think I'll rely upon anyone else as much as you for this."

    call process_character(julia, appearance = "pose handface face neutral blush false")
    julia.c "In fact, my anal experiences will likely be exclusive to you."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "Sounds like you've been waiting a long time to try it!"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "Let's go for it right now!"

    call process_character(julia, appearance = "pose armcross face curious blush false")
    julia.c "Right now?"


    call character_leave_dissolve(n)
    pause 0.5

    call process_character(n, appearance = "outfit nudehard pose handfist face neutral blush false")
    pause 0.5

    call process_character(n, appearance = "outfit nudehard pose handfist face neutral blush false")
    n.c "Sure, why not?"

    call process_character(n, appearance = "outfit nudehard pose handfist face happy blush false")
    n.c "Now's the best time for it, don't you think?"

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "(Is [n.say_name] taking charge?)"

    call process_character(julia, appearance = "outfit clothes pose handface face neutral blush false")
    julia.c "..."

    call process_character(julia, appearance = "outfit clothes pose handface face aroused blush false")
    julia.c "(That's pretty sexy...)"

    call process_character(julia, appearance = "outfit clothes pose handface face aroused blush false")
    julia.c "(And it does put me in the mood to try it...)"


    call character_leave_dissolve(julia)
    pause 0.5

    call process_character(julia, appearance = "outfit nude pose handface face happy blush false")
    pause 0.5

    call process_character(julia, appearance = "outfit nude pose handface face happy blush false")
    julia.c "Okay, you motivated me!"

    call process_character(julia, appearance = "outfit nude pose armcross face neutral blush false")
    julia.c "I'm going to try my first anal, but don't get overzealous!"

    call process_character(julia, appearance = "outfit nude pose armcross face neutral blush false")
    julia.c "I want you to follow my direction, alright?"

    call process_character(julia, appearance = "outfit nude pose armcross face neutral blush false")
    julia.c "This is unknown territory for me."

    call process_character(n, appearance = "outfit nudehard pose twohandfist face neutral blush false")
    n.c "I understand."

    call process_character(n, appearance = "outfit nudehard pose twohandfist face neutral blush false")
    n.c "I'll follow your lead!"

    call process_character(julia, appearance = "outfit nude pose handface face curious blush false")
    julia.c "Your floor is clean right?"

    call process_character(n, appearance = "outfit nudehard pose handfist face neutral blush false")
    n.c "Vacuumed just this morning!"

    call process_character(julia, appearance = "outfit nude pose handface face neutral blush false")
    julia.c "Good."

    call process_character(julia, appearance = "outfit nude pose handface face neutral blush false")
    julia.c "The first step is getting into the right position."


    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call static_still_ctc("bg julia_anal_onfloor")
    julia.c "Here's the best way to do anal for the first time...{w=0.5}I think."
    n.c "You think?"


    if stats.stat_value("times_given_anal_sex") > 0:
        julia.c "What?"
        julia.c "Do you have a better way?"
        n.c "Well..."
        n.c "I just know there's other ways to..."
        julia.c "This is the position I'm comfortable trying, so we're sticking with it."

    else:
        julia.c "You know just as little as I do."
        julia.c "We have to start somewhere."
        n.c "Good point..."
        julia.c "This is the position that popped into my head, so we're sticking with it."


    julia.c "One thing [n.say_name]..."
    julia.c "Don't jam your dick in fast!"
    n.c "Should I be careful?"
    julia.c "I'd rather you do, yes."
    julia.c "I have no idea what this will feel like."
    n.c "Okay."
    julia.c "Alright, get up close to me."
    julia.c "If we wait too long you'll get soft and this will be nigh impossible."
    n.c "..."


    call static_still_ctc("bg julia_anal_butthole")
    n.c "Alright, I'm as close as I think I'm gonna get."
    julia.c "That's fine."
    julia.c "Make sure your dick is straight."
    julia.c "Line it up with my asshole."


    call static_still_ctc("bg julia_anal_butthole_dicktouch")
    julia.c "I can feel it touching!"
    julia.c "Don't push in yet though!"
    n.c "I won't."
    julia.c "..."
    julia.c "(What is this going to feel like?)"
    n.c "..."
    n.c "I'll go when you tell me [julia.say_name]."
    julia.c "..."
    julia.c "Go ahead, but slow!"


    call static_still_ctc("bg julia_anal_butthole_pushin")
    julia.c "Oh! Ooh!"
    julia.c "Aah!"
    n.c "Hrm!"
    n.c "..."
    n.c "It's really tight!"
    julia.c "I-It is?"
    julia.c "...{p}..."
    julia.c "K-Keep trying!"
    n.c "You sure?"
    julia.c "We've gotten this far [n.say_name]!"
    julia.c "If I stop now, I'll never want to try it again!"
    n.c "..."
    n.c "I think I'll have to push a bit harder..."
    julia.c "Harder than now?"
    julia.c "..."
    julia.c "Do it...{w=1.0}do what you have to!"
    n.c "Mmm!"


    if "sam_scene_anal" in scenes_completed:
        n.c "(This reminds me of when I fucked [sa.say_name] in the butt!)"
        n.c "(Although [sa.say_name] kind of fell on my dick, so it pushed in real quick...)"
        n.c "(This is a lot tougher when going slow!)"

    elif "kira_scene_anal" in scenes_completed:
        n.c "(I've never knew it could be this tight doing anal!)"
        n.c "(When I did it with [k.say_name], I put it in without any problem!)"

    elif "simone_scene_anal" in scenes_completed:
        n.c "(I've never knew it could be this tight doing anal!)"
        n.c "(When I did it with Mom, I put it in without any problem!)"

    elif "gloryhole_scene_anal" in scenes_completed:
        n.c "(I've never knew it could be this tight doing anal!)"
        n.c "(When I did it with [gloryhole_girl.say_name], I put it in without any problem!)"

    else:
        n.c "(Man, [julia.say_name] was right!)"
        n.c "(It's way tighter than going into a pussy!)"
        n.c "(Is it even possible to do this?)"


    julia.c "Aah!"
    julia.c "Keep pushing, keep pushing!"
    julia.c "{cps=40}Eventually, it has to go in-{/cps}{w=0.75}{nw}"


    call static_still_ctc("bg julia_anal_butthole_allin")
    julia.c "Gaah!"
    n.c "Ooh!"
    n.c "I saw it!"
    n.c "It finally went in!"
    julia.c "Holy fuck..."
    n.c "..."
    n.c "You okay [julia.say_name]?"
    n.c "Should I pull it back out?"
    julia.c "(My whole ass feels like it's being shocked!)"
    julia.c "(Even my pussy is sensing it!)"
    julia.c "..."
    n.c "[julia.say_name]?"
    n.c "What's it like for you?"
    julia.c "..."
    julia.c "Fuck me."
    n.c "Really?"
    julia.c "Fuck me [n.say_name]!"
    n.c "Y-You got it!"


    $ julia_anal_had_slow_speed_message = False
    $ julia_anal_had_normal_speed_message = False
    $ julia_anal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image at main_animation_transform(IA_Animation_Julia_Anal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white
    julia.c "Oooh!"
    julia.c "Fuuuck!"
    n.c "W-Wow!"
    n.c "This is something else [julia.say_name]!"
    julia.c "Yeah, yeah!"
    julia.c "Harder, harder!"
    julia.c "Put it in deeper!"
    n.c "Deeper?"
    julia.c "Get all of your cock in my ass!"
    julia.c "Every last inch!"
    n.c "..."
    n.c "(What's gotten into [julia.say_name]?)"
    n.c "(She's normally not like this when we fuck...)"

    window hide
    $ quick_menu = False
    show screen julia_anal_speed_settings(False)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call julia_scene_anal_phase_2(dream = dream)

    return

label julia_anal_set_speed(speed):
    hide screen julia_anal_speed_settings
    $ set_main_animation_speed(speed)

    return

# Speed Options #
screen julia_anal_speed_settings(is_revisit = False, dream = False):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text = "Slow", action = Function(julia_anal_set_speed, "julia_anal_go_slow",  is_revisit, dream), enabled = main_animation_speed != julia_anal_slow_speed_multiplier)
        use main_menu_button(text = "Normal", action = Function(julia_anal_set_speed, "julia_anal_go_normal",  is_revisit, dream), enabled = main_animation_speed != 1.0)
        use main_menu_button(text = "Fast", action = Function(julia_anal_set_speed, "julia_anal_go_fast",  is_revisit, dream), enabled = main_animation_speed != julia_anal_fast_speed_multiplier)

# Speed Dialogue Alternate #
label julia_anal_go_slow(is_revisit, dream = False, skip_dialog = False):
    call julia_anal_set_speed(julia_anal_slow_speed_multiplier)
    $ dice_roll = random.randint(1,4)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                julia.c "([n.say_name]'s cock is as big as I can handle!)"
                julia.c "(His dick takes up all the space in my ass!)"
                julia.c "Gah!"

            else:
                julia.c "(Ah, f-fuck...)"
                julia.c "(My ass is more sensitive when he goes slower)"

        else:
            if dice_roll == 1:
                julia.c "Mm, yes!"
                julia.c "Push my ass open [n.say_name]!"
                julia.c "Spread it wide with your cock!"

            elif dice_roll == 2:
                n.c "..."
                n.c "(It's like doing anal totally changed her attitude...)"

            elif dice_roll == 3:
                n.c "Ahn..."
                n.c "..."
                n.c "(This must feel really good for her to act so different)"

            else:
                julia.c "(I've never been able to orgasm more than once during a fuck...)"
                julia.c "(I just had a third one!)"

        window hide
        with None
        $ julia_anal_had_slow_speed_message = True

    if julia_anal_revisit_2nd_time:
        $ renpy.call("julia_scene_anal_revisit_phase_2_2nd_revisit")

    elif is_revisit:
        $ renpy.call("julia_scene_anal_revisit_phase_2")

    else:
        $ renpy.call("julia_scene_anal_phase_2", dream = dream)

    return

label julia_anal_go_normal(is_revisit, dream = False, skip_dialog = False):
    call julia_anal_set_speed(1.0)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                julia.c "{i}Gasp!{/i}"
                julia.c "(Fuck, [n.say_name] is so deep!)"

            else:
                n.c "Ah!"
                n.c "[julia.say_name[0]]-[julia.say_name], [julia.say_name]!"

        else:
            if random.randint(0,1) == 0:
                julia.c "Haah!"
                julia.c "More, {i}pant.{/i}..{w=0.5}more, [n.say_name]!"

            else:
                julia.c "..."
                julia.c "(It may be possible that since it's my first time with anal, I wasn't prepared for its stimulation...)"
                julia.c "..."
                julia.c "(That can't be the real reason...)"
                julia.c "(No, I think this is where the most sensitive area of my body is!)"

        window hide
        with None
        $ julia_anal_had_normal_speed_message = True

    if julia_anal_revisit_2nd_time:
        $ renpy.call("julia_scene_anal_revisit_phase_2_2nd_revisit")

    elif is_revisit:
        $ renpy.call("julia_scene_anal_revisit_phase_2")

    else:
        $ renpy.call("julia_scene_anal_phase_2", dream = dream)

    return

label julia_anal_go_fast(is_revisit, dream = False, skip_dialog = False):
    call julia_anal_set_speed(julia_anal_fast_speed_multiplier)
    $ dice_roll = random.randint(1,3)

    if not skip_dialog:
        if is_revisit:
            if dice_roll == 1:
                julia.c "..."
                julia.c "(I feel so primal during this!)"
                julia.c "(It's a raw surge of lust in my psyche!)"

            elif dice_roll == 2:
                n.c "Oh, oh!"
                n.c "([julia.say_name]'s ass really squeezes my dick!)"

            else:
                julia.c "K-keep.."
                julia.c "Keep going, [n.say_name]!"
                julia.c "Fuck me!"

        else:
            if random.randint(0,1) == 0:
                julia.c "..."
                julia.c "(I've lost control over myself!)"
                julia.c "(I'm being bombarded by pleasure!)"

            else:
                julia.c "Mmm!"
                julia.c "(This supersedes any fuck I've done before!)"

        window hide
        with None
        $ julia_anal_had_fast_speed_message = True

    if julia_anal_revisit_2nd_time:
        $ renpy.call("julia_scene_anal_revisit_phase_2_2nd_revisit")

    elif is_revisit:
        $ renpy.call("julia_scene_anal_revisit_phase_2")

    else:
        $ renpy.call("julia_scene_anal_phase_2", dream = dream)

    return

# Advances the animation into the normal scene #
label julia_scene_anal_phase_2(skip_dialog = False, dream = dream):
    show screen julia_anal_speed_settings(False, True)
    call screen progress_button_screen("Cum!")
    $ quick_menu = True
    hide screen julia_anal_speed_settings
    $ renpy.suspend_rollback(False)

    call julia_scene_anal_phase_3(dream = dream)

    return

label julia_scene_anal_phase_3(dream = dream):
    $ renpy.suspend_rollback(True)
    $ quick_menu = False
    n.c "[julia.say_name]..."
    n.c "What should I do when I come?"
    julia.c "{i}Pant,{/i} {i}pant.{/i}.."
    julia.c "Mm, Mm!"
    n.c "..."
    n.c "Do you want me to come in your ass?"
    julia.c "Oh, that's so fucking good!"
    julia.c "Yes!"
    julia.c "Like that, yes!"
    n.c "..."
    n.c "(I don't even think she's hearing me...)"
    n.c "Mmn!"
    n.c "(I know I'll be coming shortly!)"
    n.c "(We haven't even stopped for a second!)"
    n.c "..."
    julia.c "Finish in me, [n.say_name]!"
    julia.c "I know you have a lot of cum in those balls!"
    julia.c "I want it to pour into my ass!"


    call julia_anal_set_speed(julia_anal_fastest_speed_multiplier)
    n.c "..."
    n.c "I-I'll give it to you [julia.say_name]!"
    n.c "I'll give it all!"
    n.c "Haaah!"


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
    show bg julia_anal_fuck_cuminside
    with Dissolve(1.5)

    pause
    $ quick_menu = True

    julia.c "{i}Gasp!{/i}"
    julia.c "Creampie my ass!"
    n.c "Mm!{p}Mm!"
    julia.c "I-I can't hold it all in!"
    julia.c "There's no way I can!"
    julia.c "Pull out [n.say_name]!"


    call static_still_ctc("bg julia_anal_fuck_cum")
    n.c "(There's still some cum attached to my dick!)"
    n.c "([julia.say_name] told me to pull out before I could completely finish!)"
    julia.c "{i}Pant,{/i} {i}pant.{/i}.."
    julia.c "My ass can't handle that much cum!"
    julia.c "I should have known!"
    julia.c "Oooh..."


    call static_still_ctc("bg julia_anal_aftercum")
    julia.c "..."
    n.c "..."
    n.c "Hey, [julia.say_name]?"
    n.c "[julia.say_name]?"
    n.c "..."
    n.c "(We didn't overdo it, did we?)"
    julia.c "I'm..."
    julia.c "I'm fine."
    julia.c "Just give me a few moments."
    julia.c "{i}Phew.{/i}.."
    n.c "I've never seen you like that before!"
    n.c "You said some crazy stuff!"
    julia.c "..."
    julia.c "I didn't expect anal to feel that way..."
    julia.c "..."
    julia.c "B-But it may have just been a fluke!"
    n.c "Hm, maybe..."
    n.c "You think we should do anal again soon?"
    julia.c "Yes!"
    julia.c "We should do it again!"
    n.c "..."
    julia.c "I-I mean, we should do anal again to see if it was indeed a fluke on how it felt!"
    julia.c "Maybe try it a few more times just to be certain!"
    n.c "Oh, uh..."
    n.c "Sure!"
    n.c "I won't complain!"
    julia.c "..."
    julia.c "Can you grab me a towel?"
    julia.c "Cum is running down my leg..."


    $ renpy.stop_predict("julia_anal_anim")

    python:
        julia.revistable_scenes.add("julia_scene_anal_revisit")

        if not dream:
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_butt", 1)
            stats.add_stat("times_seen_butthole", 1)
            stats.add_stat("times_given_anal_sex", 1)
            stats.add_stat("times_given_anal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene("julia_scene_anal", char = julia, dream = dream)

    return

label julia_scene_anal_revisit_anim_mod:
    $ renpy.start_predict("sam_vaginal_anim")

    if "julia_scene_anal_revisit" not in scenes_completed:
        jump julia_scene_anal_revisit_1st_time_anim_mod
    else:
        jump julia_scene_anal_revisit_2nd_time_anim_mod

    return

label julia_scene_anal_revisit_1st_time_anim_mod:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose twohandfist face neutral"), (julia, "pose handface face flirty blush false") ])
    julia.c "I was just about to ask you the same."
    julia.c "I want to see how it feels a second time around."

    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call static_still_ctc("bg julia_anal_onfloor")
    julia.c "This is how I was before, right?"
    n.c "Just like that, yep."
    julia.c "I'm not really ready to try some elaborate position for anal."
    julia.c "This accomplishes what we both want just fine."

    call static_still_ctc("bg julia_anal_butthole_dicktouch")
    n.c "Should I go in slow like before?"
    julia.c "Yes."
    julia.c "But push more than the first time."
    julia.c "I want to get straight to it!"


    call static_still_ctc("bg julia_anal_butthole_pushin")
    n.c "Like this right?"
    julia.c "Mm, ah..."
    julia.c "Little more, little more..."
    n.c "It's moving slightly!"
    julia.c "Any moment now..."

    call static_still_ctc("bg julia_anal_butthole_allin")
    julia.c "Ooh, it popped in!"
    julia.c "(My ass is pulsing already!)"
    n.c "Ahn!"
    n.c "I got my dick in a bit faster this time..."

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    call julia_anal_set_speed(julia_anal_fast_speed_multiplier)
    show anim_nothing_image at main_animation_transform(IA_Animation_Julia_Anal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white
    $ renpy.pause(1.50)
    $ quick_menu = True

    $ renpy.suspend_rollback(True)
    n.c "Hoo!"
    n.c "I think it still feels awesome!"
    julia.c "N-No shit!"
    julia.c "Ah, fuck!"
    julia.c "Keep the speed up!"
    n.c "N-Not a problem!"
    n.c "My body wants to go faster!"
    julia.c "Mmn, oh, aah!"
    n.c "..."

    if "sam_scene_anal" in scenes_completed:
        n.c "(I should see if [sa.say_name] would like to do this position)"
        n.c "(I'll bet she'll like it just as much as [julia.say_name] does!)"
        n.c "([sa.say_name] would probably want to take a photo of me sticking it in her butt so she could see it...)"

    elif "kira_scene_anal" in scenes_completed:
        n.c "(This position reminds me a bit of when [k.say_name] was letting me slide my penis between her butt cheeks...)"
        n.c "(But when we did anal she just sat on me!)"
        n.c "..."
        n.c "(It was fun how she went up and down on my penis though....)"

    elif "simone_scene_anal" in scenes_completed:
        n.c "(Mom and I were doing a position kind of like this)"
        n.c "(If I recall though, Mom was letting me lean on her)"
        n.c "(I think [julia.say_name] would get mad if I tried that...)"
        n.c "(She'd probably fall onto the ground from my weight)"

    julia.c "{i}Pant.{/i}.."
    julia.c "[n.say_name]..."
    julia.c "You're going to visit my house a lot after the summer."
    julia.c "Ah, ooh!"
    julia.c "Schedule at least one day every week to stop by!"

    if "janet_scene_blowjob" in scenes_completed:
        julia.c "Shouldn't be a problem since you go to my house a lot already!"
        n.c "School might make it tougher..."
        julia.c "You'll need to make it work [n.say_name]!"
        julia.c "Mm!"
        julia.c "We need to keep fucking into the fall, winter, and beyond!"

    else:
        n.c "I hope I can make that work..."
        julia.c "You'll need to make it work [n.say_name]!"
        julia.c "Mm!"
        julia.c "We need to keep fucking into the fall, winter, and beyond!"

    n.c "Maybe you can come over one week, and then I come over the next."
    julia.c "So you're saying we alternate?"
    julia.c "Ahn!"
    julia.c "Y-Yeah, that could work."

    window hide
    $ quick_menu = False
    show screen julia_anal_speed_settings(True)
    $ renpy.suspend_rollback(True)

    call julia_scene_anal_revisit_phase_2

    return

label julia_scene_anal_revisit_phase_2:
    $ quick_menu = False
    window hide
    show screen julia_anal_speed_settings(True, True)
    call screen progress_button_screen("Cum!")
    $ renpy.scene('screens')
    hide screen julia_anal_speed_settings
    $ renpy.suspend_rollback(False)

    call julia_scene_anal_revisit_1st_time_phase_3_anim_mod

    return

label julia_scene_anal_revisit_1st_time_phase_3_anim_mod:
    n.c "L-Let me come in your ass again [julia.say_name]!"
    julia.c "Aah, Mm!"
    n.c "I really want to!"
    julia.c "I'm not stopping you!"
    julia.c "D-Do what you like [n.say_name]!"
    n.c "I'm gonna push in all the way!"
    n.c "Here I go!"
    n.c "Hnng!"

    call julia_anal_set_speed(julia_anal_fastest_speed_multiplier)

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
    show bg julia_anal_fuck_cuminside
    with Dissolve(1.5)

    pause
    $ quick_menu = True
    julia.c "Hyaaa!"
    julia.c "So much!{p}So much!"

    call static_still_ctc("bg julia_anal_fuck_cum")
    n.c "I kept coming longer than I thought!"
    julia.c "Good thing you, {i}pant,{/i} {w=0.5}pulled out!"
    julia.c "My ass felt ready to explode!"

    call static_still_ctc("bg julia_anal_aftercum")
    n.c "There is some cum shooting out of your ass right now!"
    julia.c "I-I know!"
    julia.c "I'm trying to push it out!"
    julia.c "Your cum is so thick, it's tough to do!"
    n.c "Maybe I shouldn't come in your ass then..."
    julia.c "No!"
    julia.c "Keep doing it!"
    n.c "..."
    julia.c "I don't want to miss out on how I feel when your hot load pours into my ass!"
    julia.c "This is just a trade-off I have to live with!"

    jump julia_scene_anal_revisit_end_anim_mod

    return

label julia_scene_anal_revisit_2nd_time_anim_mod:
    $ no_bust_art = True

    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call julia_anal_set_speed(julia_anal_fast_speed_multiplier)

    $ julia_anal_had_slow_speed_message = False
    $ julia_anal_had_normal_speed_message = False
    $ julia_anal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    show anim_nothing_image at main_animation_transform(IA_Animation_Julia_Anal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white

    pause
    $ quick_menu = True
    julia.c "Mmm, yes!"
    julia.c "..."
    julia.c "(I've gained some control over myself now when doing this...)"
    julia.c "Fuck!"
    julia.c "Fucking fuck me [n.say_name]!"
    julia.c "(Maybe not as much control as I thought!)"
    julia.c "..."
    julia.c "(I sound like a total slut when I do this!)"
    julia.c "(I swear, if [n.say_name] tells anyone how I act during anal...)"
    julia.c "..."
    julia.c "(He just needs to be told to keep an oath of silence about this)"
    julia.c "(And if he breaks it, no more fucking for him!)"
    julia.c "(Little chance [n.say_name] will say anything with that stipulation!)"
    n.c "..."
    n.c "(I hope [sa.say_name] is wearing headphones in her room)"
    n.c "([julia.say_name] can get kinda loud during this...)"
    n.c "..."
    n.c "(If we were on my bed, it might bang against the wall)"
    julia.c "..."
    julia.c "([n.say_name]'s filled all my holes now)"
    julia.c "(I give my mouth, pussy and ass to none other than my cousin)"
    julia.c "(It's a little weird to think about)"
    julia.c "(But until someone better comes along, which I doubt will happen...)"
    julia.c "(I'll accept I'm fucking a blood relative!)"

    window hide
    $ quick_menu = False
    show screen julia_anal_speed_settings(True)
    $ renpy.suspend_rollback(True)

    call julia_scene_anal_revisit_phase_2_2nd_revisit

    return

label julia_scene_anal_revisit_phase_2_2nd_revisit:
    $ julia_anal_revisit_2nd_time = True

    $ quick_menu = False
    window hide
    show screen julia_anal_speed_settings(True, True)
    call screen progress_button_screen("Cum!")
    $ renpy.scene('screens')
    hide screen julia_anal_speed_settings
    $ renpy.suspend_rollback(False)

    call julia_scene_anal_revisit_2nd_time_phase_3_anim_mod

    return

label julia_scene_anal_revisit_2nd_time_phase_3_anim_mod:
    $ quick_menu = False
    hide screen julia_anal_speed_settings
    call julia_anal_set_speed(julia_anal_fastest_speed_multiplier)

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
    show bg julia_anal_fuck_cuminside
    with Dissolve(1.5)

    pause
    $ quick_menu = True
    n.c "Aaah..."
    julia.c "Mmmn!"
    julia.c "(I orgasm every time it happens!)"

    call static_still_ctc("bg julia_anal_fuck_cum")
    n.c "{i}Whew.{/i}.."
    julia.c "{i}Pant,{/i} {i}pant.{/i}.."
    julia.c "I may need to rest on your bed after that, [n.say_name]!"

    jump julia_scene_anal_revisit_end_anim_mod

    return

label julia_scene_anal_revisit_end_anim_mod:
    $ stop_music(fadeout=1)
    $ renpy.stop_predict("julia_anal_anim")

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_incestual_situation", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_seen_butt", 1)
        stats.add_stat("times_seen_butthole", 1)
        stats.add_stat("times_given_anal_sex", 1)
        stats.add_stat("times_given_anal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene("julia_scene_anal_revisit", char = julia, force_no_boldness = True, reset_prompted_scene = False, force_not_replayable = True, revisit = True)

    return