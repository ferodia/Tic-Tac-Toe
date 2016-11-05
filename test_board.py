from unittest import TestCase

from board import Board


class TestBoard(TestCase):

    def test_mark_cell(self):
        board = Board()
        n = 3
        self.assertFalse(board.is_full())
        board.mark_cell(1, 1, "X")
        board.mark_cell(1, 0, "O")

    def test_invalid_mark_cell(self):
        board = Board()
        board.mark_cell(1, 1, "X")
        with self.assertRaises(IndexError):
            board.mark_cell(1, 1, "O")

    def test_has_winner_true(self):
        board = Board()
        n = 3
        self.assertFalse(board.has_winner())
        for i in range(n):
            board.mark_cell(i, i, "O")
        self.assertTrue(board.has_winner())
        self.assertEqual(board.winner, "O")

    def test_has_winner_false(self):
        board = Board()
        self.assertFalse(board.has_winner())
        board.mark_cell(0, 1, "X")
        board.mark_cell(1, 1, "0")
        board.mark_cell(2, 1, "X")
        self.assertFalse(board.has_winner())

    def test__check_verticals(self):
        board = Board()
        self.assertFalse(board._check_verticals())
        board.mark_cell(0, 1, "X")
        board.mark_cell(1, 1, "X")
        board.mark_cell(2, 1, "X")
        self.assertTrue(board._check_verticals())

    def test__check_horizontals(self):
        board = Board()
        self.assertFalse(board._check_horizontals())
        board.mark_cell(0, 0, "X")
        board.mark_cell(0, 1, "X")
        board.mark_cell(0, 2, "X")
        self.assertTrue(board._check_horizontals())

    def test__check_diagonals(self):
        board = Board()
        self.assertFalse(board._check_diagonals())
        board.mark_cell(0, 0, "X")
        board.mark_cell(1, 1, "X")
        board.mark_cell(2, 2, "X")
        self.assertTrue(board._check_diagonals())

    def test__check_row(self):
        row = ['', 'X', 'O']
        self.assertFalse(Board._check_row(row))
        row = ['X', 'X', 'X']
        self.assertTrue(Board._check_row(row))
