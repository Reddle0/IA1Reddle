# Gift Database Adjustments #

# cleans up the item database for the new shop rework
# moves old items into the right tabs, hides "legacy" base game items no longer in use, and adds the new modded gift items to the new database
# also handles the shop checks the ui needs, like what should show up, what can be bought, and what counts as clothing/minigames/gifts

init 100 python:
# Item Helpers

    # every item path in here goes through "id"
    def mod_item_id(item):
        return item["id"]

    # this reads the item's tags and turns them into a normal list we can actually use
    def mod_item_tags(item):
        # if we already cleaned these tags once, just reuse them
        # that saves us from doing the same text cleanup over and over
        if "parsed_tags" in item:
            return item["parsed_tags"]

        # no tags means there is nothing to sort or check later
        if "tags" not in item:
            item["parsed_tags"] = []
            return item["parsed_tags"]

        tags = item["tags"]

        # if the tags are already a real list, keep a copy and save it
        if isinstance(tags, list):
            item["parsed_tags"] = tags[:]
            return item["parsed_tags"]

        # a lot of these tags are stored as text in the item database, so we have to clean that text up to get the actual tags
        # we are left with just the tag names
        tags = str(tags)
        tags = tags.replace("[", "")
        tags = tags.replace("]", "")
        tags = tags.replace("\"", "")
        tags = tags.replace("'", "")

        # if nothing is left after cleanup, there are no real tags here
        if not tags.strip():
            item["parsed_tags"] = []
            return item["parsed_tags"]

        parsed_tags = []

        # split the text by commas so "gift, clothing" becomes two separate tags of "gift" and "clothing"
        # this is done for items like swimsuits that needed to be moved out of the general tab, but also now have the clothing tag for the new clothing tab
        for tag in tags.split(","):
            tag = tag.strip()

            # skip blank pieces so we do not save empty tags by accident
            if tag:
                parsed_tags.append(tag)

        # save this cleaned up list of tags back into the item so we do not have to do this again later
        item["parsed_tags"] = parsed_tags
        return item["parsed_tags"]

    # small helper so the tag checks stay readable everywhere else
    def mod_item_has_tag(item, tag):
        return tag in mod_item_tags(item)

    # this puts the tags back into the same text format the item database already uses
    def mod_set_item_tags(item, tag_list):
        # the base game stores tags as text in the item database, so we rebuild that text here
        # this turns ["gift", "clothing"] back into ["gift", "clothing"]
        tag_text = "["

        # no comma before the first tag
        first_tag = True

        for tag in tag_list:
            if not first_tag:
                tag_text += ", "

            # wrap each tag in quotes so it goes back into the same format the rest of the database already uses            
            tag_text += "\"" + tag + "\""
            first_tag = False

        # close the bracket to finish rebuilding the text format
        tag_text += "]"

        # save this text back into the item so it matches the format
        item["tags"] = tag_text

        # also save the real list of tags back into the item so we do not have to do the text cleanup again later
        item["parsed_tags"] = tag_list[:]
        return

    # this keeps gift tracking tied to the real item id, so there's only one id to care about
    def mod_gift_id(item):
        return item["id"]

    # this is the main function the shop ui uses to get the list of items to show in each tab
    # it figures out which tabs should exist, and builds a list of items for the tab that is currently open
    def mod_prepare_shop_items(items, inventory_type):
        has_general = False
        has_gifts = False
        has_minigames = False
        has_clothing = False
        filtered_items = []

        for item in items:
            # grab the tags for this item so we can check which category it belongs in and whether it should be included in the current tab
            item_tags = mod_item_tags(item)

            # these four checks decide which tabs should show up at the top
            if "general" in item_tags:
                has_general = True

            if "gift" in item_tags:
                has_gifts = True

            if "minigame" in item_tags:
                has_minigames = True

            if "clothing" in item_tags:
                has_clothing = True

            # now decide whether this item belongs in the tab the player is looking at
            if inventory_type == "all":
                filtered_items.append(item)

            elif inventory_type == "general":
                if "general" in item_tags:
                    filtered_items.append(item)

            elif inventory_type == "gift":
                if "gift" in item_tags:
                    filtered_items.append(item)

            elif inventory_type == "minigame":
                if "minigame" in item_tags:
                    filtered_items.append(item)

            elif inventory_type == "clothing":
                if "clothing" in item_tags:
                    filtered_items.append(item)

        # return the tab visibility flags and the finished list of items for the current tab
        return has_general, has_gifts, has_minigames, has_clothing, filtered_items

    # some gifts are one-and-done, others can be gifted again
    # this just checks for the tag instead of hardcoding item names here
    def mod_gift_is_regiftable(item):
        return mod_item_has_tag(item, "regiftable")

    # some gifts stay in the main item list, but are really meant for one person only
    # this is where we stop them from being handed to the wrong character
    def mod_character_can_be_given_gift(char, item):
        if "gift_target" in item:
            if item["gift_target"]:
                if item["gift_target"] != char.variable_name:
                    return False

        return True

