"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 2:

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4


Problem Source: LeetCode

Solution -> O(n*log(n))
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)
        
        largest = heapq.nlargest(k, heap)
        return largest[-1]