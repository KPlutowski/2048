import random


def print_game_board(game_map):
    for row in game_map:
        print(row)


def add_new_cell(game_map):
    x = random.randint(0, len(game_map) - 1)
    y = random.randint(0, len(game_map) - 1)

    while game_map[y][x] != 0:
        x = random.randint(0, len(game_map) - 1)
        y = random.randint(0, len(game_map) - 1)
    game_map[y][x] = 2


def start_game():
    board_size = 4
    game_board = []
    for i in range(board_size):
        game_board.append([0] * board_size)
    return game_board


def move_left(game_map):
    for row in game_map:
        for k in range(1, len(game_map)):
            was_merged = False
            for i in range(k, 0, -1):
                if row[i - 1] == row[i] and was_merged is False:
                    row[i - 1] += row[i]
                    row[i] = 0
                    was_merged = True
                elif row[i - 1] == 0:
                    row[i - 1] += row[i]
                    row[i] = 0


