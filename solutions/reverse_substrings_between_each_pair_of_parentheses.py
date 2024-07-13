"""
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

Example 1:

    Input: s = "(abcd)"
    Output: "dcba"

Example 2:

    Input: s = "(u(love)i)"
    Output: "iloveu"
    Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:

    Input: s = "(ed(et(oc))el)"
    Output: "leetcode"
    Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


Problem Source: LeetCode

Solution -> O(n²)
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                string = ""
                while stack[-1] != "(":
                    string += stack.pop()
                stack.pop()

                for c in string:
                    stack.append(c)
            else:
                stack.append(char)
        
        return "".join(stack)