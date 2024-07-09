"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:

    Input: tiles = "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

    Input: tiles = "AAABBC"
    Output: 188

Example 3:

    Input: tiles = "V"
    Output: 1


Problem Source: LeetCode
"""

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []; dic = defaultdict(int)
        for char in tiles:
            dic[char] += 1    

        self.backtracking(tiles, [], dic, result)
        return len(result)
    
    def backtracking(self, tiles, word, used, result):
        if sum(used.values()) == 0:
            result.append(word.copy())
            return
        
        if word:
            result.append(word.copy())
        
        for char in used:
            if used[char] != 0:
                word.append(char)
                used[char] -= 1
                self.backtracking(tiles, word, used, result)
                word.pop()
                used[char] += 1
        
        
        return