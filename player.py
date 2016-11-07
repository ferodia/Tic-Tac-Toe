import copy
import pickle
import random


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
        """
        The steps of the move are:
        Choosing an action
        the child class
        and fill the cell
        """
        choice = self.choose_action(board)
        board.mark_cell(choice[0], choice[1], self._sign)

    def choose_action(self, board):
        """
        Choosing coordinated in the board to play
        Should be implemented by the child class
        """
        raise NotImplementedError

    def update_score(self, board):
        """
        This method  inscrements the score
        """
        self._score += 1


class RandomPlayer(Player):
    """
    A Player that bases her choice on pure randomness
    """

    def choose_action(self, board):
        options = board.empty_cells
        return random.choice(options)


class StrategyPlayer(Player):
    """
    This player analyses all the board content
    and proceeds with the following:
    - block if there is a move that will make the oppenent win
    - take a winning move
    - otherwise just play randomly
    """

    def choose_action(self, board):
        """
        Follwoing the algorithm in the description, an action is chosen
        returns coordinates of the cell in the board
        """
        options = board.empty_cells

        # In this game we look for winning possibilities
        for choice in options:
            # For each option play the option,
            # and observe the outcome
            new_board = copy.deepcopy(board)
            new_board.mark_cell(choice[0], choice[1], self._sign)
            # If a winning cell is found, occupy it
            if new_board.has_winner():
                return choice

        # In this loop we prevent loosing the game
        for choice in options:
            # For each option play the option,
            # and observe the outcome
            new_board = copy.deepcopy(board)
            new_board.mark_cell(choice[0], choice[1], self._get_opponent_sign())
            # If an opponent has a winning cell occupy it
            if new_board.has_winner():
                return choice

        # Otherwise pick randomly
        return random.choice(options)

    def _get_opponent_sign(self):
        """
        get the sign of the opponent
        """
        if self.sign == 'X':
            return 'O'
        else:
            return 'X'


class QLearningPlayer(Player):
    """
    A player using Q learning algorithm, temporal
    reinforcement learning method based on mapping
    states to actions and trying to predict the rewards
    - Q table maps states to actions
    - the key of table is the state, the value is
    the list of actions
    - Exploration is insured with a probability epsilon
    However when the player has learned enough, the value is
    decreased slowly to decrement random behavior
    """

    def __init__(self, name, sign):
        super(QLearningPlayer, self).__init__(name, sign)

        self.Q_table = pickle.load(open("Qtable_training.p", "rb"))
        self._old_state = None
        self._old_score = 0
        self.action = None
        self.epsilon = 0.2

    @property
    def Qtable(self):
        """
        return table
        """
        return self.Q_table

    def choose_action(self, board):
        """
        Choosing an optimised action from the Q table,
        or explore and play random (for a small probability)
        """
        options = board.empty_cells
        # to allow exploration, have a small probability of a random move
        p_random = random.random()
        # if the state is not in the table add it
        if (self.sign, board.state) not in self.Q_table.keys() or p_random < self.epsilon:
            values = {}
            for option in options:
                values[option] = random.random()
            self.Q_table[(self.sign, board.state)] = values
            self.action = random.choice(options)
        else:
            values = self.Q_table[(self.sign, board.state)]
            action = max(values, key=values.get)
            self.action = action

        # decrease exploration after each action
        if self.epsilon > 0:
            self.epsilon -= 0.0001

        return self.action

    def move(self, board):
        """

        :param board:
        :return:
        """
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
