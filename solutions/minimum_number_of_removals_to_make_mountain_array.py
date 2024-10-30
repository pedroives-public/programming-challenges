"""
You may recall that an array arr is a mountain array if and only if:

    - arr.length >= 3
    - There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array nums​, return the minimum number of elements to remove to make nums​​​ a mountain array.

Example 1:

    Input: nums = [1,3,1]
    Output: 0
    Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:

    Input: nums = [2,1,1,5,6,2,3,1]
    Output: 3
    Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].


Problem Source: LeetCode

Solution -> O(n²)
"""

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis = [0] * len(nums)

        for i in range(len(nums)):
            lis[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        lds = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            lds[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        ans = float('inf')
        for i in range(len(nums)):
            if lis[i] > 1 and lds[i] > 1:
                ans = min(ans, len(nums) - (lis[i] + lds[i] - 1))
        
        return ans