"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time

Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        haveNumber = False
        for i in range(len(nums)):
            if nums[i] != 0:
                haveNumber = True
                break

        if haveNumber:
            acc = 1
            haveZero = False
            zeros = 0
            
            for i in range(len(nums)):
                if nums[i] == 0:
                    haveZero = True
                    zeros += 1
                else:
                    acc *= nums[i]
            
            if haveZero:
                for i in range(len(nums)):
                    if nums[i] != 0 or zeros > 1:
                        nums[i] = 0
                    else:
                        nums[i] = acc
            else:
                for i in range(len(nums)):
                    nums[i] = acc // nums[i]
        
        return nums