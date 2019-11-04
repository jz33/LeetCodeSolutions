'''
899. Orderly Queue
https://leetcode.com/problems/orderly-queue/

A string S of lowercase letters is given.  Then, we may make any number of moves.
In each move, we choose one of the first K letters (starting from the left), remove it, and place it at the end of the string.
Return the lexicographically smallest string we could have after any number of moves.

Example 1:

Input: S = "cba", K = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".

Example 2:

Input: S = "baaca", K = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".
'''
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K > 1:
            # If K > 1, S can be updated to sorted order
            return ''.join(sorted(S))
        else:
            # If K == 1, try all chars at beginning
            return min(S[i:] + S[:i] for i in range(len(S)))
