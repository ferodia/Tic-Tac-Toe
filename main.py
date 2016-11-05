from random import shuffle
from game import Game
from player import RandomPlayer


def create_players(names):
    # Create players
    player1 = RandomPlayer(name=names[0], sign='X')
    player2 = RandomPlayer(name=names[1], sign='O')
    return [player1, player2]


def get_winner(players):
    scores = [player.score for player in players]
    max_score = max(scores)
    index = scores.index(max_score)
    print players[index].name, "has won the game with score", max_score


if __name__ == "__main__":

    print "Welcome to Tic Tac Toe"

    # Gathering inputs
    n = int(raw_input("How many rounds you wish to play ?\n"))
    input_names = raw_input("Enter names of the two players, separated by space :\n").split(' ')

    # Creating players
    players = create_players(input_names)

    # Start games
    for i in range(1, n+1):

        print "Round", i

        # shuffle players for fairness
        shuffle(players)
        print "after shuffle player", players[0].name, "is starting"

        game = Game(players)
        while not game.is_over():
            game.play()

    # Decide the winner
    get_winner(players)

    print "Goodbye"
