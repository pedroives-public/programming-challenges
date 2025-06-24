"""
Consider a money system consisting of n coins. Each coin has a positive integer value. Your task is to produce a sum of money x using the available coins in such a way that the number of coins is minimal.

For example, if the coins are {1,5,7} and the desired sum is 11, an optimal solution is 5+5+1 which requires 3 coins.

Input
    The first input line has two integers n and x: the number of coins and the desired sum of money.

    The second line has n distinct integers c_1,c_2,\dots,c_n: the value of each coin.

Output
    Print one integer: the minimum number of coins. If it is not possible to produce the desired sum, print -1.

Constraints

    1 <= n <= 100
    1 <= x <= 10^6
    1 <= c_i <= 10^6

Example
    Input:
    3 11
    1 5 7

    Output:
    3


Problem Source: CSES.fi

Solution -> O(n * x)
"""
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
MOD = (10 ** 9) + 7
INF = (10 ** 9) + 5

def solve():
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))

    dp = [INF for _ in range(x + 1)]
    dp[0] = 0

    for i in range(len(coins)):
        for j in range(coins[i], x + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
    
    print(dp[x] if dp[x] != INF else -1)

if __name__ == "__main__":
    solve() 