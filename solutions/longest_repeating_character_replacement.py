"""
You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. You can perform this 
operation at most k times.

Return the length of the longest substring containing the same letter you can get 
after performing the above operations.

Example 1:

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    There may exists other ways to achieve this answer too.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        ans, i, j, freq = 0, 0, 0, -1
        for j in range(len(s)):
            counter[s[j]] += 1
            freq = max(freq, counter[s[j]])

            if (j - i + 1) - freq > k:
                counter[s[i]] -= 1
                i += 1
            
            ans = max(ans, j - i + 1)
        
        return ans