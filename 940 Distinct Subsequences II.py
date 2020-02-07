'''
940. Distinct Subsequences II
https://leetcode.com/problems/distinct-subsequences-ii/

Given a string S, count the number of distinct, non-empty subsequences of S .

Since the result may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:

Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".

Example 3:

Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
'''
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        ctr = collections.Counter() # {used char : total count contributed}
        sub = 0
        for e in S:
            # If e is continuously distince, newSub = sub * 2 + 1
            # Record how much more e is contributed
            # So if same e is met again, minus its previous contributed amount
            newSub = sub * 2 + 1 - ctr[e]
            ctr[e] += newSub - sub       
            sub = newSub
        return sub % (10 ** 9 + 7)
