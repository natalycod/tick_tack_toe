from enum import Enum

class TickTackToeCells(Enum):
    X = 'X'
    O = 'O'
    EMPTY = '.'
    NONE = '-'

class TickTackToePlayers(Enum):
    COMPUTER = 'computer'
    USER = 'user'

class TickTackToeStates(Enum):
    DRAW = 0
    WIN = 1
    LOSE = -1
    NOT_ENDED = 100

class Enum_methods(object):
    def next_move_symbol(symb):
        if symb == TickTackToeCells.EMPTY:
            return TickTackToeCells.X
        elif symb == TickTackToeCells.X:
            return TickTackToeCells.O
        return TickTackToeCells.X

    def next_player(player):
        if (player == TickTackToePlayers.COMPUTER):
            return TickTackToePlayers.USER
        return TickTackToePlayers.COMPUTER

    def opposite_state(state):
        if state == TickTackToeStates.WIN:
            return TickTackToeStates.LOSE
        elif state == TickTackToeStates.LOSE:
            return TickTackToeStates.WIN
        return state