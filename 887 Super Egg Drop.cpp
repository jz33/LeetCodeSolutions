/*
887. Super Egg Drop
https://leetcode.com/problems/super-egg-drop/

You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than
F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is,
regardless of the initial value of F?

Example 1:

Input: K = 1, N = 2
Output: 2

Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.

Example 2:

Input: K = 2, N = 6
Output: 3

Example 3:

Input: K = 3, N = 14
Output: 4

Note:

1 <= K <= 100
1 <= N <= 10000
*/

class Solution {
public:
    int superEggDrop(int eggCount, int floorCount) {
        // dp[i] is the maximum floor that can determine using i eggs
        std::vector<int> dp(eggCount+1);
        
        // At a floor, having i eggs, at movement j. Throw 1 egg,
        // if it breaks, using solution with i-1 eggs at movement j - 1;
        // if it holds, using solution with i eggs at movement j - 1.
        // And at movement j 1 more floor can be determined.
        // Therefore dp[i, j] = dp[i-1, j-1] + dp[i, j-1] + 1
        // Since j is montonically increasing, only i is needed parameter
        // for bottom-up dynamic programming
        int moveCount = 0;
        for (; dp[eggCount] < floorCount; moveCount++) {
            for (int i = eggCount; i > 0; i--) {
                dp[i] += 1 + dp[i-1];
            }
        }
        return moveCount;
    }
};
