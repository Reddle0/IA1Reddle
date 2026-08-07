##################
# MODDER'S BLOCK #
##################
# if you're adding your own mod to this screen, check out supersexual_patch.rpy for how I did it there
# copy that pattern and swap in your own variable names
# main things you need: folder check, append to extra_mod_stories, done
# don't edit this file directly - make your own .rpy or updates will overwrite your changes

init 10 python:
    import os

    if os.path.isdir(os.path.join(config.gamedir, "mods", "my_mod")):
        my_mod_locked = not getattr(persistent, "my_mod_unlocked", False) # change this variable name to your mod's persistent variable that tracks if it's unlocked. set to False by default

        extra_mod_stories.append({
            "name": "My Mod",
            "image": "mods/my_mod/images/my_icon.png",
            "label": "my_mod_start",
            "locked": my_mod_locked, # if your mod is just a toggleable mod (i.e. it doesn't have a skip to mod content), you can set this to False
            "status": "Locked" if my_mod_locked else "Unlocked",
            "show_unlock_toast": True,
            # "toast_flag": "my_mod_toast_shown", # only include this if you want a one-time unlock toast to show when the mod is first unlocked. set to a unique variable name for your mod
            # "start_action": Show("some_modal"), # only include this if your mod needs a modal first instead of starting right away
        })

##################
# Mod Selection #
##################
# builds the mod select screen, and fills it with the "mod stories" that should show up
# mod stories are any large mods that lets you skip to it's newly added content, or is otherwise separate from the base game
# for instance, supersexual awakening lets you play the mod without having to play through the entire game
# another example is the (eventually) planned sam side story, which makes it so it has a "snapshot" of your save and can play it separately from your normal save
# adds "Mod Story" to the Main Menu if any mod stories are unlocked
# also handles one-time unlock popups

# DO NOT TOUCH THIS DEFAULT VARIABLE
# SEE MODDER'S BLOCK IF YOU'RE READING THIS FILE TO HELP WITH YOUR OWN MOD
default extra_mod_stories = []

init -100 python:
    extra_mod_story_refreshers = []

    def refresh_extra_mod_stories():
        extra_mod_stories[:] = []

        for refresh_story in extra_mod_story_refreshers:
            refresh_story()

# Main Menu Mod Story Select
init 200:
    screen main_menu():

        ## This ensures that any other menu screen is replaced.
        tag menu

        add "gui/main_menu.png"
        #add "images/interface/Title_Screen_nobg.png"

        text config.name style "default" size 120 xalign 0.5

        vbox:
            xalign 0.95
            yalign 0.4
            spacing 30
#            activate_sound = "Level_Up.wav"   
#            hovered Play("Level_Up.wav") 

            use main_menu_button(text = "New Game", action = Start)

            if not wholesome_mode:
                use main_menu_button(text = "Load Game", action = ShowMenu("load") )

#            if store.finale_julia_sam:
                use main_menu_button(text="Mod Select", action = ShowMenu("mod_story_selection"))
        
            use main_menu_button(text = "Options", action = ShowMenu("preferences") )
            use main_menu_button(text = "FAQ", action = Jump("help") )
            use main_menu_button(text = "Quit", action = Quit(confirm = not main_menu))

        #use subscribestar_button((0, 269))
        #use baraag_button((0, 480))
        #use blog_button((0, 689))
        #use discord_button((0, 884))

        vbox:
            xanchor 0.0
            xpos 0.01
            yanchor 1.0
            ypos 0.95
            spacing 20
            use hover_text_button_2("images/interface/mastodon.png", Text("Baraag", size = 64, xalign = 0.5, yalign = 0.5), action = OpenURL("https://baraag.net/@cyberhexxx"))
            use hover_text_button_2("images/interface/team cyber hexxx.png", Text("Blog", size = 64, xalign = 0.5, yalign = 0.5), action = OpenURL("https://iathegame.blogspot.com/"))
            use hover_text_button_2("images/interface/discord.png", Text("Discord", size = 64, xalign = 0.5, yalign = 0.5), action = OpenURL("https://discord.gg/qrEDPCa"))
            use hover_text_button_2("images/interface/subscribestar.png", Text("Support us!", size = 64, xalign = 0.5, yalign = 0.5), action = OpenURL("https://subscribestar.adult/cyberhexxx"))

        text "[config.version]":
            style "main_menu_version"
            size 36
            xanchor 1.0
            xpos 0.99
            yanchor 1.0
            ypos 0.97

# the unlock popup reads from this to show the story name
default mod_story_unlock_name = ""

# popup timing and dimensions
# tweak these if the popup timing or size looks off
define mod_story_toast_delay = 0.45
define mod_story_box_w = 1150
define mod_story_box_h = 360
define mod_story_box_border = 40

