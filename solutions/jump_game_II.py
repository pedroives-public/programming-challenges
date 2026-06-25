"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

  - 0 <= j <= nums[i] and
  - i + j < n

Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

Example 1:

  Input: nums = [2,3,1,1,4]
  Output: 2
  Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

  Input: nums = [2,3,0,1,4]
  Output: 2


Problem Source: LeetCode

Solution -> O(n * m)
"""

class Solution(object):
    def jump(self, nums):
        n = len(nums)
        f = [float('inf')] * n
        f[n - 1] = 0

        for i in range(n - 2, -1, -1):
            bound = min(i + nums[i], n - 1)

            if i + 1 <= bound:
                f[i] = min(f[i + 1:bound + 1]) + 1

        return f[0]

# f(i) = 1 + min(f(j)) | i + 1 <= j <= min(n-1, i + nums[i])