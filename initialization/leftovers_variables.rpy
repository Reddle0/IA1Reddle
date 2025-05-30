init 100 python:
    def mod_leftovers_options():
        return []

## Leftovers Save Variables ##
default persistent.extra_music_track_enabled = False
default julia_scene_swimsuit_revisit_nude = False

## Take It Easy 02 + Extra Option Settings ##
init 100 python:
    leftovers_old_home_evening_music_list = home_evening_music_list

    def home_evening_music_list():
        music_list = leftovers_old_home_evening_music_list()

        if persistent.extra_music_track_enabled:
            # add unused track to the array
            music_list.append("audio/music/Take it Easy 02.ogg")

        else:

            if "audio/music/Take it Easy 02.ogg" in music_list:
                # remove unused track from the array
                music_list.remove("audio/music/Take it Easy 02.ogg")

            return music_list

        return music_list

    def reset_volume():
        preferences.set_volume('music', config.default_music_volume)
        preferences.set_volume('sfx', config.default_sfx_volume)
        preferences.set_volume('voice', config.default_voice_volume)
        return

    def leftovers_extra_track_add_option(func):
        def func_extension():
            options = func()
            options.append( ("Enable \"Take It Easy 02\" Extra Music Track", "extra_music_track_enabled", persistent))
            return options
        return func_extension

    mod_leftovers_options = leftovers_extra_track_add_option(mod_leftovers_options)

init python:
    def leftovers_extra_music_track_help():
        return "Extra music track now toggled on. Plays at home, during evenings."

## #### ## #### ## ##