# Shop Helpers
    # this keeps the price text and the bought / sold out text in one place
    # so the ui does not have to guess what to show for one-time items
    def mod_buy_item_price(item):
        item_id = mod_item_id(item)
        
        # the limit here means the item is not meant to be bought forever
        # once the player hits that cap, stop showing the normal dollar price, show a status instead
        limit = item["limit"]

        if limit:
            if store.inventory.num_items_by_id(item_id) >= limit:
                # if limit is exceeded
                if limit == 1:
                    limit_text = "Bought!"
                else:
                    limit_text = "Sold Out!"

                return "{color=" + gui.accent_color + "}" + limit_text + "{/color}"

        # otherwise build the normal price text
        price_text = ""
        price = item["price"]

        # turn the number red when the player can't afford it, like the base game
        if price > store.inventory.money:
            price_text += "{color=#ff0000}"

        # dollar sign
        price_text += "$" + str(price)

        # price text display
        if price > store.inventory.money:
            price_text += "{/color}"

        return price_text

    # this decides whether the buy button should still work
    # it blocks anything the player can't afford, shouldn't see yet, or already maxed out
    def mod_buy_item_enabled(item):
        item_id = mod_item_id(item)

        # if conditions aren't met, don't show the item
        if eval(item["condition_enabled"]) == False:
            return False

        # no money means no buy
        if item["price"] > inventory.money:
            return False

        # some items are only meant to work once, even if they still stay visible
        # examples: minigame boosters, swimsuits, etc.
        if eval(item["disable_after_first_buy"]) and store.inventory.has_bought_item_before(item_id):
            return False

        limit = item["limit"]

        # if the player is already at the cap, stop listing it
        if limit:
            if store.inventory.num_items_by_id(item_id) >= limit:
                return False

        return True

    # this decides whether or not the item is visible to buy
    # if an item should disappear after being bought, then remove it from sight
    def mod_buy_item_visible(item):
        item_id = mod_item_id(item)

        # ignore broken / placeholder ids if they somehow slip in here
        if isinstance(item_id, int):
            if item_id < 1:
                return False

        # if conditions aren't met, don't show the item
        if eval(item["condition_visible"]) == False:
            return False

        # some items are only meant to work once, even if they still stay visible
        # examples: minigame boosters, swimsuits, etc.
        if eval(item["disappear_after_first_buy"]) and store.inventory.has_bought_item_before(item_id):
            return False

        limit = item["limit"]

        # if the player is already at the cap, stop listing it
        if limit:
            if store.inventory.num_items_by_id(item_id) >= limit:
                return False

        return True

    # this decides whether or not the item should still show up in the shop list
    # unlike mod_buy_item_visible, this one does not hide already-bought items
    # that way a whole tab does not disappear just because everything in it was bought
    def mod_shop_item_list_visible(item):
        item_id = mod_item_id(item)

        # ignore broken / placeholder ids if they somehow slip in here
        if isinstance(item_id, int):
            if item_id < 1:
                return False

        # if conditions aren't met, don't show the item
        if eval(item["condition_visible"]) == False:
            return False

        return True
    
    # this pulls every item with a matching tag out of the full database
    # it does not care yet whether the item should be visible right now
    # that part gets handled later by the visibility check
    def mod_items_with_tag(tag):
        items = []

        for item in store.database_items:
            item_id = mod_item_id(item)

            # ignore broken / placeholder ids if they somehow slip in here
            if isinstance(item_id, int):
                if item_id < 1:
                    continue

            if mod_item_has_tag(item, tag):
                items.append(item)

        return items

    # this grabs items with the tag and then filter out the ones the shop should not show right now
    def mod_visible_items_with_tag(tag):
        items = []

        # grab everything with that tag
        # filter out the ones the shop should not show right now
        for item in mod_items_with_tag(tag):
            if mod_buy_item_visible(item):
                items.append(item)

        return items

    # this is the list the new shop screen uses
    # it keeps category tabs present even when one-time items are already bought
    def mod_visible_all_shop_items():
        items = []

        for item in store.database_items:
            item_tags = mod_item_tags(item)

            if "general" not in item_tags and "gift" not in item_tags and "minigame" not in item_tags and "clothing" not in item_tags:
                continue

            if mod_shop_item_list_visible(item):
                items.append(item)

        return items

