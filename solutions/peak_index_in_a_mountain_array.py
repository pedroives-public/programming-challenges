"""
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

Example 1:

    Input: arr = [0,1,0]
    Output: 1

Example 2:

    Input: arr = [0,2,1,0]
    Output: 1

Example 3:

    Input: arr = [0,10,5,2]
    Output: 1


Problem Source: LeetCode

Solution -> O(logn)
"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid-1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid