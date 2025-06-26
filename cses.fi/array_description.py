import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
MOD = (10 ** 9) + 7
INF = (10 ** 9) + 5

def solve():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = [[0] * (m + 2) for _ in range(n)]
    if array[0] != 0:
        dp[0][array[0]] = 1
    else:
        for i in range(1, m + 1):
            dp[0][i] = 1

    for i in range(1, n):
        if array[i] != 0:
            for adj in [-1, 0, 1]:
                val = array[i] + adj
                if 1 <= val <= m:
                    dp[i][array[i]] = (dp[i][array[i]] + dp[i-1][val]) % MOD
        else:
            for j in range(1, m + 1):
                for adj in [-1, 0, 1]:
                    val = j + adj
                    if 1 <= val <= m:
                        dp[i][j] = (dp[i][j] + dp[i-1][val]) % MOD
    
    if array[-1] == 0:
        print(sum(dp[n-1][1:m+1]) % MOD)
        return
    
    print(dp[n-1][array[-1]])
if __name__ == "__main__":
    solve()