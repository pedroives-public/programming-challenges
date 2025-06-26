"""
Consider an n \times n grid whose squares may have traps. It is not allowed to move to a square with a trap.

Your task is to calculate the number of paths from the upper-left square to the lower-right square. You can only move right or down.

Input
    
    The first input line has an integer n: the size of the grid.
    
    After this, there are n lines that describe the grid. Each line has n characters: . denotes an empty cell, and * denotes a trap.

Output

    Print the number of paths modulo 10^9+7.

Constraints

    1 <= n <= 1000

Example

    Input:
    4
    ....
    .*..
    ...*
    *...

    Output:
    3


Problem Source: CSES.fi

Solution -> O(n²)
"""
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
MOD = (10 ** 9) + 7
INF = (10 ** 9) + 5

def solve():
    n = int(input())
    matrix = [list(input()) for i in range(n)]

    dp = [[0] * n for _ in range(n)]
    for j in range(n):
        if matrix[0][j] != "*":
            dp[0][j] = 1
        else:
            break
    
    for i in range(n):
        if matrix[i][0] != "*":
            dp[i][0] = 1
        else:
            break
    
    for i in range(1, n):
        for j in range(1, n):
            if matrix[i][j] != "*":
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(dp[-1][-1] % MOD)
    return

if __name__ == "__main__":
    solve()