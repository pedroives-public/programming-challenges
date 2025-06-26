import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
MOD = (10 ** 9) + 7
INF = (10 ** 9) + 5

def solve():
    n, x = map(int, input().split())
    prices = list(map(int, input().split()))
    pages = list(map(int, input().split()))

    dp = [[0] * (x + 1) for _ in range(len(prices) + 1)]
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if j < prices[i-1]:
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-prices[i-1]] + pages[i-1])
    
    print(dp[-1][-1])

if __name__ == "__main__":
    solve()