"""
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

Example 1:

  Input: word = "aaAbcBC"
  Output: 3
  Explanation: The special characters are 'a', 'b', and 'c'.

Example 2:

  Input: word = "abc"
  Output: 0
  Explanation: There are no special characters in word.

Example 3:
  
  Input: word = "AbBCab"
  Output: 0
  Explanation: There are no special characters in word.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        visited = set()
        last_lower = {}
        first_upper = {}
        for i in range(len(word)):
            if word[i].islower():
                last_lower[word[i]] = i
            
            if word[i].isupper():
                if word[i] not in first_upper:
                    first_upper[word[i]] = i

        ans = 0
        for i in range(len(word)):
            if word[i].isupper():
                check = word[i].lower()
                upper_check = word[i].upper()
                if check in last_lower and last_lower[check] < first_upper[upper_check] and check not in visited:
                    visited.add(check)
                    ans += 1
        
        return ans