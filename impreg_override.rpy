# Overrides existing scenes to give the player an option to impregnate a girl instead of having it be automatic (Kacey), or off-screen (Edna, Janet, Julia etc.) #
# Changes Julia and Janet's vaginal second revisit scenes to include impreg, and Vicky's and Kacey's impreg scenes will now be an option the player can choose, instead of happening automatically. #
# Also fixes Kira and Simone's threesome impreg option to now include the respective variable of "x_impreg", to be more consistent with the family foursome. #

# This also affects the pool party sequence and the photo epilogue. #

# Features: #
# The photo epilogue now works differently. All impregnation sequences have been made optional, and Nate now has to choose the option to impregnate each girl every time to see them pregnant during the final photo epilogue scene. Each girl in the photo epilogue now has separate images to match this change. #
# If the player didn't choose to impregnate a girl, they will now have a non-pregnant version of their new appearance in the epilogue time-jump. #
# If playing on an existing save, try playing through the scene again for characters that previously didn't have the option to get impregnated. #
# Julia and Janet can now be impregnated during their second vaginal revisit sequence. Edna can now be impregnated during the pool party. #
# To have all girls pregnant during the photo epilogue, once again, choose the option to impregnate them. #

# 1.0 Leftovers Epilogue for compatibility with v1.2 of IA and Cru's mod (21/06/24)#
# 15/01/24 Fix for Edna pool party (now shows up during revisits) and Kacey stall revisit.
# 26/01/24 Moved code from "cru_patch" patch into this file. Remove the "cru_patch" from your Leftovers folder if it's still in there. A patch should no longer be required. #
# 17/02/25 Updated code for new formatting, and added Kacey and Vicky bust art to the pool party selection dialogue

#eye glisten image fix for photo epilogue #
init 100 python:
    renpy.image("bg photo_epilogue_nate_np", Image("mods/leftovers_mod/images/bg/others/Photo_Epilogue/bg photo_epilogue_nate_np_new.png"))
    renpy.image("bg photo_epilogue_ednajanetkirasimone_np", Image("mods/leftovers_mod/images/bg/others/Photo_Epilogue/bg photo_epilogue_ednajanetkirasimone_np_new.png"))
    renpy.image("bg photo_epilogue_samjulia_np", Image("mods/leftovers_mod/images/bg/others/Photo_Epilogue/bg photo_epilogue_samjulia_np_new.png"))
    renpy.image("bg photo_epilogue_kaceyvicky_np", Image("mods/leftovers_mod/images/bg/others/Photo_Epilogue/bg photo_epilogue_kaceyvicky_np_new.png"))

# Save Variables #
default julia_impreg = False
default janet_impreg = False
default edna_impreg = False
default kacey_impreg = False
default vicky_impreg = False

label debug_impreg:
    "WARNING: Only works if impreg_override.rpy is detected in the \"game/mods\" folder."
    $ sam_impreg = True
    $ kira_impreg = True
    $ simone_impreg = True
    $ julia_impreg = True
    $ janet_impreg = True
    $ edna_impreg = True
    $ kacey_impreg = True
    $ vicky_impreg = True
    "Set everyone to pregnant state."
    if started_main_game:
        $ advance_time_return_location.start()
    return

# Overrides #
init 300 python:
    config.label_overrides["julia_scene_vaginal_revisit_2nd_time"] = "julia_scene_vaginal_revisit_2nd_time_impreg_override" # julia vaginal 2nd revisit
    config.label_overrides["janet_scene_vaginal_revisit_2nd_time"] = "janet_scene_vaginal_revisit_2nd_time_impreg_override" # janet vaginal 2nd revisit
    config.label_overrides["gloryhole_scene_stall_sex"] = "gloryhole_scene_stall_sex_impreg_override" # kacey initial stall scene
    config.label_overrides["gloryhole_scene_stall_revisit_2nd_time"] = "gloryhole_scene_stall_revisit_2nd_time_impreg_override" # kacey stall 2nd revisit (15/01/24)
    config.label_overrides["kira_simone_threesome_extended_content_1st_time"] = "kira_simone_threesome_extended_content_1st_time_impreg_override" # kira/simone fix
    config.label_overrides["kira_simone_threesome_extended_content_cum"] = "kira_simone_threesome_extended_content_cum_impreg_override" # kira/simone fix
    config.label_overrides["vicky_scene_vaginal_revisit_2nd_time"] = "vicky_scene_vaginal_revisit_2nd_time_impreg_override" # vicky vaginal 2nd revisit
    config.label_overrides["finale_scene_choices"] = "finale_scene_choices_impreg_override" # edna pool party impreg initial scene 1/2
    config.label_overrides["finale_scene_revisit_fuck_choices"] = "finale_scene_revisit_fuck_choices_impreg_override" # edna pool party impreg revisit
    config.label_overrides["finale_scene_end"] = "finale_scene_end_impreg_override" # edna pool party 2/2

init 2 python:
    config.label_overrides["epilogue_1"] = "epilogue_override" # v1.2 compat

# Leftovers Epilogue Choices #
init 2 python:
    leftovers_old_epilogue_pregnant_unpregnant_choices = epilogue_pregnant_unpregnant_choices

    def leftovers_epilogue_pregnant_unpregnant_choices():
        choice_list = leftovers_old_epilogue_pregnant_unpregnant_choices()

        got_everyone_pregnant = all([store.sam_impreg, store.kira_impreg, store.simone_impreg, store.julia_impreg, store.janet_impreg, store.edna_impreg, store.kacey_impreg, store.vicky_impreg])

        if ("{i}I got everyone pregnant!{/i}", "epilogue_pregnancy") in choice_list:
            choice_list.remove( ("{i}I got everyone pregnant!{/i}", "epilogue_pregnancy") )

        if got_everyone_pregnant:
            choice_list.append( ("(Leftovers Mod) {i}I got everyone pregnant!{/i}", "epilogue_pregnancy_leftovers") )

        else:
            choice_list.append( ("(Leftovers Mod) {i}I wonder who I got pregnant?{/i}", "epilogue_pregnancy_leftovers") )

        return choice_list

    epilogue_pregnant_unpregnant_choices = leftovers_epilogue_pregnant_unpregnant_choices

# CG Gallery #
init 200 python:
    julia_impreg_old_gallery_images = Julia.gallery_images

    def julia_impreg_gallery_images(self):
        images = julia_impreg_old_gallery_images(self)

        if getattr(store, 'julia_impreg', False):
            images.append("mods/leftovers_mod/images/bg/julia/bg julia_fuck_aftercum_impreg.png")

        return images

    Julia.gallery_images = julia_impreg_gallery_images

    janet_impreg_old_gallery_images = Janet.gallery_images

    def janet_impreg_gallery_images(self):
        images = janet_impreg_old_gallery_images(self)

        if getattr(store, 'janet_impreg', False):
            images.append("mods/leftovers_mod/images/bg/janet/bg janet_vaginal_behind_down_cumimpreg.png")

        return images

    Janet.gallery_images = janet_impreg_gallery_images

    edna_impreg_old_gallery_images = Edna.gallery_images

    def edna_impreg_gallery_images(self):
        images = edna_impreg_old_gallery_images(self)

        if getattr(store, 'edna_impreg', False):
            images.append("mods/leftovers_mod/images/bg/others/Finale Scene/bg party_edna_cum.png")
            images.append("mods/leftovers_mod/images/bg/others/Finale Scene/bg party_edna_cum_impreg.png")

        return images

    Edna.gallery_images = edna_impreg_gallery_images

# Julia Impreg #
label julia_scene_vaginal_revisit_2nd_time_impreg_override:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc("bg julia_fuck__xray_nocum")
    n.c "Ah, ah!"
    n.c "This feels, {i}pant,{/i}{w=0.5} so good."
    julia.c "..."
    julia.c "([n.say_name] has a high sex drive)"
    julia.c "..."
    julia.c "(Where'd he get it from though?)"
    julia.c "..."
    julia.c "(His sister [k.say_name] looks like she's gotten plenty of dick before...)"
    julia.c "(But his Mom and [sa.say_name] look devoid of any intercourse)"
    julia.c "(His sister [sa.say_name] doesn't even look like she's even seen dick, let alone touched it)"
    julia.c "Ah, ah!"
    julia.c "(I can't imagine never having sex, or not being interested in it!)"
    n.c "Mm! Mm!"
    n.c "..."
    n.c "(I wonder if [julia.say_name] would tell her Mom about what we've been doing...)"
    n.c "..."
    n.c "(I hope she doesn't)"
    n.c "(If Auntie told my Mom...)"
    n.c "(We'd probably both get in huge trouble!)"
    julia.c "Ah, ahn!"
    julia.c "(I'd love to see my Mom's face if she found out I was fucking [n.say_name])"
    julia.c "(She would totally flip out!)"
    julia.c "(It wouldn't even be the sex part that would bother her)"
    julia.c "(She'd wonder why I would fuck [n.say_name] instead of the quarterback at school...)"

    pause 0.5

    julia.c "..."
    julia.c "(At the rate we've been fucking, there's a very good chance I could...)"
    julia.c "(Get pregnant)"
    julia.c "(I hadn't considered it before, since [n.say_name]'s the first and only boy I've let cum in my pussy freely)"
    julia.c "(Should I be worried?)"
    julia.c "(The thought is a little... {w=0.5}scary, to be honest)"
    julia.c "..."
    julia.c "(To go from fucking him for pleasure, to having his child)"
    julia.c "(But it would be my child too)"
    julia.c "(Am I ready to become a mother?)"
    julia.c "(How would I even explain this to Mom?)"
    julia.c "(It's a big responsibility to take on)"
    julia.c "..."
    julia.c "[n.say_name]..."
    julia.c "There is a real possibility you could get me pregnant."
    julia.c "It'll be difficult explaining it to my Mom, but..."
    julia.c "Maybe we could actually make it work."
    julia.c "What do you think?"


    menu:
        "I want to get you pregnant [julia.say_name]!":
            $ julia_impreg = True
            julia.c "Oh yeah?"
            julia.c "Say it like you mean it."
            n.c "I really do want to get you pregnant, [julia.say_name]!"
            n.c "I've never felt so strongly about anything in my life!"
            julia.c "..."
            julia.c "(There's the assertiveness I was looking for all along)"
            julia.c "Alright, if that's how you truly feel..."
            julia.c "Then prove it to me!"
            julia.c "Impregnate me!"

            $ quick_menu = False
            window hide
            call screen progress_button_screen("Cum!", yalign = 0.1)
            $ quick_menu = True

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg julia_fuck__xray_cum")
            n.c "Hrrmm!"
            julia.c "F-Fuck, that went deep!"
            julia.c "(This is one hell of a way to get impregnated!)"
            julia.c "..."
            julia.c "(Hit my g-spot, too)"
            julia.c "(I guess it's only fitting, heh)"

            call static_still_ctc("bg julia_fuck_aftercum_impreg")
            julia.c "..."
            julia.c "Well."
            julia.c "I guess we got what we both wanted after all."
            julia.c "The way you pushed your cum in like that..."
            julia.c "There's no way you didn't just impregnate me."

        "I'll have to think about it.":
            julia.c "We'll both have to think about it carefully, [n.say_name]."
            julia.c "It's your responsibility just as much as it is mine."
            julia.c "We can't take things so lightly."

            $ quick_menu = False
            window hide
            call screen progress_button_screen("Cum!", yalign = 0.1)
            $ quick_menu = True

            call static_still_ctc("bg julia_fuck__xray_cum")
            n.c "Ooh!"
            julia.c "Haahn!"
            julia.c "(He pushed into my g-spot!)"
            julia.c "..."
            julia.c "(That made me dizzy for a moment!)"

            call static_still_ctc("bg julia_fuck_aftercum")

    pause 1.0
    n.c "..."
    n.c "{i}Whew!{/i}"
    julia.c "You're getting good at this [n.say_name]."


    if julia_impreg:
        julia.c "(Too good...)"

    jump julia_scene_vaginal_revisit_end
    return   

# Janet Impreg #
label janet_scene_vaginal_revisit_2nd_time_impreg_override:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg janet_vaginal_behind_down")
    janet.c "..."

    if 1 == 2:
        janet.c "(It's amazing to think that [n.say_name] is what helped [si.say_name] and I make amends)"
        janet.c "(Fucking my sister's son paved the way for our relationship to heal)"
        janet.c "..."
        janet.c "(I can't make this stuff up!)"

        call static_still_ctc("bg janet_vaginal_behind_up")
        janet.c "(I'm glad how it all turned out)"
        janet.c "(Now [n.say_name] and I can still fuck together whenever we'd like...)"

        call static_still_ctc("bg janet_vaginal_behind_down")
        janet.c "(And I don't have to hide it from my sister)"
        janet.c "(Things are looking up for our family!)"
        n.c "..."
        n.c "(I was worried about how Mom was going to react about Aunt [janet.say_name] and I...)"
        n.c "(For a moment I thought she was going to fight!)"
        n.c "(Thank goodness that didn't happen)"
        n.c "(I don't think Mom ever intended to do anything like that though)"

        call static_still_ctc("bg janet_vaginal_behind_up")
        n.c "(It seemed like she did want to figure out what happened, and wanted to hear what Aunt [janet.say_name] had to say)"
        n.c "(I'm glad I can still visit my Aunt!)"
        n.c "(She seems super happy that she was finally able to talk to my Mom!)"

        call static_still_ctc("bg janet_vaginal_behind_down")

    else:
        janet.c "(I don't even want to think what would happen if my sister found out about this)"
        janet.c "(She would fucking lose it!)"
        janet.c "(I don't even know what she would do to me...)"
        janet.c "..."

        call static_still_ctc("bg janet_vaginal_behind_up")
        janet.c "(I've definitely put myself in a tough spot)"
        janet.c "(The only thing I can hope for is that [n.say_name] keeps quiet about it for as long as possible)"
        janet.c "(But that's no guarantee...)"
        janet.c "..."
        janet.c "(Is it worse to confess it all to [si.say_name], or for her to find out through [n.say_name]?)"

        call static_still_ctc("bg janet_vaginal_behind_down")
        janet.c "(I think that would be like choosing an axe over a sword for execution)"
        janet.c "..."
        janet.c "(Then again, maybe I'm worrying too much)"
        janet.c "(My sister has always been better at understanding situations than I have...)"

    n.c "..."
    n.c "(I wonder if Aunt [janet.say_name] would be up for trying this on the beach!)"
    n.c "(Although we'd have to make sure no one can see us...)"
    n.c "..."
    n.c "(We could buy one of those huge umbrellas that are like a tent!)"
    n.c "(But if it's windy it might get knocked over...)"

    call static_still_ctc("bg janet_vaginal_behind_up")
    n.c "(Oh, there would be less people around at night though!)"
    n.c "(We could have sex and then go swimming, or vice versa!)"
    n.c "(That would be so cool!)"
    n.c "(I'll need to ask Aunt [janet.say_name] sometime!)"

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Cum!", xalign = 0.99, yalign = 0.1)
    $ quick_menu = True

    call static_still_ctc("bg janet_vaginal_behind_downblur")
    janet.c "Your hands are gripping me tighter!"
    janet.c "There's only one explanation for that..."
    n.c "It's because I'm gonna..."
    n.c "Hrm!"

    pause 1.0
    janet.c "..."
    janet.c "(What is this strange.. {w=0.5}desire I'm having?)"
    janet.c "(It's a burning desire)"
    janet.c "(The more I think about it, the more intense it becomes!)"
    janet.c "(It's like my body's trying to tell me something...)"
    janet.c "..."
    janet.c "H-Hold on just a minute, [n.say_name]!"
    janet.c "Now this may sound crazy..."
    janet.c "But hear me out!"
    janet.c "I...{w=1.0} I want you to impregnate me, [n.say_name]!"
    n.c "..."
    n.c "A-Are you sure, Aunt [janet.say_name]?"
    janet.c "I'm certain!"
    janet.c "I know it's sudden, but we may never get this chance again!"
    janet.c "(While I couldn't quite understand my attraction towards you at first...)"
    janet.c "(I now understand clearly what it is now!)"
    janet.c "An auntie-nephew relationship has never been quite like this one, so we should take it to the next level!"
    janet.c "(I remember saying that [n.say_name] has better qualities than most men)"
    janet.c "(Well, in the end, I was proven right!)"
    janet.c "(He is the ideal partner for me!)"
    janet.c "(There's no one else I'd share this with!)"
    janet.c "Do you feel the same way [n.say_name]?"
    janet.c "Does impregnating me sound good to you?"
    janet.c "Are you ready for that to happen?"

    menu:
        "I'm ready, Aunt [janet.say_name]!":
            $ janet_impreg = True
            janet.c "I wouldn't expect anything less from my favorite nephew!"
            janet.c "I'm so happy you feel the same way!"
            janet.c "I have complete faith in you, [n.say_name]!"
            janet.c "My eggs are ready for your sperm!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg janet_vaginal_behind_down_cumimpreg")
            janet.c "..."
            janet.c "(It seems only right that things would only blossom into something like this)"
            janet.c "(It's a wonderful feeling)"

        "I just want to come inside you.":
            $ janet_impreg = False
            janet.c "Typical boy attitude right there!"
            janet.c "Your other head does all the thinking for you!"
            n.c "..."
            janet.c "Haha!"
            janet.c "I'm just teasing you!"
            janet.c "Sometimes, all you need in the world is one good fucking, especially whenever we like!"
            janet.c "But, if we were to be serious for just a moment..."
            janet.c "You know I would gladly support you through any decision you make, [n.say_name]."
            janet.c "And I understand completely if you don't want to get me pregnant."
            janet.c "You're still a bit young yet for this sort of responsibility to start weighing in on your mind."
            janet.c "You should be making the most out of your youthful years like your Mom and I did!"
            janet.c "It doesn't last forever after all!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg janet_vaginal_behind_down_cum")
            n.c "I'm coming Aunt [janet.say_name]!"
            n.c "Aahn!"
            janet.c "Trust me, I would have known even if you didn't say!"

            call static_still_ctc("bg janet_vaginal_behind_up_cum")

    n.c "{i}Sigh.{/i}.."
    janet.c "..."
    janet.c "You look a bit tired after that [n.say_name]."

    if janet_impreg:
        janet.c "That was the creampie of the century you did right there!"
        janet.c "With the amount of cum you just let out, I'd say that was bound to get any girl pregnant, haha!"
        janet.c "..."
        janet.c "Whew, I'm beat!"
        janet.c "Let me whip you up something good."
        janet.c "You should consider it my treat!"

    janet.c "I'll blend you a special juice drink."
    janet.c "It will give you a great energy kick!"

    call janet_scene_vaginal_revisit_end

    return

