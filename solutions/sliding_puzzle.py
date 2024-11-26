"""
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Example 1:


    Input: board = [[1,2,3],[4,0,5]]
    Output: 1
    Explanation: Swap the 0 and the 5 in one move.

Example 2:


    Input: board = [[1,2,3],[5,4,0]]
    Output: -1
    Explanation: No number of moves will make the board solved.

Example 3:


    Input: board = [[4,1,2],[5,0,3]]
    Output: 5
    Explanation: 5 is the smallest number of moves that solves the board.
    An example path:
    After move 0: [[4,1,2],[5,0,3]]
    After move 1: [[4,1,2],[0,5,3]]
    After move 2: [[0,1,2],[4,5,3]]
    After move 3: [[1,0,2],[4,5,3]]
    After move 4: [[1,2,0],[4,5,3]]
    After move 5: [[1,2,3],[4,5,0]]


Problem Source: LeetCode

Solution -> O((m*n)! * (m*n))
"""

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = "123450"
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        start = ""
        for i in range(2):
            for j in range(3):
                start += str(board[i][j])
                    
        visited = set(start)
        queue = deque([(start, 0)])
        while queue:
            current, moves = queue.popleft()
            if current == target:
                return moves
            
            zero = 0
            for i in range(len(current)):
                if current[i] == "0":
                    zero = i
            
            x, y = zero // 3, zero % 3 # transformação de coordenada
            for i, j in directions:
                newX, newY = (x + i), (y + j)
                if 0 <= newX < 2 and 0 <= newY < 3:
                    pos = (newX * 3) + newY
                    lista = list(current)
                    lista[pos], lista[zero] = lista[zero], lista[pos]
                    string = ''.join(lista)
                    
                    if string in visited:
                        continue
                    
                    visited.add(string)
                    queue.append((string, moves + 1))
        return -1