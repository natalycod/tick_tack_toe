from tick_tack_toe_utils import TickTackToeCells, TickTackToePlayers, TickTackToeStates, Enum_methods

class Field:
    def __init__(self, n):
        self.num = n
        self.win_count = min(n, 5)
        self.field = []
        for i in range(self.num):
            self.field.append([TickTackToeCells.EMPTY] * self.num)
    
    def get_cell(self, x, y):
        if x < 0 or x >= self.num or y < 0 or y >= self.num:
            return TickTackToeCells.NONE
        return self.field[x][y]

    def put_cell(self, x, y, symb):
        self.field[x][y] = symb

    def current_state(self, symb):
        steps = [[1, 0], [0, 1], [1, 1], [1, -1]]
        cnt_empty = 0
        for x in range(self.num):
            for y in range(self.num):
                is_win = False
                if self.get_cell(x, y) == TickTackToeCells.EMPTY:
                    cnt_empty += 1
                    continue
                for i in range(len(steps)):
                    dx, dy = steps[i]
                    cnt = 1
                    while self.get_cell(x + dx * cnt, y + dy * cnt) == self.get_cell(x, y):
                        cnt += 1
                    if cnt >= self.win_count:
                        is_win = True
                        break
                if is_win:
                    if symb == self.get_cell(x, y):
                        return TickTackToeStates.WIN
                    return TickTackToeStates.LOSE
        if cnt_empty == 0:
            return TickTackToeStates.DRAW
        return TickTackToeStates.NOT_ENDED
