########################################################
# Adds new minigame modded items to the shop #
init 100 python:
    store.database_items.append({
        "id": "minigame_item_1",
        "name": "Tennis Tactician",
        "description": "Reduces the ball's speed by half.",
        "price": 5,
        "disable_after_first_buy": "True",
        "disappear_after_first_buy": "False",
        "condition_visible": "True",
        "condition_enabled": "True",
        "limit": 1,
        "label_on_buy": "",
        "action_on_buy": "",
        "tags": "[\"minigame\"]",
        "null": ""
    })

    store.database_items.append({
        "id": "minigame_item_2",
        "name": "Positive Thoughts",
        "description": "Removes all minus questions from the math minigame.",
        "price": 5,
        "disable_after_first_buy": "True",
        "disappear_after_first_buy": "False",
        "condition_visible": "True",
        "condition_enabled": "True",
        "limit": 1,
        "label_on_buy": "",
        "action_on_buy": "",
        "tags": "[\"minigame\"]",
        "null": ""
    })

    store.database_items.append({
        "id": "minigame_item_3",
        "name": "Slider Savant",
        "description": "Reduces the amount of pieces required to complete the slide puzzle.",
        "price": 5,
        "disable_after_first_buy": "True",
        "disappear_after_first_buy": "False",
        "condition_visible": "True",
        "condition_enabled": "True",
        "limit": 1,
        "label_on_buy": "",
        "action_on_buy": "",
        "tags": "[\"minigame\"]",
        "null": ""
    })

    store.database_items.append({
        "id": "minigame_item_4",
        "name": "One-Key Wonder",
        "description": "Only one key is required for the racing minigame.",
        "price": 5,
        "disable_after_first_buy": "True",
        "disappear_after_first_buy": "False",
        "condition_visible": "True",
        "condition_enabled": "True",
        "limit": 1,
        "label_on_buy": "",
        "action_on_buy": "",
        "tags": "[\"minigame\"]",
        "null": ""
    })

    store.database_items.append({
        "id": "minigame_item_5",
        "name": "Time Twister",
        "description": "Gives you infinite time on all minigames.",
        "price": 8,
        "disable_after_first_buy": "True",
        "disappear_after_first_buy": "False",
        "condition_visible": "True",
        "condition_enabled": "True",
        "limit": 1,
        "label_on_buy": "",
        "action_on_buy": "",
        "tags": "[\"minigame\"]",
        "null": ""
    })

    store.database_items.append({
        "id": "minigame_item_6",
        "name": "Minigame Skipper",
        "description": "Automatically skips all minigames. \nPrice is free if all minigames are completed twice.",
        "price": 30,
        "disable_after_first_buy": "True",
        "disappear_after_first_buy": "False",
        "condition_visible": "True",
        "condition_enabled": "True",
        "limit": 1,
        "label_on_buy": "",
        "action_on_buy": "",
        "tags": "[\"minigame\"]",
        "null": ""
    })

########################################################