# Kacey Impreg Optional #
label gloryhole_scene_stall_sex_impreg_override(dream = False):
    $ renpy.scene('screens')
    if dream and not persistent.disable_dream_blur:
        show screen dream_blur

    call static_still_ctc("bg gloryhole")
    gloryhole_girl.c "Hey [n.say_name]."
    gloryhole_girl.c "How's your evening been?"
    n.c "Good."
    n.c "How about yours?"
    gloryhole_girl.c "Busy day, but the evening has been decent."
    n.c "..."
    gloryhole_girl.c "..."
    gloryhole_girl.c "Isn't it a bit crazy how we talk like this?"
    n.c "Hm?"
    gloryhole_girl.c "How we communicate through this hole."
    gloryhole_girl.c "Don't get me wrong, what we do with it is great."
    gloryhole_girl.c "I just..."
    gloryhole_girl.c "I've really wanted to know what you look like [n.say_name]."
    gloryhole_girl.c "Who's the young man behind that fine cock?"
    n.c "..."
    n.c "So you want to see me?"
    gloryhole_girl.c "I'm sure you've been curious about what I look like too."
    n.c "Actually..."
    n.c "Yeah, I have."
    gloryhole_girl.c "{i}Click{/i}"
    gloryhole_girl.c "There, my stall is unlocked."
    n.c "You want me to come in right now?"
    gloryhole_girl.c "Absolutely!"
    gloryhole_girl.c "But I have one stipulation."
    n.c "..."
    gloryhole_girl.c "You have to be naked."
    gloryhole_girl.c "No clothes at all."
    n.c "No clothes?"
    n.c "..."
    n.c "A-Alright."
    gloryhole_girl.c "We've seen our most private areas exposed to each other already."
    gloryhole_girl.c "Might as well show off everything, right?"
    n.c "A-Are you going to be naked too?"
    gloryhole_girl.c "Way ahead of you."
    gloryhole_girl.c "Hang your clothes up on the stall door so they aren't on the floor."
    n.c "Okay."

    call fade_to_black(1)
    n.c "..."
    gloryhole_girl.c "You coming in?"
    n.c "..."
    n.c "I'm opening the door..."
    gloryhole_girl.c "...{p}..."
    gloryhole_girl.c "Oh my gosh!"
    gloryhole_girl.c "You are so cute!"
    n.c "Y-You have your legs spread open!"
    gloryhole_girl.c "What else did you think we were going to do in here?"
    gloryhole_girl.c "Come closer!"
    gloryhole_girl.c "Let's push our bodies together!"

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg kacey_stall_fuck")
    gloryhole_girl.c "You got a smaller body than I realized!"
    gloryhole_girl.c "Oh, ah, ah!"
    gloryhole_girl.c "That's even more impressive, considering how good you fuck!"
    n.c "Ah, ahn!"
    gloryhole_girl.c "And I love your blue eyes!"
    n.c "M-My sister has eyes like mine too."
    gloryhole_girl.c "Your short hair brings out your facial features."
    n.c "Oh!"
    n.c "Mmn!"
    n.c "I-I like being this close!"
    gloryhole_girl.c "Ah, oh fuck!"
    gloryhole_girl.c "..."
    gloryhole_girl.c "(I figured [n.say_name] was younger but...)"
    gloryhole_girl.c "(I could practically pass for his Mom!)"
    gloryhole_girl.c "..."
    n.c "Ah, ah!"
    n.c "([gloryhole_girl.say_name] sort of has a body like [k.say_name]...)"
    n.c "(Although [k.say_name] has more muscles...)"
    n.c "Ahn! Mmn!"
    n.c "(Her boobs are squishy!)"
    n.c "(They wiggle around like jello!)"
    n.c "..."
    n.c "I-I didn't realize you had big boobs."
    gloryhole_girl.c "Oh, that's right!"
    gloryhole_girl.c "You've never seen my tits before!"
    n.c "N-No..."
    gloryhole_girl.c "Are you partial to big tits?"
    gloryhole_girl.c "Most young males are."
    n.c "..."
    n.c "I-I do like them."
    gloryhole_girl.c "Why don't you suck 'em?"
    n.c "S-Suck them?"
    gloryhole_girl.c "You'll enjoy them, I'm sure!"
    gloryhole_girl.c "They're right here for you!"
    n.c "..."

    call static_still_ctc("bg kacey_stall_titsuck")
    gloryhole_girl.c "That's it!"
    gloryhole_girl.c "Ooh!"
    gloryhole_girl.c "You're pulling my nipple with your lips!"
    gloryhole_girl.c "Yes, yes!"
    n.c "{i}Mmph{/i}..."
    n.c "..."
    n.c "([gloryhole_girl.say_name]'s nipples taste pretty good!)"
    n.c "..."
    n.c "(I can't compare it to anything else...)"
    gloryhole_girl.c "{i}Pant.{/i}.."
    gloryhole_girl.c "(This feels so good!)"
    gloryhole_girl.c "..."
    gloryhole_girl.c "([n.say_name]'s turning me into a sex addict!)"
    gloryhole_girl.c "(I never knew sex could get to this level!)"
    gloryhole_girl.c "(I used to think porn would give me more satisfaction...)"
    gloryhole_girl.c "(But [n.say_name] is top tier!)"
    n.c "Mmm..."
    gloryhole_girl.c "I..."
    gloryhole_girl.c "I want you to take me from behind [n.say_name]!"
    n.c "Hm?"
    gloryhole_girl.c "There won't be any wall to impede you now."
    gloryhole_girl.c "So you can fuck me with full force!"
    n.c "..."
    
    call static_still_ctc("bg kacey_stall_fuck_nocum")
    gloryhole_girl.c "Yes!"
    gloryhole_girl.c "Like that [n.say_name]!"
    n.c "{i}Pant,{/i} {i}Pant.{/i}.."
    gloryhole_girl.c "([n.say_name] is latched onto me like a magnet!)"
    gloryhole_girl.c "(He's not stopping anytime soon either...)"
    gloryhole_girl.c "Mmm!"
    gloryhole_girl.c "(That's the advantage of being young!)"
    n.c "..."
    n.c "([gloryhole_girl.say_name]'s butt is bouncing as I push my body into it...)"
    n.c "..."
    n.c "(It's cool how it does that)"
    gloryhole_girl.c "H-Hey [n.say_name]..."
    gloryhole_girl.c "You should take it up a notch!"
    n.c "W-What do you mean?"
    gloryhole_girl.c "I mean hump me like a jackhammer!"
    gloryhole_girl.c "Really make my tits swing!"


    call static_still_ctc("bg kacey_stall_fuckahego_blur_nocum")
    n.c "Gah! Hrrm!"
    gloryhole_girl.c "Hoooly fuck!"
    gloryhole_girl.c "Hah, hah!"
    gloryhole_girl.c "(My heart is thumping!)"
    gloryhole_girl.c "..."
    gloryhole_girl.c "(Is it possible to orgasm every couple seconds?)"
    gloryhole_girl.c "(Cause that's what I'm doing!)"
    gloryhole_girl.c "Ooh..."
    gloryhole_girl.c "Y-You're making a girl quite happy [n.say_name]!"
    n.c "I-I am?"
    gloryhole_girl.c "Ooh yess..."
    n.c "Ahn..."
    n.c "Hrmm!"
    gloryhole_girl.c "..."
    gloryhole_girl.c "(I know it's a risk not telling [n.say_name] to pull out...)"
    gloryhole_girl.c "(But the logic side of my brain has shut down!)"
    gloryhole_girl.c "(I just want him to continue!)"

    menu:
        "Continue":
            n.c "[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name]!"
            n.c "Hnng!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg kacey_stall_fuck_blur_cum")
            gloryhole_girl.c "Ooh!!"
            gloryhole_girl.c "(He drove deep into me on that one!)"
            gloryhole_girl.c "(There aren't many guys that can keep going after they come...)"
            gloryhole_girl.c "..."
            gloryhole_girl.c "([n.say_name] is unique, that's for sure)"
        "Impregnate [gloryhole_girl.say_name]":
            $ kacey_impreg = True
            n.c "[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name]!"
            n.c "Hnng!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg kacey_stall_fuck_blur_cum")
            gloryhole_girl.c "Ooh!!"
            gloryhole_girl.c "(He drove deep into me on that one!)"

            call static_still_ctc("bg kacey_stall_fuck_blur_cum_impreg")
            n.c "Mm!{p}Mm!"
            gloryhole_girl.c "(Well...)"
            gloryhole_girl.c "(I think that's that)"
            gloryhole_girl.c "(I haven't been on the pill lately)"
            gloryhole_girl.c "(And with a load like that, there's no way he didn't...)"
            gloryhole_girl.c "..."
            gloryhole_girl.c "Oh, [n.say_name]..."
            gloryhole_girl.c "You are simply wonderful."
            gloryhole_girl.c "(He'll be in for a pleasant surprise in the coming months!)"
            gloryhole_girl.c "(Just wait and see, [n.say_name]!)"

            call static_still_ctc("bg kacey_stall_fuck_cum_impreg")

    n.c "..."
    n.c "{i}Sigh.{/i}.."
    gloryhole_girl.c "..."
    gloryhole_girl.c "You wipe yourself out [n.say_name]?"
    gloryhole_girl.c "I can imagine, after all you did!"
    n.c "{i}Pant.{/i}..{p}{i}Pant.{/i}.."
    gloryhole_girl.c "I don't think you'll be able to walk home in your current state."
    gloryhole_girl.c "Why don't you lay on my lap for a while?"
    gloryhole_girl.c "You can rub my tits while you rest."
    n.c "..."
    n.c "S-Sounds good."
    gloryhole_girl.c "I'm sure fondling my boobs will get your energy back in no time!"

    python:
        gloryhole_girl.revistable_scenes.add("gloryhole_scene_stall_revisit")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene("gloryhole_scene_stall", char = gloryhole_girl, dream = dream)

    return

label gloryhole_scene_stall_revisit_2nd_time_impreg_override:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg kacey_stall_titsuck")
    gloryhole_girl.c "...{p}..."
    gloryhole_girl.c "(I wonder how much more sex [n.say_name] will need when he gets older?)"
    gloryhole_girl.c "(What if he requires sex every other hour?)"
    gloryhole_girl.c "(That would be something else!)"
    gloryhole_girl.c "..."
    gloryhole_girl.c "(Though, I could totally handle it)"

    call static_still_ctc("bg kacey_stall_fuckahego_blur_nocum")
    n.c "{i}Pant,{/i} {i}pant,{/i} {i}pant.{/i}.."
    gloryhole_girl.c "..."
    gloryhole_girl.c "(I'd have to boost my energy to handle the additional fucking!)"
    gloryhole_girl.c "(Maybe I could make a super juice drink...)"
    gloryhole_girl.c "(Might have to sacrifice some late night gaming to get more rest...)"
    gloryhole_girl.c "..."
    gloryhole_girl.c "(But currently, I have no trouble taking on [n.say_name]'s pecker!)"
    n.c "..."
    n.c "(I still can't believe [gloryhole_girl.say_name] has played games for such a long time!)"
    n.c "(I bet she's an expert at some of those older platformers and RPGs!)"
    n.c "..."
    n.c "(It would be cool to check out her game collection one day...)"

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Cum!", yalign = 0.1)
    $ quick_menu = True

    menu:
        "Continue":
            n.c "[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name]!"
            n.c "Hnng!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg kacey_stall_fuck_blur_cum")

            gloryhole_girl.c "(There's another large load!)"
            gloryhole_girl.c "..."
            gloryhole_girl.c "(I don't even think my pussy can hold all of it!)"
        "Impregnate [gloryhole_girl.say_name]":
            $ kacey_impreg = True
            n.c "[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name]!"
            n.c "Hnng!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg kacey_stall_fuck_blur_cum")

            gloryhole_girl.c "Ooh!!"
            gloryhole_girl.c "(He drove deep into me on that one!)"

            call static_still_ctc("bg kacey_stall_fuck_blur_cum_impreg")

            n.c "Mm!{p}Mm!"
            gloryhole_girl.c "..."
            gloryhole_girl.c "(Well...)"
            gloryhole_girl.c "(I think that's that)"
            gloryhole_girl.c "(I haven't been on the pill lately)"
            gloryhole_girl.c "(And with a load like that, there's no way he didn't just...)"
            gloryhole_girl.c "..."
            gloryhole_girl.c "Oh, [n.say_name]..."
            gloryhole_girl.c "You are simply wonderful."
            gloryhole_girl.c "(He'll be in for a pleasant surprise in the coming months!)"
            gloryhole_girl.c "(Just wait and see, [n.say_name]!)"

    call static_still_ctc("bg kacey_stall_fuck_cum")

    n.c "{i}Whew.{/i}.."
    gloryhole_girl.c "..."

    if kacey_impreg:
        gloryhole_girl.c "(No need to worry about re-populating if someone like [n.say_name] is around...)"

    call gloryhole_scene_stall_revisit_end

    return

# Vicky Impreg Optional #
label vicky_scene_vaginal_revisit_2nd_time_impreg_override:
    $ no_bust_art = True
    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc("bg vicky_vaginal_nude")
    vicky.c "..."
    vicky.c "(I keep forgetting to pick up condoms when I'm out shopping)"
    vicky.c "(If we're going to continue fucking like this, there's a good chance [n.say_name] could get me pregnant...)"
    vicky.c "..."
    vicky.c "(I always hated condoms though)"
    vicky.c "(It's this artificial barrier that takes away a lot of the pleasure)"
    vicky.c "..."
    vicky.c "(I just need to take a morning after pill, that's easier)"
    vicky.c "(I'll need to stock up on a lot of it soon!)"
    vicky.c "(I think I have an old pack lying around somewhere)"
    vicky.c "(Not sure if it's expired at this point...)"
    n.c "..."
    n.c "(Has [vicky.say_name] come up with a payment plan for the videos we'll make?)"
    n.c "(I wonder what would be the best way to sell our videos...)"
    n.c "(We could sell them individually...)"
    n.c "(But we'd have to sell them at a low price, probably)"
    n.c "..."
    n.c "(A subscription service would be better!)"
    n.c "(People would get access to every video for a monthly fee!)"
    n.c "(That's what I'd want if I visited the website!)"
    n.c "(Although...)"
    n.c "(Making all of the videos completely free everyone would like)"
    n.c "(We could have people donate like they do now for Twinsticks!)"
    n.c "(That method has worked great so far!)"
    n.c "(I should talk with [vicky.say_name] about it the next time I get a chance)"

    call static_still_ctc("bg vicky_matingpress_nude")
    vicky.c "Ah, Mm..."
    vicky.c "I was thinking of different locations where we could shoot our videos."
    vicky.c "Aside from my apartment."
    n.c "Did you have any locations in mind?"
    n.c "Ooh!"
    vicky.c "Well, off the top of my head..."
    vicky.c "There's the beach, the park..."
    vicky.c "My car."
    n.c "We would fuck in your car?"
    vicky.c "If that's what you feel like doing."
    n.c "Won't someone see us at these places?"
    vicky.c "Not if we pick an isolated spot, or we conceal ourselves."
    vicky.c "We could also rent a boat for a day and have some fun out at sea."
    n.c "Aw, that'd be wicked cool!"
    n.c "Our own boat!"
    vicky.c "I'll inquire about it when I have the opportunity."

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Cum!", xalign = 0.1, yalign = 0.1)
    $ quick_menu = True

    menu:
        "Continue":
            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg vicky_matingpress_nude_cum")
            n.c "Hnng!"
            n.c "Hrrm!"
            vicky.c "Oh yeah!"
            vicky.c "Aah!"
            n.c "..."


            vicky.c "(I know I've been washing my bedsheets recently...)"
            vicky.c "(But I need to use a blacklight to really make sure it's clean)"
            vicky.c "(There's likely a few lingering stain spots)"

        "Impregnate [vicky.say_name]":
            $ vicky_impreg = True

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg vicky_matingpress_nude_cum")
            n.c "Hnng!"
            n.c "Hrrm!"
            vicky.c "Oh yeah!"
            vicky.c "Aah!"
            n.c "..."

            call static_still_ctc("bg vicky_matingpress_nude_cum_impreg")
            vicky.c "([n.say_name] never ceases to amaze me how much he can cum)"
            vicky.c "(He's certainly gifted in that regard, that's for sure)"
            vicky.c "..."
            vicky.c "Haah..."
            vicky.c "(I have a feeling he may know what will come from this by now)"
            vicky.c "(I'll have to keep tabs on that over the next coming days)"
            vicky.c "(Still, I hope he's given it thought like I have...)"

    call vicky_scene_vaginal_revisit_end

    return

