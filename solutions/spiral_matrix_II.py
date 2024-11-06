"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n² in spiral order.

Example 1:

    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

    Input: n = 1
    Output: [[1]]


Problem Source: LeetCode

Solution -> O(n²)
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        i, j, dx, dy = 0, 0, 1, 0
        for num in range(1, n**2 + 1):
            matrix[i][j] = num
            if (i + dy < 0 or i + dy >= n) or (j + dx < 0 or j + dx >= n) or matrix[i + dy][j + dx] != 0:
                dx, dy = -dy, dx
        
            i += dy
            j += dx
        
        return matrix