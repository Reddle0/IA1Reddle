default persistent.leftovers_extra_music_tracks_enabled = False

# Daytime Tracks
init 101 python:
    old_leftovers_home_daytime_music_list = home_daytime_music_list

    def home_daytime_music_list():
        music_list = old_leftovers_home_daytime_music_list()

        if persistent.leftovers_extra_music_tracks_enabled:
            music_list.append("mods/leftovers_mod/audio/music/Daytime_activity.ogg")
            music_list.append("mods/leftovers_mod/audio/music/Someday_in_the_Rain.ogg")

            music_list.extend(custom_music_files("home/daytime"))

            return music_list

        return music_list

init 101 python:
    leftovers_old_home_evening_music_list = home_evening_music_list

    def home_evening_music_list():
        music_list = leftovers_old_home_evening_music_list()

        if persistent.leftovers_extra_music_tracks_enabled:
            music_list.append("mods/leftovers_mod/audio/music/Lounge4.ogg")
            music_list.append("mods/leftovers_mod/audio/music/Lovely_Day-Narr.ogg")
            music_list.append("mods/leftovers_mod/audio/music/n.c.h - BGM Fun - 08 cool.ogg")
            music_list.append("mods/leftovers_mod/audio/music/n.c.h - the repository - 11 cooljazzybgm030314.ogg")

            music_list.extend(custom_music_files("home/evening"))

            return music_list

        return music_list

# Outside Tracks #
init 101 python:
    leftovers_old_outside_daytime_music_list = outside_daytime_music_list

    def outside_daytime_music_list():
        music_list = leftovers_old_outside_daytime_music_list()

        if persistent.leftovers_extra_music_tracks_enabled:
            music_list.append("mods/leftovers_mod/audio/music/Easy_Soul_90.ogg")
            music_list.append("mods/leftovers_mod/audio/music/Summer_Dawn.ogg")

            music_list.extend(custom_music_files("outside/daytime"))

            return music_list

        return music_list

init 101 python:
    leftovers_old_outside_evening_music_list = outside_evening_music_list

    def outside_evening_music_list():
        music_list = leftovers_old_outside_evening_music_list()

        if persistent.leftovers_extra_music_tracks_enabled:
            music_list.append("mods/leftovers_mod/audio/music/Warm_Tea_Time.ogg")

            music_list.extend(custom_music_files("outside/evening"))

            return music_list

        return music_list