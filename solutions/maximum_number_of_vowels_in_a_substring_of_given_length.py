"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, vowel, ans = 0, 0, 0
        for r in range(len(s)):
            if s[r] in 'aeiou':
                vowel += 1

            ans = max(ans, vowel)
            if r - l + 1 >= k:
                if s[l] in 'aeiou':
                    vowel -= 1
                l += 1

        return ans