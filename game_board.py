import random

import numpy as np


class GameCore:
    def __init__(self, game_map_size=4):
        self.game_map = np.zeros(shape=(game_map_size, game_map_size), dtype=np.integer)
        self.game_map_size = game_map_size
        self.score = 0
        self.isWin = False
        self.start_screen()
        self.add_new_cell()
        self.print_game_board()

    def reorganize_map(self):
        # left move only
        changed = False
        for i, row in enumerate(self.game_map):
            position = 0
            for j, cell in enumerate(row):
                if cell != 0:
                    self.game_map[i][position] = cell

                    if position != j:
                        self.game_map[i][j] = 0
                        changed = True
                    position += 1
        return changed

    def merge(self):
        changed = False
        for i in range(4):
            for j in range(3):
                if self.game_map[i][j] == self.game_map[i][j + 1] and self.game_map[i][j] != 0:
                    self.game_map[i][j] = self.game_map[i][j] * 2
                    self.score += self.game_map[i][j]
                    self.game_map[i][j + 1] = 0
                    changed = True
        return changed

    def move_left(self):
        is_reorganized = self.reorganize_map()
        is_merged = self.merge()
        self.reorganize_map()
        return is_reorganized or is_merged

    def move_right(self):
        self.game_map = np.flip(self.game_map)
        change = self.move_left()
        self.game_map = np.flip(self.game_map)
        return change

    def move_up(self):
        self.game_map = np.transpose(self.game_map)
        change = self.move_left()
        self.game_map = np.transpose(self.game_map)
        return change

    def move_down(self):
        self.game_map = np.transpose(self.game_map)
        change = self.move_right()
        self.game_map = np.transpose(self.game_map)
        return change

    def print_game_board(self):
        print(f"score: {self.score}")
        print(self.game_map)

    def add_new_cell(self):
        x = random.randint(0, self.game_map_size - 1)
        y = random.randint(0, self.game_map_size - 1)

        while self.game_map[y][x] != 0:
            x = random.randint(0, self.game_map_size - 1)
            y = random.randint(0, self.game_map_size - 1)

        if random.random() < 0.90:
            self.game_map[y][x] = 2
        else:
            self.game_map[y][x] = 4

    def handle_moves(self, move):
        change = False
        if move.upper() == "A":
            change = self.move_left()
        elif move.upper() == "D":
            change = self.move_right()
        elif move.upper() == "S":
            change = self.move_down()
        elif move.upper() == "W":
            change = self.move_up()
        elif move.upper() == "C":
            exit()
        return change

    def start_screen(self):
        print("'W' : Move Up")
        print("'S' : Move Down")
        print("'A' : Move Left")
        print("'D' : Move Right")
        print("'C' : Exit")

    def win_screen(self):
        print("WIN!!!!!!!!")

        chose = input("you want to continue? [Y/n]")
        if chose.upper() == "Y":
            return 0
        else:
            self.end_screen()

    def end_screen(self):
        print(f"you got {self.score} points")
        exit()

    def lose_screen(self):
        print("GAME OVER!")
        self.end_screen()

    def check_current_state(self):
        # -1 lose
        # 0 still playing
        # 1 win
        if self.isWin == False and 2048 in self.game_map:
            self.isWin = True
            self.win_screen()
        if 0 in self.game_map:
            return 0

        # no zero's and 2048
        # checks possible moves
        for i in range(3):
            for j in range(3):
                if self.game_map[i][j] == self.game_map[i][j + 1] or self.game_map[i][j] == self.game_map[i + 1][j]:
                    return 0
        for j in range(3):
            if self.game_map[3][j] == self.game_map[3][j + 1] or self.game_map[j][3] == self.game_map[j + 1][3]:
                return 0

        self.lose_screen()
        return -1
