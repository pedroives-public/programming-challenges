"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tSize = Counter(t)
        left, right = 0, 0
        
        minLen = float('inf')
        minString = ""

        windowString = defaultdict(int)
        formed = 0

        while right < len(s):
            char = s[right]
            windowString[char] += 1

            if windowString[char] == tSize[char]:
                formed += 1
            
            while left <= right and formed == len(tSize):
                char = s[left]

                if (right - left + 1) < minLen:
                    minLen = min(minLen, (right - left + 1))
                    minString = s[left:right + 1]
                
                windowString[char] -= 1
                if windowString[char] < tSize[char]:
                    formed -= 1
                
                left += 1
                
            right += 1
        
        return minString