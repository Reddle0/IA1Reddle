## Sam/Simone Cum In Both ##
init 100 python:
    sam_simone_threesome_scene_continue_old = sam_simone_threesome_scene_continue

    def sam_simone_threesome_scene_continue_leftovers(dream, revisit):
        if not revisit:
            renpy.call("sam_simone_threesome_scene_phase_3_leftovers", dream)

        return

    sam_simone_threesome_scene_continue = sam_simone_threesome_scene_continue_leftovers

init 100 python:
    sam_simone_threesome_images_old = IA_Actor.sam_simone_threesome_images

    def sam_simone_threesome_images_cum_both(self):
        images = sam_simone_threesome_images_old(self)

        if "sam_simone_threesome_scene" in store.scenes_completed:
            images.append("mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_both_samangle.png")
            images.append("mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_both_simoneangle.png")
            images.append("mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_both.png")

        return images

    IA_Actor.sam_simone_threesome_images = sam_simone_threesome_images_cum_both

init 100:
    screen sam_simone_threesome_scene_revisit_choose_partner_first_time:
        vbox:
            xalign 0.02
            yalign 0.02
            spacing 30
            use main_menu_button(text = "Mom", action = Jump("sam_simone_threesome_scene_revisit_choose_simone_first_time"), enabled = sam_simone_threesome_scene_current_partner != si)
            use main_menu_button(text = "[sa.say_name]", action = Jump("sam_simone_threesome_scene_revisit_choose_sam_first_time"), enabled = sam_simone_threesome_scene_current_partner != sa)
            use main_menu_button(text = "Cum!", action = Jump("sam_simone_threesome_scene_revisit_1st_time_phase_3_leftovers"))

    screen sam_simone_threesome_scene_revisit_choose_partner_second_time:
        vbox:
            xalign 0.02
            yalign 0.02
            spacing 30
            use main_menu_button(text = "Mom", action = Jump("sam_simone_threesome_scene_revisit_choose_simone_second_time"), enabled = sam_simone_threesome_scene_current_partner != si)
            use main_menu_button(text = "[sa.say_name]", action = Jump("sam_simone_threesome_scene_revisit_choose_sam_second_time"), enabled = sam_simone_threesome_scene_current_partner != sa)
            use main_menu_button(text = "Cum!", action = Jump("sam_simone_threesome_scene_revisit_2nd_time_phase_3_leftovers"))

init 105 python:
    config.label_overrides["sam_simone_threesome_scene_phase_3"] = "sam_simone_threesome_scene_phase_3_leftovers"
    config.label_overrides["sam_simone_threesome_scene_revisit_1st_time_phase_3"] = "sam_simone_threesome_scene_revisit_1st_time_phase_3_leftovers"
    config.label_overrides["sam_simone_threesome_scene_revisit_2nd_time_phase_3"] = "sam_simone_threesome_scene_revisit_2nd_time_phase_3_leftovers"

