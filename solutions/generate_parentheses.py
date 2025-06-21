"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

    Input: n = 1
    Output: ["()"]


Problem Source: LeetCode

Solution -> O(4^n / sqrt(n)))
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        def backtracking(left, right, string):
            if left == right == n:
                combinations.append(string)
                return
            
            if left < n:
                backtracking(left + 1, right, string + "(")
            if right < left:
                backtracking(left, right + 1, string + ")")
            
        backtracking(0, 0, "")
        return combinations