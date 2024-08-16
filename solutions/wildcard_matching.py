"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with 
support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:

    Input: s = "aa", p = "*"
    Output: true
    Explanation: '*' matches any sequence.

Example 3:

    Input: s = "cb", p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


Problem Source: LeetCode

Solution -> O(n^2)
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for i in range(len(p) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(p) + 1):
            if p[i-1] == "*":
                dp[i][0] = dp[i-1][0]
        
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                
                if p[i-1] == '*':
                        dp[i][j] = dp[i-1][j] or dp[i][j-1]
        
        return dp[-1][-1]