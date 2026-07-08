"""
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will be the same.

Example 1:

  Input: houses = [1,2,3], heaters = [2]
  Output: 1
  Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:

  Input: houses = [1,2,3,4], heaters = [1,4]
  Output: 1
  Explanation: The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.

Example 3:

  Input: houses = [1,5], heaters = [2]
  Output: 3


Problem Source: LeetCode

Solution -> O(nlogn)
"""

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def find(R):
            left = 0
            for right in range(len(houses)):
                while left < len(heaters) and heaters[left] + R < houses[right]:
                    left += 1
                    if left == len(heaters):
                        return False
                
                if heaters[left] - R > houses[right]:
                    return False
    
            return True
        
        n = 1e9
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if find(mid):
                high = mid
            else:
                low = mid + 1
        
        return int(low)