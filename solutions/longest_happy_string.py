"""
A string s is called happy if it satisfies the following conditions:

    - s only contains the letters 'a', 'b', and 'c'.
    - s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    - s contains at most a occurrences of the letter 'a'.
    - s contains at most b occurrences of the letter 'b'.
    - s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:

    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.

Example 2:

    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    Explanation: It is the only correct answer in this case.


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        priority = []
        if a > 0:
            heapq.heappush(priority, (-a, "a"))
        if b > 0:
            heapq.heappush(priority, (-b, "b"))
        if c > 0:
            heapq.heappush(priority, (-c, "c"))

        s = ""
        while priority:
            count1, char1 = heapq.heappop(priority)
            if len(s) >= 2 and s[-1] == s[-2] == char1:
                if not priority:
                    break
                
                count2, char2 = heapq.heappop(priority)
                s += char2
                count2 += 1

                if count2 != 0:
                    heapq.heappush(priority, (count2, char2))
                
                heapq.heappush(priority, (count1, char1))
            
            else:
                s += char1
                count1 += 1
                if count1 != 0:
                    heapq.heappush(priority, (count1, char1))

        return s