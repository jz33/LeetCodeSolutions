'''
727. Minimum Window Subsequence
https://leetcode.com/problems/minimum-window-subsequence/

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
'''
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        '''
        O(len(S) * len(T))
        '''
        i = 0 # iterator for S
        j = 0 # iterator for T
        rs = -1 # result start
        rl = len(S) # result length
        while i < len(S):
            if S[i] == T[j]:
                if j + 1 == len(T):
                    # Find a match. Update result
                    end = i # to update result

                    # Moving back to find shortest subsequence in S
                    # Notice the shortest subsequence does not have to start in 
                    # first place where S[i] == T[j], it could be later
                    while j > -1:
                        if S[i] == T[j]:
                            j -= 1
                        i -= 1

                    # After loop, i is 1 before the subsequence, j is -1
                    i += 1
                    if rl > end - i + 1:
                        rl = end - i + 1
                        rs = i

                    j = 0                
                else:
                    j += 1

            i += 1

        return "" if rs == -1 else S[rs : rs + rl]
