"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12


Problem Source: LeetCode

Solution -> O(m * n)
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return float('inf')
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]

            right = dp(row, col + 1)
            down = dp(row + 1, col)

            return grid[row][col] + min(down, right)
        
        return dp(0, 0)