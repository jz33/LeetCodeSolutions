'''
464. Can I Win
https://leetcode.com/problems/can-i-win/

In the "100 game," two players take turns adding, to a running total, any integer from 1..10.
The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without
replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win,
assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
'''
from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        
        summation = (maxChoosableInteger * (maxChoosableInteger+1)) >> 1
        if summation < desiredTotal:
            return False

        @lru_cache(None)
        def dfs(combination: int, total: int) -> bool:
            '''
            @combination: current combination of numbers represeted by a bitmap
            @total: the sum of current combination numbers
            @return: if current player (can be player 1 or 2) can win
            '''
            if total >= desiredTotal:
                # Total is picked by opponent.
                # To fully understand this, for example, think this is turn 3,
                # and there are 2 numbers picked, if reached here, player 1 is lost
                # If this is turn 4, there are 3 numbers, and so player 2 is lost
                return False

            for i in range(maxChoosableInteger):              
                # Check if i+1 is not yet picked
                if (combination & (1 << i)) == 0:
                    newCombination = (combination | (1 << i))
                    newTotal = total + i + 1                 
                    # If my opponenet cannot win, I win
                    if not dfs(newCombination, newTotal):
                        return True

            return False

        return dfs(0, 0)
