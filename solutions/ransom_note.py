"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:

    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:

    Input: ransomNote = "aa", magazine = "aab"
    Output: true


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rNote = defaultdict(int)
        mag = defaultdict(int)

        for char in ransomNote:
            rNote[char] += 1
        
        for char in magazine:
            mag[char] += 1

        for char in rNote:
            if rNote[char] > mag[char]:
                return False
        
        return True