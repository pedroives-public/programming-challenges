"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:

    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false


Problem Source: LeetCode

Solution -> O(log(m * n))
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m * n) - 1

        while low <= high:
            mid = (low + high) // 2
            left = mid // n
            right  = mid % n

            if matrix[left][right] == target:
                return True
            elif matrix[left][right] < target:
                low = mid + 1
            else:
                high = mid - 1