# Kira/Simone threeway impreg fix #
label kira_simone_threesome_extended_content_1st_time_impreg_override:
    call fade_to_black(1)
    si.c "It looks like no one is here right now."
    k.c "Perfecto!"
    k.c "Now I can show you what I can do!"
    k.c "Rip those clothes off [n.say_name]!"
    k.c "They're just a hinderance!"
    si.c "You took everything off so quick [k.say_name]!"
    k.c "If you thought that was impressive Mom, wait till you see this!"
    n.c "Whoa!"


    call static_still_ctc("bg kirablowjob_69")
    si.c "Oh my word [k.say_name]!"
    k.c "That's right!"
    k.c "I'm breaking out the standing sixty-nine!"
    n.c "Hah, ah!"
    si.c "Hold onto him tight [k.say_name]!"
    k.c "Oh you bet I will!"
    k.c "Mmph..."
    n.c "(I didn't expect [k.say_name] to flip me around while she was holding me!)"
    n.c "(It felt like I was on a rollercoaster for a second!)"
    si.c "You doing alright sweetie?"
    si.c "Tell me if you're getting lightheaded."
    n.c "I-I'm doing fine Mom."
    k.c "Course you are [n.say_name]!"
    k.c "You're getting sucked!"
    n.c "([k.say_name]'s not kidding there!)"
    n.c "(She's doing it so fast!)"
    k.c "I'm going so far down on your cock [n.say_name], my nose is touching your balls!"
    k.c "What do you think of that Mom?"


    si.c "(My daughter is quite the deepthroater)"
    si.c "..."
    si.c "(It's...{w=1.0}turning me on to see this)"
    si.c "(My own son and daughter going at it...)"
    si.c "(They look like they are thoroughly enjoying each other)"
    si.c "..."
    si.c "(I'm getting hot in this sweater...)"
    k.c "Mmm...hm?"
    k.c "You stripping down too Mom?"
    n.c "M-Mom is?"
    si.c "I didn't want to be the odd one out!"
    si.c "Plus I...{w=1.0}wanted to have another taste of [n.say_name]'s dick."
    k.c "Whoa-ho, Mom!"
    k.c "You're sounding rather lustful!"
    k.c "I like this side of you!"
    k.c "Hey [n.say_name]!"
    k.c "You'd better be ready for Mom!"
    k.c "She's got this look in her eyes."


    n.c "..."
    k.c "Mom's mouth wants a round two with your dick!"
    k.c "Good luck [n.say_name]!"
    n.c "G-Good luck?"


    call static_still_ctc("bg simone_underblowjob_clothed")
    si.c "Mmf, Mmf, Mmn!"
    n.c "Gaaha!"
    k.c "Oh yeah Mom!"
    k.c "There we go!"
    k.c "Work that dick!"
    k.c "You wanted [n.say_name]'s cock so bad, you didn't even fully remove your top!"
    n.c "(This isn't how Mom normally sucks!)"
    n.c "(She's doing this as hard as [k.say_name], maybe even harder!)"
    k.c "Ha, look at you [n.say_name]!"
    k.c "You were not expecting Mom to suck like this at all!"
    k.c "This is what she's truly capable of bro!"
    n.c "{i}Gasp!{/i}"
    n.c "M-Mom!"
    si.c "{i}Slurp, slurp!{/i}"
    k.c "The messier, the better Mom!"


    call static_still_ctc("bg simone_underblowjob_clothed_sloppy")
    k.c "(Mom must have activated her inner slut or something!)"
    k.c "(She's going to town with [n.say_name]'s dick!)"
    k.c "(Saliva is dripping down her chin onto her tits)"
    k.c "(Mom's a bonafide freak!)"
    k.c "(And just look at the size of her melons!)"
    k.c "(Seeing them out in the open really puts things into perspective)"
    k.c "(They probably weigh half of [n.say_name]'s total body weight, haha!)"
    n.c "Ahn!"
    k.c "Yeah, grab onto her head bro."
    k.c "Push Mom's face into your cock."
    k.c "Keep her locked in there!"
    n.c "I-Is that okay Mom?"
    si.c "Mmm...yes baby."
    si.c "Push your cock down my throat."
    k.c "Make every moment worth it with her [n.say_name]!"
    n.c "I am, I am!"
    n.c "Ah...{w=0.5}this feels so incredible!"
    n.c "I don't think this can get any better."
    k.c "You don't eh?"
    n.c "..."
    k.c "Oh bro..."
    k.c "How you'll be proven wrong..."
    n.c "I-I will?"
    k.c "Hey Mom..."
    k.c "Let's each take a ride on [n.say_name]'s pole."
    si.c "Mmm, that's a perfect idea [k.say_name]."
    k.c "Now you're in for it [n.say_name]."
    n.c "..."


    call fade_to_black(1)
    k.c "You're gonna wanna lay back for this bro..."
    k.c "..."


    call static_still_ctc("bg threesome_kirafuck_simonewatch")
    k.c "Mmm yeah, that's real good!"
    k.c "You like how you can see my pussy on your cock [n.say_name]?"
    k.c "You get to see all the action!"
    si.c "I hope [n.say_name] can handle all that force you're putting on him [k.say_name]."
    k.c "It's nothing for him."
    k.c "I've been extensively conditioning [n.say_name]'s body for this sort of thing!"
    n.c "Oh, oh!"
    si.c "My-my-my..."
    si.c "So this is the usual routine for you two."
    k.c "The one thing I will say about [n.say_name]..."
    k.c "He checks off every box for me Mom!"
    k.c "If I try something new, he catches on right away."
    k.c "For him to keep pace, and have enough in the tank to satisfy me?"
    k.c "Bro's got no equal in my eyes!"
    si.c "[k.say_name] gave you high praise [n.say_name]!"
    si.c "It takes a lot to get that from your sister."
    n.c "{i}Pant.{/i}..Y-Yeah."
    k.c "Plus this is like, a way better version of friends with benefits."
    k.c "It's family with benefits!"
    si.c "Haha, [k.say_name]!"
    k.c "Hey, I still love him as my goofy little bro."
    k.c "Only difference is we spend our time together a bit differently than most siblings..."
    n.c "A-And I like it that way."
    si.c "Haha!"
    k.c "I also know you and [n.say_name] don't have a typical mother and son relationship either..."
    k.c "Why don't you show me Mom?"
    k.c "Show me how you and [n.say_name] enjoy yourselves."
    si.c "You'd like that [k.say_name]?"
    k.c "I've seen you two before from afar..."
    k.c "You bang so much that [n.say_name] passes out on top of you!"
    si.c "[n.say_name] does tend to do that with me, yes."
    n.c "..."
    si.c "But you get a good rest whenever it happens sweetie!"
    k.c "You're gonna have no problem counting your sheep tonight bro!"


    call static_still_ctc("bg threesome_simonefuck_kirawatch")
    n.c "Aah...Mom, aah..."
    si.c "Is this good for you [n.say_name]?"
    n.c "Mhm!"
    k.c "Ride that cock Mom!"
    si.c "Yes!"
    si.c "Fuck Mommy!"
    n.c "Ha-ah!"
    k.c "(This is like my own private viewing!)"
    k.c "(I'll have no issue keeping myself wet while watching this!)"
    k.c "(Damn, Mom's ass is so wide!)"
    k.c "([n.say_name]'s dick is underneath there somewhere, ha!)"
    k.c "..."
    k.c "(That explains why [n.say_name] loves to grope Mom)"
    k.c "(I get such a kick out of how he does it so casually)"
    k.c "(Mom is cooking dinner, and suddenly there's [n.say_name] grasping onto her titties or her ass!)"
    k.c "(I like how he tries to find her nipple underneath all her clothes)"
    k.c "(Bro is determined to get a few tweaks in)"
    k.c "(That's approaching the apex of perversion!)"
    k.c "(And it's awesome to witness!)"
    si.c "..."
    si.c "([k.say_name] is masturbating to [n.say_name] and I fucking)"
    si.c "(It's incredible how comfortable I've become to this!)"
    si.c "(I did the biggest one-eighty this summer)"
    si.c "([n.say_name] was able to break down the wall I built towards sex)"
    si.c "(Not only that, he also got in the action with his big sister!)"
    si.c "(We've got our own little sexual revolution going on in our house!)"
    k.c "I'm ready to jump back into the action!"
    k.c "You should poke my ass for a bit [n.say_name]!"
    si.c "Have you done a lot of anal before [k.say_name]?"
    k.c "Have I done a lot of anal before?"
    k.c "I've done it enough to be considered an anal master!"
    si.c "Haha!"
    si.c "An anal master [k.say_name]?"
    si.c "That would be a unique entry on a resume!"
    k.c "[n.say_name] and I will show you our command of ass fucking!"


    call fade_to_black(1)
    k.c "Alright, got my butt up in the air."
    k.c "[n.say_name]'s dick is knocking on my backdoor and..."
    k.c "Push-push-push!"


    call static_still_ctc("bg foursome_groupfucknosam")
    k.c "And it's in there!"
    k.c "Oh yeah, is it in there!"
    n.c "Mmph!"
    k.c "Ha, nice Mom!"
    k.c "Dishing out the classic tit smother!"
    si.c "I wanted to show you my breast mastery!"
    n.c "Hmph?"
    k.c "Breast mastery Mom?"
    si.c "I know, that sounded uncool coming from me!"
    k.c "[n.say_name]'s face is pretty deep into your tits Mom!"
    k.c "I don't think he wants to come up for air, haha!"
    n.c "Mm, Mmn!"
    k.c "I bet [n.say_name] loves your tits as much as he loves my ass, doesn't he Mom?"
    si.c "That's an accurate comparison!"
    si.c "[n.say_name] would stare at my breasts for so long he wouldn't even know I was talking to him!"
    k.c "He kept losing count on my squat exercises because my butt was too distracting!"
    k.c "So what this means is...{w=1.0}[n.say_name] is both an ass and tits man!"
    si.c "Haha!"
    si.c "He'd never be able to choose one over the other!"
    si.c "So he just likes both!"
    n.c "..."
    n.c "Ahn..."
    n.c "I'm very closing to coming."
    k.c "Then lets give you somewhere to blow that wad!"
    k.c "My pussy is prepped for a mega load bro!"
    si.c "I'm perfectly happy to be the recipient as well [n.say_name]."
    k.c "Mom's offering her cunt up too!"
    k.c "Better make your choice fast, before your dick makes it for you!"

    menu:
        "Cum in [k.say_name]":
            call static_still_ctc("bg kiraahego_internal_nocum")
            k.c "Let's bring it on home bro!"
            n.c "Haa, ahn..."
            n.c "Gonna come, gonna come!"
            n.c "Gaaah!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg kiraahego_internal_cum")
            k.c "Ooh yeah..."
            k.c "Burst into my pussy bro!"
            n.c "Nng, Nng!"
            k.c "Mmm..."
            k.c "You did everything right that time [n.say_name]."
            k.c "Not much you need to improve upon."
            k.c "For this position anyway, hehe..."
            n.c "{i}Phew.{/i}.."


            k.c "Next time I want to see you drain your balls in Mom."
            k.c "She needs her fair share of nut busts."
            si.c "Haha, these terms and phrases you come up with [k.say_name]!"

        "Impregnate [k.say_name]":
            call static_still_ctc("bg kiraahego_internal_nocum")
            $ kira_impreg = True
            k.c "Let's bring it on home bro!"
            n.c "Haa, ahn..."
            k.c "(There's little doubt in my mind where these creampies will lead to...)"
            k.c "(Not like I didn't know before, but now I'm ready for the outcome)"
            k.c "(I accept your seed bro!)"
            k.c "(If you want to fertilize my womb, it's open for business!)"
            n.c "Gonna come, gonna come!"
            n.c "Gaaah!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg kiraahego_internal_cum")
            k.c "Ooh yeah..."
            k.c "Burst into my pussy bro!"
            n.c "Nng, Nng!"
            k.c "Mmm..."
            k.c "You did everything right that time [n.say_name]."
            k.c "Not much you need to improve upon."
            k.c "For this position anyway, hehe..."
            n.c "{i}Phew.{/i}.."


            call static_still_ctc("bg KiraAhergo_Internal_Cum_Impreg")
            k.c "Next time [n.say_name], I want to see you drain your balls in Mom."
            k.c "She needs her fair share of nut busts."
            si.c "Haha, these terms and phrases you come up with [k.say_name]!"

        "Cum in Mom":
            call static_still_ctc("bg SimoneAhego_Internal_NoCum")
            si.c "Oh yes, ah yes!"
            si.c "Keep going like this sweetie!"
            n.c "Haa, ahn..."
            n.c "(Mom is swaying back and forth on me)"
            n.c "(My dick is rubbing her pussy even more!)"
            n.c "(I'm right on the edge of exploding!)"
            si.c "([n.say_name]'s eyes are shut tight)"
            si.c "(He's going to have an intense orgasm)"
            si.c "(I know he will after all the things [k.say_name] and I did with him!)"
            n.c "Mom, I'm coming!"
            n.c "Hooo!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg simoneahego_internal_cum")
            si.c "Aah-haa!"
            si.c "I came too sweetie!"
            si.c "I was on the verge!"
            n.c "{i}Pant.{/i}.."
            si.c "I don't see any cum dripping out."
            si.c "You must have shot deep in my pussy!"
            si.c "..."


            n.c "{i}Phew.{/i}.."
            si.c "I think [n.say_name] is spent for now [k.say_name]."
            k.c "I figured he would be after how hard he blew his load."
            si.c "Next time, you should have him finish in you."
            k.c "It's only fair to share!"
            si.c "Haha!"

        "Impregnate Mom":
            call static_still_ctc("bg simoneahego_internal_nocum")
            $ simone_impreg = True
            si.c "Oh yes, ah yes!"
            si.c "Keep going like this sweetie!"
            n.c "Haa, ahn..."
            n.c "(Mom is swaying back and forth on me)"
            n.c "(My dick is rubbing her pussy even more!)"
            n.c "(I'm right on the edge of exploding!)"
            si.c "([n.say_name]'s eyes are shut tight)"
            si.c "(He's going to have an intense orgasm)"
            si.c "(I know he will after all the things [k.say_name] and I did with him!)"
            n.c "Mom, I'm coming!"
            n.c "Hooo!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg simoneahego_internal_cum")
            si.c "Aah-haa!"
            si.c "I came too sweetie!"
            si.c "I was on the verge!"
            n.c "{i}Pant.{/i}.."
            si.c "I don't see any cum dripping out."
            si.c "You must have shot deep in my pussy!"
            si.c "..."


            call static_still_ctc("bg simoneahego_internal_cum_impreg")
            si.c "(There's a very high chance [n.say_name] may have just... impregnated me)"
            si.c "(Of course I've been letting him come in my pussy freely, so the chances were always high it would happen!)"
            si.c "(I'll just have to check myself for the next few days...)"
            si.c "(Though if I am pregnant, I'll be happy it was [n.say_name]'s sperm that merged with my egg!)"
            n.c "{i}Phew.{/i}.."
            si.c "I think [n.say_name] is spent for now [k.say_name]."
            k.c "I figured he would be after how hard he blew his load."
            si.c "Next time, you should have him finish in you."
            k.c "It's only fair to share!"
            si.c "Haha!"

    $ kira_simone_threesome_part_2_done = True
    call kira_simone_threesome_scene_revisit_end
    return

