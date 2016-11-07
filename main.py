from game import Game
from util_functions import create_players, get_winner

if __name__ == "__main__":

    print "Welcome to Tic Tac Toe"

    # Gathering inputs
    n = int(raw_input("How many rounds you wish to play ?\n"))
    input_names = raw_input("Enter names of the two players, separated by space :\n").split(' ')

    # Choose to play with user, or let computer plays with itself
    reply = raw_input("Do you want to play ?\n (y/n)")

    # Creating players
    player_type = \
        int(raw_input("what kind of players you choose ? (1 for random 2 for bruteforce 3 for QlearningPlayer)\n"))

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
