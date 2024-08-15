"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:

    Input: nums = [1,2,3], k = 3
    Output: 2


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        ans = sum = 0

        for num in nums:
            sum += num
            if (sum - k) in prefixSum:
                ans += prefixSum[sum - k]
            
            if sum in prefixSum:
                prefixSum[sum] += 1
            else:
                prefixSum[sum] = 1

        return ans