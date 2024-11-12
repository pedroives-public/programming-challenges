"""
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

Example 1:

    Input: nums = [4,9,6,10]
    Output: true
    Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
    In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
    After the second operation, nums is sorted in strictly increasing order, so the answer is true.

Example 2:

    Input: nums = [6,8,11,12]
    Output: true
    Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.

Example 3:

    Input: nums = [5,8,3]
    Output: false
    Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.


Problem Source: LeetCode

Solution -> O(n * log(log(n)))
"""

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def eratosthenes_sieve(n):
            is_prime = [False, False] + [True] * (n - 1)
            for p in range(2, int(n**0.5) + 1):
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
            
            primes = [i for i, prime in enumerate(is_prime) if prime]
            return primes

        primes = eratosthenes_sieve(1000)
        for i in range(len(nums)):
            ref = nums[i-1] if i > 0 else 0
            idx = bisect_left(primes, nums[i] - ref)
            nums[i] -= primes[idx-1] if idx > 0 else 0

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i+1]:
                return False
                
        return True