label kira_simone_threesome_extended_content_cum_impreg_override:
    k.c "Ready to blow, bro?"

    menu:
        "Cum in [k.say_name]":
            call static_still_ctc("bg kiraahego_internal_nocum")
            k.c "..."
            n.c "Hrrm!"
            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg kiraahego_internal_cum")

            k.c "Aaah yeeeah..."
            k.c "Finishing strong bro!"
        "Impregnate [k.say_name]":
            call static_still_ctc("bg kiraahego_internal_nocum")
            $ kira_impreg = True

            k.c "..."
            n.c "Hrrm!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
            call static_still_ctc("bg kiraahergo_internal_cum_impreg")

            k.c "Aaah yeeeah..."
            k.c "Finishing strong bro!"
        "Cum in Mom":
            call static_still_ctc("bg simoneahego_internal_nocum")

            si.c "..."
            n.c "Aah!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg simoneahego_internal_cum")

            si.c "Oooh!"
            si.c "Magnificent sweetie!"
        "Impregnate Mom":
            call static_still_ctc("bg simoneahego_internal_nocum")
            $ simone_impreg = True

            si.c "..."
            n.c "Aah!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg simoneahego_internal_cum_impreg")

            si.c "Oooh!"
            si.c "Magnificent sweetie!"

    call kira_simone_threesome_scene_revisit_end
    return

# Edna Impreg #
label finale_scene_choices_impreg_override(dream = False):
    if finale_fucked_amount >= finale_fucked_amount_goal:
        call finale_scene_end(dream = dream)
    elif finale_fucked_amount >= 1 and not finale_kacey_arrived:
        $ finale_kacey_arrived = True
        k.c "..."
        k.c "Oh, is someone here?"
        gloryhole_girl.c "I made it!"
        k.c "Hey, it's [gloryhole_girl.say_name]!"
        n.c "H-Hi [gloryhole_girl.say_name]..."
        gloryhole_girl.c "I got a little lost on the way here, but luckily I figured it out."
        gloryhole_girl.c "Did I miss much?"
        k.c "We just got started!"
        k.c "Remove your clothes, and get comfortable!"
        si.c "Hi [gloryhole_girl.say_name], my name's [si.say_name]."
        si.c "I'm [n.say_name]'s Mom!"
        gloryhole_girl.c "Pleased to meet you [n.say_name]'s Mom!"
        gloryhole_girl.c "You're very pretty!"
        si.c "Why, thank you!"
        si.c "Help yourself to the food that's available."
        gloryhole_girl.c "Much appreciated!"
        gloryhole_girl.c "Is there an order to who has [n.say_name] next or?"
        janet.c "We're having [n.say_name] pick."
        janet.c "So any of us could be picked next!"
        gloryhole_girl.c "Oh, I like that!"
        gloryhole_girl.c "Keeps things exciting!"

    elif finale_fucked_amount >= 2 and not finale_vicky_arrived:
        $ finale_vicky_arrived = True
        k.c "..."
        k.c "Heey, there's [vicky.say_name]!"
        n.c "S-She's here?"
        vicky.c "Hello everyone."
        vicky.c "Sorry I'm late."
        vicky.c "Had to take care of a technical issue on my website."
        k.c "Glad you were able to make it [vicky.say_name]."
        k.c "So now, all of us have gathered!"
        vicky.c "I need to get acquainted!"
        vicky.c "[n.say_name] has told me so much about all of you!"
        si.c "Hopefully only the good things!"
        vicky.c "Are you, [n.say_name]'s mother?"
        si.c "Yes, I am!"
        si.c "[si.say_name]!"
        vicky.c "[vicky.say_name]."
        vicky.c "[n.say_name] greatly resembles you, that's what gave me the hunch!"
        vicky.c "You've raised a very respectable young man, [si.say_name]."
        si.c "That's wonderful to hear from a professional businesswoman!"
        vicky.c "And who are the other family members here?"
        janet.c "I'm [janet.say_name], [n.say_name]'s aunt and [si.say_name]'s sister."
        edna.c "I'm his grandmother, [edna.say_name]."

        if finale_julia_sam:
            julia.c "Cousin, [julia.say_name]."

        vicky.c "Got it."
        vicky.c "[k.say_name] I already know..."

        if finale_julia_sam:
            vicky.c "And there is [sa.say_name]!"
            sa.c "Yeah!"
            sa.c "You know about me?"
            vicky.c "Of course!"
            vicky.c "You're the other half of the channel Twinsticks!"
            vicky.c "I'm subscribed to your channel."
            vicky.c "I've watched many livestreams of you and [n.say_name]."
            sa.c "{i}Gasp!{/i}"
            sa.c "My first subscriber I get to meet in person!"

        k.c "I'm sure you'll have plenty to talk about with everyone Vicky."
        k.c "But that can come later."
        vicky.c "Indeed."
        vicky.c "[n.say_name] requires our undivided attention right now."

        if edna_impreg:
            k.c "You know, if you had arrived sooner, you could have seen [n.say_name] impregnating Grandma!"
            vicky.c "{w=1.0}...What?"
            vicky.c "You... {w=1.0}impregnated your own grandmother, [n.say_name]?"
            edna.c "Oh yes. It was exquisite."
            vicky.c "I have so many questions..."
            k.c "Better save them until the end, then!"
            k.c "You wouldn't want to miss out on all the fun!"

    menu:
        "Grandma" if not finale_chose_edna:
            if edna_fucked_vaginally() in scenes_completed or finale_chose_edna:
                $ no_bust_art = False
                show bg backyard_daytime
                with Dissolve(0.5)
                call process_character(edna, appearance = "pose handclasp face flirt blush false")
                edna.c "Let's put on a show, [n.say_name]!"

                call static_still_ctc("bg party_edna")
                edna.c "Oooh..."
                n.c "S-So warm."
                n.c "Let me grab your boobs Grandma."
                edna.c "Squeeze them all you like [n.say_name], yes!"
                k.c "You know what's really cool about this..."
                k.c "[n.say_name] has literally fucked three generations of our family!"
                k.c "That's like, mind blowing when you think about it."
                n.c "Mmn, Mm!"
                janet.c "[n.say_name] took a different approach to exploring our family tree!"
                k.c "Ha!"
                k.c "You think if [n.say_name] was a time traveler, he'd fuck our distant relatives too?"
                si.c "Haha!"


                if finale_julia_sam:
                    julia.c "I wouldn't put it past him."


                edna.c "I suppose this means [n.say_name] can fuck me at my condo, even when any of you are visiting!"
                si.c "You can do whatever you like Mom!"
                edna.c "That's great to hear [si.say_name]!"
                edna.c "Your son gets very horny over at my place."
                edna.c "He grabs my tits and ass all day!"
                si.c "That's not surprising."
                si.c "He does the same thing over here with me!"


                if finale_julia_sam:
                    sa.c "If I come over Grandma, can [n.say_name] and I fuck in the kitchen while we make cookies?!"
                    edna.c "Only if we can swap out!"
                    sa.c "No problem Grandma!"
                    edna.c "We'll have to be careful when [n.say_name] comes if the batter is nearby!"


                n.c "Aah, yeah Grandma..."
                k.c "[n.say_name] sure loves tits, doesn't he?"
                janet.c "He's a boy, haha!"
                janet.c "It's hard wired in him to love boobs!"
                edna.c "We all love his cock though, so it goes both ways!"
            else:
                $ no_bust_art = False
                show bg backyard_daytime
                with Dissolve(0.5)
                call process_character(edna, appearance = "pose handclasp face flirt blush false")
                edna.c "This will be a rather special moment for [n.say_name] and I."

                call process_character(edna, appearance = "pose handclasp face flirt blush false")
                edna.c "We haven't yet had a chance to...{w=0.5}go all the way together."

                call process_character(k, appearance = "pose handhip face neutral blush false")
                k.c "You mean this will be the first time [n.say_name]'s dick will be entering your pussy Grandma?"

                call process_character(k, appearance = "pose handhip face happy blush false")
                k.c "And we all get to witness it?!"

                call process_character(k, appearance = "pose handhip face happy blush false")
                k.c "I guess it's not just [n.say_name] who's getting lucky today!"

                call process_character(k, appearance = "pose handhip face happy blush false")
                k.c "I'm going to enjoy this spectacle!"

                call process_character(janet, appearance = "pose handchest face neutral blush false")
                janet.c "You're going to love fucking [n.say_name], Mom."

                call process_character(janet, appearance = "pose handchest face flirt blush false")
                janet.c "What [n.say_name] does with that cock of his is something special!"

                call process_character(n, appearance = "pose handsdown face aroused blush true")
                n.c "..."

                call process_character(edna, appearance = "pose handhip face flirt blush false")
                edna.c "There's an eager audience waiting on us [n.say_name]."

                call process_character(edna, appearance = "pose handhip face flirt blush false")
                edna.c "Let's start the show for them!"


                call static_still_ctc("bg party_edna")

                edna.c "Oooh..."
                edna.c "{i}Gasp!{/i}"
                edna.c "It's so far in!"
                k.c "Alright [n.say_name], tell us."
                k.c "How's Grandma's cunt feeling on your dick right now?"
                n.c "I-It's soft and hot!"
                n.c "Haaa!"
                n.c "And it keeps getting warmer!"
                k.c "Yeah, grab Grandma's titties [n.say_name]."
                k.c "Get a firm grip on them!"
                edna.c "Squeeze them all you like [n.say_name], yes!"
                n.c "{i}Pant,{/i} {i}pant.{/i}.."
                k.c "..."
                k.c "You know what's really cool about this..."
                k.c "[n.say_name] has literally fucked three generations of our family!"
                k.c "That's like, mind blowing when you think about it."
                n.c "Mmn, Mm!"
                janet.c "[n.say_name] took a different approach to exploring our family tree!"
                k.c "Ha!"
                k.c "You think if [n.say_name] was a time traveler, he'd fuck our distant relatives too?"
                si.c "Haha!"


                if finale_julia_sam:
                    julia.c "I wouldn't put it past him."


                edna.c "I suppose this means [n.say_name] can fuck me at my condo, even when any of you are visiting!"
                si.c "You can do whatever you like Mom!"
                edna.c "That's great to hear [si.say_name]!"
                edna.c "Your son gets very horny over at my place."
                edna.c "He grabs my tits and ass all day!"
                si.c "That's not surprising."
                si.c "He does the same thing over here with me!"

                if finale_julia_sam:
                    sa.c "If I come over Grandma, can [n.say_name] and I fuck in the kitchen while we make cookies?!"
                    edna.c "Only if we can swap out!"
                    sa.c "No problem Grandma!"
                    edna.c "We'll have to be careful when [n.say_name] comes if the batter is nearby!"


            menu:
                "Continue":
                    n.c "Aah, yeah Grandma..."
                    k.c "[n.say_name] sure loves tits, doesn't he?"
                    janet.c "He's a boy, haha!"
                    janet.c "It's hard wired in him to love boobs!"
                    edna.c "We all love his cock though, so it goes both ways!"

                "Impregnate Grandma":
                    $ edna_impreg = True
                    n.c "Aah, yeah Grandma..."
                    edna.c "You have a serious expression on your face, [n.say_name]."
                    edna.c "We're giving everybody a good show, so keep it up!"
                    n.c "Aaah..."
                    n.c "I... {w=1.0}I have something else in mind..."
                    edna.c "(How curious)"
                    edna.c "Just what do you have in store for me, [n.say_name]?"
                    n.c "I-I'm going for it!"


                    if persistent.enable_sex_sounds:
                        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

                    call static_still_ctc("bg party_edna_cum")
                    n.c "Hrrm!"
                    n.c "..."
                    edna.c "Well, there's my answer!"
                    k.c "One big creampie for you, Grandma!"
                    k.c "I guess your pussy was too much for him!"
                    edna.c "It would seem so!"
                    janet.c "The look on [n.say_name]'s face says it all!"
                    janet.c "If I didn't know any better, I'd say you wore him out!"


                    if finale_julia_sam:
                        sa.c "Nah, [n.say_name]'s got tons of stamina left!"
                        sa.c "He gets second winds like it's nothing!"
                        julia.c "You're far from being done just yet, [n.say_name]."
                        julia.c "Let's hope your balls don't give in before then."

                    else:
                        k.c "Nah, we all know creampies are nothing to him!"
                        k.c "Stored in those balls are magnitudes of cum just waiting to come out!"

                    call static_still_ctc("bg party_edna_cum_impreg")
                    edna.c "O-Oh..."
                    edna.c "Oh dear."
                    k.c "Everything okay, Grandma?"
                    k.c "You've turned very pale!"

                    if finale_julia_sam:
                        sa.c "It's because [n.say_name] just let out a huge load in Grandma!"
                        sa.c "He fills you up good when he does it!"
                        sa.c "It's the best feeling in the world!"

                    else:
                        k.c "Was [n.say_name]'s creampie really that good?"
                        k.c "It certainly works wonders for me!"


                    edna.c "It's not that, dear."
                    edna.c "I suspect [n.say_name] may have just... {w=0.5}impregnated me."


                    "Everyone" "!!"
                    k.c "Woah, seriously?"
                    k.c "Holy shit!"
                    k.c "Way to go, [n.say_name]!"
                    si.c "[k.say_name]!"
                    edna.c "I suppose I shouldn't be surprised."
                    edna.c "This was a very special moment for [n.say_name] and I."
                    edna.c "It was only right that it would lead to this."
                    si.c "You're awfully calm about this Mom!"
                    edna.c "I do not see any issues with it."
                    edna.c "He is my grandson, after all."
                    edna.c "The way I see it, it's his own way of proving just how much he loves his grandmother!"
                    edna.c "And I couldn't be any happier to share that love with him!"


                    if edna_fucked_vaginally() not in scenes_completed or finale_chose_edna is False:
                        k.c "The first time [n.say_name]'s dick goes inside Grandma..."
                        k.c "He goes and knocks her up!"
                        k.c "That's just so crazy to think about!"


                    k.c "But can a woman at your age still even get pregnant, though?"
                    si.c "[k.say_name]!!!"
                    si.c "That was a bit... {w=1.0}direct, don't you think?"
                    janet.c "Haha!"
                    janet.c "She definitely takes after me in that regard!"
                    si.c "..."
                    si.c "(You could have at least phrased it better, [k.say_name])"
                    janet.c "It certainly does raise an interesting question, though!"
                    edna.c "And I believe I have the answer."
                    si.c "A-And what would that be, Mom?"
                    edna.c "[n.say_name] helped me awaken my sex drive I thought I had lost."
                    edna.c "He's made me feel young again."
                    edna.c "So I am not surprised that the effect he had on me would also extend to fertility!"
                    janet.c "Incredible..."
                    janet.c "I guess age really is just a number!"
                    edna.c "Oh yes, absolutely!"
                    edna.c "I am a firm believer of that!"
                    edna.c "You are never too old to have kids, haha!"
                    si.c "..."

                    pause 1.0
                    janet.c "How are you doing, [n.say_name]?"
                    janet.c "Can we keep going?"
                    n.c "..."
                    n.c "Y-Yes!"
                    n.c "Yes, I can!"
                    k.c "Woo!"

                    if finale_julia_sam:
                        sa.c "Yess!"

                    si.c "That's the spirit, sweetie!"

            if not finale_chose_edna:
                $ finale_fucked_amount += 1

            $ finale_chose_edna = True
        "Aunt [janet.say_name]" if not finale_chose_janet:
            if not finale_chose_janet:
                $ finale_fucked_amount += 1

            $ finale_chose_janet = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character(janet, appearance = "pose handchest face flirt blush false")
            janet.c "Looks like I'm up!"


            call static_still_ctc("bg party_janet")
            janet.c "Mmn, yeah..."
            janet.c "You like it when I ride you?"
            n.c "Aah, ah..."
            n.c "I do Aunt [janet.say_name]."
            k.c "Is it true you two fuck on the beach?"
            janet.c "Yes, we do!"
            janet.c "It's a lot of fun to fuck when you're so out in the open!"
            si.c "Please be careful doing that!"
            si.c "If you ever get caught..."
            janet.c "We'll be fine sis!"
            janet.c "Many people have passed by us, and no one has ever noticed."
            edna.c "Except for when I spotted you!"
            janet.c "That doesn't count Mom!"
            janet.c "[n.say_name] told you how and where we fuck, so you had all the intel!"
            edna.c "That is true, haha!"


            if finale_julia_sam:
                julia.c "I really thought [k.say_name] was joking when she told me you were fucking [n.say_name], Mom."
                julia.c "Now I have the knowledge that [n.say_name]'s dick was in your pussy at one point."
                k.c "And ass, and mouth too."
                janet.c "I heard you had your first anal experience with [n.say_name], [julia.say_name]!"
                janet.c "According to [n.say_name], you were moaning up a storm!"
                julia.c "Don't divulge details like that [n.say_name]!"
                si.c "Haha, it's okay [julia.say_name]!"
                k.c "Yeah!"
                k.c "Nothing wrong with being a fan of taking it up the butt!"
                julia.c "..."


            janet.c "[n.say_name] and I do a lot of naked meditation before and after we fuck!"
            janet.c "I think all of us should do it after we're done!"
            edna.c "That sounds fun!"
            n.c "{i}Pant.{/i}.."
            janet.c "We're nude around the house a lot too!"
            k.c "You are, huh?"
            k.c "I gotta come over some time then!"
            k.c "I wish I could go about my daily life with no clothes!"
            janet.c "It's the next best thing when you're over at my house!"
        "[julia.say_name]" if finale_julia_sam and not finale_chose_julia:
            if not finale_chose_julia:
                $ finale_fucked_amount += 1

            $ finale_chose_julia = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character(julia, appearance = "outfit nude pose armcross face aroused blush false")
            julia.c "I'm ready to go."


            call static_still_ctc("bg party_julia")
            n.c "Gah, ah!"
            n.c "Bounce up and down like that [julia.say_name]!"
            julia.c "So I was right all along [n.say_name]...{w=1.0}you are a pervert."
            julia.c "I just didn't realize just how big of a one you were!"
            k.c "I encourage perversion!"
            k.c "When I caught [n.say_name] staring at my butt while doing squats, I gave him exactly what he wanted..."
            k.c "I literally came into his room, pulled down my shorts, and had him stare at my asshole!"
            julia.c "..."
            julia.c "Wow."
            julia.c "So you're a pervert too [k.say_name]."
            edna.c "All of us are perverts in this family [julia.say_name]."
            edna.c "And that includes you too!"
            janet.c "Anytime you take a mouthful of cum and swallow it in one go, that puts you in the pervert category, haha!"
            n.c "[julia.say_name] really loves to swallow my cum."
            n.c "She opens her mouth really wide when I'm about to shoot my jizz in her mouth."
            julia.c "..."
            sa.c "I can confirm that is totally true!"
            sa.c "[julia.say_name] will suck up any remaining cum lying on the floor!"
            si.c "[n.say_name]'s ejaculations are not exactly miniscule either!"
            si.c "He shot out so much one time, it covered my tits in a thick layer of semen!"
            edna.c "I nearly choked on his cum after he spurted into my mouth."
            k.c "What they're trying to say [julia.say_name] is...{w=1.0}you have to be quite the cum dumpster to gulp down a whole load from [n.say_name]!"
            julia.c "Okay, I get it."
            julia.c "I never said I wasn't a pervert."
            n.c "Mmn!"
            n.c "Go all the way down [julia.say_name]!"
            n.c "Aah yeah!"
        "[k.say_name]" if not finale_chose_kira:
            if not finale_chose_kira:
                $ finale_fucked_amount += 1

            $ finale_chose_kira = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character(k, appearance = "pose armsup face flirt blush false")
            k.c "Bring it on bro!"


            call static_still_ctc("bg party_kira")
            k.c "Hold on tight!"
            k.c "They don't call this the piledriver for nothing!"
            n.c "Ha-ah!"
            edna.c "What is the position called again?"
            janet.c "I think she said the piledriver."
            edna.c "The piledriver, haha!"
            k.c "I encourage everyone to practice the kamasutra!"
            janet.c "Kama-whatsa?"
            si.c "Kamasutra!"
            si.c "They're all these crazy sex positions you can perform."
            si.c "You should see some of the stuff [k.say_name] and [n.say_name] have done with each other."
            si.c "They've done a standing sixty-nine before!"
            edna.c "If I tried a position like that, my joints would lock up and I'd be stuck!"
            si.c "I'm not going to even attempt anything like what [k.say_name] does."
            si.c "I'd pull a muscle for sure!"
            janet.c "Hmm..."
            janet.c "You'll have to let me know about some of these positions [k.say_name]."
            janet.c "I think I might try one with [n.say_name] sometime!"


            if finale_julia_sam:
                sa.c "I need to pick out several for [n.say_name] and I to attempt!"
                sa.c "Maybe you can help us choose [k.say_name]!"


            k.c "The kamasutra is gaining traction in the family [n.say_name]!"
            k.c "Remember to keep yourself loose and flexible!"
            n.c "..."
            n.c "Hrm, hoo!"
            k.c "I bet this could work for anal as well [n.say_name]!"
            k.c "Another time when we're out here, that's what we'll try!"
        "Mom" if not finale_chose_simone:
            if not finale_chose_simone:
                $ finale_fucked_amount += 1

            $ finale_chose_simone = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character(si, appearance = "pose handsup face flirt blush false")
            si.c "Here we go sweetie!"


            call static_still_ctc("bg party_simone")
            n.c "Yeah Mom, yeah!"
            n.c "Oh!"
            si.c "Yes baby!"
            si.c "Bang Mommy in front of everyone!"
            si.c "Show them how much you love to fuck me!"
            edna.c "Is there really any better bond than a mother and son?"
            k.c "I don't know Grandma, but I know [n.say_name]'s dick has bonded to Mom's pussy!"
            janet.c "They look like they have fucked a lot together."
            k.c "Oh, you have no idea."
            k.c "If [n.say_name] has trouble falling asleep at night, Mom will come in..."
            k.c "And she'll suck his cock until he comes in her mouth, and then he falls asleep right after!"
            k.c "It's like clockwork!"
            edna.c "It's like a more sensual version of a goodnight kiss!"


            if finale_julia_sam:
                sa.c "[n.say_name] also has Mom give him titfucks all the time!"
                sa.c "She's always taking her boobs out!"
                janet.c "My sister has a lot to offer with those gigantic melons of hers!"


            si.c "Aah..."
            si.c "[n.say_name] knew next to nothing about sex before the summer started!"
            si.c "His penis started getting hard whenever he would look at my chest."
            k.c "And the rest was history!"
            janet.c "You opened the door for him sis!"
            janet.c "That was the right call, in my opinion!"
            si.c "Haah!"
            si.c "I don't regret it one bit!"
            n.c "Ahn, Mooom!"
            edna.c "If [n.say_name] fucks you all the time like this [si.say_name], you may end up with a new family member in the future!"


            if edna_impreg:
                edna.c "Actually, make that two new family members!"
                edna.c "Your child and my child will get along swimmingly!"
        "[sa.say_name]" if finale_julia_sam and not finale_chose_sam:
            if not finale_chose_sam:
                $ finale_fucked_amount += 1

            $ finale_chose_sam = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character(k, appearance = "pose armcross face flirt blush false")
            k.c "Come on over [sa.say_name]!"


            call static_still_ctc("bg party_sam")
            n.c "Haaah!"
            sa.c "Aah [n.say_name]!"
            sa.c "Yeah, yeah!"
            k.c "Wrap your legs around him like this."
            k.c "I'll keep you propped up a bit [sa.say_name]."
            edna.c "Now isn't that the sweetest thing, seeing all your children together [si.say_name]?"
            edna.c "They look like they know what they're doing though!"
            si.c "Can you believe [sa.say_name] and [n.say_name] do this while playing video games?"
            edna.c "Oh, they do?"
            edna.c "Haha!"
            janet.c "That doesn't surprise me."
            janet.c "They are so in tune with technology, it's easy for them to multitask!"
            edna.c "I've never looked at [n.say_name] from the back."
            edna.c "Look at how cute his balls are!"
            k.c "Nice bro."
            k.c "You're putting a good amount of force behind those thrusts!"
            n.c "Oh...{w=1.0}oh..."
            sa.c "Aah, ahn!"
        "Kacey" if finale_kacey_arrived and not finale_chose_kacey:
            if not finale_chose_kacey:
                $ finale_fucked_amount += 1

            $ finale_chose_kacey = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character(gloryhole_girl, appearance = "pose handface face flirt blush false")
            gloryhole_girl.c "I'm so ready for you [n.say_name]!"

            call process_character(gloryhole_girl, appearance = "pose handface face flirt blush false")
            gloryhole_girl.c "My pussy's been wet since I got here!"

            call static_still_ctc("bg party_kacey")
            n.c "Mm-mph!"
            gloryhole_girl.c "It's so refreshing to be out of that bathroom [n.say_name]!"
            gloryhole_girl.c "I'm so glad we aren't restricted to there anymore!"
            janet.c "You two met in a bathroom?"
            gloryhole_girl.c "Yes, at the local park!"
            gloryhole_girl.c "It's been our go to meetup place throughout the summer!"
            edna.c "How exactly did you meet each other in the same bathroom?"
            edna.c "Did you get mixed up by the signs?"
            k.c "[gloryhole_girl.say_name]'s leaving out some important aspects to the whole story."
            k.c "Such as the gloryhole."
            si.c "Gloryhole?!"
            gloryhole_girl.c "Mmn, haah..."
            gloryhole_girl.c "Y-Yes, I was spending my time in the men's bathroom at a gloryhole."
            gloryhole_girl.c "I was...{w=1.0}curious about who I may encounter."
            edna.c "That's...{w=1.0}adventurous of you."
            k.c "Strategic choice of words Grandma, haha!"
            gloryhole_girl.c "Ever since [n.say_name]'s cute cock first poked through the gloryhole, I've wanted no one else but him!"
            janet.c "We can see that."
            n.c "Mmn!"
            k.c "At this rate, [n.say_name] will pass out due to titty smothering!"
            gloryhole_girl.c "He won't."
            gloryhole_girl.c "I know [n.say_name] can handle much more than this!"
            gloryhole_girl.c "That's why he's capable of fucking all of us!"
            si.c "You don't seem to mind that [n.say_name] has been fucking all of us in addition to you!"
            gloryhole_girl.c "I don't mind at all, because [n.say_name] always makes time for me."
            gloryhole_girl.c "As long as that remains constant, he can fuck as many other girls as he likes!"
            janet.c "School is going to be a doozy for [n.say_name]."
            janet.c "Good luck [si.say_name], that's all I have to say."
            si.c "I gave [n.say_name] explicit instructions not to have any sexual encounters while at school."
            k.c "I've already bet he won't last a week."
            edna.c "I was going to say a few days!"
            k.c "I'm calling it now..."
            k.c "[n.say_name] is going to fuck his teacher."
            k.c "It's gonna happen."
            si.c "Oh dear...{w=1.0}that's the last thing I need."
            janet.c "His teacher will give him straight A's for all the \"extra credit\" he'll be doing, haha!"
            gloryhole_girl.c "Ah..."
            gloryhole_girl.c "If you need someone to pick him up from school every day, I'll volunteer."
            si.c "That's very generous of you [gloryhole_girl.say_name]!"
            si.c "I'll be sure to keep your offer in mind!"
            gloryhole_girl.c "If I pick him up, I'll probably need [n.say_name] to...{w=1.0}you know..."
            k.c "Duh, that's obvious!"
        "Vicky" if finale_vicky_arrived and not finale_chose_vicky:
            if not finale_chose_vicky:
                $ finale_fucked_amount += 1

            $ finale_chose_vicky = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character(vicky, appearance = "pose handup face flirt blush false")
            vicky.c "You'd like me to jump into the fray [n.say_name]?"

            call process_character(vicky, appearance = "pose handup face flirt blush false")
            vicky.c "I've thought of the perfect position for you and I!"

            call static_still_ctc("bg party_vicky")

            vicky.c "Mmm, yes..."
            vicky.c "..."
            vicky.c "I was hoping to meet your family one day [n.say_name]."
            vicky.c "However, I didn't expect to meet them in this kind of circumstance!"
            n.c "Aah, haa..."
            janet.c "So you and [n.say_name]...{w=1.0}work together?"
            vicky.c "That's correct."
            vicky.c "We established a business relationship over the summer."
            edna.c "Looks like it's a bit more than just business related..."
            si.c "I'll say."
            vicky.c "Ooh..."
            vicky.c "I can assure you, that while [n.say_name] and I do perform extracurricular activities together..."
            vicky.c "We have always strived for success with our endeavors, and each time it has been fruitful."
            k.c "Yeah, you haven't heard all the details yet Mom, but [vicky.say_name] has helped [n.say_name] grow his streaming channel to a huge degree!"


            if finale_julia_sam:
                sa.c "It's amazing Mom!"
                sa.c "The channel [n.say_name] and I have, has skyrocketed in subscribers ever since [n.say_name] talked to [vicky.say_name] about improvements we could make!"


            si.c "Really?"
            n.c "Yeah Mom, ah...{w=1.0}[vicky.say_name] showed me just how much the Twinsticks channel could grow."
            n.c "Now [sa.say_name] and I are generating income from it!"
            si.c "That's unbelievable!"
            si.c "So you're literally being paid to play video games all day?"
            vicky.c "Essentially, yes."
            edna.c "That's impressive of your son [si.say_name]."
            edna.c "If he's already generating income for your household, who knows how far he'll go in the next few years!"
            vicky.c "[n.say_name] and I have a lot of great things planned for the future."
            vicky.c "We're always thinking ahead!"
            si.c "I'm so proud of you [n.say_name]!"
            si.c "I can't wait to see what you and [vicky.say_name] are working on next!"
            si.c "I hope it does well, for both of you!"
            k.c "Oh I think it will Mom..."
            vicky.c "Your daughter [k.say_name] is also looking to join [n.say_name] and I in our new business venture."
            vicky.c "We think she will be well suited for it."
            si.c "That's great [k.say_name]!"
            k.c "I'll let you in on the details later Mom."
            k.c "All you need to know right now is [n.say_name] is the ideal candidate for the business [vicky.say_name] has come up with."
            si.c "..."
            si.c "I think I'm beginning to realize what it may be..."
            k.c "Hehe."

    call finale_scene_choices_impreg_override(dream = dream)

    return

