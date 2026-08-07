#default vicky_anal_revisit_complete = False
default vicky_anal_revisit_2nd_time = False

# Debug #
init 999 python:
    config.label_overrides["debug_vicky"] = "debug_vicky_anim_mod"

label debug_vicky_anim_mod:
    menu:
        "Vicky Scenes":
            call debug_vicky_scenes
        "Back":
            call debug_character
    return

# Animates Vicky's anal scene #
init python:
    def vicky_anal_set_speed(label, is_revisit, dream = False):
        renpy.call(label, is_revisit, dream = dream)

        return

image vicky_anal_anim:
    "vicky_anal_anim_0"
    pause 0.09
    "vicky_anal_anim_1"
    pause 0.09
    "vicky_anal_anim_2"
    pause 0.09
    "vicky_anal_anim_3"
    pause 0.09
    "vicky_anal_anim_4"
    pause 0.09
    "vicky_anal_anim_5"
    pause 0.09
    "vicky_anal_anim_6"
    pause 0.09
    "vicky_anal_anim_7"
    pause 0.09
    "vicky_anal_anim_8"
    pause 0.09
    "vicky_anal_anim_9"
    pause 0.09
    "vicky_anal_anim_10"
    pause 0.09
    "vicky_anal_anim_11"
    pause 0.09
    "vicky_anal_anim_12"
    pause 0.09
    "vicky_anal_anim_13"
    pause 0.09
    "vicky_anal_anim_14"
    repeat

# Overrides Scenes #
init 300 python:
    config.label_overrides["vicky_scene_anal_sex"] = "vicky_scene_anal_sex_anim_mod"
    config.label_overrides["vicky_scene_anal_revisit"] = "vicky_scene_anal_revisit_anim_mod"
    config.label_overrides["vicky_scene_anal_revisit_1st_time"] = "vicky_scene_anal_revisit_1st_time_anim_mod"
    config.label_overrides["vicky_scene_anal_revisit_2nd_time"] = "vicky_scene_anal_revisit_2nd_time_anim_mod"
    config.label_overrides["vicky_scene_anal_revisit_end"] = "vicky_scene_anal_revisit_end_anim_mod"

init 200 python:
    anim_mod_vicky_anal_old_gallery_images = Vicky.gallery_images

    def anim_mod_vicky_anal_gallery_images(self):
        images = anim_mod_vicky_anal_old_gallery_images(self)

        if "vicky_scene_anal" in scenes_completed:
            images.append("mods/leftovers_mod/images/anim_mod/animations/vicky anal/vicky_anal_anim_1.png")

        return images

    Vicky.gallery_images = anim_mod_vicky_anal_gallery_images

# Animation Class Info #
init 100 python:
    class IA_Animation_Vicky_Anal_Info(IA_Animation_Info):
        def image_base_path(self):
            return "mods/leftovers_mod/images/anim_mod/animations/vicky anal/"

        def image_name(self):
            return "vicky_anal_anim"

        def section_data(self):
            return [ ( 0 , 15 ) ]

        def last_frame(self):
            return 14

        def frame_durations(self):
            return [0.09]

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
    vicky_anal_slow_speed_multiplier = 1.10
    vicky_anal_fast_speed_multiplier = 0.75
    vicky_anal_fastest_speed_multiplier = 0.5

