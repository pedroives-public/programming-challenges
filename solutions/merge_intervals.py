"""
Given an array of intervals where intervals[i] = [start(i), end(i)], merge all overlapping intervals, and 
return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Problem Source: LeetCode

Solution -> O(n*log(n))
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        result = []
        sorted_intervals = sorted(intervals, key=lambda idx: idx[0])
        
        left = sorted_intervals[0][0]
        right = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][1] > right:
                if sorted_intervals[i][0] > right:
                    result.append([left, right])
                    right = sorted_intervals[i][1]
                    left = sorted_intervals[i][0]
                else:
                    right = sorted_intervals[i][1]
        
        result.append([left, right])
        return result