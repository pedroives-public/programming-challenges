"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.

Example 1:

    Input: n = 16
    Output: true

Example 2:

    Input: n = 5
    Output: false

Example 3:

    Input: n = 1
    Output: true


Problem Source: LeetCode

Solution -> O(1)
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #0x55555555 -> checkerboard mask
        mask = 0x55555555
        if n != 0 and (n & (n - 1)) == 0 and ((n | mask) == mask):
            return True
        return False