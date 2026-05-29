"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

  - For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:

  Input: numCourses = 2, prerequisites = [[1,0]]
  Output: true
  Explanation: There are a total of 2 courses to take. 
  To take course 1 you should have finished course 0. So it is possible.

Example 2:

  Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
  Output: false
  Explanation: There are a total of 2 courses to take. 
  To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Problem Source: LeetCode

Solution -> O(V + E)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(prereq)

        visited = set()
        def dfs(node, seen):
            if node in seen:
                return False
            
            if node in visited:
                return True

            seen.add(node)
            if node in graph:
                for neighbor in graph[node]:
                    if not dfs(neighbor, seen):
                        return False
            
            seen.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            seen = set()
            if not dfs(course, seen):
                return False
        
        return True