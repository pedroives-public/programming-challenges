"""
You are given an array of integers nums, there is a sliding window 
of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation: 
    
    Window position               Max
    ---------------              -----
    [1  3  -1] -3  5  3  6  7      3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7

Example 2:

    Input: nums = [1], k = 1
    Output: [1]


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()
        for j in range(len(nums)):
            if dq and (j - k + 1) > dq[0]:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
                
            dq.append(j)
            if j + 1 >= k:
                result.append(nums[dq[0]])

        return result