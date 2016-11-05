import copy
import random


class Player(object):
    """
    Abstract Player class containing the necessary attributes
    """

    def __init__(self, name, sign):
        self.__name = name
        self._sign = sign
        self.__score = 0

    @property
    def sign(self):
        return self._sign

    @property
    def score(self):
        return self.__score

    @property
    def name(self):
        return self.__name

    def move(self, board):
        choice = self.choose_action(board)
        board.mark_cell(choice[0], choice[1], self._sign)

    def choose_action(self):
        raise NotImplementedError

    def update_score(self):
        self.__score += 1


class RandomPlayer(Player):
    """
    A Player that bases her choice on pure randomness
    """

    def choose_action(self, board):
        options = board.empty_cells
        return random.choice(options)


class BruteForcePlayer(Player):
    """
    This player analyses all the board content
    and proceeds with the following:
    - block if there is a move that will make the oppenent win
    - take a winning move
    - otherwise just play randomly
    """
    def choose_action(self, board):
        options = board.empty_cells

        # In this game we look for winning possibilities
        for choice in options:
            new_board = copy.deepcopy(board)
            new_board.mark_cell(choice[0], choice[1], self._sign)
            # If a winning cell is found, occupy it
            if new_board.has_winner():
                return choice

        # In this loop we prevent loosing the game
        for choice in options:
            new_board = copy.deepcopy(board)
            new_board.mark_cell(choice[0], choice[1], self._get_oppenent_sign())
            # If a winning cell is found, occupy it
            if new_board.has_winner():
                return choice

        # Otherwise pick randomly
        return random.choice(options)

    def _get_oppenent_sign(self):
        if self.sign == 'X':
            return 'O'
        else:
            return 'X'


class QLearningPlayer(Player):
    """
    A player using Q learning algorithm, temporal
    reinforcement learning method based on mapping
    states to actions and trying to predict the rewards
    """

    def choose_action(self, board):
        pass
