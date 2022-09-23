from tick_tack_toe_utils import TickTackToeCells, TickTackToePlayers, TickTackToeStates, Enum_methods
from tick_tack_toe_field import Field

class TickTackToe:
    def __init__(self, n, first_player):
        self.field = Field(n)
        self.num = n

        self.current_symbol = TickTackToeCells.X
        self.current_player = first_player
        self.user_symbol = TickTackToeCells.X
        if self.current_player == TickTackToePlayers.COMPUTER:
            self.user_symbol = TickTackToeCells.O

    def print_rules():
        print("There should be rules (there are no rules now)")

    def print_field(self):
        print('Current field:')
        for i in range(self.num):
            for j in range(self.num):
                print(self.field.get_cell(i, j).value, end='')
            print()

    def get_result(self, symb):
        result = self.field.current_state(self.current_symbol)
        if result == TickTackToeStates.LOSE and self.current_symbol != symb:
            return TickTackToeStates.WIN
        return result

    def make_move(self, x, y):
        if self.field.get_cell(x, y) != TickTackToeCells.EMPTY \
                or self.field.current_state(self.current_symbol) != TickTackToeStates.NOT_ENDED:
            return False
        self.field.put_cell(x, y, self.current_symbol)
        self.current_symbol = Enum_methods.next_move_symbol(self.current_symbol)
        self.current_player = Enum_methods.next_player(self.current_player)
        return True

    def minimax_best_move(self, symb):
        result_now = self.field.current_state(symb)
        if (result_now != TickTackToeStates.NOT_ENDED):
            return -1, -1, result_now
        is_draw_possible = False
        draw_x, draw_y = 0, 0
        lose_x, lose_y = 0, 0
        for x in range(self.num):
            for y in range(self.num):
                if self.field.get_cell(x, y) == TickTackToeCells.EMPTY:
                    self.field.put_cell(x, y, symb)
                    x_best, y_best, state = self.minimax_best_move(Enum_methods.next_move_symbol(symb))
                    self.field.put_cell(x, y, TickTackToeCells.EMPTY)
                    state = Enum_methods.opposite_state(state)
                    if state == TickTackToeStates.WIN:
                        return x, y, state
                    elif state == TickTackToeStates.DRAW:
                        draw_x, draw_y = x, y
                        is_draw_possible = True
                    else:
                        lose_x, lose_y = x, y
        if is_draw_possible:
            return draw_x, draw_y, TickTackToeStates.DRAW
        return lose_x, lose_y, TickTackToeStates.LOSE

    def find_best_move(self):
        x, y, state = self.minimax_best_move(self.current_symbol)
        return x + 1, y + 1
