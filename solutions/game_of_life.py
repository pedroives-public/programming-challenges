"""
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:

    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]


Problem Source: LeetCode

Solution -> O(m*n)
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1), (1, 0), (1, 1)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                ones = 0
                for x, y in directions:
                    newX, newY = (r + x), (c + y)
                    if 0 <= newX < len(board) and 0 <= newY < len(board[0]):
                        if board[newX][newY] == 1 or board[newX][newY] == 3:
                            ones += 1
                
                if board[r][c] == 1 or board[r][c] == 3:
                    if ones == 2 or ones == 3:
                        board[r][c] = 3
                else:
                    if ones == 3:
                        board[r][c] = 2
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] < 2:
                    board[r][c] = 0
                else:
                    board[r][c] = 1