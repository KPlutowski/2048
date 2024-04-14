import game_board as gm

game_map = gm.start_game()
while True:
    gm.add_new_cell(game_map)
    gm.print_game_board(game_map)
    move = input("aaaa:")
    if move.upper()=="A":
        gm.move_left(game_map)
    elif move.upper()=="D":
        # gm.move_right(game_map)
