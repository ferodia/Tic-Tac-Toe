
class Board(object):

    def __init__(self):
        self.n = 3
        self.grid = [[' ' for _ in range(self.n)] for _ in range(self.n)]
        self.number_cells = self.n * self.n
        self.__winner = None
        self.__empty_cells = [(i, j) for i in range(self.n) for j in range(self.n)]

    @property
    def empty_cells(self):
        return self.__empty_cells

    def show(self):
        return '\n'.join([str(row) for row in self.grid])

    def is_full(self):
        if self.number_cells == 0:
            return True
        return False

    def mark_cell(self, x, y, sign):
        if self.grid[x][y] == ' ':
            self.grid[x][y] = sign
            self.number_cells -= 1
            self.__empty_cells.remove((x, y))
        else:
            raise IndexError("Cell already played, choose another one")

    def has_winner(self):

        if (self._check_verticals() or
                self._check_horizontals() or
                self._check_diagonals()):

            return True

        return False

    @property
    def winner(self):
        return self.__winner

    def _check_verticals(self):
        for row in zip(*self.grid):
            if self._check_row(row):
                self.__winner = row[0]
                return True
        return False

    def _check_horizontals(self):
        for row in self.grid:
            if self._check_row(row):
                self.__winner = row[0]
                return True
        return False

    def _check_diagonals(self):
        diagonal1 = [self.grid[i][i] for i in xrange(self.n)]
        diagonal2 = [self.grid[i][self.n - 1 - i] for i in xrange(self.n)]
        for row in [diagonal1, diagonal2]:
            if self._check_row(row):
                self.__winner = row[0]
                return True

        return False

    @staticmethod
    def _check_row(row):
        if len(set(row)) == 1 and row[0] != ' ':
            return True

    def print_board(self):

        print (' ' + self.grid[0][0] + ' | ' + self.grid[0][1] + ' | ' + self.grid[0][2])
        print ('--- --- ---')
        print (' ' + self.grid[1][0] + ' | ' + self.grid[1][1] + ' | ' + self.grid[1][2])
        print ('--- --- ---')
        print (' ' + self.grid[2][0] + ' | ' + self.grid[2][1] + ' | ' + self.grid[2][2])