label sam_simone_threesome_scene_phase_3_leftovers(dream = False):
    n.c "Hrrm!"
    n.c "Nng!"
    si.c "[n.say_name] has to ejaculate soon [sa.say_name]..."
    si.c "He's getting close."
    sa.c "So [n.say_name] will have to come in one of us Mom!"
    si.c "Indeed he will."
    n.c "I-I am close..."
    sa.c "So how about it [n.say_name]?"
    sa.c "Which pussy will get filled up with your cream?"
    si.c "Haha, you call it cream sweetie?"
    sa.c "I call [n.say_name]'s cum a lot of things!"
    si.c "Well [n.say_name]..."
    si.c "[sa.say_name] is eagerly awaiting for the moment!"

    window hide
    menu:
        "Cum in Mom":
            if sam_simone_threesome_scene_current_partner != si:
                call static_still_ctc("bg sam_simone_group_sprawl_fuck_simone")
            n.c "Haaa..."
            n.c "Hrrm!"
            si.c "You're nearly there [n.say_name]!"
            n.c "Mooom!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg sam_simone_group_sprawl_cum_simone")
            si.c "That's it sweetie!"
            si.c "Give it all to me!"
            n.c "{i}Pant.{/i}.."
            sa.c "Dude, [n.say_name]!"
            sa.c "You're like, filling Mom up with your spunk!"

            call static_still_ctc("bg sam_simone_group_sprawl_aftercum_simone")

        "Cum in [sa.say_name]":
            if sam_simone_threesome_scene_current_partner != sa:
                call static_still_ctc("bg sam_simone_group_sprawl_fuck_sam")
            n.c "Haaa..."
            n.c "Hrrm!"
            sa.c "Bring it on!"
            n.c "Aaaah!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
            call static_still_ctc("bg sam_simone_group_sprawl_cum_sam")
            sa.c "It's all going in me [n.say_name]!"
            n.c "Hoo! Ooh!"
            si.c "O-Oh my..."
            si.c "..."
            si.c "[n.say_name] did put everything in you."
            sa.c "I always let him do that in my pussy!"
            si.c "I see..."

            call static_still_ctc("bg sam_simone_group_sprawl_aftercum_sam")

        "Cum in Both":
            n.c "I want to come in both of you!"
            si.c "While I appreciate the enthusiasm, sweetie..."
            si.c "Is such a feat really possible?"
            si.c "I'm not sure how you could manage it."

            if stats.stat_value('times_had_group_sex') > 0 and "sam_julia_threesome_scene" in scenes_completed:
                n.c "I still want to try!"

            else:
                n.c "I-I don't know, but I want to try!"

            sa.c "Nothing's impossible, Mom!"

            if stats.stat_value('times_had_group_sex') > 0 and "sam_julia_threesome_scene" in scenes_completed:
                sa.c "In fact, he's done this before!"
                si.c "Wh-what?"
                si.c "(Did I...{w=1.0}hear her right?)"
                si.c "What does she mean, [n.say_name]?"
                n.c "..."
                sa.c "Haha, oops..."
                sa.c "Well, I guess the cat's out of the bag now!"
                sa.c "[n.say_name] unloaded his cum into me and [julia.say_name]!"


                if stats.stat_value('times_had_group_sex') > 0 and "sam_julia_threesome_scene" and "family_foursome_scene" in scenes_completed:
                    si.c "(...!)"
                    si.c "([julia.say_name] is involved in this too)"
                    si.c "(With the way things were going, I guess it was inevitable at some point)"
                    si.c "(Wait...)"
                    si.c "(If he's...{w=1.0}then that must mean...)"
                    si.c "([n.say_name] is having sex with everyone in this house!)"
                    si.c "(How is that even possible!?)"
                    si.c "(Has it always been this way, and I just never noticed?)"
                    si.c "(Or is my [n.say_name] really that irresistible to every girl around him?)"
                    si.c "(Or, or...)"

                    pause 1.0
                    si.c "(...)"
                    si.c "(Come to think of it, [julia.say_name] has been in higher spirits recently)"
                    si.c "(To think it'd be because she's having sex with [n.say_name])"
                    si.c "(...)"
                    si.c "(He sure has come a long way since that day I caught him masturbating in the bathroom)"
                    si.c "([n.say_name]'s somehow singlehandedly turned our household into some sort of sex haven!)"
                    si.c "(And it seems I was none the wiser)"

                else:
                    si.c "(!!!)"
                    si.c "([julia.say_name[0]]-[julia.say_name] is involved in this too?)"
                    sa.c "You should have seen it Mom, it was amazing!"
                    sa.c "Our pussies were dripping with cum!"
                    si.c "..."
                    si.c "How you got [julia.say_name] wrapped up in all of this is something I'll never understand."
                    si.c "But maybe I don't have to."
                    si.c "Instead, maybe I should wonder what else you two have been up to while I wasn't looking."
                    n.c "..."

                si.c "Promise me you won't tell your Auntie about this!"
                si.c "I mean it!"
                sa.c "We promise, Mom!"
                si.c "(If she knew, I wouldn't hear the end of it!)"
                si.c "(She'd flip out!)"

                pause 1.0
                si.c "..."
                sa.c "Well [n.say_name], I think we've waited long enough!"
                sa.c "So pump that cream into us already!"
                n.c "I'm going for it!"
                n.c "Haaaahh!"

            else:
                si.c "..."
                si.c "Good luck, sweetie!"
                sa.c "You can do it [n.say_name]!"
                n.c "I'm going for it!"
                n.c "Haaaahh!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            if sam_simone_threesome_scene_current_partner == sa:
                call static_still_ctc("bg sam_simone_group_sprawl_cum_sam")
                n.c "Hoo! Ooh!"
                sa.c "Nice!"
                sa.c "It's all going in me [n.say_name]!"
                si.c "(That was a huge orgasm!)"


                pause 1.0
                si.c "(...)"
                si.c "([sa.say_name]'s pussy is overflowing from it all)"
                si.c "(But he's still determined to see this through!)"
                si.c "(At this rate, there won't be any cum left in those balls of his!)"
                n.c "Mom!"

            else:
                call static_still_ctc("bg sam_simone_group_sprawl_cum_simone")
                n.c "Hoo! Ooh!"
                si.c "Very good, sweetie!"
                si.c "That was a big load!"

                pause
                si.c "(...)"
                si.c "(My pussy's overflowing from it all)"
                si.c "(If he's not careful, he'll end up running out of cum before he can get to [sa.say_name]...)"
                sa.c "I'm next, I'm next!"
                si.c "Your sister seems very eager to have you see this through, [n.say_name]!"
                n.c "[sa.say_name]!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            if sam_simone_threesome_scene_current_partner != si:
                call static_still_ctc("bg sam_simone_group_sprawl_cum_both_simoneangle")
                n.c "Haahnn!"
                si.c "(I-Incredible...)"
                sa.c "Woah, Mom's pussy is getting filled!"
                sa.c "That's crazy how you still have enough cum!"
                si.c "Those small balls of yours must be working overtime!"

            else:
                call static_still_ctc("bg sam_simone_group_sprawl_cum_both_samangle")
                n.c "Haahnn!"
                sa.c "{i}Gasp!{/i}"
                sa.c "There's still so much of it left!"
                sa.c "My pussy is getting filled!"
                si.c "Those small balls of his are working overtime!"


            call static_still_ctc("bg sam_simone_group_sprawl_aftercum_both")
            si.c "{i}Pant.{/i}.."
            sa.c "{i}Phew.{/i}.."
            si.c "..."
            si.c "O-Oh my..."
            sa.c "You did it [n.say_name]!"
            sa.c "Dude, you actually did it!"
            sa.c "You came in both of us!"
            sa.c "That was so epic!"
            si.c "..."
            si.c "I don't even know what to say right now..."
            sa.c "You left Mom speechless!"
            sa.c "I've never seen her like that!"
            si.c "..."
            sa.c "How do you even do it?"
            n.c "..."
            n.c "I knew I had to act fast."
            n.c "And I guess I was able to time it just right."
            sa.c "Oh man, you should have seen your face, haha!"
            sa.c "You had such a serious game-face when you came inside Mom!"
            si.c "Y-Yes, he did."
            si.c "He was simply lost in the moment."
            si.c "I think that may have been one of the biggest loads you've ever had [n.say_name]!"
            n.c "..."
            n.c "Maybe..."
            sa.c "I'll say!"
            sa.c "[n.say_name]'s cum is practically pouring out of our pussies!"
            sa.c "I swear, the amount [n.say_name] cums could fill an ocean!"
            si.c "Oh, I wouldn't go that far!"
            si.c "But I wouldn't be surprised if it did!"

    pause
    n.c "...{p}..."
    n.c "{i}Pant,{/i} {i}pant.{/i}.."
    sa.c "{i}Whew.{/i}.."
    si.c "{i}Sigh.{/i}.."
    n.c "..."
    n.c "This was great!"
    n.c "I'm really glad you did this with us Mom!"
    sa.c "I am too!"
    sa.c "You're the best Mom in the world!"
    si.c "I love spending time with both of you."
    si.c "This makes us feel even closer!"
    sa.c "You're definitely right Mom!"
    n.c "I agree!"
    si.c "..."
    si.c "Woo!"
    si.c "Can't believe there's a whole day still ahead of us!"
    si.c "I'm wiped out already, haha!"
    n.c "Floating in the pool seems like a great option right now..."
    sa.c "I hear that [n.say_name]!"
    si.c "You two enjoy it then!"
    si.c "My garden needs some urgent tending!"

    call sam_simone_threesome_scene_end(dream = dream)
    return

