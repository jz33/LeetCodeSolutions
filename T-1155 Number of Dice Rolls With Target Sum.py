'''
1155. Number of Dice Rolls With Target Sum
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so
the sum of the face up numbers equals target.

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.

'''
MOD = 10**9+7

class Solution:
    def numRollsToTarget(self, dices: int, faces: int, target: int) -> int:
        if target < dices or target > dices * faces:
            return 0
        if target == dices or target == dices * faces:
            return 1

        dp = [1] # [sum : count]
        for d in range(dices):
            # A dp row is [0, 1, ... max possible sum value]
            # Cannot accumalate on old dp because only faces of dics are count
            # This is different part to Coin Change
            newDp = [0] * (min(target, (d+1) * faces) + 1)
            for i in range(1, faces + 1):
                # Iterate old dp throught its smallest value to max value
                for j in range(d, len(dp)):
                    if i + j >= len(newDp):
                        break
                    newDp[i+j] = (newDp[i+j] + dp[j]) % MOD
            dp = newDp   
        return dp[-1]              
