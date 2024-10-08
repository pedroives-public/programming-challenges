"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:

    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

    Input: heights = [2,4]
    Output: 4


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                index, maxHeight = stack.pop()
                ans = max(ans, maxHeight * (i - index))

            stack.append([index, heights[i]])
    
        for i, height in stack:
            ans = max(ans, height * (len(heights) - i))
        
        return ans