label sam_simone_threesome_scene_revisit_1st_time_phase_3_leftovers:
    n.c "Y-You both feel so good..."
    n.c "I'm ready to come!"
    sa.c "Your choice dude!"
    si.c "It's up to you sweetie!"

    window hide
    menu:
        "Cum in Mom":
            if sam_simone_threesome_scene_current_partner != si:
                call static_still_ctc("bg sam_simone_group_sprawl_fuck_simone")

            si.c "Yes baby, yes!"
            si.c "Go all the way inside me!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg sam_simone_group_sprawl_cum_simone")
            n.c "Nngh!"
            si.c "Very good sweetie!"
            si.c "Let out as much as you want!"
            n.c "Aaah..."
            n.c "..."

            call static_still_ctc("bg sam_simone_group_sprawl_aftercum_simone")
            sa.c "That was epic [n.say_name]!"
            sa.c "You took that load like a boss Mom!"

        "Cum in [sa.say_name]":
            if sam_simone_threesome_scene_current_partner != sa:
                call static_still_ctc("bg sam_simone_group_sprawl_fuck_sam")

            sa.c "Haa, ah!"
            sa.c "Go for it [n.say_name]!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg sam_simone_group_sprawl_cum_sam")
            n.c "Nngh!"
            sa.c "Yeeaah [n.say_name]!"
            sa.c "I can feel you squirting in me!"
            n.c "Aaah.."
            n.c "..."

            call static_still_ctc("bg sam_simone_group_sprawl_aftercum_sam")
            si.c "..."
            si.c "([sa.say_name]'s pussy is dripping out semen...)"
            si.c "..."
            si.c "(Does she know about what happens when...)"

        "Cum in Both":
            if sam_simone_threesome_scene_current_partner == sa:
                call static_still_ctc("bg sam_simone_group_sprawl_fuck_sam")
            else:
                call static_still_ctc("bg sam_simone_group_sprawl_fuck_simone")

            n.c "I'm gonna come in both of you again!"
            sa.c "Sounds good to me!"
            si.c "Do your best, sweetie!"


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            if sam_simone_threesome_scene_current_partner == sa:
                call static_still_ctc("bg sam_simone_group_sprawl_cum_sam")
                n.c "Hrrg!"
                sa.c "Nice, [n.say_name]!"
                sa.c "Pump that cream into me!"

                call static_still_ctc("bg sam_simone_group_sprawl_cum_both_simoneangle")
                n.c "Here's some for you, Mom!"
                si.c "Don't let a drop go to waste, sweetie!"
                sa.c "Fill Mom's pussy up to the brim, [n.say_name]!"

            else:
                call static_still_ctc("bg sam_simone_group_sprawl_cum_simone")
                n.c "Hraa!"
                si.c "That's it, baby!"
                si.c "Let all your cum inside me!"

                call static_still_ctc("bg sam_simone_group_sprawl_cum_both_samangle")
                n.c "Here's some for you, [sa.say_name]!"
                sa.c "I can feel it flowing into me!"
                si.c "O-Oh my..."

    call sam_simone_threesome_scene_revisit_end
    return

