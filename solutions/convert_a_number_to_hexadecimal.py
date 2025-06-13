"""
Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem. 

Example 1:

    Input: num = 26
    Output: "1a"

Example 2:

    Input: num = -1
    Output: "ffffffff"


Problem Source: LeetCode

Solution -> O(log(n))
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
            
        if num < 0:
            mask = (1 << 32) - 1
            num &= mask

        digits = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

        remainders = []
        while num > 0:
            remainders.append((num % 16))
            num //= 16
        
        ans = ""
        for i in range(len(remainders) - 1, -1, -1):
            ans += digits[remainders[i]]
        
        return ans