label finale_scene_revisit_fuck_choices_impreg_override:
    $ dice_roll = random.randint(1,2)
    menu:
        "Grandma":
            if not finale_chose_edna:
                $ finale_fucked_amount += 1

            $ finale_chose_edna = True

            call static_still_ctc("bg party_Edna")

            menu:
                "Continue":
                    if dice_roll == 1:
                        edna.c "It's a good thing you come from a family with high vitality!"
                    else:
                        edna.c "Will you be inviting any additional girls to these parties?"
                "Impregnate Grandma":
                    $ edna_impreg = True
                    n.c "Aah, yeah, Grandma..."
                    edna.c "You have a serious expression on your face, [n.say_name]."
                    edna.c "We're giving everybody a good show, so keep it up!"
                    n.c "Aaah..."
                    n.c "I... ah,{w=1.0}I have something else in mind..."
                    edna.c "Oh?"
                    edna.c "How curious!"
                    edna.c "Just what do you have in store for me, [n.say_name]?"
                    n.c "I-I'm going for it!"

                    if persistent.enable_sex_sounds:
                        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

                    call static_still_ctc("bg party_edna_cum")

                    n.c "Hrrm!"
                    n.c "..."
                    edna.c "Well, there's my answer!"
                    k.c "One big creampie for you, Grandma!"
                    k.c "I guess your pussy was too much for him!"
                    edna.c "It would seem so!"
                    janet.c "The look on [n.say_name]'s face says it all!"
                    janet.c "If I didn't know any better, Mom, I'd say you wore him out!"

                    if finale_julia_sam:
                        sa.c "Nah, [n.say_name]'s got tons of stamina left!"
                        sa.c "He gets second winds like it's nothing!"
                        julia.c "You're far from being done just yet, [n.say_name]."
                        julia.c "Let's hope your balls don't give in before then."
                    else:
                        k.c "Nah, we all know creampies are nothing to him!"
                        k.c "Stored in those balls are magnitudes of cum just waiting to come out, still."
                        k.c "That was just the beginning!"

                    call static_still_ctc("bg party_edna_cum_impreg")

                    edna.c "O-Oh..."
                    edna.c "Oh dear."
                    k.c "Everything okay, Grandma?"
                    k.c "You've turned very pale, haha!"

                    if finale_julia_sam:
                        sa.c "It's because [n.say_name] just let out a huge load in Grandma!"
                        sa.c "He fills you up good when he does it!"
                        sa.c "It's the best feeling in the world!"
                    else:
                        k.c "Was [n.say_name]'s creampie really that good?"
                        k.c "It certainly works wonders for me!"

                    edna.c "It's not that, dear."
                    edna.c "I suspect [n.say_name] may have just... {w=0.5}impregnated me."

                    "Everyone" "!!"

                    k.c "Woah, seriously?"
                    k.c "Holy shit!"
                    k.c "Way to go, [n.say_name]!"
                    si.c "[k.say_name]!"
                    edna.c "I suppose I shouldn't be surprised."
                    edna.c "This was a very special moment for [n.say_name] and I."
                    edna.c "It was only right that it would lead to this."
                    si.c "You're awfully calm about this, Mom!"
                    edna.c "I do not see any issues with it."
                    edna.c "He is my beloved grandson, after all."
                    edna.c "The way I see it, this is his own way of proving just how much he loves his grandmother!"
                    edna.c "And I couldn't be any happier to share that love with him!"

                    if edna_fucked_vaginally() not in scenes_completed or finale_chose_edna is False:
                        k.c "The first time [n.say_name]'s dick goes inside Grandma..."
                        k.c "He goes and knocks her up!"
                        k.c "That's just so crazy to think about!"

                    k.c "But can a woman of your age still even get pregnant, though?"
                    si.c "[k.say_name]!!"
                    si.c "That was a bit... {w=1.0}direct, don't you think?"
                    janet.c "Haha!"
                    janet.c "She definitely takes after me in that regard!"
                    si.c "..."
                    si.c "(You could have at least phrased it better, [k.say_name])"
                    janet.c "It certainly does raise an interesting question, though."
                    edna.c "And I believe I have the answer."
                    si.c "A-And what would that be, Mom?"
                    edna.c "[n.say_name] helped me awaken my sex drive I thought I had lost."
                    edna.c "He's made me feel young again."
                    edna.c "So I am not surprised that the effect he had on me would also extend to fertility!"
                    janet.c "Incredible..."
                    janet.c "I guess age really is just a number!"
                    edna.c "Oh yes, absolutely!"
                    edna.c "I am a firm believer of that!"
                    edna.c "You are never too old to have kids, haha!"
                    si.c "..."

                    pause 1.0

                    janet.c "How are you doing, [n.say_name]?"
                    janet.c "Can we keep going?"
                    n.c "..."
                    n.c "Y-Yes!"
                    n.c "Yes, I can!"
                    janet.c "Woo!"
                    k.c "Nice, bro!"

                    if finale_julia_sam:
                        sa.c "Yess!"

                    si.c "That's the spirit, sweetie!"

        "Aunt [janet.say_name]":
            if not finale_chose_janet:
                $ finale_fucked_amount += 1

            $ finale_chose_janet = True
            call static_still_ctc("bg party_Janet")

            if dice_roll == 1:
                janet.c "You'll definitely need all of us on speedial [n.say_name]!"
            else:
                janet.c "We should all practice some yoga poses that increase our sex drive!"

        "[julia.say_name]" if finale_julia_sam:
            if not finale_chose_julia:
                $ finale_fucked_amount += 1
            call static_still_ctc("bg party_julia")

            $ finale_chose_julia = True

            if dice_roll == 1:
                julia.c "If you come over to my house in the future, just know that both my Mom and I will fuck you."
            else:
                julia.c "I wonder if you could handle doing some anal with all of us too."


        "[k.say_name]":
            if not finale_chose_kira:
                $ finale_fucked_amount += 1
            call static_still_ctc("bg party_kira")

            if dice_roll == 1:
                k.c "I might start making holes in the back of my shorts [n.say_name]."
                k.c "Then you can just come up and butt fuck me whenever you want!"
            else:
                k.c "I want to hear all about what you do at school [n.say_name]."
                k.c "I bet you'll be fucking five girls at minimum before winter break!"

            $ finale_chose_kira = True

        "Mom":
            if not finale_chose_simone:
                $ finale_fucked_amount += 1
            call static_still_ctc("bg party_simone")

            if dice_roll == 1:
                si.c "We're going to need a lot more furniture out here with this much company becoming regular!"
            else:
                si.c "Remember, you can always take a break sweetie."
                si.c "Not that you really want to do that most of the time!"

            $ finale_chose_simone = True

        "[sa.say_name]" if finale_julia_sam:
            if not finale_chose_sam:
                $ finale_fucked_amount += 1
            call static_still_ctc("bg party_sam")

            if dice_roll == 1:
                sa.c "I hope we meet some cool new friends at school [n.say_name]."
                sa.c "Then we could invite them over to these parties!"
            else:
                sa.c "It would be epic if you came in all of our pussies!"
                k.c "It would!"

            $ finale_chose_sam = True

        "Kacey":
            if not finale_chose_kacey:
                $ finale_fucked_amount += 1
            call static_still_ctc("bg party_kacey")

            if dice_roll == 1:
                gloryhole_girl.c "I should see if I can apply to be a teacher at your school [n.say_name]."
                gloryhole_girl.c "Then we could see each other even more!"
            else:
