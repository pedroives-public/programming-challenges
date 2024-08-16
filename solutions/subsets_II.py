"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

    Input: nums = [0]
    Output: [[],[0]]


Problem Source: LeetCode

Solution -> O(n*(2^n))
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, subset, nums):
            result.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                if subset not in result:
                    backtracking(i + 1, subset, nums)
                subset.pop()
                
        nums.sort()
        result = []
        backtracking(0, [], nums)
        return result