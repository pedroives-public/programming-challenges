"""
You are given an integer array nums of length n.

Your goal is to start at index 0 and reach index n - 1. You can only jump to indices greater than your current index.

The score for a jump from index i to index j is calculated as (j - i) * nums[i].

Return the maximum possible total score by the time you reach the last index.

Example 1:

    Input: nums = [1,3,1,5]

    Output: 7

    Explanation:

    First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.

Example 2:

    Input: nums = [4,3,1,3,2]

    Output: 16

    Explanation:

    Jump directly to the last index. The final score is 4 * 4 = 16.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        pos = 0
        soma = 0
        best = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[pos]:
                soma += (i - pos) * nums[pos]
                pos = i
                best = soma + (nums[i] * (len(nums)-i-1))
        
        best = soma + (nums[pos] * (len(nums)-pos-1))
        return best