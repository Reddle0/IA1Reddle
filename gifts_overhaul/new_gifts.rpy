# New Gifts System #

# complete overhaul of how gifts work, to be more in line with IA2
# adds the new "gift" option to character menus, handles giving items to characters, etc.
# also swaps nate's room shopping label over to the new shop screen

init 200 python:
    # override base game labels
    config.label_overrides["character_menu"] = "mod_character_menu"
    config.label_overrides["nate_room_shopping"] = "mod_nate_room_shopping"

# Inventory Helpers
    def mod_inventory_remove_item(self, item, quantity = 1): # remove one item from the inventory by using the item id
        self.remove_item_by_id(mod_item_id(item), quantity)
        return

    # remove items by id
    def mod_inventory_remove_item_by_id(self, item_id, quantity = 1):
        # if the item is not in inventory, there is nothing to remove
        if item_id not in self.items:
            return

        # subtract the amount we are removing
        self.items[item_id] -= quantity

        # once it hits zero, wipe the entry
        if self.items[item_id] <= 0:
            del self.items[item_id]

        return

    # rebuilds the gift list from the normal inventory
    # filters as items tagged as "gifts", and items the player actually has at least one of
    def mod_inventory_gifts(self):
        gift_items = []

        for item in store.database_items:
            item_id = mod_item_id(item)

            # skip broken / placeholder ids
            if isinstance(item_id, int) and item_id < 1:
                continue

            # only keep items tagged as gifts
            if not mod_item_has_tag(item, "gift"):
                continue

            # if the player does not own an item, don't have it show up in the "give gift" menu
            if self.num_items_by_id(item_id) <= 0:
                continue

            gift_items.append(item)

        # final list the gift screen uses
        return gift_items

    # add these onto inventory so the rest of this file can use them
    Inventory.remove_item = mod_inventory_remove_item
    Inventory.remove_item_by_id = mod_inventory_remove_item_by_id
    Inventory.gifts = mod_inventory_gifts

# Actor Gift Defaults  
    # make these vars here so gift code does not blow up when they are missing
    def mod_initialize_gift_data(self):
        if not hasattr(self, "gifted"):
            self.gifted = set()

        # keep a running count so characters can react differently later
        if not hasattr(self, "times_given_a_gift"):
            self.times_given_a_gift = 0

        return

    # characters may hand disliked gifts back
    def mod_returns_disliked_gifts(self):
        return False

    # whether the character should be able to receive gifts
    def mod_can_be_given_gifts(self):
        return True

    # default relationship point values received from gifts
    def mod_gift_love_points(self):
        return 6

    def mod_gift_like_points(self):
        return 4

    def mod_gift_neutral_points(self):
        return 2

    # whether repeated gifts lose value
    def mod_gift_depreciates_on_repeat(self, gift_id):
        return True

    # this asks the automated_gifts_feedback.rpy file how the character feels about the gift
    def mod_gift_feedback(self, gift_id):
        self.initialize_gift_data()
        return automated_character_feedback_points(gift_id, self)

    # custom intro/feedback labels per-character
    def mod_gift_feedback_label(self):
        return None

    def mod_gift_introduction_label(self):
        return None

    # this is the main function for turning feedback into relationship points
    # the more they like the gift, the more relationship points the player will receive towards that character
    def mod_gift_points(self, gift_id):
        self.initialize_gift_data()

        # first ask the character how they feel about this gift
        gift_feedback = self.gift_feedback(gift_id)
        
        # start at zero, then fill in the proper value below
        gift_points = 0

        # turn the feedback into points
        if gift_feedback == "love":
            gift_points = self.gift_love_points()
        elif gift_feedback == "like":
            gift_points = self.gift_like_points()
        elif gift_feedback == "neutral":
            gift_points = self.gift_neutral_points()
        elif gift_feedback == "neutral spend time":
            gift_points = 1

        # repeated gifts still count, just for less
        if self.gift_depreciates_on_repeat(gift_id) and gift_id in self.gifted:
            gift_points = int(gift_points / 2)

        # never let this go below zero
        if gift_points < 0:
            gift_points = 0

        return gift_points

    # while testing, i found that nate will automatically say that he doesn't have anything to gift after just giving a gift (no kidding, nate)
    # i'm including this as a work-around, works slightly different from IA2 where you can spam gifts
    # this helps alleviate the issue
    def mod_already_received_gift(self):
        return self.already_received_gift_today

    IA_Actor.already_received_gift_today = False

    # give actors the default gift functions here, then character code can replace what it needs
    IA_Actor.initialize_gift_data = mod_initialize_gift_data
    IA_Actor.returns_disliked_gifts = mod_returns_disliked_gifts
    IA_Actor.can_be_given_gifts = mod_can_be_given_gifts
    IA_Actor.gift_love_points = mod_gift_love_points
    IA_Actor.gift_like_points = mod_gift_like_points
    IA_Actor.gift_neutral_points = mod_gift_neutral_points
    IA_Actor.gift_depreciates_on_repeat = mod_gift_depreciates_on_repeat
    IA_Actor.gift_feedback = mod_gift_feedback
    IA_Actor.gift_feedback_label = mod_gift_feedback_label
    IA_Actor.gift_introduction_label = mod_gift_introduction_label
    IA_Actor.gift_points = mod_gift_points
    IA_Actor.already_received_gift = mod_already_received_gift

