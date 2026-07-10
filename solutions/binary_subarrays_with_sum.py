"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:

  Input: nums = [1,0,1,0,1], goal = 2
  Output: 4
  Explanation: The 4 subarrays are bolded and underlined below:
  [1,0,1,0,1]
  [1,0,1,0,1]
  [1,0,1,0,1]
  [1,0,1,0,1]

Example 2:

  Input: nums = [0,0,0,0,0], goal = 0
  Output: 15


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left, ans1, count = 0, 0, 0
        for right in range(len(nums)):
            count += nums[right]

            while count > goal:
                count -= nums[left]
                left += 1
            
            ans1 += (right - left + 1)

        left, ans2, count = 0, 0, 0
        for right in range(len(nums)):
            count += nums[right]

            while goal > 0 and count > goal - 1:
                count -= nums[left]
                left += 1

            ans2 += (right - left + 1)
        
        return (ans1 - ans2) if goal != 0 else ans1