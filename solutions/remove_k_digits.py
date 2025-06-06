"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        stack = []
        for i in range(len(num)):
            curr = num[i]
            while (stack and curr < stack[-1]) and k > 0:
                k -= 1
                stack.pop()
            stack.append(curr)
        
        s = ''.join(stack)
        i = 0
        while i < len(s) and s[i] == "0":
            i += 1
        
        # after change the num to a monotonic-increase stack, check if I still have k, so I can continue removing k digits
        if k:
            s = s[i:-k]
            return s if len(s) else "0"
        
        return s[i:] if i < len(s) else "0"