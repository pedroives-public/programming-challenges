"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and 
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for char in s:
            if char.isalnum():
               ans += char.lower()
               
        i, j = 0, len(ans)-1
        while i <= j:
            if ans[i] != ans[j]:
                return False
            i += 1
            j -= 1
        
        return True