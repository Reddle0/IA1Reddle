# Encore Mod - split automated gift feedback mapping for IA1
#
# This file houses automated_character_feedback_points().

init 101 python:
    # IA2-style automated gift feedback remapped onto IA1 characters.
    #
    # The taste mapping here is a best-fit translation from the uploaded IA2
    # feedback file. Any IA1 characters without a mapped taste profile fall back
    # to neutral so the system stays stable.

    def automated_character_feedback_points(gift_id, char):
        # IA2 automated feedback points adapted only where there is a clear IA1
        # character equivalent. Unmapped IA1 characters fall back to neutral.

        if char == store.si:
            if gift_id in ["a_beautiful_line", "breast_chicken_ever", "call_of_leotard", "hello_music_my_old_buddy", "infinite_boundaries", "little_sausage_pizza", "mama_chef", "mind_filler_meals", "mind_over_mind", "moisturizer_cream", "movie_gift_card", "munchy_conditions", "nate_the_great", "pajamas", "pasta_pillar", "premium_motorcycle_helmet", "restaurant_gift_card", "roadshow_rumble", "rock_and_stone_with_todd_moss", "smartphone_case", "sneakers", "spinnin_noodles", "stiff_mornings", "sunglasses", "the_hot_line", "the_suck_zone", "thick_buns_burger", "toolset", "twist_of_the_wrist"]:
                return "love"
            if gift_id in ["1000_iq", "5_in_1_board_game_set", "a_touch_of_tenderness", "boldest_beef", "bulging_out", "cosplay_cafe", "creme_de_la_cream", "dead_wake", "dorothys_daring_dinners", "e-book_reader", "finger_hero", "goliath_of_the_stars", "headphones", "jam_in_the_clam", "junk_in_the_trunk", "laser_tag_guns", "my_ten_frogs", "playground", "seat_cushion_massager", "sleep_mask", "solder_point", "the_godmother", "the_knob_polishers", "the_thumb_is_always_greener", "thermos", "todd_mosss_crystal_collection", "training_gloves", "treats_&_teats", "veg_in_cart", "wool_slippers", "yoooo!_kais"]:
                return "like"
            if gift_id in ["beach_blanket", "bean_flicker_tacos", "box_of_chocolates", "hot_sauce_gift_set", "juiced_up", "motivational_poster"]:
                return "dislike"
            if gift_id in ["wireless_earbuds"]:
                return "hate"

        if char == store.k:
            if gift_id in ["beach_blanket", "bean_flicker_tacos", "boldest_beef", "bouncy_ball", "box_of_chocolates", "breast_chicken_ever", "bromance_of_the_three_bros", "bulging_out", "cosplay_cafe", "cream_pie_maker", "cuddle_whamples_teddy_bear", "dead_wake", "dorothy_hetero", "dorothys_daring_dinners", "goliath_of_the_stars", "grandma_isabellas_lovely_food", "hero_plush", "hot_sauce_gift_set", "l33t_fr3ak", "laser_light_projector", "laser_tag_guns", "little_sausage_pizza", "movego_action_camera", "movie_gift_card", "my_ten_frogs", "neon_yo-yo", "nutbusters", "plain_of_spirits", "playground", "ppii_fitness", "sneakers", "solder_point", "spinnin_noodles", "sprockets_of_strife", "steamborg", "thick_buns_burger", "training_gloves", "wireless_earbuds"]:
                return "love"
            if gift_id in ["balls_to_the_face", "curry_cupid", "dumbell_set", "fornimate_capsule", "happy_ending_buffet", "jam_in_the_clam", "kira_plush", "munchy_conditions", "nate_plush", "nate_the_great", "pajamas", "pasta_pillar", "pirate_ship_model_kit", "restaurant_gift_card", "sane_in_the_membrane", "suplex_for_gold", "the_hot_line", "the_pen_and_the_sword", "thermos", "twist_of_the_wrist", "wolf_girl_plush"]:
                return "like"
            if gift_id in ["a_beautiful_line", "creme_de_la_cream", "deep_fish_shine", "e-book_reader", "mind_filler_meals", "moisturizer_cream", "motivational_poster", "school", "sunglasses", "veg_in_cart", "vicky_plush", "wool_slippers"]:
                return "dislike"
            if gift_id in ["lipstick", "makeup_kit"]:
                return "hate"

        if char == store.sa:
            if gift_id in ["balls_to_the_face", "beach_blanket", "box_of_chocolates", "cream_pie_maker", "creme_de_la_cream", "dead_wake", "finger_hero", "for_the_win", "fornimate_capsule", "grandma_isabellas_lovely_food", "headphones", "jam_in_the_clam", "jitter_whirler", "juiced_up", "junk_in_the_trunk", "laser_light_projector", "laser_tag_guns", "mall", "must_be_this_tall_to_find_love", "my_ten_frogs", "nate_the_great", "nutbusters", "pajamas", "reflexviz.tv_emoji_stickers", "sleep_mask", "smartphone_case", "stephanie_cosmos", "todd_mosss_crystal_collection", "treats_&_teats", "twist_of_the_wrist"]:
                return "love"
            if gift_id in ["boldest_beef", "breast_chicken_ever", "bromance_of_the_three_bros", "call_of_leotard", "cosplay_cafe", "dorothy_hetero", "hair_comb_pack", "hello_music_my_old_buddy", "hot_sauce_gift_set", "l33t_fr3ak", "little_sausage_pizza", "mama_chef", "movego_action_camera", "movie_gift_card", "pasta_pillar", "pirate_ship_model_kit", "plain_of_spirits", "playground", "ppii_fitness", "rock_and_stone_with_todd_moss", "sam_plush", "sneakers", "spinnin_noodles", "steamborg", "sunglasses", "thick_buns_burger", "veg_in_cart", "wireless_earbuds"]:
                return "like"
            if gift_id in ["curry_cupid", "deep_fish_shine", "dumbell_set", "e-book_reader", "happy_ending_buffet", "seat_cushion_massager", "thermos"]:
                return "dislike"
            if gift_id in ["toolset"]:
                return "hate"

        if char == store.julia:
            if gift_id in ["5_in_1_board_game_set", "a_touch_of_tenderness", "battlefield:_love", "bean_flicker_tacos", "boldest_beef", "bromance_of_the_three_bros", "cosplay_cafe", "curry_cupid", "dead_wake", "deep_fish_shine", "dorothys_daring_dinners", "e-book_reader", "hot_sauce_gift_set", "motivational_poster", "my_ten_frogs", "plain_of_spirits", "sleep_mask", "solder_point", "toolset", "twist_of_the_wrist", "wool_slippers"]:
                return "love"
            if gift_id in ["a_touch_of_tenderness", "box_of_chocolates", "for_the_win", "hair_comb_pack", "headphones", "l33t_fr3ak", "laser_tag_guns", "lipstick", "makeup_kit", "mall", "moisturizer_cream", "movie_gift_card", "munchy_conditions", "neon_yo-yo", "pajamas", "pirate_ship_model_kit", "restaurant_gift_card", "school", "steamborg", "stephanie_cosmos", "the_pen_and_the_sword", "wireless_earbuds", "yoooo!_kais"]:
                return "like"
            if gift_id in ["balls_to_the_face", "dumbell_set", "ppii_fitness", "sneakers", "sunglasses", "thermos", "todd_mosss_crystal_collection", "training_gloves"]:
                return "dislike"

        return "neutral"
