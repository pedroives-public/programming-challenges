"""
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

Example 1:

    Input: arr = [1,2,3,10,4,2,3,5]
    Output: 3
    Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
    Another correct solution is to remove the subarray [3,10,4].

Example 2:

    Input: arr = [5,4,3,2,1]
    Output: 4
    Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:

    Input: arr = [1,2,3]
    Output: 0
    Explanation: The array is already non-decreasing. We do not need to remove any elements.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        suffix = len(arr) - 1
        while suffix > 0 and arr[suffix] >= arr[suffix-1]:
            suffix -= 1
        
        ans = suffix
        prefix = 0

        while prefix < suffix and (prefix == 0 or arr[prefix - 1] <= arr[prefix]):
            while suffix < len(arr) and arr[prefix] > arr[suffix]:
                suffix += 1
            
            ans = min(ans, suffix - prefix - 1)
            prefix += 1
        
        return ans