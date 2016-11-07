import pickle

import util_functions
from game import Game

if __name__ == "__main__":
    """
    This script's aim is to train the Q learning player but
    making two players play with each other
    the number of rounds is fixed, then at the end the Q table
    learned during the game is recorded and serialized thanks to
    Python package Pickle.
    This learned table is used by the player during a game
    """

    players = util_functions.create_players(['Qlearner1', 'Qlearner2'], 3, 'n')

    # Start games
    n = 50000
    for i in range(1, n + 1):

        print "Round", i

        # switch players at the beginning of each game for fairness
        players.reverse()

        game = Game(players)
        while not game.is_over():
            game.play()

        pickle.dump(players[0].Qtable, open("Qtable_training-e-greedy.p", "wb"))
