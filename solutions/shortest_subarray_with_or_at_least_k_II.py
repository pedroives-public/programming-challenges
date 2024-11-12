"""
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty 
subarray of nums, or return -1 if no special subarray exists.

Example 1:

    Input: nums = [1,2,3], k = 2

    Output: 1

    Explanation:

    The subarray [3] has OR value of 3. Hence, we return 1.

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
        left = right = 0
        bits = [0] * 32

        def update(num, delta):
            for i in range(32):
                if num & (1 << i):
                    bits[i] += delta
        
        def convert():
            ans = 0
            for i in range(32):
                if bits[i]:
                    ans |= (1 << i)
            return ans

        while right < len(nums):
            update(nums[right], 1)
            while (left <= right and convert() >= k):
                minLength = min(minLength, right - left + 1)
                update(nums[left], -1)
                left += 1

            right += 1

        return -1 if minLength == float('inf') else minLength