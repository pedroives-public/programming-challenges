"""
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

    - a1 has an odd frequency in the string.
    - a2 has an even frequency in the string.

Return this maximum difference. 

Example 1:

    Input: s = "aaaaabbc"

    Output: 3

    Explanation:

    The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
    The maximum difference is 5 - 2 = 3.

Example 2:

    Input: s = "abcabcab"

    Output: 1

    Explanation:

    The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
    The maximum difference is 3 - 2 = 1.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def maxDifference(self, s: str) -> int:
        letters = [0] * 26
        for char in s:
            letters[ord(char) - 97] += 1
        
        oddMax, evenMin = -1, float('inf')
        for freq in letters:
            if (freq % 2) == 0 and freq != 0:
                evenMin = min(evenMin, freq)
            else:
                oddMax = max(oddMax, freq)

        return (oddMax - evenMin)