/*
691. Stickers to Spell Word
https://leetcode.com/problems/stickers-to-spell-word/

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from
your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3

Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words,
and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.
*/
class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        const int targetSize = target.size();
        const int inf = targetSize + 1;
        
        // Select a char or not select a char of target, the total combination count is 1 << targetSize
        const int iterationSize = 1 << targetSize;
        
        // dp[i] is the minimum match count for a combination
        std::vector<int> dp(iterationSize, inf);
        dp[0] = 0;
        
        for (int i = 0; i < iterationSize; ++i) {
            
            // Use known matches to extend new matches
            if (dp[i] != inf) {
                for (std::string& sticker : stickers) {
                    int bitmap = i;
                    
                    // Add 1 sticker to current combination
                    for (char cs : sticker) {
                        for (int t = 0; t < targetSize; ++t) {
                            if (target[t] == cs && !(bitmap & (1 << t))) {
                                bitmap |= (1 << t);
                                break;
                            }
                        }
                    }
                    dp[bitmap] = std::min(dp[bitmap], dp[i] + 1);
                }
            }
        }
        
        return dp[iterationSize - 1] == inf ? -1 : dp[iterationSize - 1];
    }
};
