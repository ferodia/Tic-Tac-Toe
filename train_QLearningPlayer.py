import pickle

from game import Game
import util_functions

if __name__ == "__main__":

    players = util_functions.create_players(['Qlearner1','Qlearner2'], 3, 'n')

    # Start games
    n = 100000
    for i in range(1, n+1):

        print "Round", i

        # switch players at the beginning of each game for fairness
        players.reverse()

        game = Game(players)
        while not game.is_over():
            game.play()

        pickle.dump(players[0].Qtable, open("Qtable_training-e-greedy.p", "wb"))