#                gloryhole_girl.c "You should come hang out at my place someday [n.say_name]."
#                gloryhole_girl.c "We can fuck all day and all night over there!"
                gloryhole_girl.c "You should invite me to your house more, [n.say_name]."
                gloryhole_girl.c "We can fuck whenever you want, all day and all night!"

# ^^ rewritten dialogue to account for what's said in the kacey apartment intro about her landlord
# circumventing lack of artist for a kacey sex scene at her apartment

            $ finale_chose_kacey = True

        "Vicky":
            if not finale_chose_vicky:
                $ finale_fucked_amount += 1
            call static_still_ctc("bg party_vicky")

            if dice_roll == 1:
                vicky.c "All your family are perfect candidates for the website!"
                vicky.c "I just have to see if I can convince any of them to be filmed..."
            else:
                vicky.c "You should think about fucking some high profile female executives."
                vicky.c "We could score some huge business deals that way!"

            $ finale_chose_vicky = True
        "Cum" if finale_fucked_amount >= 3:
            if finale_julia_sam:
                call static_still_ctc("bg party_Group_NoCum")
            else:
                call static_still_ctc("bg party_Group_NoJS_NoCum")
            jump finale_scene_cum

    jump finale_scene_revisit_fuck_choices

    return

label finale_scene_end_impreg_override(dream = dream):
    k.c "..."
    k.c "Everyone had a turn at this point?"
    si.c "I believe so, yes!"
    janet.c "How are you holding up [n.say_name]?"

    if edna_impreg:
        n.c "I..."
        n.c "I-I'm fine."
        k.c "He's already busted one nut."
        k.c "But we all know he's got another big one coming!"
        janet.c "[k.say_name]'s right, [n.say_name]!"
        janet.c "You must be ready to explode by now!"
        n.c "I-I don't know how I've held this one in this long..."
        edna.c "Me neither!"
        edna.c "I'm still feeling the effects of the first one, haha!"
        k.c "Release that tension from your balls, [n.say_name]."
        k.c "You know you want to!"

    else:
        janet.c "You must be ready to explode by now!"
        n.c "I-I don't know how I've held it in this long..."
        edna.c "Me neither!"
        edna.c "You need to release the tension from your balls!"

    gloryhole_girl.c "I can help with that [n.say_name]."
    gloryhole_girl.c "You know I can take your whole load."

    if finale_julia_sam:
        sa.c "Aw, but I want to get splattered with [n.say_name]'s nut butter!"
        julia.c "You're not the only one that can take a full load from [n.say_name], [gloryhole_girl.say_name]."
        julia.c "I've had no problem doing it before."

    janet.c "How about I deepthroat you [n.say_name] while you come?"
    janet.c "I know how to control my gag reflex!"
    si.c "Would you like to cover my face, sweetie?"
    k.c "Hold it, hold it!"
    k.c "..."

    if edna_impreg:
        k.c "This is silly to debate who should take the wad from [n.say_name]."
        k.c "Grandma's already beaten us to it, after all."
        edna.c "Now, now, I certainly didn't mean to hog [n.say_name]'s cum all to myself!"
        edna.c "In fact, I think it would be lovely if we could all share!"
        janet.c "Are you saying [n.say_name] should come on all of us, Mom?"

    else:
        k.c "This is silly to debate who should take the wad from [n.say_name]."
        k.c "Why should one girl hog all that cream, when we can share?"
        edna.c "Are you saying, [n.say_name] should come on all of us?"

    if edna_impreg:
        edna.c "Absolutely, yes!"
        edna.c "He still has plenty of cream to go around!"
        edna.c "We've all had a turn with him, correct?"
    else:
        k.c "He fucked all of us, right?"

    if edna_impreg:
        edna.c "In that case, he should have no problem giving us all a {i}\"jizz coating!\"{/i}"
        k.c "Haha!"
        k.c "I like the way you think, Grandma!"

    else:
        k.c "So he should have no problem giving us all a jizz coating!"

    n.c "..."

    call fade_to_black(1)
    k.c "Everyone, gather around like we're taking a photo."
    k.c "Push in as close as you can!"

    if finale_julia_sam:
        sa.c "This is gonna be fun!"
        k.c "[sa.say_name] and [julia.say_name], you go up front there."
        k.c "Mom, you want to go over here?"

    si.c "Oh, I see what you're doing [k.say_name]."
    si.c "Hurry, before [n.say_name] comes!"
    janet.c "'Scuse me, while I wedge myself in here..."
    k.c "Okay...{w=1.0}okay..."
    k.c "I think that's as good as we'll get!"
    k.c "Everybody, on the count of three..."
    k.c "Open wide, stick out your tongues and say {i}\"aah!\"{/i}"

    if finale_julia_sam:
        call static_still_ctc("bg party_Group_NoCum")
    else:
        call static_still_ctc("bg party_Group_NoJS_NoCum")

    if finale_julia_sam:
        sa.c "Aaah!"
        sa.c "I want it all in my mouth!"

    gloryhole_girl.c "Shoot some over here [n.say_name]!"
    gloryhole_girl.c "Let me taste your cum!"
    edna.c "Don't forget Grandma [n.say_name]!"

    if finale_julia_sam:
        julia.c "Try not to shoot your jizz in my eye [n.say_name]."
        julia.c "Aim a bit lower when you target me."

    si.c "You can be as messy as you like with me, sweetie!"
    si.c "I don't mind!"
    janet.c "You and I think alike on that, sis!"
    janet.c "I'll take everything you give me [n.say_name]!"
    vicky.c "I hope you'll have enough left to get over to me, [n.say_name]!"
    vicky.c "Best of luck!"
    n.c "Oooh man..."
    n.c "This one is gonna be really big!"
    k.c "I'm widening my mouth some more then!"
    n.c "I've never had the urge to come as much as I do now!"
    n.c "Mmggh..."
    n.c "Mmnh!"
    n.c "Ooooh!!"

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    show bg party_group_nate_cum2 as cum
    with Dissolve(0.5)
    pause

    if finale_julia_sam:
        sa.c "I bet I'll get covered in more cum than you, [julia.say_name]!"
        julia.c "Heh, we'll see about that."

        hide cum
        show bg party_group_sam_cum as cum_sam
        show bg party_group_julia_cum as cum_julia
        with Dissolve(0.5)
        pause
        k.c "You two were directly in the line of fire!"
        k.c "Lucky..."
        sa.c "Mmm..."
        sa.c "That's why I wanted to be up front!"
        n.c "Aah, aah..."
        julia.c "I think that cumshot was only the beginning."
        sa.c "Give us another blast [n.say_name]!"
        n.c "Y-You got it!"
        n.c "Another one is...{w=1.0}coming!"

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

        show bg party_group_nate_cum2 as cum
        with Dissolve(0.5)
        pause
        k.c "Right here, bro, right here!"
        gloryhole_girl.c "Cover me [n.say_name]!"
        gloryhole_girl.c "I want that delicious cum!"

        hide cum
        show bg party_group_kacey_cum as cum_kacey
        show bg_party_group_kira_cum_juliasam as cum_kira
        with Dissolve(0.5)
        pause

        gloryhole_girl.c "Thank you, [n.say_name], thank you!"
        k.c "I got my healthy portion!"
        k.c "I can always go for more though!"
        k.c "I'll suck it all down!"
        gloryhole_girl.c "So can I!"
        gloryhole_girl.c "Would you give us more, [n.say_name]?"
        n.c "I-I think I can."
        si.c "Send some over here, sweetie."
        si.c "I'd like to have a taste!"
        vicky.c "You don't want your Mom's mouth to get dry, do you, [n.say_name]?"
        vicky.c "She and I require refreshment!"
        si.c "Haha!"
        si.c "Yes, that's right!"
        n.c "O-Okay!"
        n.c "I'll give it to both of you!"
        n.c "Get ready!"

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
        show bg party_group_nate_cum1 as cum
        with Dissolve(0.5)
        pause
        n.c "Gaah!"
        vicky.c "There it is!"
        si.c "That's my boy!"

        hide cum
        show bg party_group_vicky_cum as cum_vicky
        show bg party_group_simone_cum as cum_simone
        with Dissolve(0.5)
        pause
        k.c "Another nice shot, [n.say_name]!"

        k.c "That went whizzing past my ear!"
        vicky.c "This feels great on my face!"
        vicky.c "And the taste is as good as ever!"
        si.c "I knew my son's semen was something special!"
        si.c "And I'm not just saying that because I'm your Mom!"
        gloryhole_girl.c "Your Mom's right, [n.say_name]!"
        gloryhole_girl.c "I could swallow your cum all day!"
        k.c "Your jizz could practically be it's own food group!"
        sa.c "I'd have it every day!"
        julia.c "If it was on some chocolate or peanut butter, I'd go for it."
        janet.c "[n.say_name], don't forget about us!"
        edna.c "We're still waiting!"
        n.c "Sorry Aunt [janet.say_name] and Grandma."
        n.c "I hope I can get one more out."
        janet.c "You have to, [n.say_name], you have to!"
        edna.c "You can do it, [n.say_name]!"
        edna.c "Will that last cumshot out!"
        k.c "Yeah, reach deep down into your balls for it!"
        n.c "Ah..."
        n.c "Yes, I...{w=1.0}I have it!"
        n.c "I've got one more in me!"
        janet.c "[n.say_name]'s saved the best for last!"
        edna.c "Our patience will be rewarded!"
        n.c "Mmn!"
        n.c "Aunt [janet.say_name]...{w=1.0}Grandma..."
        n.c "Here's some for you!"


        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
        show bg party_group_nate_cum3 as cum
        with Dissolve(0.5)
        pause
        janet.c "Don't miss it Mom!"
        edna.c "I won't, I won't!"

        hide cum
        show bg_party_group_janet_cum_juliasam as cum_janet
        show bg_party_group_edna_cum_juliasam as cum_edna
        with Dissolve(0.5)
        pause
        janet.c "Aww yeah!"
        janet.c "Nice and messy!"
        edna.c "It was very much worth the wait!"
        edna.c "Your cum is still thick, even after all your other cumshots!"
        n.c "{i}Pant...pant...{/i}"
        n.c "That's...that's it."
        n.c "I don't think I have a single drop left."
        sa.c "That's okay, [n.say_name]!"
        sa.c "All targets have been hit!"
        k.c "Yep!"
        k.c "All of us got coated by your man milk!"
        k.c "Now we're all one big, white, sticky mess!"

    else:
        k.c "It begins!"
        k.c "Right here bro, right here!"
        gloryhole_girl.c "Cover me [n.say_name]!"
        gloryhole_girl.c "I want that delicious cum!"


        hide cum
        show bg party_group_kacey_cum as cum_kacey
        show bg party_group_kira_cum as cum_kira
        with Dissolve(0.5)
        pause
        gloryhole_girl.c "Thank you [n.say_name], thank you!"
        k.c "I got my healthy portion!"
        k.c "I can always go for more though!"
        k.c "I'll suck it all down!"
        gloryhole_girl.c "So can I!"
        gloryhole_girl.c "Would you give us more, [n.say_name]?"
        n.c "I-I think I can."
        si.c "Send some over here, sweetie."
        si.c "I'd like to have a taste!"
        vicky.c "You don't want your Mom's mouth to get dry, do you [n.say_name]?"
        vicky.c "She and I require refreshment!"
        si.c "Haha!"
        si.c "Yes, that's right!"
        n.c "O-Okay!"
        n.c "I'll give it to both of you!"
        n.c "Get ready!"


        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
        show bg party_group_nate_cum1 as cum
        with Dissolve(0.5)
        pause
        n.c "Gaah!"
        vicky.c "There it is!"
        si.c "That's my boy!"

        hide cum
        show bg party_group_vicky_cum as cum_vicky
        show bg party_group_simone_cum as cum_simone
        with Dissolve(0.5)
        pause
        k.c "Another nice shot [n.say_name]!"
        k.c "That went whizzing past my ear!"
        vicky.c "This feels great on my face!"
        vicky.c "And the taste is as good as ever!"
        si.c "I knew my son's semen was something special!"
        si.c "And I'm not just saying that because I'm your Mom!"
        gloryhole_girl.c "Your Mom's right [n.say_name]!"
        gloryhole_girl.c "I could swallow your cum all day!"
        k.c "Your jizz could practically be it's own food group!"
        janet.c "[n.say_name], don't forget about us!"
        edna.c "We're still waiting!"
        n.c "Sorry Aunt [janet.say_name] and Grandma."
        n.c "I hope I can get one more out."
        janet.c "You have to, [n.say_name], you have to!"
        edna.c "You can do it, [n.say_name]!"
        edna.c "Will that last cumshot out!"
        k.c "Yeah, reach deep down into your balls for it!"
        n.c "Ah..."
        n.c "Yes, I...{w=1.0}I have it!"
        n.c "I've got one more in me!"
        janet.c "[n.say_name]'s saved the best for last!"
        edna.c "Our patience will be rewarded!"
        n.c "Mmn!"
        n.c "Aunt [janet.say_name]...{w=1.0}Grandma..."
        n.c "Here's some for you!"


        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
        show bg party_group_nate_cum3 as cum
        with Dissolve(0.5)
        pause
        janet.c "Don't miss it Mom!"
        edna.c "I won't, I won't!"

        hide cum
        show bg party_group_janet_cum as cum_janet
        show bg party_group_edna_cum as cum_edna
        with Dissolve(0.5)
        pause
        janet.c "Aww yeah!"
        janet.c "Nice and messy!"
        edna.c "It was very much worth the wait!"
        edna.c "Your cum is still thick, even after your other cumshots!"
        n.c "{i}Pant...{w=1.0}pant...{/i}"
        n.c "That's...{w=1.0}that's it."
        n.c "I don't think I have a single drop left."
        k.c "That's alright, bro!"
        k.c "All of us got coated by your man milk!"
        k.c "Now we're all one big, white, sticky mess!"
        n.c "..."


    if finale_julia_sam and edna_impreg:
        sa.c "And the cherry on top, [n.say_name] impregnated Grandma!"
        si.c "..."
        edna.c "Oh, yes!"
        edna.c "We certainly cannot forget that part!"
        sa.c "It was amazing to watch!"

    gloryhole_girl.c "This has been a most excellent party!"
    gloryhole_girl.c "Thank you for inviting me to it!"
    vicky.c "Yes, thank you!"
    vicky.c "I'm happy I was able to make it over in time!"
    si.c "You're welcome!"
    si.c "I hope we can do this again sometime!"

    if finale_julia_sam:
        sa.c "Yeah!"
        sa.c "I'd love to have more frequent parties like this!"
        julia.c "I'm normally not into parties."
        julia.c "But this type, I can get into."


    k.c "Oh, there will most certainly be more parties like this."
    k.c "As long as [n.say_name]'s dick remains active, we'll be seeing each other more and more!"
    janet.c "It will be getting too cool out soon to have parties at the pool."
    janet.c "We'll need to relocate inside."
    edna.c "I'd be more than willing to host a party at my condo!"
    si.c "Our house is available as well!"
    vicky.c "Just contact me ahead of time, and I should be able to make it to them without issue."
    gloryhole_girl.c "I can't wait to have these parties year round!"
    gloryhole_girl.c "Isn't that exciting [n.say_name]?"
    n.c "Yeah, it sure is!"
    k.c "We'll figure it all out."
    k.c "I'm starving from all this fucking."
    k.c "Do we still got some chips out here?"

    if finale_julia_sam:
        julia.c "I need something sugary."
        julia.c "Do you know if Grandma baked any cookies?"
        sa.c "I'd like to make a fruit smoothie!"

    edna.c "We all need to recharge our batteries after this!"
    vicky.c "I wish I had a swimsuit with me to go in the pool."
    janet.c "Ah, just go in naked!"
    janet.c "Not like any of us would mind!"
    gloryhole_girl.c "Do you think you'll want to fuck again later [n.say_name]?"
    n.c "..."

    call finale_scene_end_helper

    python:
        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_group_sex", 1)
            stats.add_stat("times_given_facial", 1) #new
            stats.add_stat("times_cummed_in_mouth", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_vaginal_sex", 1) #new
            stats.add_stat("times_had_sex", 1)
            stats.add_stat("times_had_incestual_situation", 1) #new

    call process_end_of_scene("finale_scene", dream = dream)

    return

label epilogue_override:
    call epilogue_loli_debug

    $ renpy.scene('screens')
    $ stop_music(fadeout=1)
    call fade_to_black(2)
    $ replace_position = True

    "{i}A few weeks later...{/i}"

    $ play_music("audio/music/Daily_Music_01.ogg", fadeout=1)
    call process_scene_beginning(bg = "bg nate_room_daytime")

    call process_character(n, appearance = "outfit nudesoft pose handsdown face aroused blush false")
    n.c "{i}Yawn.{/i}.."

    call process_character(n, appearance = "outfit nudesoft pose handsdown face aroused blush false")
    n.c "..."

    call process_character(n, appearance = "outfit nudesoft pose handsdown face concerned blush false")
    n.c "(Well, it's official...)"

    call process_character(n, appearance = "outfit nudesoft pose handsdown face concerned blush false")
    n.c "(One more day of summer, and then it's back to school...)"

    call process_character(n, appearance = "outfit nudesoft pose handsdown face concerned blush false")
    n.c "..."

    call process_character(n, appearance = "outfit nudesoft pose twohandfist face happy blush false")
    n.c "(Man, this summer was epic!)"

    call process_character(n, appearance = "outfit nudesoft pose twohandfist face happy blush false")
    n.c "(I thought the start of it was crazy with all the moving and unpacking)"

    call process_character(n, appearance = "outfit nudesoft pose handsdown face happy blush false")
    n.c "(But that was just the beginning!)"

    if finale_scene_completed_with_julia_sam:
        sa.c "[n.say_name], are you awake?"

        call process_character(n, appearance = "pose handsdown face neutral blush false")
        n.c "Just got up!"

        call process_character(sa, appearance = "outfit nude pose handsbehind face neutral blush false")
        sa.c "Come on downstairs!"

        call process_character(sa, appearance = "outfit nude pose handsbehind face neutral blush false")
        sa.c "Mom, Grandma, and everybody else is here to take the group photo!"

        call process_character(n, appearance = "pose twohandfist face neutral blush false")
        n.c "Oh that's right, we were gonna do that today!"

        call process_character(sa, appearance = "outfit nude pose handface face neutral blush false")
        sa.c "And don't forget our sex party afterward!"

        call process_character(sa, appearance = "outfit nude pose handface face happy blush false")
        sa.c "Doggy style position is the theme!"

        call process_character(n, appearance = "pose handfist face happy blush false")
        n.c "Yes, I love that position!"

        call process_character(sa, appearance = "outfit nude pose leaning face happy blush false")
        sa.c "Me too!"

    else:
        k.c "Bro, are you still sleeping or what?"

        call process_character(n, appearance = "pose handsdown face neutral blush false")
        n.c "Just got up!"

        call process_character(k, appearance = "outfit nude pose armcross face neutral blush false")
        k.c "Come on slowpoke!"

        call process_character(k, appearance = "outfit nude pose armcross face neutral blush false")
        k.c "Everybody's waiting on you for the group photo!"

        call process_character(n, appearance = "pose twohandfist face neutral blush false")
        n.c "Oh that's right, we were gonna do that today!"

        call process_character(k, appearance = "outfit nude pose handhip face neutral blush false")
        k.c "Yeah, and afterward we're playing spin the bottle, with you as the bottle!"

        call process_character(n, appearance = "pose behindhead face neutral blush false")
        n.c "We are?"

        call process_character(k, appearance = "outfit nude pose armsup face happy blush false")
        k.c "Well, we will be after I suggest it!"

        call process_character(k, appearance = "outfit nude pose armsup face happy blush false")
        k.c "So come on, move your cock and balls downstairs!"

    call process_scene_beginning(bg = "bg hallway_daytime")

    call process_character(n, appearance = "outfit nudesoft pose handsdown face neutral blush false")
    n.c "(Good thing I'm continuing to work on improving my sex capacity)"

    call process_character(n, appearance = "outfit nudesoft pose handsdown face happy blush false")
    n.c "(On average, I can fuck about three times a day!)"

    call process_character(n, appearance = "outfit nudesoft pose behindhead face neutral blush false")
    n.c "(I think if I'm lucky, I can push for five or six times a day)"

    if finale_scene_completed_with_julia_sam:
        call process_character(n, appearance = "pose handsdown face neutral blush false")
        n.c "(In the morning, it's usually Mom or [sa.say_name] that wakes me up with a blowjob or handjob)"

        call process_character(n, appearance = "pose handsdown face neutral blush false")
        n.c "(There's also a chance for [k.say_name] to come in to lift me up and suck my cock while walking to the kitchen)"

        call process_new_location("bg kitchen_daytime")

        call process_character(n, appearance = "outfit nudesoft pose behindhead face neutral blush false")
        n.c "(After that, it purely depends on who's turn it is in the rotation to bang)"

        call process_character(n, appearance = "pose behindhead face neutral blush false")
        n.c "(Aunt [janet.say_name] and [julia.say_name] like to stop by on the weekends, and they double team me)"

        if had_kacey_apartment_intro:
            call process_character(n, appearance = "pose behindhead face neutral blush false")
            n.c "([gloryhole_girl.say_name]'s new apartment is really cool!)"

            call process_character(n, appearance = "pose behindhead face neutral blush false")
            n.c "(I end up going there a lot!)"

            call process_character(n, appearance = "pose twohandfist face happy blush false")
            n.c "(Sometimes [sa.say_name] tags along, and we have some awesome gaming sessions together!)"
        else:
            call process_character(n, appearance = "pose behindhead face neutral blush false")
            n.c "([gloryhole_girl.say_name] rents an apartment just a couple blocks away, and I go see her at night)"

            call process_character(n, appearance = "pose twohandfist face happy blush false")
            n.c "(Sometimes [sa.say_name] tags along, and we have some awesome gaming sessions together!)"

    else:
        call process_character(n, appearance = "pose handsdown face neutral blush false")
        n.c "(In the morning, it's usually Mom that wakes me up with a blowjob or handjob)"

        call process_character(n, appearance = "pose handsdown face neutral blush false")
        n.c "(There's also a chance for [k.say_name] to come in to lift me up and suck my cock while walking to the kitchen)"

        call process_new_location("bg kitchen_daytime")

        call process_character(n, appearance = "outfit nudesoft pose behindhead face neutral blush false")
        n.c "(After that, it purely depends on who's turn it is in the rotation to bang)"

        call process_character(n, appearance = "pose behindhead face neutral blush false")
        n.c "(Aunt [janet.say_name] usually stops by on the weekends, and usually I have a foursome with her, Mom, and [k.say_name]!)"

        if had_kacey_apartment_intro:
            call process_character(n, appearance = "pose behindhead face neutral blush false")
            n.c "([gloryhole_girl.say_name]'s new apartment is really cool!)"

            call process_character(n, appearance = "pose behindhead face neutral blush false")
            n.c "(I end up going there a lot!)"

            call process_character(n, appearance = "pose twohandfist face happy blush false")
            n.c "(Sometimes [sa.say_name] tags along, and we have some awesome gaming sessions together!)"
        else:
            call process_character(n, appearance = "pose behindhead face neutral blush false")
            n.c "([gloryhole_girl.say_name] rents an apartment just a couple blocks away, and I go see her at night)"

            call process_character(n, appearance = "pose twohandfist face happy blush false")
            n.c "(Sometimes [sa.say_name] tags along, and we have some awesome gaming sessions together!)"

    call process_character(n, appearance = "pose twohandfist face happy blush false")
    n.c "(I like to lay on top of [gloryhole_girl.say_name] and stick my dick in her ass or pussy while we play!)"

    call process_new_location("bg living_room_daytime")

    call process_character(n, appearance = "outfit nudesoft pose handsdown face neutral blush false")
    n.c "([vicky.say_name] has hired Mom as a secretary for her business)"

    call process_character(n, appearance = "pose handsdown face happy blush false")
    n.c "(Both of them are topless when in the office, so I can play with their boobs all day!)"

    call process_character(n, appearance = "pose handfist face neutral blush false")
    n.c "(And fridays are specially reserved for Grandma)"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "(We fuck for several hours straight now, it's awesome!)"

    call process_character(si, appearance = "outfit nude pose handsup face neutral blush false")
    si.c "There you are sweetie!"

    call process_character(n, appearance = "outfit nudesoft pose behindhead face neutral blush false")
    n.c "Sorry for making everyone wait Mom."

    call process_character(si, appearance = "outfit nude pose handsup face happy blush false")
    si.c "We would have had to have waited anyway, due to [janet.say_name]!"

    call process_character(n, appearance = "outfit nudesoft pose handsdown face neutral blush false")

    call process_character(janet, appearance = "outfit nude pose handchest face neutral blush false")
    janet.c "I want to get just the right lighting for this photo."

    call process_character(janet, appearance = "outfit nude pose handchest face happy blush false")
    janet.c "Nothing worse than having a washed out image from a camera flash!"

    call process_character(janet, appearance = "outfit nude pose handhips face neutral blush false")
    janet.c "It's better to use natural light with a little diffusion."

    call process_character(si, appearance = "outfit nude pose armunder face happy blush false")
    si.c "I am clueless when it comes to that stuff!"

    call process_character(si, appearance = "outfit nude pose armunder face happy blush false")
    si.c "I just know you press a button on the camera, and it takes a picture!"

    call process_character(edna, appearance = "outfit nude pose handclasp face happy blush false mouth red")
    edna.c "Can the camera make me look twenty years younger?"

    call process_character(k, appearance = "outfit nude pose handhip face neutral blush false")
    k.c "Photo editing programs can help with that, Grandma."

    if finale_scene_completed_with_julia_sam:
        call process_character(sa, appearance = "outfit nude pose leaning face neutral blush false")
        sa.c "Okay, I got the timer settings up for the camera Aunt [janet.say_name]!"

        call process_character(sa, appearance = "outfit nude pose leaning face neutral blush false")
        sa.c "Should I set it for thirty seconds?"

        call process_character(julia, appearance = "outfit nude pose armcross face neutral blush false")
        julia.c "Probably better to set it for a minute."

        call process_character(julia, appearance = "outfit nude pose armcross face neutral blush false")
        julia.c "Who knows how long it will take for all of us to get into position."

        call process_character(gloryhole_girl, appearance = "outfit nude pose handface face neutral blush false")
        gloryhole_girl.c "Is the camera far away enough to capture us all?"

        call process_character(vicky, appearance = "outfit nude pose handup face neutral blush false")
        vicky.c "If we have to squeeze in tighter to the frame, so be it."

        call process_character(k, appearance = "pose armsup face neutral blush false")
        k.c "We may end up having our boobs pushed up against each other."

        call process_character(k, appearance = "pose armsup face happy blush false")
        k.c "[n.say_name] would approve!"

        call process_character(n, appearance = "pose behindhead face curious blush false")
        n.c "..."

        call process_character(sa, appearance = "outfit nude pose handface face embarrassed blush false")
        sa.c "Oops, I hit the button already!"

        call process_character(sa, appearance = "outfit nude pose handface face embarrassed blush false")
        sa.c "The camera is counting down!"

        call process_character(si, appearance = "pose handsfront face embarrassed blush false")
        si.c "Oh jeez, let's get to our spots!"

        call process_character(si, appearance = "pose handsfront face embarrassed blush false")
        si.c "Hurry, hurry!"

        $ no_bust_art = True
        $ clear_characters()
        show bg photo_epilogue_background
        show family_milf_layer:
            Null()
        show nate_layer:
            Null()
        show julia_sam_layer:
            Null()
        show nonrelated_layer:
            Null()
        with Dissolve(0.5)

        si.c "Okay, let's see..."
        si.c "Mom, you stand over there."
        si.c "[janet.say_name], you want to be next to Mom?"
        janet.c "Sure!"
        si.c "And I'll stand opposite to you."
        si.c "[k.say_name], you're the tallest so you should be in the back with us."
        k.c "Going right next to you Mom."

        $ play_music("audio/music/Smooth 01.ogg", fadeout=1)

        $ quick_menu = False
        window hide
        show bg photo_epilogue_ednajanetkirasimone_np as family_milf_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
        janet.c "Can you check if we're in the frame [julia.say_name]?"
        julia.c "..."
        julia.c "Yeah, you are."
        si.c "Now as for you [n.say_name], can you..."
        si.c "[n.say_name], stop fingering [sa.say_name] for the time being."
        si.c "We need you over here."
        n.c "Oh, yep!"
        si.c "Why don't you go..."
        si.c "..."
        k.c "[n.say_name] could be right smack dab in the middle."
        k.c "He'll be surrounded by titties!"
        si.c "Yes, perfect!"
        si.c "Stand just in front of [janet.say_name] and I, sweetie."

        $ quick_menu = False
        window hide
        show bg photo_epilogue_nate_np as nate_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
        n.c "Like this?"
        k.c "Grandma, you're looking so stoic!"
        edna.c "I tend to look better in photos where my smile is subdued."
        si.c "Alright, [sa.say_name] and [julia.say_name]..."
        si.c "It would be nice to have our daughters in front of us [janet.say_name], what do you think?"
        janet.c "I like that!"
        edna.c "Why don't [sa.say_name] and [julia.say_name] get close to [n.say_name], maybe they can put their arms around him."
        edna.c "That would be very cute."
        si.c "That does sound adorable!"

        $ quick_menu = False
        window hide
        show bg photo_epilogue_samjulia_np as julia_sam_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
        janet.c "This is a rare feat to get [julia.say_name] in front of a camera."
        janet.c "It may be our only chance!"
        julia.c "Hey, I don't avoid cameras that much."
        julia.c "Okay I do, but..."
        edna.c "I'm not fond of cameras either [julia.say_name], but this is a special occasion!"
        si.c "A very special occssion!"
        si.c "I love photos of the whole family!"
        janet.c "Make sure to smile!"

        $ quick_menu = False
        window hide
        pause 0.5
        show camera:
            Solid("#ffffff", xsize = 1920, ysize = 1080)
            alpha 0.0
            linear .25 alpha 1.0
            pause .25
            linear .25 alpha 0.0

        pause 2
        window show
        $ quick_menu = True
        gloryhole_girl.c "..."
        gloryhole_girl.c "The image came out great you guys!"
        vicky.c "I agree, it looks very nice on the camera screen."
        si.c "Now we want an image including you two!"
        si.c "You spend so much time with [n.say_name] and us, you're practically family too!"
        k.c "We're one big, happy, fucking family!"
        k.c "Emphasis on the fucking!"
        sa.c "Press the camera button [gloryhole_girl.say_name]!"
        gloryhole_girl.c "..."
        gloryhole_girl.c "I see it blinking!"

        $ quick_menu = False
        window hide
        show bg photo_epilogue_kaceyvicky_np as nonrelated_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
        k.c "We're really bunched up now!"
        vicky.c "I think it'll be fine."
        vicky.c "Not like we'll be circulating this photo."
        si.c "Haha, no, absolutely not!"
        si.c "This is a private photo, only for us!"
        k.c "Hey, if it did get posted somewhere, we could just say we're a nudist family."
        si.c "[k.say_name]..."
        sa.c "I'm gonna make this my background image on my computer!"
        gloryhole_girl.c "I might do the same [sa.say_name]!"
        vicky.c "I think we should consider taking this kind of photo periodically."
        vicky.c "Would be interesting to see how much we change."
        edna.c "You mean how we get old, haha!"
        vicky.c "I hope I age as gracefully as you have, [edna.say_name]."
        julia.c "So one more photo, and we're good?"
        si.c "As long as nobody sneezes, or closes their eyes at the wrong time!"
        k.c "Or decides to shake their tits uncontrollably!"
        sa.c "Haha!"
        gloryhole_girl.c "Hey [k.say_name], want to do a boob battle after this?"
        k.c "You're on!"
        k.c "And let's do it while [n.say_name] has his dick in between us!"
        n.c "Heck yeah!"
        sa.c "I am so recording that!"
        si.c "Try to keep your excitement curbed a little longer!"
        si.c "Once the photo is taken, all of you can go crazy!"
        k.c "Everyone say \"Jizz\"!"

        "Everyone" "Jizz!"

        $ quick_menu = False
        window hide
        pause 0.5
        show camera:
            Solid("#ffffff", xsize = 1920, ysize = 1080)
            alpha 0.0
            linear .25 alpha 1.0
            pause .25
            linear .25 alpha 0.0

        pause 2
        window show
        $ quick_menu = True

        n.c "(It's gonna be hard to top this summer)"
        n.c "(Have to wait a whole year for the next one)"
        n.c "(Hope it will be just as good, or even better!)"
        n.c "(But first, I gotta go through school again...)"
        n.c "..."
        n.c "(Maybe it won't be so bad)"
        n.c "(There could be some cool classmates for me and [sa.say_name] to hang out with)"
        n.c "(I wonder what the teachers will be like at the school...)"
        n.c "(I hope one of them has big tits!)"
        k.c "Yo, [n.say_name]!"
        k.c "Let's get your dick ready for this boob showdown!"
        gloryhole_girl.c "I can slick it up with my tongue for you!"
        n.c "Alright, let's get it started!"
        n.c "..."
        n.c "(At least I know I'll have a ton of fun after school!)"

    else:
        call process_character(janet, appearance = "pose handhips face neutral blush false")
        janet.c "Okay, I've got the camera timer set for thirty seconds."

        call process_character(janet, appearance = "pose handhips face curious blush false")
        janet.c "Actually, let's go for sixty."

        call process_character(janet, appearance = "pose handhips face neutral blush false")
        janet.c "We'll likely shuffle around for a moment to frame a good portrait."

        call process_character(gloryhole_girl, appearance = "outfit nude pose handface face neutral blush false")
        gloryhole_girl.c "Is the camera far away enough to capture us all?"

        call process_character(vicky, appearance = "outfit nude pose handhip face neutral blush false")
        vicky.c "If we have to squeeze in tighter to the frame, so be it."

        call process_character(k, appearance = "pose armsup face neutral blush false")
        k.c "We may end up having our boobs pushed up against each other."

        call process_character(k, appearance = "pose armsup face happy blush false")
        k.c "[n.say_name] would approve!"

        call process_character(n, appearance = "pose behindhead face curious blush false")
        n.c "..."

        call process_character(janet, appearance = "pose handface face happy blush false")
        janet.c "Alright, the camera is counting down!"

        call process_character(si, appearance = "pose handsfront face embarrassed blush false")
        si.c "Oh jeez, let's get to our spots!"

        call process_character(si, appearance = "pose handsfront face embarrassed blush false")
        si.c "Hurry, hurry!"

        $ no_bust_art = True
        $ clear_characters()
        show bg photo_epilogue_background
        show family_milf_layer:
            Null()
        show nate_layer:
            Null()
        show julia_sam_layer:
            Null()
        show nonrelated_layer:
            Null()
        with Dissolve(0.5)

        si.c "Okay, let's see..."
        si.c "Mom, you stand over there."
        si.c "[janet.say_name], you want to be next to Mom?"
        janet.c "Sure!"
        si.c "And I'll stand opposite to you."
        si.c "[k.say_name], you're the tallest so you should be in the back with us."
        k.c "Going right next to you Mom."

        $ play_music("audio/music/Smooth 01.ogg", fadeout=1)

        $ quick_menu = False
        window hide
        show bg photo_epilogue_ednajanetkirasimone_np as family_milf_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
        janet.c "Can you check if we're in the frame [vicky.say_name]?"
        vicky.c "..."
        vicky.c "You're good!"
        si.c "Now as for you [n.say_name], can you..."
        si.c "[n.say_name], stop pulling [gloryhole_girl.say_name]'s nipples for a moment."
        si.c "We need you over here."
        n.c "Oh, yep!"
        si.c "Why don't you go..."
        si.c "..."
        k.c "[n.say_name] could be right smack dab in the middle."
        k.c "He'll be surrounded by titties!"
        si.c "Yes, perfect!"
        si.c "Stand just in front of [janet.say_name] and I, sweetie."

        $ quick_menu = False
        window hide
        show bg photo_epilogue_nate_np as nate_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
        n.c "Like this?"
        k.c "Grandma, you're looking so stoic!"
        edna.c "I tend to look better in photos where my smile is subdued."
        janet.c "This is a rare feat for all of us to be in front of a camera!"
        edna.c "It's a special occasion."
        si.c "A very special occassion!"
        si.c "I love photos of the family!"
        janet.c "Make sure to smile!"

        $ quick_menu = False
        window hide
        pause 0.5
        show camera:
            Solid("#ffffff", xsize = 1920, ysize = 1080)
            alpha 0.0
            linear .25 alpha 1.0
            pause .25
            linear .25 alpha 0.0

        pause 2
        window show
        $ quick_menu = True
        gloryhole_girl.c "..."
        gloryhole_girl.c "The image came out great you guys!"
        vicky.c "I agree, it looks very nice on the camera screen."
        si.c "Now we want an image including you two!"
        si.c "You spend so much time with [n.say_name] and us, you're practically family too!"
        k.c "We're one big, happy, fucking family!"
        k.c "Emphasis on the fucking!"
        janet.c "Can you press the camera button [gloryhole_girl.say_name]?"
        gloryhole_girl.c "..."
        gloryhole_girl.c "I see it blinking!"

        $ quick_menu = False
        window hide
        show bg photo_epilogue_kaceyvicky_np as nonrelated_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        k.c "We're really bunched up now!"
        vicky.c "I think it'll be fine."
        vicky.c "Not like we'll be circulating this photo."
        si.c "Haha, no, absolutely not!"
        si.c "This is a private photo, only for us!"
        k.c "Hey, if it did get posted somewhere, we could just say we're a nudist family."
        si.c "[k.say_name]..."
        gloryhole_girl.c "I might make this my desktop background on my computer!"
        vicky.c "I think we should consider taking this kind of photo periodically."
        vicky.c "It would be interesting to see how much we change."
        edna.c "You mean how old we get, haha!"
        vicky.c "I hope I age as gracefully as you have, [edna.say_name]."
        janet.c "One more photo, and we should be good!"
        si.c "As long as nobody sneezes, or closes their eyes at the wrong time!"
        k.c "Or decides to shake their tits uncontrollably!"
        gloryhole_girl.c "Haha!"
        gloryhole_girl.c "Hey [k.say_name], want to do a boob battle after this?"
        k.c "You're on!"
        k.c "And let's do it while [n.say_name] has his dick in between us!"
        n.c "Heck yeah!"
        si.c "Try to keep your excitement curbed a little longer!"
        si.c "Once the photo is taken, all of you can go crazy!"
        k.c "Everyone say \"Jizz\"!"

        "Everyone" "Jizz!"

        $ quick_menu = False
        window hide
        pause 0.5
        show camera:
            Solid("#ffffff", xsize = 1920, ysize = 1080)
            alpha 0.0
            linear .25 alpha 1.0
            pause .25
            linear .25 alpha 0.0

        pause 2
        window show
        $ quick_menu = True

        n.c "(It's gonna be hard to top this summer)"
        n.c "(Have to wait a whole year for the next one)"
        n.c "(Hope it will be just as good, or even better!)"
        n.c "(But first, I gotta go through school again...)"
        n.c "..."
        n.c "(Maybe it won't be so bad)"
        n.c "(There could be some cool classmates for me and [sa.say_name] to hang out with)"
        n.c "(I wonder what the teachers will be like at the school)"
        n.c "(I hope one of them has big tits!)"
        k.c "Yo, [n.say_name]!"
        k.c "Let's get your dick ready for this boob showdown!"
        gloryhole_girl.c "I can slick it up with my tongue for you!"
        n.c "Alright, let's get it started!"
        n.c "..."
        n.c "(At least I know I'll have a ton of fun after school!)"

    return

label epilogue_pregnancy_leftovers:
    $ epilogue_pregnancy_completed = True
    hide kira_layer
    hide simone_layer
    hide janet_layer
    hide edna_layer
    hide nate_layer
    hide sam_layer
    hide julia_layer
    hide kacey_layer
    hide vicky_layer
    $ stop_music(fadeout=1)
    call fade_to_black(2)

    "{i}Several months later...{/i}"

    call kira_epilogue_main

    call fade_to_black(1)
    n.c "{i}Yep, it's just another average day.{/i}"
    n.c "{i}Although, by most standards, my days are far from average.{/i}"
    n.c "{i}I'm super lucky to have all these great girls in my life.{/i}"

    $ no_bust_art = True
    $ clear_characters()
    show bg photo_epilogue_background
    show kira_layer:
        Null()
    show simone_layer:
        Null()
    show janet_layer:
        Null()
    show edna_layer:
        Null()
    show nate_layer:
        Null()
    show sam_layer:
        Null()
    show julia_layer:
        Null()
    show kacey_layer:
        Null()
    show vicky_layer:
        Null()
    with Dissolve(0.5)
    n.c "{i}Now that I think about it, all of us have had major changes since this past summer!{/i}"
    n.c "{i}Let me see if I can remember everything...{/i}"

    $ play_music("audio/music/Resort Loop2.ogg", fadeout=1)

    $ quick_menu = False
    window hide
    if kira_impreg:
        show bg photo_epilogue_kira_p as kira_layer
    else:
        show bg photo_epilogue_kira_np_alt as kira_layer
    with Dissolve(0.5)
    pause
    window show
    $ quick_menu = True
    n.c "{i}[k.say_name] did take up [vicky.say_name]'s offer to star in porn videos with me, but she still has a part time job at the fitness center.{/i}"
    n.c "{i}She says she wants to bring me in one day to see all her co-workers.{/i}"
    n.c "{i}Apparently, they're all eager to see me for some reason...{/i}"

    $ quick_menu = False
    window hide
    if simone_impreg:
        show bg photo_epilogue_simone_p as simone_layer
    else:
        show bg photo_epilogue_simone_np_alt as simone_layer
    with Dissolve(0.5)
    pause
    window show
    $ quick_menu = True
    n.c "{i}Mom has started a blog about gardening with help from [sa.say_name], and it has been gaining popularity.{/i}"
    n.c "{i}She's also received a pay raise from [vicky.say_name] due to the Empornium's steady increase in revenue!{/i}"

    $ quick_menu = False
    window hide
    if janet_impreg:
        show bg photo_epilogue_janet_p as janet_layer
    else:
        show bg photo_epilogue_janet_np_alt as janet_layer
    with Dissolve(0.5)
    pause
    window show
    $ quick_menu = True
    n.c "{i}Aunt [janet.say_name] provides private yoga lessons now.{/i}"
    n.c "{i}She's been surprised at how many people want to do it in the nude!{/i}"
    n.c "{i}Sometimes she'll call me to come over when she thinks I'll enjoy watching some of the girls do yoga outside.{/i}"

    $ quick_menu = False
    window hide
    if edna_impreg:
        show bg photo_epilogue_edna_p as edna_layer
    else:
        show bg photo_epilogue_edna_np_alt as edna_layer
    with Dissolve(0.5)
    pause
    window show
    $ quick_menu = True
    n.c "{i}Grandma has been enjoying the new casino at her condominium.{/i}"
    n.c "{i}Last I heard she's been doing really well at the slots!{/i}"
    n.c "{i}On top of that, she's garnered support from residents for the construction of a beachside pool with hot tubs.{/i}"
    n.c "{i}I can't wait for that to get finished!{/i}"

    $ quick_menu = False
    window hide
    if kacey_impreg:
        show bg photo_epilogue_kacey_p as kacey_layer
    else:
        show bg photo_epilogue_kacey_np_alt as kacey_layer
    with Dissolve(0.5)
    pause
    window show
    $ quick_menu = True
    n.c "{i}[gloryhole_girl.say_name] applied to be a teacher's assistant at my school!{/i}"
    n.c "{i}When my primary teacher is out, [gloryhole_girl.say_name] gets to substitute in my class.{/i}"
    n.c "{i}It's awesome to be able to see her, and she's a good instructor.{/i}"
    n.c "{i}I think she's studying to earn an official teaching degree.{/i}"

    $ quick_menu = False
    window hide
    if vicky_impreg:
        show bg photo_epilogue_vicky_p as vicky_layer
    else:
        show bg photo_epilogue_vicky_np_alt as vicky_layer
    with Dissolve(0.5)
    pause
    window show
    $ quick_menu = True
    n.c "{i}[vicky.say_name]'s business has been booming!{/i}"
    n.c "{i}Her website is already ranked one of the top ten porn providers online!{/i}"
    n.c "{i}She's planning to hire more actresses to work with me soon.{/i}"
    n.c "{i}I can't wait!{/i}"

    if finale_scene_completed_with_julia_sam:
        $ quick_menu = False
        window hide
        show bg photo_epilogue_nate_p as nate_layer
        with Dissolve(0.5)
        pause

        if julia_impreg:
            show bg photo_epilogue_julia_p as julia_layer
        else:
            show bg photo_epilogue_julia_np_alt as julia_layer
        if sam_impreg:
            show bg photo_epilogue_sam_p as sam_layer
        else:
            show bg photo_epilogue_sam_np_alt as sam_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
        n.c "{i}[julia.say_name] is looking to write and publish her first fantasy novel!{/i}"
        n.c "{i}She decided it was time to put her fiction work out there, and I think that was a great decision!{/i}"
        n.c "{i}I even helped her name some of the characters in her book.{/i}"
        n.c "{i}From what I've read so far, the story is freaking amazing!{/i}"

        $ quick_menu = False
        window hide
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
        n.c "{i}[sa.say_name] and I have made Twinsticks one of of the top channels on ReflexViz.HD!{/i}"
        n.c "{i}It has grown so much, we now sell merch to our fans!{/i}"
        n.c "{i}We got t-shirts, hats, keychains, and even mousepads!{/i}"
        n.c "{i}Game developers send us games in the mail all the time.{/i}"
        n.c "{i}We get early access to all of the latest titles, and it's the greatest thing ever!{/i}"

        $ quick_menu = False
        window hide
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True
    else:
        $ quick_menu = False
        window hide
        show bg photo_epilogue_nate_p as nate_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

    n.c "{i}So much has been happening for us.{/i}"
    n.c "{i}And we won't be slowing down anytime soon!{/i}"
    n.c "{i}Oh yeah, and I almost forgot...{/i}"
    n.c "{i}This coming summer, the size of our family is going to be expanding dramatically!{/i}"

    jump epilogue_end

    return
