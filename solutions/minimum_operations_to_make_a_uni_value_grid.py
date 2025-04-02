"""
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:

    Input: grid = [[2,4],[6,8]], x = 2
    Output: 4
    Explanation: We can make every element equal to 4 by doing the following: 
    - Add x to 2 once.
    - Subtract x from 6 once.
    - Subtract x from 8 twice.
    A total of 4 operations were used.

Example 2:

    Input: grid = [[1,5],[2,3]], x = 1
    Output: 5
    Explanation: We can make every element equal to 3.

Example 3:

    Input: grid = [[1,2],[3,4]], x = 2
    Output: -1
    Explanation: It is impossible to make every element equal.


Problem Source: LeetCode

Solution -> O(m * n)
"""

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                arr.append(grid[i][j])
        
        ref = arr[0] % x
        for i in range(1, len(arr)):
            if arr[i] % x != ref:
                return -1

        arr.sort()
        
        ans = 0
        target = arr[len(arr) // 2]
        for num in arr:
            ans += abs(target - num) // x
        
        return ans