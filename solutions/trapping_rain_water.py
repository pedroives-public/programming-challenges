"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

    Input: height = [4,2,0,3,2,5]
    Output: 9


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = [], []
        
        maxL = 0
        for i in range(len(height)):
            l.append(maxL)
            maxL = max(maxL, height[i])
        
        maxR = 0
        for i in range(len(height) - 1, -1, -1):
            r.append(maxR)
            maxR = max(maxR, height[i])

        r.reverse() # -> computar altura maxima da esquerda para a direita

        ans = 0
        for i in range(len(height)):
            ans += max(min(l[i], r[i]) - height[i], 0)
        
        return ans