# small pop-in animation for the unlock box
transform mod_story_panel_reveal:
    alpha 0.0
    zoom 0.98
    yoffset 20
    easein 0.25 alpha 1.0 zoom 1.0 yoffset 0

# Mod Story Toast (unlock popup) #
screen mod_story_unlocked_modal():
    # this is the popup that shows when a mod story gets unlocked
    modal True
    zorder 200

    # play the level-up sound once when the popup appears
    on "show" action Play("sound", "audio/sounds/Level_Up.wav")

    # darken the screen behind the popup
    add Solid("#000") at Transform(alpha = 0.55)

    # clicking outside closes it
    button:
        xfill True
        yfill True
        background None
        action Hide("mod_story_unlocked_modal")

    # main popup box
    fixed:
        xalign 0.5
        yalign 0.5
        xsize mod_story_box_w
        ysize mod_story_box_h
        at mod_story_panel_reveal

        # fill so the box isn't see-through
        add Solid("#111016") xpos 24 ypos 24 xsize (mod_story_box_w - 48) ysize (mod_story_box_h - 48) alpha 0.98

        # outer frame
        add (
            Frame("images/interface/ShoppingMenuBox.png", mod_story_box_border, mod_story_box_border)
            if mod_story_box_border > 0
            else im.Scale("images/interface/ShoppingMenuBox.png", mod_story_box_w, mod_story_box_h)
        )

        # text and button
        frame:
            background None
            xfill True
            yfill True
            xpadding 48
            ypadding 36

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 18

                text "[mod_story_unlock_name] is now unlocked!" size 56 xalign 0.5 color "#fff" outlines [(3, "#000c", 0, 0)]
                text "You can start it from Mod Select." size 30 xalign 0.5 color "#fff" outlines [(2, "#000a", 0, 0)]

                textbutton "OK":
                    xalign 0.5
                    text_size 34
                    action Hide("mod_story_unlocked_modal")

# Mod Selection Screen
screen mod_story_selection():
    # it's part of the main menu, so tag it as such
    tag menu

    # rebuild extra mod stories before building the list
    # needed for mods like supersexual awakening
    $ refresh_extra_mod_stories()

    # track which page we're on
    default side_page = 1

    # build the list fresh each time
    # that way locks/unlocks always match the current save state
    $ mod_stories = []

    # Sam Side Story
    if os.path.isdir(os.path.join(config.gamedir, "mods", "sam_side_story")):
        $ side_story_locked = not getattr(persistent, "side_story_unlocked", True)

        $ mod_stories.append({
            "name": "Sam Side Story",
            "image": "images/interface/Sam_Face_Icon.png",
            "label": "start_side_story",
            "locked": side_story_locked,
            "status": "Locked" if side_story_locked else "Unlocked",
        })

    # mods add their own stories here through the extra_mod_stories list
    for story in extra_mod_stories:
        $ mod_stories.append(story)

    # check if any mod story needs to show the unlock popup
    $ story_toast = None
    for story in mod_stories:
        if not story.get("locked", True) and story.get("show_unlock_toast", False):
            if story.get("toast_flag"):
                if not getattr(persistent, story["toast_flag"], False):
                    $ story_toast = story

    if story_toast:
        timer mod_story_toast_delay action [
            SetVariable("unlock_story_name", story_toast["name"]),
            Show("mod_story_unlocked_modal"),
            Function(setattr, persistent, story_toast["toast_flag"], True),
            Function(renpy.save_persistent)
        ]

    # filler entry so the screen doesn't break if mod stories aren't installed
    # tried making this conditional but then the grid shifts around weird when it's empty
    $ mod_stories.append({
        "name": "Coming Soon...",
        "image": "images/interface/Vicky_Face_Icon_Hidden.png",
        "label": "no_label",
        "locked": True,
        "status": "Locked",
        "show_unlock_toast": False,
        "toast_flag": "",
    })

