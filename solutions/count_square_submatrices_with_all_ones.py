"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

    Input: matrix =
    [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
    ]
    Output: 15
    Explanation: 
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.

Example 2:

    Input: matrix = 
    [
    [1,0,1],
    [1,1,0],
    [1,1,0]
    ]
    Output: 7
    Explanation: 
    There are 6 squares of side 1.  
    There is 1 square of side 2. 
    Total number of squares = 6 + 1 = 7.


Problem Source: LeetCode

Solution -> O(n*m)
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        def solve(i, j):
            if (i < 0 or j < 0) or (matrix[i][j] == 0):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            left = solve(i, j - 1)
            top = solve(i - 1, j)
            diagonal = solve(i - 1, j - 1)

            dp[i][j] = 1 + min(left, top, diagonal)
            return dp[i][j]

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans += solve(i, j)
        
        return ans