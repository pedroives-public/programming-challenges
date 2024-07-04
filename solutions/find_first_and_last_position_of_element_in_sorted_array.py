"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given 
target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Example 3:

    Input: nums = [], target = 0
    Output: [-1,-1]


Problem Source: LeetCode

Solution -> O(logn)
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        left, right = -1, -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                left = mid

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                right = mid
            
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return [left, right]