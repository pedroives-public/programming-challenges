"""
Given an integer array nums and an integer k, return true if there are two distinct 
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:

    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:

    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if dic.get(nums[i]) and abs((i + 1) - dic[nums[i]]) < k + 1:
                return True     
            dic[nums[i]] = i + 1
        
        return False