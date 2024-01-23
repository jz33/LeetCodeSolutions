'''
403. Frog Jump
https://leetcode.com/problems/frog-jump/

A frog is crossing a river. The river is divided into some number of units, and at each unit,
there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order,
determine if the frog can cross the river by landing on the last stone.
Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units.
The frog can only jump in the forward direction.

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone,
then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone,
4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

Constraints:
    2 <= stones.length <= 2000
    0 <= stones[i] <= 231 - 1
    stones[0] == 0
    stones is sorted in a strictly increasing order.
'''
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Dp cache is the positions for iterations. {stone : set{units}}
        # As next jump can only be unit - 1, unit, unit + 1, needs to record all previous units
        # Initialized with all stones for easy lookup
        dp = dict([(stone, set()) for stone in stones])
        dp[0] = {0}

        # Record the furthestStone that is ever reached, for early break
        furthestStone = 0

        for stone in stones:
            if stone > furthestStone:
                return False
            
            if stone == stones[-1] and len(dp[stone]):
                return True

            # Trick of this question: only consider current stone
            # Current may not be reached, as frog does not need to jump on every stone
            for unit in dp[stone]:
                for nextUnit in unit - 1, unit, unit + 1:
                    if nextUnit > 0:
                        nextStone = nextUnit + stone
                        furthestStone = max(furthestStone, nextStone)
                        if nextStone in dp:
                            dp[nextStone].add(nextUnit)
        
        return False