"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:

    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3


Problem Source: LeetCode

SOlution -> O(m*n)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def dfs(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return 0

            if grid[row][col] == "0" or (row, col) in visited:
                return 0
            
            visited.add((row, col))
            for i, j in directions:
                newR, newC = (row + i), (col + j)
                dfs(newR, newC)

            return 1

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += dfs(i, j)

        return islands