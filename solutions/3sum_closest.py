"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

  Input: nums = [-1,2,1,-4], target = 1
  Output: 2
  Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

  Input: nums = [0,0,0], target = 1
  Output: 0
  Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Problem Source: LeetCode

Solution -> O(n²)
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float('inf')
        closest = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            total = 0
            j = i + 1; k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total

                if abs(total - target) < min_diff:
                    min_diff = abs(total - target)
                    closest = total

        return closest