# Character Menu
    # save old choice_list functions first
    # we need to add the gift option to the character choice menu
    mod_old_gift_choice_list = IA_Actor.choice_list

    # override the choice menu so the new "Give Gift" option exists
    def mod_add_gift_option(choice_list, char):
        if not char.can_be_given_gifts():
            return choice_list

        # add the new "Give Gift" option into the choice list
        choice_list.append(("Give Gift", "mod_character_give_gift"))

        if ("Back", "back") in choice_list:
            choice_list.remove(("Back", "back"))
            choice_list.append(("Back", "back"))

        return choice_list

    def mod_actor_choice_list(self):
        # start with the normal menu choices
        choice_list = mod_old_gift_choice_list(self)
        
        # add "Give Gift" into the list
        choice_list = mod_add_gift_option(choice_list, self)
        
        # then return with the new list
        return choice_list

    IA_Actor.choice_list = mod_actor_choice_list

    # run this now and again after load so old saves pick up the same item cleanup
    mod_apply_gift_database_patch()
    config.after_load_callbacks.append(mod_apply_gift_database_patch)

# overriding of the base game's character menu
label mod_character_menu(char = None, draw_characters = True):
    window hide # hide the normal dialogue window before rebuilding the character menu screens

    # if this gets called without a character, fall back to whoever the menu was opened on
    if char is None:
        $ char = last_selected_character

    python:
        # make sure the character has the gift vars before opening the gift screen
        char.initialize_gift_data()

        # draw character sprites as usual
        if draw_characters:
            if char.display_bust_art_in_character_menu():
                display_multiple_characters([(player_character, ""), (char, "position " + char_menu_char_position)])
            else:
                display_multiple_characters([(player_character, "")])

        # base game screens
        renpy.scene('screens')
        renpy.show_screen('hud_zone_select')
        renpy.show_screen('hud')
        
        # use the choice list with the gift option added in
        chosen_option = renpy.display_menu(char.choice_list())

        # adding the new option to choice_list is only half of it
        # this label still has to know what to do when "gift" gets picked since it's not natively part of IA1

        # once the player picks anything other than "Give Gift", clear the one-time skip for the empty gift line
        if chosen_option != "mod_character_give_gift":
            char.already_received_gift_today = False

        # base game options, but with the extra "gift" option
        if chosen_option == "debug_minigame_instant":
            renpy.call(chosen_option, char)
        elif chosen_option == "cheat_points":
            char.add_points(999, force_no_popup = False)
            narrator("Added 999 points")
            renpy.call("day_advance_time")
        elif chosen_option == "talk":
            char.talk()
        elif chosen_option == "scene_revisit":
            char.display_scene_menu()
        elif chosen_option == "minigame":
            char.display_minigame_menu()
        elif chosen_option == "mod_character_give_gift":
            renpy.call(chosen_option, char)
        elif chosen_option == "retry_prompt_boldness_failure":
            renpy.call(chosen_option, char)
        elif chosen_option == "scene_limit_notice":
            renpy.call(chosen_option, char)
        elif chosen_option == "back":
            renpy.call("location_select", store.stats.current_location)
        else:
            renpy.call(chosen_option)

    return

