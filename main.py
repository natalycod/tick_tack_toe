from tick_tack_toe_utils import TickTackToeCells, TickTackToePlayers, TickTackToeStates
from tick_tack_toe import TickTackToe

def run_game():
    TickTackToe.print_rules()
    print('Hi! What\'s the number of rows you wanna play?')
    num = int(input())
    print('Wanna make first move? (Y/N)')
    player = TickTackToePlayers.COMPUTER
    if (input() == 'Y'):
        player = TickTackToePlayers.USER
    game = TickTackToe(num, player)
    print('Gotcha!')
    game.print_field()

    while (game.get_result(TickTackToeCells.X) == TickTackToeStates.NOT_ENDED):
        if (game.current_player == TickTackToePlayers.USER):
            x, y = map(int, input().split())
            while not game.make_move(x - 1, y - 1):
                print('Sorry, your move is incorrect. Try other cell')
                x, y = map(int, input().split())
            print('Player\'s move:', x, y)
        else:
            x, y = game.find_best_move()
            game.make_move(x - 1, y - 1)
            print('Computer\'s move:', x, y)
        game.print_field()
    
    result = game.get_result(game.user_symbol)
    if result == TickTackToeStates.WIN:
        print('Congratulations! You won!')
    elif result == TickTackToeStates.LOSE:
        print('Sorry, but computer was more clever. Maybe next time?')
    else:
        print('It\'s a draw!')

run_game()
