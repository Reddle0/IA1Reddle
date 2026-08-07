init python:
    def mod_leftovers_options():
        return []

## Leftovers Save Variables ##
default julia_scene_swimsuit_revisit_nude = False

init 100 python:
    def leftovers_extra_track_add_option(func):
        def func_extension():
            options = func()
            options.append( ("Enable Extra Music", "leftovers_extra_music_tracks_enabled"))
            return options
        return func_extension

    mod_leftovers_options = leftovers_extra_track_add_option(mod_leftovers_options)

    def leftovers_extra_music_track_help():
        return "Extra music track now toggled on. Plays at home, during evenings."