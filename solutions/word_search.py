"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

Example 3:

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false


Problem Source: LeetCode

Solution -> O(n*m)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        # Verify if all characters exist in matrix
        chars = defaultdict(int)
        for row in board:
            for c in row:
                chars[c] += 1
        for char in word:
            if chars[char] == 0:
                return False

        # Start by the last character if its more frequent
        if chars[word[0]] > chars[word[-1]]:
            word = word[::-1]

        def dfs(row, col, idx):
            if board[row][col] != word[idx]:
                return False
            if idx == len(word)-1:
                return True

            visited[row][col] = True
            for i, j in directions:
                nr = row + i
                nc = col + j
                if (0 <= nr < len(board) and 0 <= nc < len(board[0])) and not visited[nr][nc]:
                    if dfs(nr, nc, idx+1):
                        return True
            
            visited[row][col] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False