label vicky_scene_anal_sex_anim_mod(dream = False):
    call process_scene_beginning(bg = "bg nate_room_daytime", dream = dream)
    call process_character(n, appearance = "outfit underwear pose handsdown face aroused blush false", text = "...{p}...")
    call process_character(n, appearance = "outfit underwear pose behindhead face curious blush false", text = "(Hm?)")
    call process_character(n, appearance = "outfit underwear pose behindhead face curious blush false", text = "(I got text messages this early in the morning?)")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "(The only person I know who would do that is...)")
    call process_character(n, appearance = "outfit underwear pose handfist face happy blush false", text = "([vicky.say_name], I thought so!)")
    call process_character(n, appearance = "outfit underwear pose handfist face happy blush false", text = "...")
    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false", text = "\"[n.say_name], I have fantastic news!\"")
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
    call process_character(n, appearance = "blush false", text = "Why are you clearing off your desk, [vicky.say_name]?")
    call process_character(vicky, appearance = "", text = "To make room for us.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "Does that mean...")
    call process_character(vicky, appearance = "", text = "It's time to show your stuff, [n.say_name]!")
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
        call process_character(n, appearance = "blush false", text = "I haven't had the chance to fuck your ass, [vicky.say_name]!")
        call process_character(vicky, appearance = "", text = "You sound excited by how firm that decision was!")
        call process_character(vicky, appearance = "", text = "Now I'm intrigued!")
        call process_character(vicky, appearance = "", text = "Show my ass a good time, [n.say_name]!")
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
    call process_character(n, appearance = "blush false", text = "It's sliding into your ass, [vicky.say_name]!")

    call static_still_ctc("bg vicky_anal_behind")

    call process_character(vicky, appearance = "", text = "Oh yeah, [n.say_name]!")
    call process_character(vicky, appearance = "", text = "My ass is taking all of your dick!")
    call process_character(vicky, appearance = "", text = "Start thrusting your body!")
    call process_character(n, appearance = "blush false", text = "Alright!")
    call process_character(n, appearance = "blush false", text = "Mm, Mmn!")
    call process_character(n, appearance = "blush false", text = "How's that, [vicky.say_name]?")
    call process_character(vicky, appearance = "", text = "Yes!")
    call process_character(vicky, appearance = "", text = "That's what I want, [n.say_name]!")
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
    call process_character(vicky, appearance = "", text = "I'm going to start the welcome message, [n.say_name].")
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
    call process_character(n, appearance = "blush false", text = "Sorry, [vicky.say_name]!")
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

    # replacing this ctc with the new anim code
    #call static_still_ctc("bg vicky_anal_fuck")
    $ vicky_anal_had_slow_speed_message = False
    $ vicky_anal_had_normal_speed_message = False
    $ vicky_anal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image at main_animation_transform(IA_Animation_Vicky_Anal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white

    call process_character(vicky, appearance = "", text = "Oh, oh!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "([n.say_name]'s getting into it now!)")
    call process_character(vicky, appearance = "", text = "(He's very happy we're continuing!)")

    window hide
    $ quick_menu = False
    show screen vicky_anal_speed_settings(False)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call vicky_scene_anal_phase_2(dream = dream)

    return

label vicky_anal_set_speed(speed):
    hide screen vicky_anal_speed_settings
    $ set_main_animation_speed(speed)

    return

# Speed Options #
screen vicky_anal_speed_settings(is_revisit = False, dream = False):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text = "Slow", action = Function(vicky_anal_set_speed, "vicky_anal_go_slow",  is_revisit, dream), enabled = main_animation_speed != vicky_anal_slow_speed_multiplier)
        use main_menu_button(text = "Normal", action = Function(vicky_anal_set_speed, "vicky_anal_go_normal",  is_revisit, dream), enabled = main_animation_speed != 1.0)
        use main_menu_button(text = "Fast", action = Function(vicky_anal_set_speed, "vicky_anal_go_fast",  is_revisit, dream), enabled = main_animation_speed != vicky_anal_fast_speed_multiplier)

# Speed Dialogue Alternate #
label vicky_anal_go_slow(is_revisit, dream = False, skip_dialog = False):
    call vicky_anal_set_speed(vicky_anal_slow_speed_multiplier)
    $ dice_roll = random.randint(1,4)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                vicky.c "By the way, [n.say_name]..."
                vicky.c "If you have any ideas for videos, let me know so I can jot them down."
                n.c "I was actually thinking about some just now!"
                vicky.c "Great!"
                vicky.c "If we get a big enough list going, we can rate the best concepts and put them at the top!"

            else:
                vicky.c "The porn we deliver on [vicky.say_name]'s Empornium is going to be top tier, I just know it!"

        else:
            if random.randint(0,1) == 0:
                n.c "..."
                n.c "I can't wait to do more of this, [vicky.say_name]!"
                vicky.c "There's plenty for us to work on."
                vicky.c "We'll be at this for a long time."

            else:
                vicky.c "There's a bright business future ahead of you [n.say_name]."
                vicky.c "You'll get to fuck and earn a buck..."
                vicky.c "It's the perfect job for you [n.say_name]!"
                n.c "T-That does sound perfect..."

        window hide
        with None
        $ vicky_anal_had_slow_speed_message = True

    if vicky_anal_revisit_2nd_time:
        $ renpy.call("vicky_scene_anal_revisit_phase_2_2nd_revisit_anim_mod")

    elif is_revisit:
        $ renpy.call("vicky_scene_anal_revisit_1st_time_phase_2_anim_mod")

    else:
        $ renpy.call("vicky_scene_anal_phase_2", dream = dream)

    return

label vicky_anal_go_normal(is_revisit, dream = False, skip_dialog = False):
    call vicky_anal_set_speed(1.0)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                n.c "..."
                n.c "(I wonder how many videos [vicky.say_name] and I will end up making?)"

            else:
                vicky.c "When you're fucking me like this, I can tell you're really putting your all into it!"

        else:
            if random.randint(0,1) == 0:
                vicky.c "Aah yeah, [n.say_name]..."
                vicky.c "We're going to make great videos together."

            else:
                vicky.c "[vicky.say_name]'s Empornium will be a huge success, I just know it!"
                vicky.c "We'll reach a level of quality that no competitor will be able to rival."

        window hide
        with None
        $ vicky_anal_had_normal_speed_message = True

    if vicky_anal_revisit_2nd_time:
        $ renpy.call("vicky_scene_anal_revisit_phase_2_2nd_revisit_anim_mod")

    elif is_revisit:
        $ renpy.call("vicky_scene_anal_revisit_1st_time_phase_2_anim_mod")

    else:
        $ renpy.call("vicky_scene_anal_phase_2", dream = dream)

    return

label vicky_anal_go_fast(is_revisit, dream = False, skip_dialog = False):
    call vicky_anal_set_speed(vicky_anal_fast_speed_multiplier)
    $ dice_roll = random.randint(1,3)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                n.c "(It would be awesome if we could do some fantasy themed stuff!)"
                n.c "([vicky.say_name] could be a sorceress, and I could be her apprentice or something!)"
                n.c "(Oh man, now that I'm thinking about it, there's so many cool things we could do!)"
                n.c "(It's gonna be awesome!)"

            else:
                vicky.c "I can't wait to see how many videos we end up making together, [n.say_name]!"
                vicky.c "I have so many ideas for us to try out, and I know you do too!"

        else:
            if random.randint(0,1) == 0:
                n.c "Mmf..."
                n.c "(I can't help but fuck [vicky.say_name] as fast as I can!)"
                n.c "(Her ass is tightening on my dick!)"
                n.c "(The squeezing is intense!)"

            else:
                n.c "{i}Pant,{/i} {i}pant.{/i}.."
                n.c "I want to try everything!"
                n.c "As long as it feels like this!"
                vicky.c "..."
                vicky.c "(He's letting the sex dictate most of his thoughts right now...)"
                vicky.c "(But I don't doubt he's being sincere)"

        window hide
        with None
        $ vicky_anal_had_fast_speed_message = True

    if vicky_anal_revisit_2nd_time:
        $ renpy.call("vicky_scene_anal_revisit_phase_2_2nd_revisit_anim_mod")

    elif is_revisit:
        $ renpy.call("vicky_scene_anal_revisit_1st_time_phase_2_anim_mod")

    else:
        $ renpy.call("vicky_scene_anal_phase_2", dream = dream)

    return

label vicky_scene_anal_phase_2(skip_dialog = False, dream = dream):
    show screen vicky_anal_speed_settings(False, True)
    call screen progress_button_screen("Cum!")
    $ quick_menu = True
    hide screen vicky_anal_speed_settings
    $ renpy.suspend_rollback(False)

    call vicky_scene_anal_phase_3(dream = dream)

    return

label vicky_scene_anal_phase_3(dream = dream):
    $ renpy.suspend_rollback(True)
    $ quick_menu = False

    call process_character(n, appearance = "blush false", text = "Haah!")
    call process_character(n, appearance = "blush false", text = "I'm gonna come, [vicky.say_name], I'm gonna come!")
    call process_character(vicky, appearance = "", text = "That's the all important money shot, [n.say_name]!")
    call process_character(vicky, appearance = "", text = "The spotlight is on you!")
    call process_character(n, appearance = "blush false", text = "Hrrm!")

    call vicky_anal_set_speed(vicky_anal_fastest_speed_multiplier)
    # dialogue here

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
    show bg vicky_anal_behind_cum
    with Dissolve(1.5)

    pause
    $ quick_menu = True

    #if persistent.enable_sex_sounds:
    #    $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    #call static_still_ctc("bg vicky_anal_behind_cum")

    call process_character(vicky, appearance = "", text = "Oooh!")
    call process_character(vicky, appearance = "", text = "(My fingers are curling!)")
    call process_character(vicky, appearance = "", text = "(And my legs are shaking!)")
    call process_character(n, appearance = "blush false", text = "Uh, uhn!")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "{i}Sigh.{/i}..")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Only you can cause me to orgasm like that, [n.say_name].")
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

    $ renpy.stop_predict("vicky_anal_anim")

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

label vicky_scene_anal_revisit_anim_mod:
    $ no_bust_art = False

    if "vicky_scene_anal_revisit" in scenes_completed:
        call vicky_scene_anal_revisit_2nd_time_anim_mod
    else:
        call vicky_scene_anal_revisit_1st_time_anim_mod

    return

label vicky_scene_anal_revisit_1st_time_anim_mod:
    $ no_bust_art = True

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character(vicky, appearance = "", text = "Haha, and just after I sorted and cleaned everything on here!")
    call process_character(vicky, appearance = "", text = "I need to invest in a prop desk for us!")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "I'll help put everything back the way it was after.")
    call process_character(vicky, appearance = "", text = "It's not a big deal, but thank you for offering to help!")
    call process_character(vicky, appearance = "", text = "I end up having to clean my desk frequently anyway.")
    call process_character(vicky, appearance = "", text = "It gets piled up with all kinds of notes, papers, and other junk.")
    call process_character(n, appearance = "blush false", text = "I gotcha.")
    call process_character(n, appearance = "blush false", text = "My Mom has me clean my desk at home.")
    call process_character(vicky, appearance = "", text = "It's good she's teaching you to keep yourself organized and tidy.")
    call process_character(vicky, appearance = "", text = "It may seem boring and arduous, but it will save you a ton of time to have an orderly desk.")
    call process_character(vicky, appearance = "", text = "Anyway...")

    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg vicky_sit_tease")

    call process_character(vicky, appearance = "", text = "Let's get back on track to what we'll be doing...")

    call static_still_ctc("bg vicky_anal_probe")

    call process_character(vicky, appearance = "", text = "You remember every little detail don't you?")
    call process_character(n, appearance = "blush false", text = "Hm?")
    call process_character(vicky, appearance = "", text = "You're setup identical to the first time you fucked my ass!")
    call process_character(n, appearance = "blush false", text = "Oh, yeah...")
    call process_character(n, appearance = "blush false", text = "I have a pretty good memory, or so my family tells me.")
    call process_character(vicky, appearance = "", text = "Mine's not the greatest, so I have to be superb at scheduling.")
    call process_character(vicky, appearance = "", text = "When you run a business, you can't just go with the flow.")
    call process_character(vicky, appearance = "", text = "If you do, it will spell disaster.")

    call static_still_ctc("bg vicky_anal_behind")

    call process_character(n, appearance = "blush false", text = "Aah, ooh...")
    call process_character(n, appearance = "blush false", text = "It's awesome when my dick first goes into your ass, [vicky.say_name].")
    call process_character(vicky, appearance = "", text = "Mmm, do you get this warm shiver over your body?")
    call process_character(vicky, appearance = "", text = "That's what happens to me.")
    call process_character(n, appearance = "blush false", text = "I-It is just like a warm shiver, yeah!")
    call process_character(n, appearance = "blush false", text = "And it gets warmer and warmer!")
    call process_character(vicky, appearance = "", text = "Our body heat practically increases the office temperature a few degrees by the time we finish!")

    call static_still_ctc("bg vicky_anal_shirt")

    call process_character(n, appearance = "blush false", text = "...{p}...")
    call process_character(vicky, appearance = "", text = "I've compiled the footage from the welcome message we did.")
    call process_character(vicky, appearance = "", text = "There's a lot to go through!")
    call process_character(n, appearance = "blush false", text = "Will it take a while to complete?")
    call process_character(vicky, appearance = "", text = "It might...")
    call process_character(vicky, appearance = "", text = "But I want to select only the best pieces for the video.")
    call process_character(vicky, appearance = "", text = "I may put together a condensed version, and then a longer, more complete version.")
    call process_character(vicky, appearance = "", text = "Easier to tease people with quick snippets of the whole product.")
    call process_character(n, appearance = "blush false", text = "What's gonna be our next video we make?")
    call process_character(vicky, appearance = "", text = "I'll be sure to go over all of that with you another time.")
    call process_character(vicky, appearance = "", text = "I've setup a master spreadsheet detailing our schedule.")
    call process_character(vicky, appearance = "", text = "You're gonna be one busy boy, [n.say_name]!")
    call process_character(n, appearance = "blush false", text = "What about when I'm back at school?")
    call process_character(vicky, appearance = "", text = "I've already factored that in.")
    call process_character(vicky, appearance = "", text = "It won't disrupt your education at all.")
    call process_character(n, appearance = "blush false", text = "...")
    call process_character(n, appearance = "blush false", text = "Will there be any days off?")
    call process_character(n, appearance = "blush false", text = "I like to have free time to play video games.")
    call process_character(vicky, appearance = "", text = "Ha, of course!")
    call process_character(vicky, appearance = "", text = "We'll work it all out.")
    call process_character(vicky, appearance = "", text = "Remember, we have total control over when and how we work, [n.say_name]!")
    call process_character(vicky, appearance = "", text = "That's the beauty of it!")

    call static_still_ctc("bg vicky_anal_shirtpull")

    call process_character(n, appearance = "blush false", text = "I like that a lot.")
    call process_character(n, appearance = "blush false", text = "{i}Pant.{/i}..")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "Hey, I was curious, [n.say_name]...")
    call process_character(vicky, appearance = "", text = "Do you happen to know of any other girls who may want to be in some videos?")
    call process_character(n, appearance = "blush false", text = "Do I know any?")
    call process_character(vicky, appearance = "", text = "If you don't that's fine.")
    call process_character(vicky, appearance = "", text = "Right now I'm looking for any potential women who may want to work with you on additional videos.")

    #call static_still_ctc("bg vicky_anal_fuck")

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    call vicky_anal_set_speed(vicky_anal_fast_speed_multiplier)
    show anim_nothing_image at main_animation_transform(IA_Animation_Vicky_Anal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white
    $ renpy.pause(1.50)
    $ quick_menu = True

    $ renpy.suspend_rollback(True)

    call process_character(n, appearance = "blush false", text = "W-Work with me?")
    call process_character(n, appearance = "blush false", text = "But what about you?")
    call process_character(vicky, appearance = "", text = "Oh, I'll still work extensively with you, [n.say_name], haha!")
    call process_character(vicky, appearance = "", text = "But for some videos I'd like to be behind the camera, and have a bit more control over the composition.")
    call process_character(vicky, appearance = "", text = "As I said, if you don't know any it's no big deal.")
    call process_character(vicky, appearance = "", text = "It means more screen time for you and me!")
    call process_character(n, appearance = "blush false", text = "...")

    $ fucked_amount = girls_fucked_amount() - 1
    if fucked_amount >= 3:
        call process_character(n, appearance = "blush false", text = "I-I know of several girls that may be interested...")
        call process_character(vicky, appearance = "", text = "Really?")
        call process_character(vicky, appearance = "", text = "Several girls, [n.say_name]?")
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(vicky, appearance = "", text = "Actually, I shouldn't be that surprised.")
        call process_character(vicky, appearance = "", text = "You have a certain charm that pulls women towards you.")
        call process_character(n, appearance = "blush false", text = "You think so?")
        call process_character(vicky, appearance = "", text = "I'd say you are a chick magnet!")
        call process_character(vicky, appearance = "", text = "Which is perfect for us to attract new talent to work for the website!")
    elif fucked_amount >= 2:
        call process_character(n, appearance = "blush false", text = "I-I know of a couple of girls that may be interested...")
        call process_character(vicky, appearance = "", text = "A couple?")
        call process_character(vicky, appearance = "", text = "I hope you're not trying to double date them, haha!")
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(vicky, appearance = "", text = "I'm just kidding.")
        call process_character(vicky, appearance = "", text = "That's great though!")
        call process_character(vicky, appearance = "", text = "Ask them both if they would be willing to get in front of a camera.")
        call process_character(vicky, appearance = "", text = "Tell them there is great pay involved too!")
    elif fucked_amount == 1:
        call process_character(n, appearance = "blush false", text = "I might know of one girl...")
        call process_character(vicky, appearance = "", text = "One is perfectly acceptable!")
        call process_character(vicky, appearance = "", text = "I had a hunch you knew more girls than just me.")
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(vicky, appearance = "", text = "I'd really like to talk with her!")
        call process_character(vicky, appearance = "", text = "If you think she'd be comfortable in front of a camera, have her contact me!")
        call process_character(vicky, appearance = "", text = "Remind me to give you a couple of my business cards before you leave.")
    else:
        call process_character(n, appearance = "blush false", text = "I-I don't know of any other girls that would be interested.")
        call process_character(n, appearance = "blush false", text = "Sorry, [vicky.say_name].")
        call process_character(vicky, appearance = "", text = "No need to be sorry, [n.say_name]!")
        call process_character(vicky, appearance = "", text = "You and I are more than capable of making the majority of the videos together!")
        call process_character(vicky, appearance = "", text = "There's also plenty of avenues for us to acquire some additional women.")
        call process_character(vicky, appearance = "", text = "I know we'll get plenty of hits if I post a picture of you and say you will be working with them!")
        call process_character(n, appearance = "blush false", text = "...")
        call process_character(vicky, appearance = "", text = "A lot of women will find you cute, [n.say_name], and that will interest them more.")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        call process_character(vicky, appearance = "", text = "Is [sa.say_name] one of the girls [n.say_name]?")
        call process_character(n, appearance = "blush false", text = "Yeah, she is.")
        call process_character(vicky, appearance = "", text = "Then I know for sure she'll do it!")
        call process_character(vicky, appearance = "", text = "She has more on screen experience than I do!")
    elif fucked_amount == 1 and "sam_scene_vaginal" in scenes_completed:
        call process_character(vicky, appearance = "", text = "Wait, is [sa.say_name] the girl you're talking about, [n.say_name]?")
        call process_character(n, appearance = "blush false", text = "Yeah, she is.")
        call process_character(vicky, appearance = "", text = "Then I know for sure she'll do it!")
        call process_character(vicky, appearance = "", text = "She has more on screen experience than I do!")

    window hide
    $ quick_menu = False
    show screen vicky_anal_speed_settings(True)
    $ renpy.suspend_rollback(True)

    call vicky_scene_anal_revisit_1st_time_phase_2_anim_mod

    return

label vicky_scene_anal_revisit_1st_time_phase_2_anim_mod:
    $ quick_menu = False
    window hide
    show screen vicky_anal_speed_settings(True, True)
    call screen progress_button_screen("Cum!")
    $ renpy.scene('screens')
    hide screen vicky_anal_speed_settings
    $ renpy.suspend_rollback(False)

    call vicky_scene_anal_revisit_1st_time_phase_3_anim_mod

    return

label vicky_scene_anal_revisit_1st_time_phase_3_anim_mod:
    n.c "Ah!"
    n.c "Mmn!"
    n.c "I'm gonna come, [vicky.say_name]!"
    vicky.c "We were so caught up in discussion, I almost forget you were pumping my ass this whole time!"
    n.c "Hooo!"

    call vicky_anal_set_speed(vicky_anal_fastest_speed_multiplier)

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
    show bg vicky_anal_behind_cum
    with Dissolve(1.5)

    pause
    $ quick_menu = True

    vicky.c "That's a good hot load, [n.say_name]!"
    vicky.c "Ahh, yeah..."
    n.c "{i}Whew.{/i}.."
    vicky.c "Don't stop quite yet, [n.say_name]!"
    vicky.c "Keep fucking my ass!"
    n.c "E-Even after I came in it?"
    vicky.c "I want that cock in me one more time!"

    call vicky_scene_anal_revisit_end_anim_mod

    return

label vicky_scene_anal_revisit_2nd_time_anim_mod:
    $ no_bust_art = True

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout = 1.0, fadein = 1.0)

    call vicky_anal_set_speed(vickt_anal_fast_speed_multiplier)

    $ vicky_anal_had_slow_speed_message = False
    $ vicky_anal_had_normal_speed_message = False
    $ vicky_anal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    show anim_nothing_image at main_animation_transform(IA_Animation_Vicky_Anal_Info()) as main_animation
    with Dissolve(1.15)
    show bg white

    pause
    $ quick_menu = True

    #call static_still_ctc("bg vicky_anal_shirtpull")

    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(I have to just accept it...)")
    call process_character(vicky, appearance = "", text = "(When [n.say_name] is around, I can't help but turn into a dick crazed slut)")
    call process_character(vicky, appearance = "", text = "(Any other time, I would be a professional business women around people)")
    call process_character(vicky, appearance = "", text = "(It's good that I'm able to keep this behavior separated)")
    call process_character(vicky, appearance = "", text = "(Thank goodness I don't have clients coming into the office anymore)")
    call process_character(vicky, appearance = "", text = "(Just the other day I noticed there was a dried up cum stain on the surface of my desk!)")

    window hide
    $ quick_menu = False
    show screen vicky_anal_speed_settings(True)
    $ renpy.suspend_rollback(True)

    call vicky_scene_anal_revisit_phase_2_2nd_revisit_anim_mod

    return

