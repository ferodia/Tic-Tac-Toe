from board import Board

class Game(object):

    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.turn = 0

    def _get_player(self, sign):
        for player in self.players:
            if player.sign == sign:
                return player

    def is_over(self):
        if self.board.has_winner():
            winner = self._get_player(self.board.winner)
            winner.update_score()
            print "Winner is", winner.name
            return True
        elif self.board.is_full():
            print "Board is full, no winner"
            return True

    def play(self):

        player = self.players[self.turn]
        print player.name, "is playing"
        player.move(self.board)
        self.board.print_board()
        self.turn = (self.turn + 1) % 2
