"""
The edit distance between two strings is the minimum number of operations required to transform one string into the other.

The allowed operations are:

    - Add one character to the string.
    - Remove one character from the string.
    - Replace one character in the string.

For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.

Your task is to calculate the edit distance between two strings.

Input
    The first input line has a string that contains n characters between A–Z.
    The second input line has a string that contains m characters between A–Z.

Output
    Print one integer: the edit distance between the strings.

Constraints

    1 <= n,m <= 5000

Example
    Input:
    LOVE
    MOVIE

    Output:
    2


Problem Source: CSES.fi

Solution -> O(n * m)
"""
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
MOD = (10 ** 9) + 7
INF = (10 ** 9) + 5

def solve():
    s1 = input()
    s2 = input()

    n = len(s1)
    m = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for j in range(1, n + 1):
        dp[0][j] = j   
    for i in range(1, m + 1):
        dp[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    print(dp[-1][-1])

if __name__ == "__main__":
    solve()