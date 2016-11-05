import random


class Player(object):

    def __init__(self, name, sign):
        self.__name = name
        self._sign = sign
        self.__score = 0

    def update_score(self):
        self.__score += 1

    @property
    def score(self):
        return self.__score

    @property
    def name(self):
        return self.__name

    def move(self, board):
        raise NotImplementedError()


class RandomPlayer(Player):

    def move(self, board):
        options = board.empty_cells
        choice = random.choice(options)
        board.mark_cell(choice[0], choice[1], self._sign)

