"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

  Input: candidates = [10,1,2,7,6,1,5], target = 8
  Output: 
  [
  [1,1,6],
  [1,2,5],
  [1,7],
  [2,6]
  ]

Example 2:

  Input: candidates = [2,5,2,1,2], target = 5
  Output: 
  [
  [1,2,2],
  [5]
  ]


Problem Source: LeetCode

Solution -> O(n * 2^n)
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        possibilities = []
        candidates.sort()
        
        def backtracking(index, combination, current_sum):
            if current_sum == target:
                possibilities.append(combination[::])
                return
                
            if index >= len(candidates) or (current_sum > target):
                return
            
            previous = 0
            for i in range(index, len(candidates)):
                if previous == candidates[i]:
                    continue

                combination.append(candidates[i])
                current_sum += candidates[i]
                
                backtracking(i + 1, combination, current_sum)
                
                combination.pop()
                current_sum -= candidates[i]
                previous = candidates[i]
            
            return
        
        backtracking(0, [], 0)
        return possibilities