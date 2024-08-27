"""
Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

Example 1:

    Input: s = "ab-cd"
    Output: "dc-ba"

Example 2:

    Input: s = "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"

Example 3:

    Input: s = "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = list(s)
        i = 0
        j = len(s) - 1
        while i <= j:
            if not (97 <= ord(result[i].lower()) <= 122):
                i += 1
            elif not (97 <= ord(result[j].lower()) <= 122):
                j -= 1
            else:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1
        
        return ''.join(result)