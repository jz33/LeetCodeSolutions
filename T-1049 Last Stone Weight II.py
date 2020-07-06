'''
1049. Last Stone Weight II
https://leetcode.com/problems/last-stone-weight-ii/

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]

Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 100
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        This question is equivalent to dividing stones into 2 groups, 
        what is the minimum difference between the sum of two groups.
        '''
        totals = {0} # set of all possible sums
        for s in stones:
            newTotals = set()
            for t in totals:
                newTotals.add(s + t)
            totals |= newTotals
        
        ss = sum(stones)
        return min(abs(ss - t - t) for t in totals)
