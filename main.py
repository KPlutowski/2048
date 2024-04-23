import game_board as gm

game_map = gm.GameCore()

while True:

    if game_map.handle_moves(input("type move:")):
        game_map.add_new_cell()
    game_map.print_game_board()
    game_map.check_current_state()
