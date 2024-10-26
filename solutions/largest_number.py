"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

    Input: nums = [10,2]
    Output: "210"

Example 2:

    Input: nums = [3,30,34,5,9]
    Output: "9534330"


Problem Source: LeetCode

Solution -> O(n*log(n))
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strNums = []
        for num in nums:
            strNums.append(str(num))

        relation = sorted(strNums, key=lambda x: x * 10, reverse=True)
        return "0" if relation[0] == "0" else ''.join(relation)