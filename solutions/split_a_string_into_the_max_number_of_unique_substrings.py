"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

Example 1:

    Input: s = "ababccc"
    Output: 5
    Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:

    Input: s = "aba"
    Output: 2
    Explanation: One way to split maximally is ['a', 'ba'].

Example 3:

    Input: s = "aa"
    Output: 1
    Explanation: It is impossible to split the string any further.


Problem Source: LeetCode

Solution -> O(2^n)
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, used):
            if start == len(s):
                return 0
            
            maxUnique = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in used:
                    used.add(substring)
                    maxUnique = max(maxUnique, 1 + backtrack(end, used))
                    used.remove(substring)
            
            return maxUnique

        return backtrack(0, set())