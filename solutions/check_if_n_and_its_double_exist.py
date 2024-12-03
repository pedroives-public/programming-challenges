"""
Given an array arr of integers, check if there exist two indices i and j such that :

    - i != j
    - 0 <= i, j < arr.length
    - arr[i] == 2 * arr[j]

Example 1:

    Input: arr = [10,2,5,3]
    Output: true
    Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

    Input: arr = [3,1,7,11]
    Output: false
    Explanation: There is no i and j that satisfy the conditions.


Problem Source: LeetCode

Solution -> O(n*log(n))
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        arr = sorted(arr)
        for i in range(len(arr)):
            l = 0
            r = n - 1
            while l <= r:
                mid = (l + r)//2
                if arr[mid] >= 0 or arr[i] >= 0:
                    if i != mid and 2 * arr[mid] == arr[i]:
                        return True
                    elif i != mid and 2 * arr[mid] < arr[i]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if i != mid and 2 * abs(arr[mid]) == abs(arr[i]):
                        return True
                    elif i != mid and 2 * abs(arr[mid]) < abs(arr[i]):
                        r = mid - 1
                    else:
                        l = mid + 1
        
        return False