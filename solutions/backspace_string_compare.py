"""
Given two strings s and t, return true if they are equal when both are typed into empty 
text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".

Example 2:

    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

Example 3:

    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".


Problem Source: LeetCode

Solution -> O(n) | O(1) space
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        countI, countJ = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    countI += 1
                    i -= 1
                elif countI > 0:
                    countI -= 1
                    i -= 1
                else: break
            
            while j >= 0:
                if t[j] == '#':
                    countJ += 1
                    j -= 1
                elif countJ > 0:
                    countJ -= 1
                    j -= 1
                else: break

            if s[i] != t[j] and i >= 0 and j >= 0:
                return False

            i -= 1; j -= 1
    
        if i != j:
            return False
        return True