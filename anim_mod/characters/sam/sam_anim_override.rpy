default sam_off_stream_revisit_complete = False

# Debug #
init 999 python:
    config.label_overrides["debug_sam"] = "debug_sam_anim_mod"

label debug_sam_anim_mod:
    menu:
        "Sam Scenes":
            call debug_sam_scenes
        "Sam Conversations":
            call debug_character_conversations(sa, sam_room)
        "Sam Vaginal First Scene":
            call sam_scene_vaginal_sex
        "Sam Vaginal Revisit On Stream":
            call sam_scene_vaginal_revisit_on_stream
        "Sam Vaginal Revisit Test":
            call sam_scene_vaginal_revisit
        "Sam Vaginal Revisit Off Stream":
            call sam_scene_vaginal_revisit_off_stream
    return

# Animates Sam's vaginal scene #
init python:
    def sam_vaginal_set_speed(label, is_revisit, dream = False):
        renpy.call(label, is_revisit, dream = dream)

        return

image sam_vaginal_anim:
    "sam_vaginal_anim_0"
    pause 0.08
    "sam_vaginal_anim_1"
    pause 0.08
    "sam_vaginal_anim_2"
    pause 0.08
    "sam_vaginal_anim_3"
    pause 0.08
    "sam_vaginal_anim_4"
    pause 0.08
    "sam_vaginal_anim_5"
    pause 0.08
    "sam_vaginal_anim_6"
    pause 0.08
    "sam_vaginal_anim_7"
    pause 0.08
    "sam_vaginal_anim_8"
    pause 0.08
    "sam_vaginal_anim_9"
    pause 0.08
    "sam_vaginal_anim_10"
    pause 0.08
    "sam_vaginal_anim_11"
    pause 0.08
    "sam_vaginal_anim_12"
    pause 0.08
    "sam_vaginal_anim_13"
    pause 0.08
    "sam_vaginal_anim_14"
    repeat

# Overrides Scenes #
init 200 python:
    config.label_overrides["sam_scene_vaginal_sex"] = "sam_scene_vaginal_sex_anim_mod"
    config.label_overrides["sam_scene_vaginal_revisit"] = "sam_scene_vaginal_revisit_anim_mod"
    config.label_overrides["sam_scene_vaginal_revisit_on_stream"] = "sam_scene_vaginal_revisit_on_stream_anim_mod"
    config.label_overrides["sam_scene_vaginal_revisit_off_stream"] = "sam_scene_vaginal_revisit_off_stream_anim_mod"
    config.label_overrides["sam_scene_vaginal_revisit_end"] = "sam_scene_vaginal_revisit_end_anim_mod"

init 200 python:
    anim_mod_sam_vaginal_old_gallery_images = Sam.gallery_images

    def anim_mod_sam_vaginal_gallery_images(self):
        images = anim_mod_sam_vaginal_old_gallery_images(self)

        if "sam_scene_vaginal" in scenes_completed:
            images.append("mods/leftovers_mod/images/anim_mod/animations/sam vaginal/sam_vaginal_anim_0.png")

        return images

    Sam.gallery_images = anim_mod_sam_vaginal_gallery_images

# Animation Class Info #
init 100 python:
    class IA_Animation_Sam_Vaginal_Info(IA_Animation_Info):
        def image_base_path(self):
            return "mods/leftovers_mod/images/anim_mod/animations/sam vaginal/"

        def image_name(self):
            return "sam_vaginal_anim"

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
    sam_vaginal_slow_speed_multiplier = 1.10
    sam_vaginal_fast_speed_multiplier = 0.75
    sam_vaginal_fastest_speed_multiplier = 0.5

init 100 python:
    def prompt_label(self, scene_name):
        if scene_name == "sam_scene_1_seq_1":
            return "I'm ready to stream!"
        elif scene_name == "sam_scene_1_seq_2":
            return "Let's fire up the stream again!"
        elif scene_name == "sam_scene_2_seq_1":
            return "Alright, tell me about the updates!"
        elif scene_name == "sam_scene_2_seq_2":
            return "L-let's be in our underwear again."
        elif scene_name == "sam_scene_4":
            return "W-what did you want to know about my penis?"
        elif scene_name == "sam_scene_vaginal":
            return "Alright, I'm ready to go for the stream!"

        return ""

    Sam.prompt_label = prompt_label

# Scenes #
label sam_scene_vaginal_anim_mod:
    $ display_multiple_characters([ (n, ""), (sa, "") ])
    sa.c "[n.say_name]!"
    sa.c "Dude, I got into the early access of Demon Can Laugh 2!"
    sa.c "If we stream the game, we'll be one of the few people playing it!"
    sa.c "We'll get loads of viewers for sure!"
    sa.c "Let's jump into it right now!"


    call prompt_menu_boldness_check("This stream will be epic!", "I'm kind of tied up today.", "sam_scene_vaginal", sa)

    return

