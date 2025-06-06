"""
You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

    - word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
    - All the split words are put into a box.

Find the lexicographically largest string from the box after all the rounds are finished.

Example 1:

    Input: word = "dbca", numFriends = 2

    Output: "dbc"

    Explanation: 

    All possible splits are:

    "d" and "bca".
    "db" and "ca".
    "dbc" and "a".

Example 2:

    Input: word = "gggg", numFriends = 4

    Output: "g"

    Explanation: 

    The only possible split is: "g", "g", "g", and "g".


Problem Source: LeetCode

Solution -> O(n²)
"""

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        window = len(word) - numFriends + 1
        maxSubstring = ""

        for i in range(len(word)):
            maxLength = min(window, len(word) - i)
            current = word[i:i+maxLength]
            maxSubstring = max(maxSubstring, current)

        return maxSubstring