"""
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

    - If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
    - Otherwise, you do not get any points, and you end this process.

After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

Example 1:

    Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
    Output: [5,8,1]
    Explanation: The diagrams above show which cells we visit to get points for each query.

Example 2:

    Input: grid = [[5,2,1],[1,1,2]], queries = [3]
    Output: [0]
    Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.


Problem Source: LeetCode

Solution -> O(m*n + k*log(k))
"""

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])
        ans = [0] * len(queries)
        
        dq = []
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        heapq.heappush(dq, (grid[0][0], 0, 0))
        visited[0][0] = True
        count = 0

        for qr, idx in queries:
            while dq and dq[0][0] < qr:
                val, row, col = heapq.heappop(dq)
                count += 1
                for i, j in directions:
                    newR = row + i
                    newC = col + j
                    if (0 <= newR < len(grid) and 0 <= newC < len(grid[0])) and not visited[newR][newC]:
                        heapq.heappush(dq, (grid[newR][newC], newR, newC))
                        visited[newR][newC] = True
                
            ans[idx] = count
        
        return ans