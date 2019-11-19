'''
943. Find the Shortest Superstring
https://leetcode.com/problems/find-the-shortest-superstring/

Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.

Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.

Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
'''
class Solution:
    def deduction(self, a: str, b: str) -> int:
        d = 0
        for i in range(1, min(len(a), len(b))+1):
            if a[-i:] == b[:i]:
                d = i
        return d

    def shortestSuperstring(self, A: List[str]) -> str:
        '''
        Travelling salesman problem, O(2^N * N^2)
        '''
        size = len(A)
        graph = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if i != j:
                    graph[i][j] = self.deduction(A[i], A[j])

        # The row of the dp matrix is a bit mask represeting the string appreance
        # dp[i][j] records the shortest superstring with bit mask i and ending with string j
        dp = [[''] * size for _ in range(1 << size)]
        for m in range(1 << size): # iterate through all string combinations
            for i in range(size):
                # skip if A[i] is not in mask
                if not (m & (1 << i)):
                    continue

                # if mask only contains i
                if m == (1 << i):
                    dp[m][i] = A[i]
                    continue

                for j in range(size):
                    if i == j:
                        continue

                    if not (m & (1 << j)):
                        continue

                    # s is the shortest superstring ending with j when i is removed
                    s = dp[m ^ (1 << i)][j]
                    s += A[i][graph[j][i]:]
                    if dp[m][i] == '' or len(s) < len(dp[m][i]):
                        dp[m][i] = s

        # find the shortest superstring of all candidates ending with different string
        minSuperString = ''.join(['0'] * 250)
        for i in range(size):
            s = dp[(1 << size) - 1][i]
            if len(s) < len(minSuperString):
                minSuperString = s
        return minSuperString  
