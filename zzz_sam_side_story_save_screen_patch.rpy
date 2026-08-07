init 9999 python:
    def sam_side_story_save_json_callback(data):
        data["sam_side_story_save"] = bool(store.sam_side_story_mode)
        return

    if sam_side_story_save_json_callback not in config.save_json_callbacks:
        config.save_json_callbacks.append(sam_side_story_save_json_callback)


init 999:
    screen file_slots(title):
        default page_name_value = FilePageNameInputValue(pattern = _("Page {}"), auto = _("Automatic saves"), quick = _("Quick saves"))

        use game_menu(title):

            fixed:
                order_reverse True

                button:
                    style "page_label"

                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value

                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5

                            $ slot_time_text = FileTime(slot, format = _("{#file_time}%A, %B %d %Y, %H:%M"), empty = _("empty slot"))
                            if FileJson(slot, "sam_side_story_save", empty = False):
                                $ slot_time_text += " ★"

                            text slot_time_text:
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)

                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()