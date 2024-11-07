"""
You are given an m x n grid where each cell can have one of three values:

    - 0 representing an empty cell,
    - 1 representing a fresh orange, or
    - 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:

    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Problem Source: LeetCode

Solution -> O(n * m)
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dq = deque()

        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    dq.append((i, j))

        mins = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while dq:
            paths = len(dq)
            for path in range(paths):
                x, y = dq.popleft()
                for dx, dy in directions:
                    adjX = x + dx
                    adjY = y + dy

                    if 0 <= adjX < n and 0 <= adjY < m and grid[adjX][adjY] == 1:
                        grid[adjX][adjY] = 2
                        fresh -= 1
                        dq.append((adjX, adjY))
            
            if dq:
                mins += 1

        return mins if fresh == 0 else -1