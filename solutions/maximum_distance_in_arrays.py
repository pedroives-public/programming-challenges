"""
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. 
We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

Example 1:

    Input: arrays = [[1,2,3],[4,5],[1,2,3]]
    Output: 4
    Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and 
    pick 5 in the second array.

Example 2:

    Input: arrays = [[1],[1]]
    Output: 0


Problem Source: LeetCode

Solution -> O(n*log(n))
"""

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays = sorted(arrays, key=lambda x: x[0])
        
        firstMin = arrays[0][0]
        firstMax = arrays[1][-1]
        for i in range(2, len(arrays)):
            firstMax = max(firstMax, arrays[i][-1])

        secondMin = arrays[1][0]
        secondMax = arrays[0][-1]
        for i in range(2, len(arrays)):
            secondMin = min(secondMin, arrays[i][0])

        return max((firstMax - firstMin), (secondMax - secondMin))