# UI Layout Variables
    # adjust these to change the layout of the mod story selection screen
    # See comments for what each variable does
    
    # size of the main box
    $ box_width = 1500
    $ box_height = 725

    # grid setup
    # originally wanted this to auto-scale to any number of columns
    # but that got messy, so I'm capping it at 3
    # go higher and things get cramped anyway
    $ num_cols = 3
    # $ grid_spacing = 48  # tried this but icons looked too far apart
    $ grid_spacing = 36

    # title and grid positions
    # these get adjusted later if there's only one row
    $ title_ypos = 20
    $ grid_ypos = 130

    # 1 row = bigger icons since there's more space
    # 2 rows = smaller so everything fits without scrolling
    $ icon_size_1row = 220
    $ icon_size_2rows = 180
    # $ icon_size_2rows = 160  # was too small, bumped it back up

    # text and button sizes
    $ name_text_size = 27
    $ status_text_size = 18
    $ button_text_size = 30

    # fixed text/button heights keep rows aligned even when text lengths differ
    $ name_height = 52
    $ status_height = 22
    $ btn_height = 26
    $ cell_spacing = 0

    $ items_per_page = 6
    
    # six entries per page (two rows of three)
    $ total_items = len(mod_stories)
    $ total_pages = max(1, (total_items + items_per_page - 1) // items_per_page)
    $ side_page = max(1, min(side_page, total_pages))

    # clamp page number so it stays in bounds
    $ side_page = max(1, min(side_page, total_pages))

    # get the stories for the current page
    $ page_start = (side_page - 1) * items_per_page
    $ page_end = page_start + items_per_page
    $ page_items = mod_stories[page_start:page_end]

    $ num_items = len(page_items)

    # one row if 3 or fewer entries, two rows otherwise
    $ num_rows = 1 if num_items <= 3 else 2

    # cell width accounting for spacing between columns
    $ cell_width = (box_width - ((num_cols - 1) * grid_spacing)) / num_cols

    # center the grid better when there's only one row
    # otherwise it sits too low and looks weird
    if num_rows == 1:
        $ grid_ypos = 175

    $ icon_size = icon_size_1row if num_rows == 1 else icon_size_2rows
    $ icon_scale = icon_size / float(icon_size_1row)

    # shrink text/buttons proportionally when using two rows
    # but don't let them get too small or they become unreadable
    $ name_sz = max(14, int(name_text_size * icon_scale))
    $ status_sz = max(12, int(status_text_size * icon_scale))
    $ btn_sz = max(14, int(button_text_size * icon_scale))

    # these need to scale too
    $ name_h = max(16, int(name_height * icon_scale))
    $ status_h = max(10, int(status_height * icon_scale))
    $ button_h = max(14, int(btn_height * icon_scale))

    # main box
    add "images/interface/ShoppingMenuBox.png" xalign 0.5 yalign 0.5

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 0

        frame:
            background None
            xalign 0.5
            yalign 0.5
            xsize BOX_W
            ysize BOX_H

            fixed:
                xfill True
                yfill True

                # title is always centered at the top
                text "Select Your Story" size 60 color "#fff" xalign 0.5 ypos TITLE_Y

                # story grid
                # always builds a full grid even if the last page has fewer entries
                # keeps the layout from jumping around between pages
                grid num_cols num_rows spacing grid_spacing xalign 0.5 ypos grid_ypos:
                    $ total_cells = num_rows * num_cols

                    for i in range(total_cells):
                        if i < num_items:
                            $ s = page_items[i]

                            # each story gets one fixed-width cell so the rows stay lined up
                            vbox:
                                xsize cell_width
                                spacing cell_spacing
                                xalign 0.5

                                # fixed icon area so every entry lines up
                                fixed:
                                    xsize cell_w
                                    ysize icon_size

                                    # scale every icon to the same size
                                    # keeps one odd-sized image from throwing off the whole grid
                                    add im.Scale(s["image"], icon_size, icon_size) xalign 0.5 yalign 0.5

                                # mod name
                                text s["name"] size name_sz color "#fff" text_align 0.5 xalign 0.5 ysize name_h

                                # locked/unlocked status
                                text s["status"] size status_sz color "#ccc" text_align 0.5 xalign 0.5 ysize status_h

                                # fixed button area so all buttons stay level with one another
                                fixed:
                                    xsize cell_width
                                    ysize button_h
                                    xalign 0.5

                                    # unlocked stories get a start button
                                    # locked ones just show "Locked"                         
                                    if not s["locked"]:
                                        if "start_action" in s:
                                            textbutton "Start" action s["start_action"] xalign 0.5 text_size btn_sz
                                        else:
                                            textbutton "Start" action Start(s["label"]) xalign 0.5 text_size btn_sz
                                    else:
                                        textbutton "Locked" action NullAction() xalign 0.5 text_size btn_sz

                        else:
                            # filler cell to keep the grid aligned
                            # works even if the last page has fewer entries than expected
                            null width cell_width height (icon_size + name_h + status_h + button_h + cell_spacing)


    # only show page controls if there's more than one page
    if total_pages > 1:
        vbox:
            xalign 0.5
            yalign 0.95

            # current page indicator
            text "Page [side_page] / [total_pages]" size 48 xalign 0.5

            hbox:
                spacing 20

                # previous page
                textbutton "<":
                    action SetScreenVariable("side_page", side_page - 1)
                    sensitive side_page > 1
                    text_size 48

                # page jump buttons
                for p in range(1, total_pages + 1):
                    textbutton "[p]":
                        action SetScreenVariable("side_page", p)
                        text_size 48

                # next page
                textbutton ">":
                    action SetScreenVariable("side_page", side_page + 1)
                    sensitive side_page < total_pages
                    text_size 48

    # reuse the back button
    use back_button(click_action = Return(), xalign = 0.98, yalign = 0.98)