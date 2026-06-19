"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

Example 1:

  Input: words = ["cat","bt","hat","tree"], chars = "atach"
  Output: 6
  Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

  Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
  Output: 10
  Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Problem Source: LeetCode

Solution -> O(n * m)
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        frequency = [0] * 26

        for char in chars:
            frequency[ord(char) - ord('a')] += 1

        for word in words:
            flag = True
            count = frequency[:]
            for char in word:
                if count[ord(char) - ord('a')] == 0:
                    flag = False
                    break
                    
                count[ord(char) - ord('a')] -= 1

            if flag:
                result += len(word)
        
        return result