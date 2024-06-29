"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Example 3:
    Input: nums = [3,3,3,3,3]
    Output: 3


Problem Source: LeetCode

Solution -> O(n) time | O(1) space -> Floyd's Cycle Detection
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s2 = 0
        while s != s2:
            s = nums[s]
            s2 = nums[s2]
        return s2