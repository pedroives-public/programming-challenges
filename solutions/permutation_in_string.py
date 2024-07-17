"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mapS1 = Counter(s1)
        mapS2 = Counter()

        for i in range(len(s1)):
            mapS2[s2[i]] += 1
            if mapS2 == mapS1:
                return True
                
        for i in range(len(s1), len(s2)):
            mapS2[s2[i]] += 1
            mapS2[s2[i-len(s1)]] -= 1
            
            if not mapS2[s2[i-len(s1)]]:
                del mapS2[s2[i-len(s1)]]

            if mapS2 == mapS1:
                return True

        return False
        
            
            