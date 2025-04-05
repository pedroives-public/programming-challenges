"""
You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

    - 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
    - 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
    - 0, if none of the previous conditions holds.

Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

Example 1:

    Input: nums = [1,2,3]
    Output: 2
    Explanation: For each index i in the range 1 <= i <= 1:
    - The beauty of nums[1] equals 2.

Example 2:

    Input: nums = [2,4,6,4]
    Output: 1
    Explanation: For each index i in the range 1 <= i <= 2:
    - The beauty of nums[1] equals 1.
    - The beauty of nums[2] equals 0.

Example 3:

    Input: nums = [3,2,1]
    Output: 0
    Explanation: For each index i in the range 1 <= i <= 1:
    - The beauty of nums[1] equals 0.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        maxL = [0] * len(nums)
        minR = [0] * len(nums)

        maxL[0] = nums[0]
        currentMax = maxL[0]
        for i in range(1, len(nums)):
            if nums[i] > currentMax:
                currentMax = nums[i]
            maxL[i] = currentMax

        minR[-1] = nums[-1]
        currentMin = minR[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < currentMin:
                currentMin = nums[i]
            minR[i] = currentMin

        beauty = 0
        for i in range(1, len(nums)-1):
            if maxL[i-1] < nums[i] < minR[i+1]:
                beauty += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                beauty += 1
            
        return beauty