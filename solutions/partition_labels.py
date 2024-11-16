"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:

    Input: s = "eccbbbbdec"
    Output: [10]


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sizes = []
        positions = {}
        for i in range(len(s)):
            positions[s[i]] = i
            
        start, end = 0, 0
        for i in range(len(s)):
            end = max(end, positions[s[i]])
            if i == end:
                sizes.append(end - start + 1)
                end += 1
                start = end
        
        return sizes