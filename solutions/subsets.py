"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

    Input: nums = [0]
    Output: [[],[0]]


Problem Source: LeetCode

Solution -> O(n*2^n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, 0, [], result)
        return result
    
    def backtracking(self, nums: List[int], index: int, digits: List[int], result: List[List[int]]):
        if index == len(nums):
            result.append(digits.copy())
            return

        digits.append(nums[index])
        self.backtracking(nums, index + 1, digits, result)
        digits.pop()
        self.backtracking(nums, index + 1, digits, result)