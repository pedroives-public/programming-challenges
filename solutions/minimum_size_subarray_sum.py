"""
Given an array of positive integers nums and a positive integer target, return the minimal 
length of a subarray whose sum is greater than or equal to target. If there is no such subarray, 
return 0 instead.

Example 1:

    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

    Input: target = 4, nums = [1,4,4]
    Output: 1

Example 3:

    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window, distance = 0, float('inf')
        
        i = 0
        for j in range(len(nums)):
            window += nums[j]
            while window >= target:
                window -= nums[i]
                distance = min(distance, j - i + 1)
                i += 1
        
        return distance if distance != float('inf') else 0