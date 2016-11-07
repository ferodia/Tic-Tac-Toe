import copy
import random

import pickle


class Player(object):
    """
    Abstract Player class containing the necessary attributes
    """

    def __init__(self, name, sign):
        self.__name = name
        self._sign = sign
        self._score = 0

    @property
    def sign(self):
        return self._sign

    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return self.__name

    def move(self, board):
        choice = self.choose_action(board)
        board.mark_cell(choice[0], choice[1], self._sign)

    def choose_action(self, board):
        raise NotImplementedError

    def update_score(self, board):
        self._score += 1


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
            new_board.mark_cell(choice[0], choice[1], self._get_opponent_sign())
            # If a winning cell is found, occupy it
            if new_board.has_winner():
                return choice

        # Otherwise pick randomly
        return random.choice(options)

    def _get_opponent_sign(self):
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

    def __init__(self, name, sign):
        super(QLearningPlayer, self).__init__(name, sign)
        # Q table maps states to actions
        # the key of table is the state, the value is
        # the list of actions
        #self.Q_table = {}
        self.Q_table = pickle.load(open("Qtable_training.p", "rb"))
        self._old_state = None
        self._old_score = 0
        self.action = None

    @property
    def Qtable(self):
        return self.Q_table

    def choose_action(self, board):

        options = board.empty_cells
        # to allow exploration, have a small probability of a random move
        epsilon = 0.2
        p_random = random.random()
        # if the state is not in the table add it
        if (self.sign, board.state) not in self.Q_table.keys() or p_random < epsilon:
            values = {}
            for option in options:
                values[option] = random.random()
            self.Q_table[(self.sign, board.state)] = values
            self.action = random.choice(options)
        else:
            values = self.Q_table[(self.sign, board.state)]
            action = max(values, key=values.get)
            self.action = action
        return self.action

    def move(self, board):
        self._old_state = board.state
        choice = self.choose_action(board)
        board.mark_cell(choice[0], choice[1], self._sign)

    def update_score(self, board):
        self._score += 1
        # Update as well the Q table with the results
        self.update_Q_table(1, board)

    def update_Q_table(self, reward, board):
        learning_rate = 0.9
        discount = 0.1
        if (self.sign, board.state) in self.Q_table.keys():
            expected = reward + (discount * max(self.Q_table[(self.sign, board.state)]))
        else:
            expected = reward

        actual = self.Q_table[(self.sign, self._old_state)][self.action]
        change = learning_rate * (expected - actual)
        self.Q_table[(self.sign, self._old_state)][self.action] += change


class HumanPlayer(Player):
    """
    Player taking input from user
    """
    def choose_action(self, board):
        i, j = [int(e) for e in
                raw_input("it's your turn: input the coordinates separated by space").split(' ')]
        return i, j
