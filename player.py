import random


class Player(object):

    def __init__(self, name, sign):
        self.__name = name
        self.sign = sign

    @property
    def name(self):
        return self.__name

    def move(self, board):
        options = board.empty_cells
        choice = random.choice(options)
        board.mark_cell(choice[0],choice[1], self.sign)