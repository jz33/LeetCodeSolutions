'''
475. Heaters
https://leetcode.com/problems/heaters/

Winter is coming! During the contest,
your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line,
return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

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

Constraints:
    1 <= houses.length, heaters.length <= 3 * 104
    1 <= houses[i], heaters[i] <= 109
'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radiusNeeded = 0
        hi = 0 # iterator on heater
        for house in houses:
            while hi + 1 < len(heaters) and abs(heaters[hi+1] - house) <= abs(heaters[hi] - house):
                hi += 1
            radiusNeeded = max(radiusNeeded, abs(heaters[hi] - house))
        return radiusNeeded
    