# Item Cleanup Helpers

    # this catches the old base game shop items that aren't seeing use anymore
    # we keep them in the database, but hide them so they do not sit beside the new gift system
    # called the items "legacy" since it's no longer being used
    def mod_is_legacy_gift_item(item):
        # if the item name doesn't match, don't include
        if "name" not in item:
            return False

        return item["name"].startswith("Gift For ")

    # does the same with minigame boosters
    # also includes the new modded minigame boosters
    # they are now under the "minigames" tab
    def mod_is_minigame_item(item):
        # if the item name doesn't match, don't include
        if "name" not in item:
            return False

        item_name = item["name"]

        # base game minigame boosters
        if item_name == "Running Insoles":
            return True
        if item_name == "Speed Typing Tips":
            return True
        if item_name == "Hire Review Help":
            return True
        if item_name == "Math Wizard":
            return True
        if item_name == "Dictionary":
            return True

        # modded boosters
        if item_name == "Tennis Tactician":
            return True
        if item_name == "Positive Thoughts":
            return True
        if item_name == "Slider Savant":
            return True
        if item_name == "One-Key Wonder":
            return True
        if item_name == "Time Twister":
            return True
        if item_name == "Minigame Skipper":
            return True

        return False

    # same for swimsuit items
    # they are now under the "clothing" tab
    def mod_is_clothing_item(item):
        # if the item name doesn't match, don't include
        if "name" not in item:
            return False

        item_name = item["name"]

        # swimsuit list
        if item_name == "Swimsuit For [sa.say_name]":
            return True

        if item_name == "Swimsuit For [si.say_name]":
            return True

        # includes julia's new swimsuit just in case
        if item_name == "Swimsuit for [julia.say_name]":
            return True

        return False

    # removes the old "general" tag and replaces it with the new category
    # this keeps old tags from stacking up into weird category combos
    def mod_move_item_to_tag(item, new_tag):
        # start with whatever tags the item already has
        old_tags = mod_item_tags(item)
        new_tags = []

        for old_tag in old_tags:
            # drop "general" so the item stops living in the old tab
            # prevents overbloat of that tab
            if old_tag == "general":
                continue

            # keep the other tags, but don't duplicate
            if old_tag not in new_tags:
                new_tags.append(old_tag)

        # add the new home for the item
        if new_tag not in new_tags:
            new_tags.append(new_tag)

        mod_set_item_tags(item, new_tags)
        return

    # this looks through the database so we can update an item with exact ids instead of stacking duplicates
    def mod_find_item_by_id(item_id):
        for item in store.database_items:
            if "id" in item:
                if item["id"] == item_id:
                    return item

        return None

    # keep the existing item object, just refresh its data from the new gift database entry
    # that way the list stays stable and we do not stack duplicates every time the game starts
    def mod_update_item_data(existing_item, new_item):
        for key in new_item:
            existing_item[key] = new_item[key]

        return

# Main Cleanup
    # this runs through the database once and sorts categories / old items / new gift entries into the way the new shop expects
    def mod_apply_gift_database_patch():
        for item in store.database_items:
            if mod_is_minigame_item(item):
                mod_move_item_to_tag(item, "minigame")

        for item in store.database_items:
            if mod_is_clothing_item(item):
                mod_move_item_to_tag(item, "clothing")

        for item in store.database_items:
            if mod_is_legacy_gift_item(item):
                item["condition_visible"] = "False"
                item["condition_enabled"] = "False"
                item["action_on_buy"] = ""
                item["label_on_buy"] = ""
                mod_set_item_tags(item, ["legacy"])

        # brand new item, so just add it to the database
        for gift_item in mod_gift_database_entries():
            existing_item = mod_find_item_by_id(gift_item["id"])

            # if it already exists, refresh the old entry with the new data
            if existing_item is None:
                store.database_items.append(gift_item)
            else:
                # prevents adding a second copy of the same item
                mod_update_item_data(existing_item, gift_item)

        return