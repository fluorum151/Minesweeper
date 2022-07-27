from minesweeper import Minesweeper

game = Minesweeper()

while True:
    game.initiate_game()
    while True:
        if game.player_move() == 0:
            print('============================')
            print('        D E F E A T         ')
            print('============================')
            print(game.field.print_field(hide_mines=False))
            break
        if game.check_player_won():
            print('============================')
            print('        W I C T O R Y       ')
            print('============================')
            print(game.field.print_field(hide_mines=False))
            break

    print('Do you want to play again?')
    print('Print N to exit. Anything else will restart the game.')
    answer = input()
    if answer.upper() == 'N':
        break
