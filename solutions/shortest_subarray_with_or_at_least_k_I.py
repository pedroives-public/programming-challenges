"""
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

Example 1:

    Input: nums = [1,2,3], k = 2

    Output: 1

    Explanation:

    The subarray [3] has OR value of 3. Hence, we return 1.

    Note that [2] is also a special subarray.

Example 2:

    Input: nums = [2,1,8], k = 10

    Output: 3

    Explanation:

    The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

    Input: nums = [1,2], k = 0

    Output: 1

    Explanation:

    The subarray [1] has OR value of 1. Hence, we return 1.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        minLength = float('inf')
        bits = [0] * 6

        def updateBits(n, delta):
            for i in range(6):
                if (n & (1 << i)) != 0:
                    bits[i] += delta

        def getCurrentOR():
            result = 0
            for i in range(6):
                if bits[i] > 0:
                    result |= (1 << i)
            return result

        left = 0
        for right in range(len(nums)):
            updateBits(nums[right], 1)
            while left <= right and getCurrentOR() >= k:
                updateBits(nums[left], -1)
                minLength = min(minLength, right - left + 1)
                left += 1
        
        return minLength if minLength != float('inf') else -1