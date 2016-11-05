from board import Board

class Game(object):

    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.turn = 0
        self.map_to_player = {'X': 0, 'O': 1}

    def _get_player(self, sign):
        index = self.map_to_player[sign]
        return self.players[index]

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
