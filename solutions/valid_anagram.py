"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.

Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        
        for char in s:
            sDict[char] += 1
        
        for char in t:
            tDict[char] += 1
        
        return sDict == tDict 