# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
# https://assets.leetcode.com/uploads/2018/10/12/8-queens.png
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


# COULD USE A LOT OF OPTIMIZATION

import pprint
pp = pprint.PrettyPrinter(indent=4)


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.board = [['.']*n for i in range(n)]
        self.size = n
        self.solutions = []

        self._solve(0)

        return self.solutions

    def _solve(self, x):

        if self._solved():
            self.solutions.append(self._copyBoardForOutput())
            return True

        solved = False
        for y in range(self.size):
            if not self._queen_exists(x, y):
                if not self._queen_collides(x, y):
                    self.board[x][y] = 'Q'
                    if self._solve(x+1):
                        solved = True
                    self.board[x][y] = '.'

        return solved

    def _queen_exists(self, x, y):
        return self.board[x][y] == 'Q'

    def _copyBoardForOutput(self):
        copy = []
        for x in range(self.size):
            copy.append("")
            for y in range(self.size):
                copy[x] += self.board[x][y]

        return copy

    def _solved(self):
        num_queens = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 'Q':
                    num_queens += 1
                    if num_queens == self.size:
                        return True
        return False


    def _queen_collides(self, x, y):

        check_x = x
        check_y = y
        # check squares north
        while check_y < self.size-1:
            check_y += 1
            if self._queen_exists(x, check_y):
                return True

        check_x = x
        check_y = y
        # check squares south
        while check_y > 0:
            check_y -= 1
            if self._queen_exists(x, check_y):
                return True

        check_x = x
        check_y = y
        # check squares east
        while check_x < self.size-1:
            check_x += 1
            if self._queen_exists(check_x, y):
                return True

        check_x = x
        check_y = y
        # check squares west
        while check_x > 0:
            check_x -= 1
            if self._queen_exists(check_x, y):
                return True

        check_x = x
        check_y = y
        # check squares northwest
        while check_x > 0 and check_y < self.size - 1:
            check_x -= 1
            check_y += 1
            if self._queen_exists(check_x, check_y):
                return True

        check_x = x
        check_y = y
        # check squares northeast
        while check_x < self.size-1 and check_y < self.size - 1:
            check_x += 1
            check_y += 1
            if self._queen_exists(check_x, check_y):
                return True

        check_x = x
        check_y = y
        # check squares southwest
        while check_x > 0 and check_y > 0:
            check_x -= 1
            check_y -= 1
            if self._queen_exists(check_x, check_y):
                return True

        # check squares southeast
        check_x = x
        check_y = y
        while check_x < self.size-1 and check_y > 0:
            check_x += 1
            check_y -= 1
            if self._queen_exists(check_x, check_y):
                return True

        return False




pp.pprint(Solution().solveNQueens(4))




