"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:

    Input: nums = [7,7,7,7,7,7,7]
    Output: 1



Problem Source: LeetCode

Solution -> O(n²)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxSeq = float('inf') * (-1)
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

            maxSeq = max(maxSeq, dp[i])
        
        return maxSeq