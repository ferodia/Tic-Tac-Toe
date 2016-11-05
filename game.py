from board import Board
from player import Player


class Game(object):

    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = 0
        self.map_to_player = {'X': player1, 'O': player2}

    def is_over(self):
        if self.board.has_winner():
            print "Winner is ", self.map_to_player[self.board.winner].name
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


if __name__ == "__main__":

    print "Welcome to Tic Tac Toe"
    n = int(raw_input("How many games you wish to play ?"))

    # players
    player1 = Player(name="mannino", sign='X')
    player2 = Player(name="mannina", sign='O')

    for i in range(n):
        print "Starting a game"
        game = Game(player1, player2)
        while not game.is_over():
            game.play()

    print "Goodbye"