label vicky_scene_anal_revisit_phase_2_2nd_revisit_anim_mod:
    $ vicky_anal_revisit_2nd_time = True

    $ quick_menu = False
    window hide
    show screen vicky_anal_speed_settings(True, True)
    call screen progress_button_screen("Cum!")
    $ renpy.scene('screens')
    hide screen vicky_anal_speed_settings
    $ renpy.suspend_rollback(False)

    call vicky_scene_anal_revisit_2nd_time_phase_3_anim_mod

    return

label vicky_scene_anal_revisit_2nd_time_phase_3_anim_mod:
    $ quick_menu = False
    hide screen vicky_anal_speed_settings
    call vicky_anal_set_speed(vicky_anal_fastest_speed_multiplier)

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
    show bg vicky_anal_behind_cum
    with Dissolve(1.5)

    pause
    $ quick_menu = True

    call process_character(vicky, appearance = "", text = "More [n.say_name], more!")
    call process_character(vicky, appearance = "", text = "...")
    call process_character(vicky, appearance = "", text = "(My nipples are rock hard!)")
    call process_character(vicky, appearance = "", text = "(I swear, they could poke a hole through the table!")

    call static_still_ctc("bg vicky_anal_behind_cum")

    call process_character(n, appearance = "blush false", text = "Nng!")
    call process_character(vicky, appearance = "", text = "{i}Gasp!{/i}")
    call process_character(vicky, appearance = "", text = "Blast your load in deep, [n.say_name]!")

    call vicky_scene_anal_revisit_end_anim_mod

    return

label vicky_scene_anal_revisit_end_anim_mod:
    $ renpy.stop_predict("vicky_anal_anim")

    python:
        stats.add_stat("times_seen_breasts", 1) # added stat here for consistency with the scene
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_butt", 1)
        stats.add_stat("times_seen_butthole", 1)
        stats.add_stat("times_given_anal_sex", 1)
        stats.add_stat("times_given_anal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene("vicky_scene_anal_revisit", char = vicky, reset_prompted_scene = False, force_no_boldness = True, force_not_replayable = True, revisit = True)

    return