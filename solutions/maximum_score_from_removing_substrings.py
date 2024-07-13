"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

    - Remove substring "ab" and gain x points.
        - For example, when removing "ab" from "cabxbae" it becomes "cxbae".
    
    - Remove substring "ba" and gain y points.
        - For example, when removing "ba" from "cabxbae" it becomes "cabxe".
        
Return the maximum points you can gain after applying the above operations on s.

Example 1:

    Input: s = "cdbcbbaaabab", x = 4, y = 5
    Output: 19
    Explanation:
    - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
    - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
    - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
    - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
    Total score = 5 + 4 + 5 + 5 = 19.

Example 2:

    Input: s = "aabbaaxybbaabb", x = 5, y = 4
    Output: 20


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        substring1, substring2 = "ba", "ab"
        if x > y:
            substring1 = "ab"
            substring2 = "ba"
            x, y = y, x
        
        string2, count1 = self.countChars(s, substring1)
        string2, count2 = self.countChars(string2, substring2)

        return (count1 * y) + (count2 * x)
    
    def countChars(self, string, substring):
        sum_ = 0; s = ""
        stack = []
        for char in string:
            if stack and char == substring[1] and stack[-1] == substring[0]:
                stack.pop()
                sum_ += 1
            else:
                stack.append(char)
        
        return stack, sum_