"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        ans, i, = 0, 0

        for j in range(len(s)):
            counter[s[j]] += 1
            while counter[s[j]] > 1:
                counter[s[i]] -= 1
                i += 1
            
            ans = max(ans, j - i + 1)
        
        return ans