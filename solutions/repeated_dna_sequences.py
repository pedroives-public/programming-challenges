"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

  - For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

  Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
  Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

  Input: s = "AAAAAAAAAAAAA"
  Output: ["AAAAAAAAAA"]


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = {}
        ans = {}

        for i in range(len(s) - 10 + 1):
            dna = s[i:i+10]
            if dna not in sequences:
                sequences[dna] = 1
            else:
                if dna not in ans:
                    ans[dna] = 1
        
        return list(ans.keys())