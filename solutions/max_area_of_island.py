"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0


Problem Source: LeetCode

Solution -> O(m * n)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return 0

            if (grid[row][col] == 0) or (visited[row][col]):
                return 0

            area = 1
            visited[row][col] = True
            for dx, dy in directions:
                nr = row + dx
                nc = col + dy
                area += dfs(nr, nc)
            
            return area

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        
        return maxArea