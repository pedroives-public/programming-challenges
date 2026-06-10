"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

  Input: nums = [1,5,11,5]
  Output: true
  Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

  Input: nums = [1,2,3,5]
  Output: false
  Explanation: The array cannot be partitioned into equal sum subsets.


Problem Source: LeetCode

Solution -> O(n * sum(nums))
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i-1][j]
                
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
        
        return dp[len(nums)][target]