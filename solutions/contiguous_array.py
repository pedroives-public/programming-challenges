"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

    Input: nums = [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

    Input: nums = [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_, ans = 0, 0
        
        dic = {}
        dic[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                sum_ += -1
            else:
                sum_ += 1

            if sum_ in dic:
                ans = max(ans, i - dic[sum_])
            else:
                dic[sum_] = i
        
        return ans