from tick_tack_toe_field import Field
from tick_tack_toe import TickTackToe
from random import randrange
from tick_tack_toe_utils import TickTackToeCells, TickTackToePlayers, TickTackToeStates, Enum_methods

class Generator:
    def gen_win_field(n, symb):
        print('There is no generator here')

    def gen_draw_field(n, symb):
        print('There is no generator here')

    def gen_not_ended_field(n, symb):
        print('There is no generator here')

class FieldTests:
    def gen_rand_field():
        n = randrange(8) + 3
        return Field(n)

    def init_test():
        n = randrange(8) + 3
        f = Field(n)
        assert f.num == n, 'Size of field should be equal to argument N'
        assert f.win_count == min(n, 5), 'With n = ' + str(n) + ' win_count should be equal ' + str(min(n, 5))
        assert len(f.field) == n, 'Field should have size NxN'
        for x in range(n):
            assert len(f.field[x]) == n, 'Field should have size NxN'
            for y in range(n):
                assert f.field[x][y] == TickTackToeCells.EMPTY, 'All field cell should be marked as empty'
    def get_cell_test():
        n = randrange(8) + 3
        f = Field(n)
        states = [TickTackToeCells.X, TickTackToeCells.O, TickTackToeCells.EMPTY]
        for i in range(10000):
            x = randrange(n)
            y = randrange(n)
            state = states[randrange(3)]
            f.field[x][y] = state
            assert f.get_cell(x, y) == state, 'get_cell should return cell value'

    def put_cell_test():
        n = randrange(8) + 3
        f = Field(n)
        states = [TickTackToeCells.X, TickTackToeCells.O, TickTackToeCells.EMPTY]
        for i in range(10000):
            x = randrange(n)
            y = randrange(n)
            state = states[randrange(3)]
            f.put_cell(x, y, state)
            assert f.field[x][y] == state, 'put_cell should put value to cell'

    def current_state_test():
        print('no test here, sorry :(')
        # there should be test

class TickTackToeTests:
    def init_test():
        players = [TickTackToePlayers.COMPUTER, TickTackToePlayers.USER]
        player = players[randrange(2)]
        n = randrange(8) + 3
        game = TickTackToe(n, player)
        assert game.num == n, 'Number of rows in game should be equal to given N'
        assert game.current_symbol == TickTackToeCells.X, 'First symbol should be X'
        assert game.current_player == player, 'First player should be equal to given in arguments'
        if player == TickTackToePlayers.USER:
            assert game.user_symbol == TickTackToeCells.X, 'User should have X symbol'
        else:
            assert game.user_symbol == TickTackToeCells.O, 'User should have O symbol'

    def get_result_test():
        print('no test here, sorry :(')
        # there should be test

    def make_move_test():
        players = [TickTackToePlayers.COMPUTER, TickTackToePlayers.USER]
        player = players[randrange(2)]
        n = randrange(8) + 3
        game = TickTackToe(n, player)
        game.field = Generator.gen_draw_field(n)
        for x in range(n):
            for y in range(n):
                assert not game.make_move(x, y), 'Nobody should be able to make moves in ended game'
        game.field = Generator.gen_win_field(n, TickTackToeCells.X)
        for x in range(n):
            for y in range(n):
                assert not game.make_move(x, y), 'Nobody should be able to make moves in ended game'
        game.field = Generator.gen_win_field(n, TickTackToeCells.O)
        for x in range(n):
            for y in range(n):
                assert not game.make_move(x, y), 'Nobody should be able to make moves in ended game'
        game.field = Generator.gen_not_ended_field(n)
        for x in range(n):
            for y in range(n):
                if game.field[x][y] == TickTackToeCells.EMPTY:
                    assert game.make_move(x, y),\
                         'There should be a possibility to make a move to an empty cell'
                    assert game.field[x][y] == Enum_methods.next_player(game.current_player)

                else:
                    assert not game.make_move(x, y),\
                         'Nobody should be able to make a move to not empty cell'

        print('no test here, sorry :(')
        # there should be test

    def minimax_best_move_test():
        print('no test here, sorry :(')
        # there should be test

    def find_best_move_test():
        print('no test here, sorry :(')
        # there should be test

#test Field class
for i in range(1000):
    FieldTests.init_test()
    FieldTests.get_cell_test()
    FieldTests.put_cell_test()
