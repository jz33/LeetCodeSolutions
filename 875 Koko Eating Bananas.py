'''
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas.There are N piles of bananas, the i-th pile has piles[i] bananas.
The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.
Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
'''
class Solution:
    def getHours(self, piles: List[int], k: int) -> int:
        return sum(p // k if p % k == 0 else p // k + 1 for p in piles)
        
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        k = right
        while left <= right:
            mid = left + (right - left) // 2
            hours = self.getHours(piles, mid)
            if hours <= H:
                k = min(k, mid)
                right = mid - 1
            else:
                left = mid + 1
        return k
