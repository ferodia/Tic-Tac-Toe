class Board(object):
    """
    Representation of the board game and associated methods
    size is fixed at 3
    """
    def __init__(self):
        self.__n = 3
        self.__grid = [[' ' for _ in range(self.__n)] for _ in range(self.__n)]
        self.__number_cells = self.__n * self.__n
        self.__winner = None
        self.__empty_cells = [(i, j) for i in range(self.__n) for j in range(self.__n)]

    @property
    def state(self):
        """
        return the board state in the format of a string
        it is formed by the concatenation of the cells
        """
        state = ''
        for row in self.__grid:
            for e in row:
                state += e
        return state

    @property
    def empty_cells(self):
        """
        Returns the empty cells in the grid
        """
        return self.__empty_cells

    def show(self):
        """
        Returns the grid
        """
        return '\n'.join([str(row) for row in self.__grid])

    def is_full(self):
        """
        checks whether the grid is full
        """
        if self.__number_cells == 0:
            return True
        return False

    def mark_cell(self, x, y, sign):
        """
        add a sign in the specified cell
        """
        if self.__grid[x][y] == ' ':
            self.__grid[x][y] = sign
            self.__number_cells -= 1
            self.__empty_cells.remove((x, y))
        else:
            raise IndexError("Cell already played, choose another one")

    def has_winner(self):
        """
        Checks the grid if there is a win situation
        """
        if (self.__check_verticals() or
                self.__check_horizontals() or
                self.__check_diagonals()):
            return True

        return False

    @property
    def winner(self):
        """
        returns the winner
        """
        return self.__winner

    def __check_verticals(self):
        """"
        """
        for row in zip(*self.__grid):
            if self.__check_row(row):
                self.__winner = row[0]
                return True
        return False

    def __check_horizontals(self):
        for row in self.__grid:
            if self.__check_row(row):
                self.__winner = row[0]
                return True
        return False

    def __check_diagonals(self):
        diagonal1 = [self.__grid[i][i] for i in xrange(self.__n)]
        diagonal2 = [self.__grid[i][self.__n - 1 - i] for i in xrange(self.__n)]
        for row in [diagonal1, diagonal2]:
            if self.__check_row(row):
                self.__winner = row[0]
                return True

        return False

    @staticmethod
    def __check_row(row):
        if len(set(row)) == 1 and row[0] != ' ':
            return True

    def print_board(self):

        print (' ' + self.__grid[0][0] + ' | ' + self.__grid[0][1] + ' | ' + self.__grid[0][2])
        print ('--- --- ---')
        print (' ' + self.__grid[1][0] + ' | ' + self.__grid[1][1] + ' | ' + self.__grid[1][2])
        print ('--- --- ---')
        print (' ' + self.__grid[2][0] + ' | ' + self.__grid[2][1] + ' | ' + self.__grid[2][2])
