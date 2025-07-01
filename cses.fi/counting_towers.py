import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
MOD = (10 ** 9) + 7
INF = (10 ** 9) + 5

dp = [[0] * 2 for _ in range(1000000 + 1)]
def solve():
    dp[1][0] = 1 # one block bar
    dp[1][1] = 1 # two block bar

    for i in range(2, 1000000 + 1):
        dp[i][0] = dp[i-1][1] % MOD
        dp[i][1] = dp[i-1][0] % MOD

        dp[i][0] += (2 * dp[i-1][0]) % MOD
        dp[i][1] += (4 * dp[i-1][1]) % MOD

if __name__ == "__main__":
    t = int(input())
    solve()
    for i in range(t):
        n = int(input())
        print((dp[n][0] + dp[n][1]) % MOD)