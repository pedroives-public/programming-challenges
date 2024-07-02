"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.


Example 1:

    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

    Input: s = "3z4"
    Output: ["3z4","3Z4"]


Problem Source: LeetCode

Solution -> O(L*2^L) -> L = length of the input string
"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        solve = []
        self.backtracking('' * len(s), 0, s, solve)
        return solve
    
    def backtracking(self, string: str, index: int, word: str, solve: str):
        if index == len(word):
            solve.append(string)
            return

        char = word[index]
        if char.isdigit():
            self.backtracking(string + char, index + 1, word, solve)
        else:
            self.backtracking(string + char.lower(), index + 1, word, solve)
            self.backtracking(string + char.upper(), index + 1, word, solve)