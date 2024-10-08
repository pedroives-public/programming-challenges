"""
Given an array of integers nums and an integer k, return the number of contiguous 
subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

    Input: nums = [10,5,2,6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are:
    [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

    Input: nums = [1,2,3], k = 0
    Output: 0


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        dq = deque()
        subarrays, multiply = 0, 1
        for num in nums:
            multiply *= num
            dq.append(num)
            
            while multiply >= k and dq:
                multiply //= dq.popleft()
                
            subarrays += len(dq)
            
        return subarrays