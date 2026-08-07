init 100 python:
    store.database_items.append({
        "id": "15",
        "name": "Swimsuit for [julia.say_name]",
        "description": "Unlocks a small scene and outfit for [julia.say_name]. Purchase during daytime only.",
        "price": 12,
        "disable_after_first_buy": "True",
        "disappear_after_first_buy": "False",
        "condition_visible": "store.had_julia_arrived_scene",
        "condition_enabled": "store.week.time == \"day\"",
        "limit": 1,
        "label_on_buy": "julia_scene_swimsuit",
        "action_on_buy": "",
        "tags": "[\"clothing\"]", # updated tag from "general" to "clothing" for the new gifts system
        "null": ""
    })