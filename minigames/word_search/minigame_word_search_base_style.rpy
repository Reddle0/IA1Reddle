init python:

    class Word_Search_Displayable(renpy.Displayable):

        def __init__(self, words, size, directions, **kwargs):
            renpy.Displayable.__init__(self)

            self.rows = size
            self.cols = size
            self.cell_size = 60
            self.directions = directions

            self.grid_x = 60
            self.grid_y = 150
            self.panel_padding = 16
            self.tile_gap = 4
            grid_pixel_width = self.cols * self.cell_size
            grid_pixel_height = self.rows * self.cell_size

            self.side_x = self.grid_x + grid_pixel_width + 60
            self.side_width = 360
            self.side_inset = 18
            self.word_list_height = 430
            self.word_list_line_height = 44
            self.stats_height = 90
            self.stats_line_height = 40

            self.board_width = self.side_x + self.side_width + 40
            self.board_height = self.grid_y + grid_pixel_height + 60

            self.board_color = "#0f1220"
            self.panel_color = "#181d30"
            self.tile_color = "#242c44"

            self.title_text = "Word Search"
            self.title_size = 52
            self.title_color = "#ffffff"
            self.title_y = 34

            self.instruction_size = 28
            self.instruction_color = "#c9cfe0"
            self.instruction_y = 100

            self.letter_size = 38
            self.letter_color = "#ffffff"

            self.word_list_heading_size = 38
            self.word_list_heading_color = "#ffffff"
            self.word_list_size = 30
            self.word_list_color = "#e8e8f0"
            self.word_list_found_color = "#7ce0a0"

            self.stats_size = 30
            self.stats_color = "#ffffff"

            self.stroke_thickness = 16
            self.stroke_end_trim = 8
            self.found_stroke_color = "#ffe37a"
            self.preview_stroke_color = "#9ed4ff"
            self.found_stroke_alpha = 0.8
            self.preview_stroke_alpha = 0.7

            self.words = []
            for raw_word in words:
                self.words.append(raw_word.upper().replace(" ", ""))

            self.select_start = None
            self.select_end = None
            self.found_words = []
            self.found_paths = []

            self.letter_images = {}
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                self.letter_images[letter] = Text(letter, size = self.letter_size, color = self.letter_color)

            self.grid = None
            self.build_grid()

        def blank_grid(self):
            grid = []
            for row in range(0, self.rows):
                grid.append([" "] * self.cols)
            return grid

        def place_one_word(self, grid, word):
            length = len(word)

            spot_attempt = 0
            while spot_attempt < 300:
                spot_attempt = spot_attempt + 1

                direction = random.choice(self.directions)
                row_step = direction[0]
                col_step = direction[1]

                start_row = random.randint(0, self.rows - 1)
                start_col = random.randint(0, self.cols - 1)

                end_row = start_row + row_step * (length - 1)
                end_col = start_col + col_step * (length - 1)

                if end_row < 0 or end_row > self.rows - 1:
                    continue
                if end_col < 0 or end_col > self.cols - 1:
                    continue

                spot_is_clear = True
                for step in range(0, length):
                    r = start_row + row_step * step
                    c = start_col + col_step * step
                    letter_here = grid[r][c]
                    if letter_here != " " and letter_here != word[step]:
                        spot_is_clear = False
                        break

                if not spot_is_clear:
                    continue

                for step in range(0, length):
                    r = start_row + row_step * step
                    c = start_col + col_step * step
                    grid[r][c] = word[step]
                return True

            return False

        def fill_blanks(self, grid):
            for r in range(0, self.rows):
                for c in range(0, self.cols):
                    if grid[r][c] == " ":
                        grid[r][c] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            return

        def build_grid(self):
            board_attempt = 0
            grid = self.blank_grid()
            while board_attempt < 50:
                board_attempt = board_attempt + 1
                grid = self.blank_grid()

                placed_every_word = True
                for word in self.words:
                    if not self.place_one_word(grid, word):
                        placed_every_word = False
                        break

                if placed_every_word:
                    self.fill_blanks(grid)
                    self.grid = grid
                    return

            self.fill_blanks(grid)
            self.grid = grid
            return

        def sign(self, number):
            if number > 0:
                return 1
            if number < 0:
                return -1
            return 0

        def cell_at(self, x, y):
            if x < self.grid_x or y < self.grid_y:
                return None
            col = int((x - self.grid_x) // self.cell_size)
            row = int((y - self.grid_y) // self.cell_size)
            if row < 0 or row > self.rows - 1:
                return None
            if col < 0 or col > self.cols - 1:
                return None
            return (row, col)

        def snap_to_line(self, start, current):
            start_row = start[0]
            start_col = start[1]
            row_diff = current[0] - start_row
            col_diff = current[1] - start_col

            if row_diff == 0 and col_diff == 0:
                return start

            up_down = abs(row_diff)
            left_right = abs(col_diff)

            if up_down > left_right * 2:
                row_step = self.sign(row_diff)
                col_step = 0
                length = up_down
            elif left_right > up_down * 2:
                row_step = 0
                col_step = self.sign(col_diff)
                length = left_right
            else:
                row_step = self.sign(row_diff)
                col_step = self.sign(col_diff)
                length = max(up_down, left_right)

            while length > 0:
                end_row = start_row + row_step * length
                end_col = start_col + col_step * length
                on_board = end_row >= 0 and end_row <= self.rows - 1 and end_col >= 0 and end_col <= self.cols - 1
                if on_board:
                    return (end_row, end_col)
                length = length - 1

            return start

        def cells_between(self, start, end):
            row_step = self.sign(end[0] - start[0])
            col_step = self.sign(end[1] - start[1])
            steps = max(abs(end[0] - start[0]), abs(end[1] - start[1]))

            cells = []
            for step in range(0, steps + 1):
                cells.append((start[0] + row_step * step, start[1] + col_step * step))
            return cells

        def letters_along(self, cells):
            word = ""
            for cell in cells:
                word = word + self.grid[cell[0]][cell[1]]
            return word

        def check_selection(self):
            cells = self.cells_between(self.select_start, self.select_end)

            if len(cells) < 2:
                return

            spelled = self.letters_along(cells)
            spelled_backwards = spelled[::-1]

            for word in self.words:
                if word not in self.found_words:
                    if word == spelled or word == spelled_backwards:
                        self.found_words.append(word)
                        self.found_paths.append(cells)
                        return
            return

        def instruction_string(self):
            if self.select_start:
                return "Drag through the word, then release on the last letter."
            return "Click and drag a straight line through each hidden word."

        def stroke_for_cells(self, board, cells, color, alpha, st, at):
            if len(cells) < 2:
                return

            first_cell = cells[0]
            last_cell = cells[-1]

            first_x = self.grid_x + first_cell[1] * self.cell_size + self.cell_size / 2.0
            first_y = self.grid_y + first_cell[0] * self.cell_size + self.cell_size / 2.0
            last_x = self.grid_x + last_cell[1] * self.cell_size + self.cell_size / 2.0
            last_y = self.grid_y + last_cell[0] * self.cell_size + self.cell_size / 2.0

            across = last_x - first_x
            down = last_y - first_y
            gap_length = math.hypot(across, down)

            bar_length = int(gap_length + self.cell_size - self.stroke_end_trim)
            angle = math.degrees(math.atan2(down, across))

            flat_bar = Solid(color, xysize = (bar_length, self.stroke_thickness))
            angled_bar = Transform(child = flat_bar, rotate = angle, rotate_pad = True, xanchor = 0.5, yanchor = 0.5, alpha = alpha)
            angled_render = renpy.render(angled_bar, self.board_width, self.board_height, st, at)

            angled_width = angled_render.get_size()[0]
            angled_height = angled_render.get_size()[1]
            middle_x = (first_x + last_x) / 2.0
            middle_y = (first_y + last_y) / 2.0
            board.blit(angled_render, (int(middle_x - angled_width / 2.0), int(middle_y - angled_height / 2.0)))
            return

        def draw_word_list(self, board, st, at):
            board.blit(renpy.render(Solid(self.panel_color), self.side_width, self.word_list_height, st, at), (self.side_x, self.grid_y))

            x = self.side_x + self.side_inset
            y = self.grid_y + self.side_inset

            heading = Text("Words", size = self.word_list_heading_size, color = self.word_list_heading_color)
            board.blit(renpy.render(heading, self.side_width, 60, st, at), (x, y))
            y = y + self.word_list_line_height + 10

            for word in self.words:
                if word in self.found_words:
                    shown = Text("FOUND - " + word, size = self.word_list_size, color = self.word_list_found_color)
                else:
                    shown = Text(word, size = self.word_list_size, color = self.word_list_color)
                board.blit(renpy.render(shown, self.side_width, self.word_list_line_height, st, at), (x, y))
                y = y + self.word_list_line_height
            return

        def draw_stats(self, board, st, at):
            stats_top = self.grid_y + self.word_list_height + 20
            board.blit(renpy.render(Solid(self.panel_color), self.side_width, self.stats_height, st, at), (self.side_x, stats_top))

            x = self.side_x + self.side_inset
            y = stats_top + self.side_inset

            progress_line = "Found: " + str(len(self.found_words)) + " / " + str(len(self.words))
            shown = Text(progress_line, size = self.stats_size, color = self.stats_color)
            board.blit(renpy.render(shown, self.side_width, self.stats_line_height, st, at), (x, y))
            return

        def render(self, width, height, st, at):
            board = renpy.Render(self.board_width, self.board_height)

            board.blit(renpy.render(Solid(self.board_color), self.board_width, self.board_height, st, at), (0, 0))

            panel_left = self.grid_x - self.panel_padding
            panel_top = self.grid_y - self.panel_padding
            panel_size = self.cols * self.cell_size + self.panel_padding * 2
            board.blit(renpy.render(Solid(self.panel_color), panel_size, panel_size, st, at), (panel_left, panel_top))

            tile_size = self.cell_size - self.tile_gap * 2
            tile_render = renpy.render(Solid(self.tile_color), tile_size, tile_size, st, at)
            for r in range(0, self.rows):
                for c in range(0, self.cols):
                    tile_left = self.grid_x + c * self.cell_size + self.tile_gap
                    tile_top = self.grid_y + r * self.cell_size + self.tile_gap
                    board.blit(tile_render, (tile_left, tile_top))

            for cells in self.found_paths:
                self.stroke_for_cells(board, cells, self.found_stroke_color, self.found_stroke_alpha, st, at)

            if self.select_start and self.select_end:
                dragging_cells = self.cells_between(self.select_start, self.select_end)
                self.stroke_for_cells(board, dragging_cells, self.preview_stroke_color, self.preview_stroke_alpha, st, at)

            for r in range(0, self.rows):
                for c in range(0, self.cols):
                    letter_render = renpy.render(self.letter_images[self.grid[r][c]], self.cell_size, self.cell_size, st, at)
                    letter_width = letter_render.get_size()[0]
                    letter_height = letter_render.get_size()[1]
                    cell_left = self.grid_x + c * self.cell_size
                    cell_top = self.grid_y + r * self.cell_size
                    letter_x = cell_left + (self.cell_size - letter_width) // 2
                    letter_y = cell_top + (self.cell_size - letter_height) // 2
                    board.blit(letter_render, (letter_x, letter_y))

            title = Text(self.title_text, size = self.title_size, color = self.title_color)
            title_render = renpy.render(title, self.board_width, self.title_size + 20, st, at)
            title_width = title_render.get_size()[0]
            board.blit(title_render, ((self.board_width - title_width) // 2, self.title_y))

            instruction = Text(self.instruction_string(), size = self.instruction_size, color = self.instruction_color)
            instruction_render = renpy.render(instruction, self.board_width, self.instruction_size + 20, st, at)
            instruction_width = instruction_render.get_size()[0]
            board.blit(instruction_render, ((self.board_width - instruction_width) // 2, self.instruction_y))

            self.draw_word_list(board, st, at)
            self.draw_stats(board, st, at)

            return board

        def event(self, ev, x, y, st):
            import pygame

            if store.minigame_word_search_disable_interaction:
                return

            cell = self.cell_at(x, y)

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if cell:
                    self.select_start = cell
                    self.select_end = cell
                    renpy.redraw(self, 0)
                return

            if ev.type == pygame.MOUSEMOTION and self.select_start:
                if cell:
                    self.select_end = self.snap_to_line(self.select_start, cell)
                    renpy.redraw(self, 0)
                return

            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                if self.select_start and self.select_end:
                    self.check_selection()
                self.select_start = None
                self.select_end = None
                renpy.redraw(self, 0)
                if len(self.found_words) >= len(self.words):
                    renpy.call("minigame_word_search_win")
                return

            return

    def minigame_word_search_word_pool():
        words = []
        words.append("BOOK")
        words.append("NOVEL")
        words.append("STORY")
        words.append("PAGES")
        words.append("READER")
        words.append("CHAPTER")
        words.append("LIBRARY")
        words.append("FANTASY")
        words.append("WIZARD")
        words.append("DRAGON")
        words.append("QUEST")
        words.append("LEGEND")
        words.append("KINGDOM")
        words.append("PROLOGUE")
        
        return words

screen word_search_screen:
    add minigame_word_search_puzzle:
        xalign 0.5
        yalign 0.5

    if not minigame_word_search_disable_interaction:
        textbutton "Give Up" action Jump("minigame_word_search_too_slow") xalign 0.99 yalign 0.99

label minigame_word_search(partner = None):
    call process_scene_beginning
    call minigame_word_search_intro(partner)
    call minigame_word_search_initialize
    call minigame_word_search_begin

    return

label minigame_word_search_initialize:
    python:
        if minigame_word_search_difficulty == "easy":
            minigame_word_search_size = 10
            minigame_word_search_word_count = 5
            minigame_word_search_directions = [ (0, 1), (1, 0) ]
            minigame_word_search_time_limit = False
        elif minigame_word_search_difficulty == "medium":
            minigame_word_search_size = 11
            minigame_word_search_word_count = 6
            minigame_word_search_directions = [ (0, 1), (1, 0), (1, 1) ]
            minigame_word_search_time_limit = True
            minigame_countdown_duration = 300
        else:
            minigame_word_search_size = 12
            minigame_word_search_word_count = 8
            minigame_word_search_directions = [ (0, 1), (1, 0), (1, 1), (-1, 1) ]
            minigame_word_search_time_limit = True
            minigame_countdown_duration = 600

        #if config.developer:
        #    minigame_word_search_word_count = 2
        #    minigame_word_search_time_limit = False

        minigame_word_search_disable_interaction = False

        minigame_word_search_words = minigame_word_search_word_pool()
        random.shuffle(minigame_word_search_words)
        minigame_word_search_words = minigame_word_search_words[:minigame_word_search_word_count]

        minigame_word_search_puzzle = Word_Search_Displayable(minigame_word_search_words, minigame_word_search_size, minigame_word_search_directions)

    return

label minigame_word_search_begin:
    $ quick_menu = False
    call bust_art_background("bg black")
    pause 0.5

    show screen word_search_screen
    with Dissolve(0.75)
    $ quick_menu = True

    if minigame_word_search_time_limit:
        call minigame_countdown(minigame_countdown_duration, "minigame_word_search_too_slow")

    call screen hard_block_screen

    return

label minigame_word_search_intro(partner = None):
    $ no_bust_art = False

    if config.developer and 1 == 2:
        "DEBUG/DEVELOPER MODE: Reduced difficulty."

    if partner:
        $ minigame_word_search_partner = partner
    else:
        $ minigame_word_search_partner = julia

    if minigame_word_search_partner == julia:
        $ diceroll = random.randint(1, 3)

        if diceroll == 1:
            $ display_multiple_characters([ (n, ""), (julia, "pose handface face neutral blush false") ], reset = True)
            call process_character(julia, appearance = "pose handface face neutral blush false", text = "I found one of these word search puzzles tucked in the back of a magazine.")
            call process_character(julia, appearance = "pose handface face neutral blush false", text = "Care to see how many words you can dig out?")
        elif diceroll == 2:
            $ display_multiple_characters([ (n, ""), (julia, "pose handup face happy blush false") ], reset = True)
            call process_character(julia, appearance = "pose handup face happy blush false", text = "There are words hiding all through this grid, [n.say_name].")
        else:
            $ display_multiple_characters([ (n, ""), (julia, "pose handup face neutral blush false") ], reset = True)
            call process_character(julia, appearance = "pose handup face neutral blush false", text = "I always keep a word puzzle handy for between chapters.")

    window hide
    menu:
        "Easy":
            $ minigame_word_search_difficulty = "easy"
        "Medium (Boldness Opportunity!)":
            $ minigame_word_search_difficulty = "medium"
        "Hard (Boldness Opportunity!)":
            $ minigame_word_search_difficulty = "hard"

    if minigame_word_search_partner == julia:
        if minigame_word_search_difficulty == "easy":
            call process_character(julia, appearance = "pose handface face neutral blush false", text = "A gentle grid to warm up on.")
        elif minigame_word_search_difficulty == "medium":
            call process_character(julia, appearance = "pose handup face neutral blush false", text = "A few more words this time, and they hide a little better.")
        else:
            call process_character(julia, appearance = "pose armcross face neutral blush false", text = "This one will really test your vocabulary.")

    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()

    return

label minigame_word_search_win:
    $ minigame_word_search_disable_interaction = True
    call hide_minigame_countdown
    pause 1.0
    hide screen word_search_screen
    hide screen hard_block_screen

    if minigame_word_search_difficulty == "easy":
        $ minigame_word_search_win_money = 4
    elif minigame_word_search_difficulty == "medium":
        $ minigame_word_search_win_money = 6
    else:
        $ minigame_word_search_win_money = 8

    $ renpy.pause(0.25)
    if minigame_word_search_partner == julia:
        if minigame_word_search_difficulty == "easy":
            $ display_multiple_characters([ (n, ""), (julia, "pose handup face happy blush false") ], reset = True)
            $ julia.add_points(2, minigame = True)
            call process_character(julia, appearance = "pose handup face happy blush false", text = "There they all are! Nicely spotted.")
        elif minigame_word_search_difficulty == "medium":
            $ display_multiple_characters([ (n, ""), (julia, "pose armcross face happy blush false") ], reset = True)
            call add_points_and_boldness(julia, 3, 1, minigame = True)
            call process_character(julia, appearance = "pose armcross face happy blush false", text = "You've got a sharp eye for this, [n.say_name]!")
        else:
            $ display_multiple_characters([ (n, ""), (julia, "pose handup face happy blush false") ], reset = True)
            call add_points_and_boldness(julia, 4, 1, minigame = True)
            call process_character(julia, appearance = "pose handup face happy blush false", text = "Not one word slipped past you. Very impressive!")

    show screen hud
    python hide:
        inventory.add_money(minigame_word_search_win_money, minigame = True)
        narrator("Got $" + str(minigame_word_search_win_money) + " for winning.")

    call minigame_word_search_end

    return

label minigame_word_search_too_slow:
    $ minigame_word_search_disable_interaction = True
    call hide_minigame_countdown
    pause 1.0
    hide screen word_search_screen
    hide screen hard_block_screen

    if minigame_word_search_partner == julia:
        if minigame_word_search_difficulty == "easy":
            $ display_multiple_characters([ (n, "face curious"), (julia, "pose handface face concerned blush false") ])
            call process_character(julia, appearance = "pose handface face concerned blush false", text = "Some of them are sneaky. We can always try again.")
        else:
            $ display_multiple_characters([ (n, "face curious"), (julia, "pose armcross face neutral blush false") ])
            call process_character(julia, appearance = "pose armcross face neutral blush false", text = "Time got away from us. They do get trickier.")

    call minigame_word_search_end

    return

label minigame_word_search_end:
    $ renpy.scene('screens')
    $ minigame_word_search_puzzle = None

    $ enable_saving()
    $ renpy.block_rollback()
    $ enable_rollback()

    call process_end_of_minigame("minigame_word_search")

    return

init 1 python:
    julia_available_minigames_original = Julia.available_minigames

    def julia_available_minigames_with_word_search(self):
        minigame_call_labels = julia_available_minigames_original(self)
        if "minigame_word_search" not in minigame_call_labels:
            minigame_call_labels.append("minigame_word_search")
        return minigame_call_labels

    Julia.available_minigames = julia_available_minigames_with_word_search

    minigame_option_label_original = IA_Actor.minigame_option_label

    def minigame_option_label_with_word_search(self, call_label):
        if call_label == "minigame_word_search":
            return "Word Search Minigame"
        return minigame_option_label_original(self, call_label)

    IA_Actor.minigame_option_label = minigame_option_label_with_word_search
