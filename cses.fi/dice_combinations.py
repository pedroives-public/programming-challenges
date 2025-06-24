"""
Your task is to count the number of ways to construct sum n by throwing a dice one or more times. Each throw produces an outcome between 1 and 6.

For example, if n=3, there are 4 ways:

    - 1+1+1
    - 1+2
    - 2+1
    - 3

Input
    The only input line has an integer n.

Output
    Print the number of ways modulo 10^9+7.

Constraints

    - 1 <= n <= 10^6

Example
    Input:
    3

    Output:
    4


Problem Source: CSES.fi

Solution -> O(n)
"""

class Solution:
    def diceCombinations(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for idx in range(1, n + 1):
            combinations = 0
            for i in range(1, 7):
                if idx - i >= 0:
                    combinations += dp[idx - i]
            dp[idx] = combinations % MOD
        
        return dp[n]
        
sol = Solution()
n = int(input())
print(sol.diceCombinations(n))