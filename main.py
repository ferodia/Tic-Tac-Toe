from random import shuffle
from game import Game
from player import RandomPlayer, BruteForcePlayer, HumanPlayer

playersTypes = {
    1: RandomPlayer,
    2: BruteForcePlayer
}


def create_players(names, p_type, user_playing):
    # Create players
    if user_playing == "y":
        player1 = HumanPlayer(name=names[0], sign='X')
    else:
        player1 = playersTypes[p_type](name=names[0], sign='X')
    player2 = playersTypes[p_type](name=names[1], sign='O')
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

    # Choose to play with user, or let computer plays with itself
    reply = raw_input("Do you want to play ?\n (y/n)")

    # Creating players
    player_type = int(raw_input("what kind of players you choose ? (1 for random 2 for bruteforce)\n"))

    players = create_players(input_names, player_type, reply)

    # Start games
    for i in range(1, n+1):

        print "Round", i

        # switch players at the beginning of each game for fairness
        players.reverse()
        print players[0].name, "is starting"

        game = Game(players)
        while not game.is_over():
            game.play()

    # Decide the winner
    get_winner(players)

    print "Goodbye"