label sam_scene_vaginal_refusal_anim_mod(text, insufficient_points):
    if insufficient_points:
        call process_character(n, appearance = "pose behindhead face neutral", text = text)
        call process_character(n, appearance = "pose behindhead face concerned")
        n.c "(I-I don't know if I'm ready to stream naked in front of a lot more people...)"

        call process_character(n, appearance = "pose behindhead face curious")
        n.c "(What if [sa.say_name] wants to try something new with me?)"

    else:
        call process_character(n, appearance = "pose behindhead face neutral")

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "Well, untie yourself then!"

    call process_character(sa, appearance = "pose leaning face neutral")
    sa.c "This window of opportunity won't be open forever, you know!"


    call prompt_refusal_end(sa)

    return

#label sam_scene_vaginal_anim_mod:
#    call sam_scene_vaginal_sex_anim_mod

#    return

label sam_scene_vaginal_sex_anim_mod(dream = False):
    $ renpy.start_predict("sam_vaginal_anim")
    call process_scene_beginning(bg = "bg sam_room_evening", char_tuple_array = [ (n, "outfit nudesoft pose handsdown"), (sa, "outfit nude pose leaning face happy") ], dream = dream )

    call process_character(sa, appearance = "pose leaning face happy blush false")
    sa.c "Thanks everyone for stopping by our stream!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "We'll be showing some more early access of Demon Can Laugh 2 next time!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "I'm really digging it so far!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "The controls are way better than the first one!"

    call process_character(n, appearance = "pose twohandfist face neutral blush false")
    n.c "And the framerate is super smooth, no lag spikes!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "Makes the fighting gameplay way more fun!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "Anyway, we will see you all again soon!"


    call process_character(sa, appearance = "pose leaning face happy blush false")
    call process_character(n, appearance = "pose handfist face happy blush false")
    "[sa.say_name] & [n.say_name]" "\"Twinsticks Disconnected!\""
    call process_character(n, appearance = "pose handsdown face neutral blush false")

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face happy blush false")
    sa.c "Holy moly, that stream!"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "It was insane!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "We had one thousand people online!"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "That's more than double what we usually get!"

    call process_character(n, appearance = "pose handsdown face neutral blush false")
    n.c "People love seeing early access games."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "It's because they can find out if it's good or not!"

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "I'd want to know before placing a pre-order!"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "They also like seeing us and how we do the stream."

    call process_character(n, appearance = "pose handsdown face neutral blush false")
    n.c "Definitely."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "Like, everyone expects us with no clothes all the time now."

    call process_character(sa, appearance = "pose leaning face neutral blush false")
    sa.c "I heard some people are trying to copycat with their own naked streams."

    call process_character(sa, appearance = "pose handface face happy blush false")
    sa.c "But they can't match the original!"

    call process_character(n, appearance = "pose handsdown face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "pose handsdown face neutral blush false")
    n.c "I feel like we should wind down with something after a long stream."

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "Want to watch a movie or listen to some music?"

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face curious blush false")
    sa.c "I was actually thinking..."

    call process_character(n, appearance = "pose handsdown face neutral blush false")
    n.c "Hm?"

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "Well..."

    call process_character(sa, appearance = "pose handface face neutral blush false")
    sa.c "I wanted to do something different to celebrate this epic stream!"

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "Oh yeah?"

    call process_character(n, appearance = "pose behindhead face neutral blush false")
    n.c "What did you want to try?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush false")
    sa.c "It was something I saw online."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "It..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush false")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "It showed a penis going into a vagina."

    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "O-Oh..."

    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "Yeah?"

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "Actually..."

    call process_character(sa, appearance = "pose handsbehind face concerned blush true")
    sa.c "The video title said \"Dick shoved in tight pussy\" or something like that..."

    call process_character(n, appearance = "pose handsdown face concerned blush true")
    n.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "I..."

    call process_character(sa, appearance = "pose handface face concerned blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "I want us to do that!"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "{i}Gulp!{/i}"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "Y-You sure?"

    call process_character(sa, appearance = "pose handface face neutral blush true")
    sa.c "I know, we've never done that before..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "But it looked super easy!"

    call process_character(n, appearance = "pose behindhead face concerned blush true")
    n.c "..."

    call process_character(n, appearance = "pose behindhead face concerned blush true")
    n.c "O-Okay."

    call process_character(n, appearance = "pose behindhead face curious blush true")
    n.c "But, can you let me know what to do?"

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "Sure!"

    call process_character(sa, appearance = "pose leaning face neutral blush true")
    sa.c "Trust me, it's a breeze!"

    call process_character(n, appearance = "pose handsdown face curious blush true")
    n.c "..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "Here, watch."

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "I'll just copy exactly what I saw."

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "..."

    call process_character(sa, appearance = "pose handsbehind face neutral blush true")
    sa.c "First, need to lay on my back..."


    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg sam_vaginal_spread")
    n.c "..."
    sa.c "A-Ah..."
    sa.c "The girl in the video was spreading her pussy with her fingers like this."
    sa.c "I-I like how it feels."
    n.c "..."
    n.c "So, {w=0.5}what do I do?"
    sa.c "You have to lay on top of me."
    n.c "L-Lay on top of you?"
    sa.c "When you start to lay on me..."
    sa.c "Y-You put your dick in my pussy."


    call static_still_ctc("bg sam_vaginal_dick_out")
    n.c "L-like this?"
    sa.c "I-I can feel it starting to go in..."
    n.c "Y-yeah, ah..."
    sa.c "..."
    sa.c "You need to push it all the way in."
    sa.c "P-Push your body down on me..."


    call static_still_ctc("bg sam_vaginal_dick_in_eyes_closed")
    sa.c "Haaah!"
    sa.c "([n.say_name]'s in me!)"
    n.c "(It's warm!)"
    sa.c "Mmm, a-ah."
    sa.c "..."


    call static_still_ctc("bg sam_vaginal_dick_in")
    sa.c "Can you do some movement?"
    n.c "M-Movement?"
    sa.c "We don't stay still like this."
    sa.c "You lift up, and come back down."


    call static_still_ctc("bg sam_vaginal_dick_out")
    n.c "..."


    call static_still_ctc("bg sam_vaginal_dick_in_eyes_closed")
    sa.c "Ahn!"
    sa.c "..."


    call static_still_ctc("bg sam_vaginal_dick_in")
    sa.c "D-Do that again."


    call static_still_ctc("bg sam_vaginal_dick_out")
    n.c "..."


    call static_still_ctc("bg sam_vaginal_dick_in")
    n.c "Ahh, t-that does feel good."
    n.c "(M-My dick is slippery after going into [sa.say_name]...)"
    sa.c "(E-Every time he does it...)"


    call static_still_ctc("bg sam_vaginal_dick_out")
    sa.c "...{p}..."

    pause 1.0
    n.c "{i}Pant, Pant{/i}"
    sa.c "([n.say_name]'s panting like a dog)"
    sa.c "(H-He's thrusting harder each time...)"


    call static_still_ctc("bg sam_vaginal_dick_in")
    n.c "{i}Pant{/i}"

    $ n.c(sa.say_name[0] + "-" + sa.say_name + "...")
    n.c "I-It's getting tighter inside you."
    sa.c "Mmm, I feel it too!"
    n.c "S-should I keep going?"
    sa.c "I-I think you should..."
    sa.c "It's been feeling great."
    n.c "M-Me too, ah!"


    $ sam_vaginal_had_slow_speed_message = False
    $ sam_vaginal_had_normal_speed_message = False
    $ sam_vaginal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image at main_animation_transform(IA_Animation_Sam_Vaginal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white

    window hide
    $ quick_menu = False
    show screen sam_vaginal_speed_settings(False)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call sam_scene_vaginal_phase_2(dream = dream)

    return

label sam_vaginal_set_speed(speed):
    hide screen sam_vaginal_speed_settings
    $ set_main_animation_speed(speed)

    return

# Speed Options #
screen sam_vaginal_speed_settings(is_revisit = False, dream = False):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text = "Slow", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_slow",  is_revisit, dream), enabled = main_animation_speed != sam_vaginal_slow_speed_multiplier)
        use main_menu_button(text = "Normal", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_normal",  is_revisit, dream), enabled = main_animation_speed != 1.0)
        use main_menu_button(text = "Fast", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_fast",  is_revisit, dream), enabled = main_animation_speed != sam_vaginal_fast_speed_multiplier)

# Speed Dialogue Alternate #
label sam_vaginal_go_slow(is_revisit, dream = False, skip_dialog = False):
    call sam_vaginal_set_speed(sam_vaginal_slow_speed_multiplier)
    $ dice_roll = random.randint(0,1)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                sa.c "G-Going slower?"
                sa.c "Yeah, no need to rush things, I-I guess.."
                sa.c "We should be enjoying this."

            else:
                n.c "(The skin on my penis moves when I...)"
                n.c "..."
                n.c "(Push in and pull out)"

        else:
            if random.randint(0,1) == 0:
                sa.c "G-Going slower?"
                sa.c "Yeah, no need to rush things, I-I guess.."
                sa.c "We should be enjoying this."

            else:
                n.c "(The skin on my penis moves when I...)"
                n.c "..."
                n.c "(Push in and pull out)"


        window hide
        with None
        $ sam_vaginal_had_slow_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2")
    else:
        $ renpy.call("sam_scene_vaginal_phase_2", dream = dream)

    return

label sam_vaginal_go_normal(is_revisit, dream = False, skip_dialog = False):
    call sam_vaginal_set_speed(1.0)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                sa.c "..."
                sa.c "(I wonder if it will feel weird if [n.say_name]...)"
                sa.c "(Comes while he's doing this?)"

            else:
                sa.c "Ah!"
                sa.c "This feels great, [n.say_name]!"

        else:
            if random.randint(0,1) == 0:
                sa.c "..."
                sa.c "(I wonder if it will feel weird if [n.say_name]...)"
                sa.c "(Comes while he's doing this?)"

            else:
                sa.c "Ah!"
                sa.c "This feels great, [n.say_name]!"


        window hide
        with None
        $ sam_vaginal_had_normal_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2")
    else:
        $ renpy.call("sam_scene_vaginal_phase_2", dream = dream)

    return

label sam_vaginal_go_fast(is_revisit, dream = False, skip_dialog = False):
    call sam_vaginal_set_speed(sam_vaginal_fast_speed_multiplier)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                sa.c "W-Woah!"
                sa.c "This really is just like the video!"

            else:
                sa.c "Ah..."
                sa.c "(I feel a rush of excitement!)"

        else:
            if random.randint(0,1) == 0:
                sa.c "W-Woah!"
                sa.c "This really is just like the video!"

            else:
                sa.c "Ah..."
                sa.c "(I feel a rush of excitement!)"


        window hide
        with None
        $ sam_vaginal_had_fast_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2")
    else:
        $ renpy.call("sam_scene_vaginal_phase_2", dream = dream)

    return

# Advances the animation into the normal scene #
label sam_scene_vaginal_phase_2(skip_dialog = False, dream = dream):
    show screen sam_vaginal_speed_settings(False, dream = dream)
    call screen progress_button_screen("Continue")
    $ quick_menu = True
    hide screen sam_vaginal_speed_settings
    $ renpy.suspend_rollback(False)

    call sam_scene_vaginal_phase_3(dream = dream)

    return

label sam_scene_vaginal_phase_3(dream = False):
    $ renpy.suspend_rollback(True)
    $ quick_menu = False
    n.c "Ah, ooh..."
    n.c "(If I keep going, the jizz will go into [sa.say_name]'s...)"
    n.c "..."
    n.c "D-Did you want me to {w=1.0}come while we're doing this?"
    sa.c "Ah, ah!"
    sa.c "Only if you want to..."
    n.c "Y-yeah, let's try it."
    sa.c "I-I want to see if I can tell when it happens."


    call sam_vaginal_set_speed(sam_vaginal_fast_speed_multiplier)
    n.c "..."
    n.c "(It won't be much longer...)"
    n.c "(My dick is hot!)"
    sa.c "(The lower half of me is trembling)"
    sa.c "(I-I can't control it...)"


    call sam_vaginal_set_speed(sam_vaginal_fastest_speed_multiplier)
    n.c "Oh!"
    n.c "(I-It's definitely that time...)"
    n.c "(A jolt is going through my penis)"
    n.c "Hurgh!"


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
    show bg sam_vaginal_xray_cum
    with Dissolve(1.5)

    pause
    $ quick_menu = True
    sa.c "..."
    sa.c "(H-He's spurting inside...)"
    sa.c "..."
    sa.c "(It's a funny feeling...)"
    sa.c "(B-But a nice feeling)"
    n.c "..."
    n.c "(I wonder how much is in her...)"
    n.c "..."
    n.c "D-Did you feel it?"
    sa.c "I-I did."
    n.c "..."
    n.c "Do you know if it can come out?"
    sa.c "I-I don't know..."
    sa.c "..."
    sa.c "Maybe when you pull out, some of it will?"
    n.c "Hm, you think?"
    n.c "..."


    call static_still_ctc("bg sam_vaginal_spread_cum")
    n.c "I do see some of it!"
    n.c "Some of it is coming out!"
    sa.c "..."
    sa.c "Well [n.say_name]..."
    sa.c "W-We were fucking."
    n.c "T-That was fucking?"
    n.c "..."
    sa.c "I guess it was one way of fucking, yeah."
    n.c "You mean, there are more ways?"
    sa.c "From what I've seen..."
    sa.c "A lot more."


    $ renpy.stop_predict("sam_vaginal_anim")

    python:
        sa.revistable_scenes.add("sam_scene_vaginal_revisit")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_flat_breasts", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_incestual_situation", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene("sam_scene_vaginal", char = sa, dream = dream)

    return

# Revisits #
init 100 python:
    def revisitable_scene_choice_label(self, scene_name):
        if scene_name == "sam_scene_1_revisit":
            return "I'm feeling up for streaming!"

        if scene_name == "sam_scene_2_revisit":
            return "Did you want to look at my penis again?"

        if scene_name == "sam_scene_3_revisit":
            return "Let's stream for some more donations!"

        if scene_name == "sam_scene_4_revisit":
            return "Did you want to...rub against each other again?"

        if scene_name == "sam_scene_vaginal_revisit":
            if "sam_scene_vaginal_revisit" not in scenes_completed:
                return "Shall we fuck again?"
            elif sam_off_stream_revisit_complete and "sam_scene_vaginal_revisit" in store.scenes_completed:
                return "Let's fuck!"
            else:
                return "Can we fuck off-stream?"

        if scene_name == "sam_scene_blowjob_revisit":
            if "sam_scene_blowjob_revisit" not in scenes_completed:
                return "Can you put your mouth on my dick again?"
            else:
                return "Can you suck my dick again?"

        if scene_name == "sam_scene_anal_revisit":
            if "sam_scene_anal_revisit" not in scenes_completed:
                return "Can I stick my dick in your butt [sa.say_name]?"
            else:
                return "Let's do some more butt fucking!"

        if scene_name == "sam_scene_swimsuit_revisit":
            if "sam_scene_swimsuit_revisit" in scenes_completed:
                if "sam_scene_swimsuit_revisit_first_time_has_done_vaginal" in scenes_completed:
                    return "Let's go fuck in the pool today!"
                elif "sam_scene_swimsuit_revisit_first_time_has_done_grinding" in scenes_completed:
                    return "You wanna swim naked again?"
                else:
                    return "Up for a swim in the pool today?"

            return "Want to go in the pool today?"

        if scene_name == "sam_simone_threesome_scene_revisit_sam":
            return "Mom should join us for sex again!"

        if scene_name == "sam_julia_threesome_scene_revisit_sam":
            return "Want [julia.say_name] to join us for sex again [sa.say_name]?"


        if scene_name == "family_foursome_scene_revisit_sam":
            return "Let's get [k.say_name] and Mom together with us so we can all fuck!"

        return ""

    Sam.revisitable_scene_choice_label = revisitable_scene_choice_label

init python:
    def sam_vaginal_on_stream_animation_lines():
       lines = []

       lines.append( { "char": sa, "text": "For those wondering, {w=0.5}ah, {w=0.5}we will be streaming some more Demon Can Laugh 2 later!" } )
       lines.append( { "char": sa, "text": "We just thought you'd enjoy our special opening!" } )
       lines.append( { "char": sa, "text": "Ah, ah!" } )

       lines.append( { "char": sa, "text": "TreekMeek3 says..." } )
       lines.append( { "char": sa, "text": "\"I'll bust a good nut tonight! Thanks!\"" } )
       lines.append( { "char": sa, "text": "That's awesome we've aided you towards your nut busting TreekMeek3!" } )

       # random.shuffle(lines)

       return lines

label sam_scene_vaginal_revisit_anim_mod:
    $ renpy.start_predict("sam_vaginal_anim")
    $ no_bust_art = False
    if sam_off_stream_revisit_complete:
        call process_character(n, appearance = "pose twohandfist face neutral")
        call process_character(sa, appearance = "pose handface face neutral")
        sa.c "Yeah!"

        call process_character(sa, appearance = "pose handsbehind face neutral")
        sa.c "We could fuck on stream..."

        call process_character(sa, appearance = "pose handsbehind face neutral")
        sa.c "Or we can fuck off stream instead."

        call process_character(sa, appearance = "pose leaning face neutral")
        sa.c "I'll let you pick!"


        $ renpy.suspend_rollback(False)
        $ quick_menu = False

        menu:
            "Let's fuck on stream!":
                $ quick_menu = True
                call process_character(sa, appearance = "pose handsbehind face happy")
                sa.c "You got it!"

                call process_character(sa, appearance = "pose handface face neutral")
                sa.c "Let me make sure the stream is ready to go."


                call sam_scene_vaginal_revisit_on_stream_anim_mod

            "How about we do it off-stream?":
                $ quick_menu = True
                call process_character(sa, appearance = "pose handsbehind face happy")
                sa.c "Sounds good to me!"


                call sam_scene_vaginal_revisit_off_stream_anim_mod

    elif "sam_scene_vaginal_revisit" not in scenes_completed:
        call process_character(n, appearance = "pose twohandfist face neutral")
        call process_character(sa, appearance = "pose handface face neutral")
        sa.c "Yeah!"

        call process_character(n, appearance = "pose handpocket face neutral")
        call process_character(sa, appearance = "pose handface face neutral")
        sa.c "Let me make sure the stream is ready to go."

        call process_character(sa, appearance = "pose leaning face neutral")
        sa.c "Our viewers are gonna get such a surprise!"


        call sam_scene_vaginal_revisit_on_stream_anim_mod
    else:
        call process_character(n, appearance = "pose behindhead face neutral")
        call process_character(sa, appearance = "pose handface face neutral")
        sa.c "I don't see why not!"

        call sam_scene_vaginal_revisit_off_stream_anim_mod

    return

# On Stream #
screen sam_vaginal_speed_settings_on_stream(is_revisit, skip_dialog = True, dream = False):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text = "Slow", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_slow_on_stream", is_revisit, dream), enabled = main_animation_speed != sam_vaginal_slow_speed_multiplier)
        use main_menu_button(text = "Normal", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_normal_on_stream", is_revisit, dream), enabled = main_animation_speed != 1.0)
        use main_menu_button(text = "Fast", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_fast_on_stream", is_revisit, dream), enabled = main_animation_speed != sam_vaginal_fast_speed_multiplier)

label sam_vaginal_go_slow_on_stream(is_revisit, skip_dialog = True, dream = False):
    call sam_vaginal_set_speed(sam_vaginal_slow_speed_multiplier)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                pass
        else:
            pass
    else:
        if random.randint(0,1) == 0:
            pass
        else:
            pass

        window hide
        with None
        $ sam_vaginal_had_slow_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2")
    else:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2", dream = dream)

    return

label sam_vaginal_go_normal_on_stream(is_revisit, skip_dialog = True, dream = False):
    call sam_vaginal_set_speed(1.0)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                pass
        else:
            pass
    else:
        if random.randint(0,1) == 0:
            pass
        else:
            pass

        window hide
        with None
        $ sam_vaginal_had_normal_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2")
    else:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2", dream = dream)

    return

label sam_vaginal_go_fast_on_stream(is_revisit, skip_dialog = True, dream = False):
    call sam_vaginal_set_speed(sam_vaginal_fast_speed_multiplier)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                pass
        else:
            pass
    else:
        if random.randint(0,1) == 0:
            pass
        else:
            pass

        window hide
        with None
        $ sam_vaginal_had_fast_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2")
    else:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2", dream = dream)

    return

label sam_scene_vaginal_revisit_on_stream_anim_mod(dream = False):
    python hide:
         play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    $ set_main_animation_speed(1.0)
    $ sam_vaginal_had_slow_speed_message = True
    $ sam_vaginal_had_normal_speed_message = True
    $ sam_vaginal_had_fast_speed_message = True

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    show anim_nothing_image at main_animation_transform(IA_Animation_Sam_Vaginal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white

    pause
    $ quick_menu = True
    sa.c "W-Welcome everyone!"
    sa.c "Great to see all of you!"
    n.c "Can you see who's online?"
    n.c "I can't see the screen."
    sa.c "I can see the chat from here."
    sa.c "..."
    sa.c "Haha!"
    sa.c "[n.say_name], I can see your butt in the video preview!"

    sa.c "Ah, hah..."
    sa.c "..."
    sa.c "These chat comments!"
    n.c "W-What are they saying?"
    sa.c "There's a couple subscribers that keep saying, \"Dat Ass.\""
    sa.c "I think they mean your butt [n.say_name]!"

    n.c "..."
    n.c "Sorry, I can't see the chat everyone. Ah..."
    n.c "T-This position makes it tough."
    sa.c "I'm seeing a lot of newcomers jumping in!"

    window hide
    $ quick_menu = False
    call show_temp_window_text_popup("sam_vaginal_on_stream_animation_lines()", xalign = 0.01, yalign = 0.01, min_width = 200, max_width = 800)
    show screen sam_vaginal_speed_settings_on_stream(True)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call sam_scene_vaginal_revisit_phase_2

    return

label sam_scene_vaginal_revisit_phase_2(skip_dialog = True, dream = False):
    $ quick_menu = False
    window hide
    # it's a revisit. so the first parameter (revisit) is True and the dream parameter is False.
    show screen sam_vaginal_speed_settings_on_stream(True)
    call screen progress_button_screen("Continue")
    $ renpy.scene('screens')
    hide screen sam_vaginal_speed_settings_on_stream
    $ renpy.suspend_rollback(False)

    call sam_scene_vaginal_revisit_phase_3

    return

label sam_scene_vaginal_revisit_phase_3:
    $ quick_menu = True
    sa.c "...{p}..."
    sa.c "That's a great suggestion MuuvOver!"
    n.c "What was it?"
    sa.c "He said we should have a counter that tracks how many viewers \"bust a nut\" during the stream!"
    sa.c "I wonder what it should be called?"


    pause 1.0
    n.c "Ah, ah."
    n.c "Did the chat come up with any good names?"
    sa.c "..."
    sa.c "Hmm, ahh..."
    sa.c "N-Not yet."
    sa.c "..."

    hide screen sam_vaginal_speed_settings_on_stream
    $ renpy.suspend_rollback(False)
    $ quick_menu = False

    menu:
        "How about \"NutBuster?\"":
            $ quick_menu = True
            sa.c "Yeah, I guess that is an obvious choice."
            sa.c "Sometimes the most obvious names are the best ones!"

        "How about \"NutCracker?\"":
            $ quick_menu = True
            call add_points(sa, 1, tag = "sam_scene_vaginal_revisit_nutcracker")
            sa.c "Haha!"
            sa.c "NutCracker?"
            sa.c "Did you guys hear what [n.say_name] said?"
            sa.c "..."
            sa.c "The chat certainly liked that name [n.say_name]!"
            sa.c "I think you chose the undisputed winner!"


    call sam_scene_vaginal_revisit_phase_4

    return

label sam_scene_vaginal_revisit_phase_4:
    call static_still_ctc("bg sam_vaginal_xray")
    sa.c "Aaah..."
    sa.c "..."
    sa.c "Yeah, he's definitely doing that, chat!"
    n.c "What's that?"
    sa.c "Ahn..."
    sa.c "You're going far into me with your dick!"
    sa.c "T-They're calling it \"balls deep\"."
    sa.c "..."
    n.c "Ah, ah..."
    sa.c "[n.say_name], they want you to go faster!"
    n.c "Y-You got it..."
    n.c "I-I'll go as long as I can like this!"

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    call sam_vaginal_set_speed(sam_vaginal_fast_speed_multiplier)
    show anim_nothing_image at main_animation_transform(IA_Animation_Sam_Vaginal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white
    $ renpy.pause(1.50)
    $ quick_menu = True

    sa.c "Keep at it! Keep at it!"
    sa.c "We've almost set a new record for viewers!"
    n.c "..."
    n.c "T-The faster I go, the sooner I'll..."
    sa.c "I-I'm getting that feeling as well."
    sa.c "B-But if we can just hold on..."

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Cum!")

    call sam_vaginal_set_speed(sam_vaginal_fastest_speed_multiplier)
    n.c "Hrm, ah!"
    n.c "[sa.say_name[0]]-[sa.say_name]..."
    sa.c "Haah, ah!"
    sa.c "G-Get ready everyone!"
    n.c "C-Can't hold it..."

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
    show bg sam_vaginal_xray_cum
    with Dissolve(1.5)

    pause
    $ quick_menu = True

    "[n.say_name] & [sa.say_name]" "Oooh!"
    sa.c "..."
    sa.c "A-And there it is!"
    sa.c "..."
    sa.c "Give [n.say_name] some credit, he was hanging in there!"
    n.c "..."
    sa.c "[n.say_name] can only go so far..."
    sa.c "He has to nut like the rest of us!"
    n.c "B-But I'll last longer next time!"
    sa.c "Yeah..."
    sa.c "And the chat will ask you to go faster, haha!"
    n.c "..."
    sa.c "..."
    sa.c "The chat is asking if you \"filled me up.\""


    call static_still_ctc("bg sam_vaginal_spread_cum")
    sa.c "I'd say so!"
    sa.c "If you look close, you can see some of it dripping out..."
    n.c "It felt like I shot out a good amount."
    sa.c "..."
    sa.c "Alright..."
    sa.c "Give [n.say_name] and I a moment to clean up and get some water."
    sa.c "And when we return, we'll get to some gaming!"

    call sam_scene_vaginal_revisit_end_anim_mod

    return

# Off Stream Revisit #
screen sam_vaginal_speed_settings_off_stream(is_revisit, dream = False, skip_dialog = False):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text = "Slow", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_slow_off_stream",  is_revisit, dream), enabled = main_animation_speed != sam_vaginal_slow_speed_multiplier)
        use main_menu_button(text = "Normal", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_normal_off_stream",  is_revisit, dream), enabled = main_animation_speed != 1.0)
        use main_menu_button(text = "Fast", action = Function(sam_vaginal_set_speed, "sam_vaginal_go_fast_off_stream",  is_revisit, dream), enabled = main_animation_speed != sam_vaginal_fast_speed_multiplier)

label sam_vaginal_go_slow_off_stream(is_revisit, dream = False, skip_dialog = False):
    hide screen sam_vaginal_speed_settings_off_stream
    call sam_vaginal_set_speed(sam_vaginal_slow_speed_multiplier)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                call process_character(sa, appearance = "", text = "Mmm!")
                call process_character(sa, appearance = "", text = "...")
                call process_character(sa, appearance = "", text = "(I-I actually like it when he goes slow)")
                call process_character(sa, appearance = "", text = "(Every spot inside my pussy gets touched...)")
        else:
            call process_character(sa, appearance = "", text = "Mmm!")
            call process_character(sa, appearance = "", text = "...")
            call process_character(sa, appearance = "", text = "(I-I actually like it when he goes slow)")
            call process_character(sa, appearance = "", text = "(Every spot inside my pussy gets touched...)")
    else:
        if random.randint(0,1) == 0:
            call process_character(sa, appearance = "", text = "Mmm!")
            call process_character(sa, appearance = "", text = "...")
            call process_character(sa, appearance = "", text = "(I-I actually like it when he goes slow)")
            call process_character(sa, appearance = "", text = "(Every spot inside my pussy gets touched...)")
        else:
            call process_character(sa, appearance = "", text = "Mmm!")
            call process_character(sa, appearance = "", text = "...")
            call process_character(sa, appearance = "", text = "(I-I actually like it when he goes slow)")
            call process_character(sa, appearance = "", text = "(Every spot inside my pussy gets touched...)")

    window hide
    with None
    $ sam_vaginal_had_normal_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2_off_stream")
    else:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2_off_stream", dream = dream)

    return

label sam_vaginal_go_normal_off_stream(is_revisit, dream = False, skip_dialog = False):
    hide screen sam_vaginal_speed_settings_off_stream
    call sam_vaginal_set_speed(1.0)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                n.c "..."
                n.c "(My dick goes in so easy!)"

        else:
            n.c "..."
            n.c "(My dick goes in so easy!)"

    else:
        if random.randint(0,1) == 0:
            n.c "..."
            n.c "(My dick goes in so easy!)"

        else:
            n.c "..."
            n.c "(My dick goes in so easy!)"

    window hide
    with None
    $ sam_vaginal_had_normal_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2_off_stream")
    else:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2_off_stream", dream = dream)

    return

label sam_vaginal_go_fast_off_stream(is_revisit, dream = False, skip_dialog = False):
    hide screen sam_vaginal_speed_settings_off_stream
    call sam_vaginal_set_speed(sam_vaginal_fast_speed_multiplier)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
               call process_character(n, appearance = "", text = "Let's go faster, [sa.say_name].")
               call process_character(sa, appearance = "", text = "Okay!")
        else:
            call process_character(n, appearance = "", text = "Let's go faster, [sa.say_name].")
            call process_character(sa, appearance = "", text = "Okay!")
    else:
        if random.randint(0,1) == 0:
           call process_character(n, appearance = "", text = "Let's go faster, [sa.say_name].")
           call process_character(sa, appearance = "", text = "Okay!")
        else:
           call process_character(n, appearance = "", text = "Let's go faster, [sa.say_name].")
           call process_character(sa, appearance = "", text = "Okay!")

    window hide
    with None
    $ sam_vaginal_had_fast_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2_off_stream")
    else:
        $ renpy.call("sam_scene_vaginal_revisit_phase_2_off_stream", dream = dream)

    return

label sam_scene_vaginal_revisit_off_stream_anim_mod:
    python hide:
         play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    $ set_main_animation_speed(1.0)
    $ sam_vaginal_had_slow_speed_message = True
    $ sam_vaginal_had_normal_speed_message = True
    $ sam_vaginal_had_fast_speed_message = True

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    show anim_nothing_image at main_animation_transform(IA_Animation_Sam_Vaginal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white

    pause
    $ quick_menu = True

#    $ clear_characters()
#    $ quick_menu = False
#    window hide
#    $ play_sex_sounds = True
#    $ set_main_animation_speed(1.0)
#    show anim_nothing_image at main_animation_transform(IA_Animation_Sam_Vaginal_Info()) as main_animation
#    with Dissolve(1.15)
#    show bg white
#    $ renpy.pause(1.50)
#    $ quick_menu = True

    sa.c "You know..."
    sa.c "It's kind of nice we're doing this off-stream."
    sa.c "We can just enjoy how it feels."
    sa.c "And not have to keep up with the chat."
    n.c "Y-Yeah..."

    sa.c "..."
    sa.c "(I wonder how often other people do this)"
    sa.c "(Seems impossible to resist wanting to do it every day!)"
    sa.c "..."
    sa.c "(I prefer this over video games!)"
    sa.c "..."
    sa.c "(Well, equal to video games for sure)"

    window hide
    $ quick_menu = False
    show screen sam_vaginal_speed_settings_off_stream(False)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call sam_scene_vaginal_revisit_phase_2_off_stream

    return

label sam_scene_vaginal_revisit_phase_2_off_stream(skip_dialog = False, dream = False):
    $ quick_menu = False
    window hide
    show screen sam_vaginal_speed_settings_off_stream(False)
    call screen progress_button_screen("Cum!")
    $ renpy.scene('screens')
    hide screen sam_vaginal_speed_settings_off_stream
    $ renpy.suspend_rollback(False)

    call sam_scene_vaginal_revisit_phase_3_off_stream

    return

label sam_scene_vaginal_revisit_phase_3_off_stream:
    call sam_vaginal_set_speed(sam_vaginal_fastest_speed_multiplier)
    n.c "{i}Pant, Pant{/i}"
    n.c "..."
    n.c "[sa.say_name[0]]-[sa.say_name]..."
    n.c "..."
    n.c "(C-Can't... {w=0.5}hold it any longer)"
    n.c "(Have to...)"

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
    show bg sam_vaginal_xray_cum
    with Dissolve(1.5)

    pause
    $ quick_menu = True
    n.c "Hrm!"
    sa.c "..."
    sa.c "(He burst into me!)"
    sa.c "..."
    sa.c "(That one must have been good for him)"
    sa.c "(It felt awesome for me!)"

    call static_still_ctc("bg sam_vaginal_spread_cum")
    sa.c "...{p}..."
    sa.c "(I-I'd be fine doing this anytime)"
    sa.c "(Both on and off stream...)"
    sa.c "..."
    sa.c "(As long as we're having a good time, it doesn't matter to me)"

    $ sam_off_stream_revisit_complete = True

    call sam_scene_vaginal_revisit_end_anim_mod

    return

label sam_scene_vaginal_revisit_end_anim_mod:
    $ renpy.stop_predict("sam_vaginal_anim")

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_incestual_situation", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene("sam_scene_vaginal_revisit", char = sa, force_no_boldness = True, reset_prompted_scene = False, force_not_replayable = True, revisit = True)

    return