label sam_simone_threesome_scene_revisit_2nd_time_phase_3_leftovers:
    menu:
        "Cum in Mom":
            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg sam_simone_group_sprawl_cum_simone")
            n.c "Hyaah!"
            si.c "Try to keep your voice down a bit sweetie."
            sa.c "He can't help it Mom!"
            sa.c "Our pussies feel too good!"


        "Cum in [sa.say_name]":
            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc("bg sam_simone_group_sprawl_cum_sam")
            n.c "Mmn!"
            sa.c "Ding!"
            sa.c "Another pussy cumshot for me!"

        "Cum in Both":
            n.c "I'm gonna come in both of you again!"
            si.c "Give it to us both, baby!"
            sa.c "Yeah, what Mom said!"

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            if sam_simone_threesome_scene_current_partner == sa:
                call static_still_ctc("bg sam_simone_group_sprawl_cum_sam")
                n.c "Hraah!"
                sa.c "Zing!"

                call static_still_ctc("bg sam_simone_group_sprawl_cum_both_simoneangle")
                n.c "And some for you Mom!"
                si.c "Excellent, sweetie!"

            else:
                call static_still_ctc("bg sam_simone_group_sprawl_cum_simone")
                n.c "Aaah!"
                si.c "Yes, baby, yes!"


                call static_still_ctc("bg sam_simone_group_sprawl_cum_both_samangle")
                n.c "And some for you [sa.say_name]!"
                sa.c "Yesss!"

            call static_still_ctc("bg sam_simone_group_sprawl_aftercum_both")
            si.c "..."
            sa.c "[n.say_name] sure does let out a lot, doesn't he?"
            si.c "..."
            si.c "Y-yes, he does."

    call sam_simone_threesome_scene_revisit_end

    return