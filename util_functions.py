
from player import RandomPlayer, BruteForcePlayer, HumanPlayer, QLearningPlayer


playersTypes = {
    1: RandomPlayer,
    2: BruteForcePlayer,
    3: QLearningPlayer
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