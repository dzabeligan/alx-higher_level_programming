#!/usr/bin/python3
"""NQueenSolver"""

import sys


class NQueensSolver:
    """
    Class to solve the N-queens problem.
    """

    def __init__(self, num):
        """
        Initialize the N-queens solver.

        Args:
            N (int): Number of queens and board size.
        """
        self.num = num
        self.board = [['.' for _ in range(num)] for _ in range(num)]
        self.solutions = []

    def is_safe(self, row, col):
        """
        Check if a queen can be placed at the given position.

        Args:
            row (int): Row index.
            col (int): Column index.

        Returns:
            bool: True if the position is safe, False otherwise.
        """
        # Check the row on the left side
        for i in range(col):
            if self.board[row][i] == 'Q':
                return False

        # Check the upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        # Check the lower diagonal on the left side
        for i, j in zip(range(row, self.num, 1), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        return True

    def solve(self):
        """
        Solve the N-queens problem and return all solutions.

        Returns:
            list: List of solutions, where each solution is a list of [row, col] coordinates.
        """
        self.backtrack(0)
        return self.solutions

    def backtrack(self, col):
        """
        Backtracking function to find all solutions.

        Args:
            col (int): Current column index.
        """
        # Base case: all queens have been placed
        if col == self.num:
            _solution = [[r, c] for r, c in enumerate(
                self.board[row].index('Q') for row in range(self.num))]
            self.solutions.append(_solution)
            return

        # Try placing a queen in each row of the current column
        for row in range(self.num):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.backtrack(col + 1)
                self.board[row][col] = '.'


# Main program
if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse and validate the input value of N
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print the solutions
    solver = NQueensSolver(N)
    solutions = solver.solve()
    for solution in solutions:
        print(solution)
