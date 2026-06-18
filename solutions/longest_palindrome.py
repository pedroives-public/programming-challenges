"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:

  Input: s = "abccccdd"
  Output: 7
  Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

  Input: s = "a"
  Output: 1
  Explanation: The longest palindrome that can be built is "a", whose length is 1.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = Counter(s)
        odd = False

        longest = 0
        for freq in frequency.values():
            longest += (freq // 2) * 2
            if freq % 2 != 0:
                odd = True

        if odd:
            longest += 1

        return longest