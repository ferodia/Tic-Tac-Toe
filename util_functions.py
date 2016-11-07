"""
This file contains util functions used by the main
"""
from player import RandomPlayer, StrategyPlayer, HumanPlayer, QLearningPlayer

# Types of players available, to choose from
playersTypes = {
    1: RandomPlayer,
    2: StrategyPlayer,
    3: QLearningPlayer
}


def create_players(names, p_type, user_playing):
    """
    This function creates players based on following criteriq:
    names : associate names to players
    p_type : players type
    user_playing : a boolean indicating whether one of the players is the user
    """
    # Create players
    if user_playing == "y":
        player1 = HumanPlayer(name=names[0], sign='X')
    else:
        player1 = playersTypes[p_type](name=names[0], sign='X')
    player2 = playersTypes[p_type](name=names[1], sign='O')
    return [player1, player2]


def get_winner(players):
    """
    Based on the score print the winner along with his score
    """
    scores = [player.score for player in players]
    max_score = max(scores)
    index = scores.index(max_score)
    print players[index].name, "has won the game with score", max_score
