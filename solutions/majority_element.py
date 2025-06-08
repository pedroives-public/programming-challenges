"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

    Input: nums = [3,2,3]
    Output: 3

Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2


Problem Source: LeetCode

Solution -> O(n) time complexity, O(1) space complexity
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        for n in nums:
            if freq[n] > (len(nums) // 2):
                return n