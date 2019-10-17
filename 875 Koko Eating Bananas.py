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
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        total = sum(piles)
        
        # left/right is the minimum/maximum bananas to eat
        left = total // H if total % H == 0 else total // H + 1
        right = max(piles)
        
        # binary search to lower bound
        res = right
        while left <= right:
            mid = left + ((right - left) >> 1)
            
            s = sum(p // mid if p % mid == 0 else p // mid + 1 for p in piles)
            
            if s <= H:          
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res
