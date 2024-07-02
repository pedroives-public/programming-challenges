"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:

    Input: nums = [1]
    Output: [[1]]


Problem Source: LeetCode

Solution -> O(n*n!)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [0] * len(nums)

        self.backtracking(nums, [], visited, result)
        return result
    
    def backtracking(self, nums, perm, visited, result):
        if len(perm) == len(nums):
            result.append(perm.copy())
            return
        
        for i in range(len(nums)):
            if(visited[i] != 1):
                perm.append(nums[i])
                visited[i] = 1
                self.backtracking(nums, perm, visited, result)
                perm.pop()
                visited[i] = 0