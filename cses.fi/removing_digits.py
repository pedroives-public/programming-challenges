"""
You are given an integer n. On each step, you may subtract one of the digits from the number.

How many steps are required to make the number equal to 0?

Input
    The only input line has an integer n.

Output
    Print one integer: the minimum number of steps.

Constraints

    1 <= n <= 10^6

Example

    Input:
    27

    Output:
    5

    Explanation: An optimal solution is 27 -> 20 -> 18 -> 10 -> 9 -> 0.


Problem Source: CSES.fi

Solution -> O(n)
"""
class Solution:
    def removingDigits(self, n: int) -> int:
        ans = 0
        while n > 0:
            digit = max(int(d) for d in str(n))
            n -= digit
            ans += 1
        return ans
        
sol = Solution()
n = int(input())
print(sol.removingDigits(n))