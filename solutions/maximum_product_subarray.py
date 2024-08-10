"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:

    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMin = nums[0]
        currentMax = nums[0]
        maxProduct = nums[0]

        for i in range(1, len(nums)):
            tempMax = currentMax
            tempMin = currentMin

            currentMax = max(nums[i], nums[i] * tempMax, nums[i] * tempMin)
            currentMin = min(nums[i], nums[i] * tempMax, nums[i] * tempMin)
            maxProduct = max(maxProduct, currentMax)
        
        return maxProduct