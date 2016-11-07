from unittest import TestCase

from board import Board
from player import RandomPlayer, BruteForcePlayer


class TestPlayer(TestCase):
    def test_name(self):
        player = RandomPlayer(name="Doris", sign='O')
        self.assertEqual(player.name, "Doris")

    def test_score(self):
        player = RandomPlayer(name="Doris", sign='O')
        self.assertEqual(player.score, 0)
        player.update_score()
        self.assertEqual(player.score, 1)


class TestBruteForcePlayer(TestCase):
    def test_winning_move(self):
        board = Board()
        player = BruteForcePlayer(name="Baris", sign='X')
        board.mark_cell(0, 0, 'X')
        board.mark_cell(1, 1, 'X')
        self.assertEqual((2, 2), player.choose_action(board))

    def test_not_loosing_move1(self):
        board = Board()
        player = BruteForcePlayer(name="Jon", sign='O')
        board.mark_cell(0, 0, 'X')
        board.mark_cell(1, 1, 'X')
        self.assertEqual((2, 2), player.choose_action(board))

    def test_not_loosing_move2(self):
        board = Board()
        player = BruteForcePlayer(name="Jon", sign='O')
        board.mark_cell(1, 1, 'X')
        board.mark_cell(2, 1, 'X')
        self.assertEqual((0, 1), player.choose_action(board))
