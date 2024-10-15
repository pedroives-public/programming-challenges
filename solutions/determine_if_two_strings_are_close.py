"""
Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
    For example, abcde -> aecdb
    
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    
    For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
    
    You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

    Input: word1 = "abc", word2 = "bca"
    Output: true
    Explanation: You can attain word2 from word1 in 2 operations.
    Apply Operation 1: "abc" -> "acb"
    Apply Operation 1: "acb" -> "bca"

Example 2:
    
    Input: word1 = "a", word2 = "aa"
    Output: false
    Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

    Input: word1 = "cabbba", word2 = "abbccc"
    Output: true
    Explanation: You can attain word2 from word1 in 3 operations.
    Apply Operation 1: "cabbba" -> "caabbb"
    Apply Operation 2: "caabbb" -> "baaccc"
    Apply Operation 2: "baaccc" -> "abbccc"


Problem Source: LeetCode

Solution -> O(n*log(n))
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        letters1 = [0] * 26
        letters2 = [0] * 26

        for char in word1:
            letters1[ord(char) - ord('a')] += 1

        for char in word2:
            letters2[ord(char) - ord('a')] += 1

        return sorted(letters1) == sorted(letters2)