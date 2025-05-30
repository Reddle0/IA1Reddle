init 100 python:
    store.database_items.append({
        "id": "julia_swimsuit",
        "name": "Swimsuit for [julia.say_name]",
        "description": "Unlocks a small scene and outfit for [julia.say_name]. Purchase during daytime only.",
        "price": 12,
        "disable_after_first_buy": "True",
        "disappear_after_first_buy": "False",
        "condition_visible": "store.had_julia_arrived_scene and store.week.time == \"day\"",
        "condition_enabled": "True",
        "limit": 1,
        "label_on_buy": "julia_scene_swimsuit",
        "action_on_buy": "",
        "tags": "[\"general\"]",
        "null": ""
    })

init 100 python:
    store.database_items.append({
        "id": "15",
        "name": "Gift For [vicky.say_name]",
        "description": "Adds 4 [vicky.say_name] points.",
        "price": 4,
        "disable_after_first_buy": "False",
        "disappear_after_first_buy": "False",
        "condition_visible": "store.had_vicky_intro_scene",
        "condition_enabled": "True",
        "limit": 0,
        "label_on_buy": "",
        "action_on_buy": "vicky.add_points(4, yalign = 0.025)",
        "tags": "[\"general\"]",
        "null": ""
    })

init 100 python:
    store.database_items.append({
        "id": "16",
        "name": "Gift For [gloryhole_girl.say_name]",
        "description": "Adds 4 [gloryhole_girl.say_name] points.",
        "price": 4,
        "disable_after_first_buy": "False",
        "disappear_after_first_buy": "False",
        "condition_visible": "\"gloryhole_handjob_scene\" in store.scenes_completed",
        "condition_enabled": "True",
        "limit": 0,
        "label_on_buy": "",
        "action_on_buy": "gloryhole_girl.add_points(4, yalign = 0.025)",
        "tags": "[\"general\"]",
        "null": ""
    })
