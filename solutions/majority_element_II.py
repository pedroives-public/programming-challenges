"""
Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

Example 1:

  Input: nums = [3,2,3]
  Output: [3]

Example 2:

  Input: nums = [1]
  Output: [1]

Example 3:

  Input: nums = [1,2]
  Output: [1,2]


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = {}
        for num in nums:
            if num in times:
                times[num] += 1
            else:
                times[num] = 1
        
        ans = set()
        for num in nums:
            if times[num] > int(len(nums)/3):
                ans.add(num)
        
        return list(ans)