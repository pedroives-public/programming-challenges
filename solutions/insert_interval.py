"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [start(i), end(i)] represent 
the start and the end of the ith interval and intervals is sorted in ascending order by start(i). You are also 
given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start(i) and intervals 
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals += [newInterval]
        arrays = sorted(intervals, key=lambda idx: idx[0])

        left = arrays[0][0]
        right = arrays[0][1]
        for i in range(1, len(arrays)):
            if arrays[i][1] > right:
                if arrays[i][0] > right:
                    result.append([left, right])
                    left = arrays[i][0]
                    right = arrays[i][1]
                else:
                    right = arrays[i][1]

        result.append([left, right])
        return result