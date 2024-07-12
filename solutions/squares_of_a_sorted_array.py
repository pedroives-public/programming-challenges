"""
Given an integer array nums sorted in non-decreasing order, return an array 
of the squares of each number sorted in non-decreasing order.

Example 1:

    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

Example 2:

    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i, j = 0, len(nums) - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                ans.append(abs(nums[i]) * abs(nums[i]))
                i += 1
            else:
                ans.append(abs(nums[j]) * abs(nums[j]))
                j -= 1
        
        return ans[::-1]