from board import Board


class Game(object):
    """"
    Class representing the game instance
    it contains : a board, players, and turn:
    index of the player who's turn to play
    """
    def __init__(self, players):
        self.__board = Board()
        self.__players = players
        self.__turn = 0

    def _get_player(self, sign):
        """
        Finds the player with the associated sign
         'X' or 'O'
        """
        for player in self.__players:
            if player.sign == sign:
                return player

    def is_over(self):
        """
        The game is over if a player has won
        or the board is full
        """
        if self.__board.has_winner():
            winner = self._get_player(self.__board.winner)
            winner.update_score(self.__board)
            print "Winner is", winner.name
            return True
        elif self.__board.is_full():
            print "Board is full, no winner"
            return True

    def play(self):
        """
        method orchestrating the player's turn
        """
        player = self.__players[self.__turn]
        print player.name, "is playing"
        player.move(self.__board)
        self.__board.print_board()
        self.__turn = (self.__turn + 1) % 2