label mod_character_give_gift(char = None):
    # if the menu called this by label name, grab the last character the menu was opened on
    if char is None:
        $ char = last_selected_character

    # make sure these vars exist before we touch any gift data
    $ char.initialize_gift_data()
    
    # get the list of gift items from nate's inventory
    # no non-gift items and items the player doesn't have
    $ available_gifts = inventory.gifts()

    # if there's nothing to gift, nate will say so
    if len(available_gifts) <= 0:
        # wasn't here previously, but i've added it to circumvent a slightly annoying issue:
        # nate automatically saying he has no gifts when the player gives away the last gift from the inventory (no shit, nate)
        if char.already_received_gift():
            $ char.already_received_gift_today = False
            return

        call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned")
        n.c "I don't have anything to give as a gift right now."
        call character_menu(char, draw_characters = False)
        return

    # open the gift screen, then save the item the player picked
    with navigation_dissolve
    $ gift_item = renpy.call_screen("inventory_shopping_gifts", items = available_gifts, gifts = True, char = char)
    with navigation_dissolve

    # if the gift menu is closed, just go back to the character menu
    if gift_item == "closed":
        $ char.already_received_gift_today = False
        call character_menu(char, draw_characters = False)
        return

    # save the name once here so the menu text can use it directly
    $ gift_name = gift_item["name"]

    # final confirmation before the item is handed over
    menu:
        "Give [gift_name] to [char.say_name]?"
        "Yes":
            # character-specific intro scene before gift reaction
            call mod_character_gift_intro(char, gift_item)

            "You gave [gift_name] to [char.say_name]."

            $ char.times_given_a_gift += 1

            # handle the reaction, item removal, and points
            call mod_character_gift_feedback(char, gift_item)

            # only mark this if that was the last gift left
            if len(inventory.gifts()) <= 0:
                $ char.already_received_gift_today = True
            else:
                $ char.already_received_gift_today = False

            call character_menu(char, draw_characters = False)
            return
        "No":
            $ char.already_received_gift_today = False
            call character_menu(char, draw_characters = False)
            return

    return

# gift intro label
label mod_character_gift_intro(char, gift_item):
    # use the item id here because the intro label checks the gift by id, not by the whole item
    $ gift_id = gift_item["id"]

    # make sure the gift vars exist before the custom intro
    $ char.initialize_gift_data()

    # call a custom gift intro label if the character has one
    if char.gift_introduction_label() is not None:
        $ renpy.call(char.gift_introduction_label(), gift_id)

    return

# gift feedback label
label mod_character_gift_feedback(char, gift_item):
    # use the item id here again like we did with intro
    # unlike intro, the rest of this label checks the gift by id
    $ gift_id = gift_item["id"]

    # make sure the gift vars exist before checking feedback and saving gift state
    $ char.initialize_gift_data()

    # ask the character what they think of this gift before we remove it or hand out points
    $ gift_feedback = char.gift_feedback(gift_id)

    # call a custom gift feedback label if the character has one
    if char.gift_feedback_label() is not None:
        $ renpy.call(char.gift_feedback_label(), gift_id, gift_feedback)
    else:
        # otherwise just use feedback lines below
        if gift_feedback == "love":
            "[char.say_name] loved that."
        elif gift_feedback == "like":
            "[char.say_name] liked that."
        elif gift_feedback == "neutral":
            "[char.say_name] appreciated that."
        elif gift_feedback == "neutral spend time":
            "[char.say_name] appreciated spending time with you."
        elif gift_feedback == "hate":
            "[char.say_name] hated that."
        else:
            "[char.say_name] disliked that."

    # remove gift from inventory after giving it
    $ inventory.remove_item(gift_item)

    # characters may return gifts they dislike
    if gift_feedback == "dislike" and char.returns_disliked_gifts():
        $ inventory.add_item(gift_item, 1)

    # give points based off of the feedback
    $ char.gifted.add(gift_id)
    call add_points(char, char.gift_points(gift_id), delay = True, yalign = 0.025)

    return

# overridden shopping label 
label mod_nate_room_shopping:
    window hide

    # same screen as gifting, just with shop items instead
    # self-explanatory because this is just the shop menu, as usual
    call screen inventory_shopping_gifts(items = mod_visible_all_shop_items(), shop = True, after_buy_label = "mod_nate_room_shopping") with navigation_dissolve
    with navigation_dissolve
    return