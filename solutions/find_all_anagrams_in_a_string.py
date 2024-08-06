"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.

Example 1:

    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freqP = [0] * 26
        freqS = [0] * 26
        for char in p:
            freqP[ord(char) - ord('a')] += 1

        ans = []; i = 0
        for j in range(len(s)):
            if (j - i + 1) > len(p):
                freqS[ord(s[i]) - ord('a')] -= 1
                i += 1

            freqS[ord(s[j]) - ord('a')] += 1
            if freqS == freqP:
                ans.append(i)

        return ans