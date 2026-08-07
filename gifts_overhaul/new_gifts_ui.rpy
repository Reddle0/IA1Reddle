# Gift Shop UI #

# complete overhaul of the gift shop UI, with a modified layout and design
# looks more visually similar to IA2 style-wise, but obviously maintains the IA1 look by reusing the shoppingmenubox image
# also includes a new system for determining which items can be gifted to which characters, and how characters respond to gifts, based on IA2

screen inventory_shopping_gifts(items = [], shop = False, gifts = False, char = None, after_buy_label = None):
    zorder 100
    modal True

    # which tab is currently selected in the shop
    # "all", "general", "gift", "minigame", "clothing"
    default inventory_type = "all"

    # saves won't have these yet, so set them up before checking any gift stuff
    # this is required to properly check gift conditions and display gift feedback
    if gifts and char is not None:
        $ char.initialize_gift_data()

    # this decides which tab categories should exist at all
    # only show tabs that actually have something in them
    $ has_general = False
    $ has_gifts = False
    $ has_minigames = False
    $ has_clothing = False

    # this should do two jobs at once:
    # 1. decide which tabs should show up
    # 2. build the item list for the tab we are on
    $ has_general, has_gifts, has_minigames, has_clothing, filtered_items = mod_prepare_shop_items(items, inventory_type)

    # dim background when shop is open
    add Solid("#0006")

    # this is the main shop box
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 700
        background Frame("images/interface/ShoppingMenuBox.png", 40, 40)
        xpadding 35
        ypadding 25

        fixed:
            xfill True
            yfill True

            # this row just swaps which filtered list gets shown
            hbox:
                spacing 8
                xalign 0.5
                ypos 8

                textbutton "All":
                    xpadding 6
                    ypadding 4

                    if inventory_type == "all":
                        # we're using nullaction here so the spacing and hitbox stay the same, clicking it does nothing
                        action NullAction()
                        text_color "#b44cff"
                    else:
                        action SetScreenVariable("inventory_type", "all")
                        text_color "#ffffff"

                    text_size 32
                    text_hover_color "#b44cff"
                    text_outlines [(3, "#000000", 0, 0)]
                    background None
                    hover_background None

                # general
                if has_general:
                    textbutton "General":
                        xpadding 6
                        ypadding 4

                        if inventory_type == "general":
                            action NullAction()
                            text_color "#b44cff"
                        else:
                            action SetScreenVariable("inventory_type", "general")
                            text_color "#ffffff"

                        text_size 32
                        text_hover_color "#b44cff"
                        text_outlines [(3, "#000000", 0, 0)]
                        background None
                        hover_background None

                # gifts
                if has_gifts:
                    textbutton "Gifts":
                        xpadding 6
                        ypadding 4

                        if inventory_type == "gift":
                            action NullAction()
                            text_color "#b44cff"
                        else:
                            action SetScreenVariable("inventory_type", "gift")
                            text_color "#ffffff"

                        text_size 32
                        text_hover_color "#b44cff"
                        text_outlines [(3, "#000000", 0, 0)]
                        background None
                        hover_background None

                # minigames
                if has_minigames:
                    textbutton "Minigames":
                        xpadding 6
                        ypadding 4

                        if inventory_type == "minigame":
                            action NullAction()
                            text_color "#b44cff"
                        else:
                            action SetScreenVariable("inventory_type", "minigame")
                            text_color "#ffffff"

                        text_size 32
                        text_hover_color "#b44cff"
                        text_outlines [(3, "#000000", 0, 0)]
                        background None
                        hover_background None

                # clothing
                if has_clothing:
                    textbutton "Clothing":
                        xpadding 6
                        ypadding 4

                        if inventory_type == "clothing":
                            action NullAction()
                            text_color "#b44cff"
                        else:
                            action SetScreenVariable("inventory_type", "clothing")
                            text_color "#ffffff"

                        text_size 32
                        text_hover_color "#b44cff"
                        text_outlines [(3, "#000000", 0, 0)]
                        background None
                        hover_background None

            # scroll area for the item list
            fixed:
                xsize 860
                ysize 560
                xalign 0.5
                ypos 65

                # keep the list in a viewport so long shop lists can scroll without stretching the whole box
                viewport id "mod_items":
                    xsize 800
                    ysize 560
                    draggable True
                    mousewheel True

                    vbox:
                        spacing 0

                        # don't leave the panel blank if the tab has nothing
                        if len(filtered_items) <= 0:
                            text "No items available." size 24 xalign 0.5 color "#ffffff" outlines [(3, "#000000", 0, 0)]

                        else:
                            # filtered_items was already built above by mod_prepare_shop_items
                            # this part just goes through those items and grabs their tags when needed
                            for item in filtered_items:
                                $ item_tags = mod_item_tags(item)

                                vbox:
                                    xsize 800
                                    spacing 4

                                    add Null(height = 10)

                                    # item name
                                    text item["name"] size 34 color "#ffffff" outlines [(3, "#000000", 0, 0)]

                                    # item description
                                    if item["description"]:
                                        text "{i}" + item["description"] + "{/i}" size 24 color "#ffffff" outlines [(3, "#000000", 0, 0)]

                                    # this part is mainly just here to work around swimsuits
                                    # they are not actually added to the player's inventory when bought, and can only be gifted once
                                    if "clothing" in item_tags:
                                        if store.inventory.has_bought_item_before(mod_item_id(item)):
                                            text "Owned: Yes" size 24 color "#ffffff" outlines [(3, "#000000", 0, 0)]
                                        else:
                                            text "Owned: No" size 24 color "#ffffff" outlines [(3, "#000000", 0, 0)]
                                    else:
                                        # use the item id here so the count always matches the real inventory entry
                                        text ("In Possession: %s" % inventory.num_items_by_id(mod_item_id(item))) size 24 color "#ffffff" outlines [(3, "#000000", 0, 0)]

                                    # same list, two functions to check for:
                                    # whether the player is in the shop
                                    # whether the player is gifting
                                    if shop:
                                        text ("Price: %s" % mod_buy_item_price(item)) size 24 color "#ffffff" outlines [(3, "#000000", 0, 0)]

                                        textbutton "Buy":
                                            action Function(inventory.buy, item, after_buy_label)
                                            sensitive mod_buy_item_enabled(item)
                                            text_size 34
                                            text_hover_color "#b44cff"
                                            text_outlines [(3, "#000000", 0, 0)]
                                            background None
                                            hover_background None

                                    # gift mode uses the give button and the gift checks below
                                    elif gifts and char is not None:
                                        # use the item id here so the checks below all read the same gift
                                        $ gift_id = mod_gift_id(item)

                                        # keep the item visible even if the game is blocking it so the player can still see why
                                        if "ungiftable" in item_tags:
                                            textbutton "Cannot be gifted":
                                                sensitive False
                                                text_size 34
                                                text_outlines [(3, "#000000", 0, 0)]
                                                background None
                                                hover_background None

                                        elif not mod_character_can_be_given_gift(char, item):
                                            textbutton "Cannot be gifted to this character":
                                                sensitive False
                                                text_size 34
                                                text_outlines [(3, "#000000", 0, 0)]
                                                background None
                                                hover_background None

                                        elif gift_id in char.gifted and not mod_gift_is_regiftable(item):
                                            textbutton "Cannot be regifted":
                                                sensitive False
                                                text_size 34
                                                text_outlines [(3, "#000000", 0, 0)]
                                                background None
                                                hover_background None

                                        else:
                                            textbutton "Give":
                                                action Return(item)
                                                text_size 34
                                                text_hover_color "#b44cff"
                                                text_outlines [(3, "#000000", 0, 0)]
                                                background None
                                                hover_background None

                                    # divider between items
                                    add Null(height = 8)
                                    add Solid("#ffffff", xsize = 780, ysize = 2)
                                    add Null(height = 14)

                # scrollbar for the item list above
                vbar value YScrollValue("mod_items"):
                    xpos 820
                    ysize 560

    # self-explanatory, reusing the back button
    use back_button(navigation_back, xalign = 0.98, yalign = 0.98)