'''
465. Optimal Account Balancing
https://leetcode.com/problems/optimal-account-balancing/

A group of friends went on holiday and sometimes lent each other money.
For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride.
We can model each transaction as a tuple (x, y, z) which means person x gave person y $z.
Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID),
the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people,
return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
'''
from collections import Counter

class Solution:
    def backtrack(self, i: int, people: List[int]) -> int:
        '''
        Similar backtrack method like 40 Combination Sum II
        @i: index of the person who will pay debt to others
        @return: transaction count
        '''
        while i < len(people) and people[i] == 0:
            i += 1

        res = float('inf')
        prev = 0
        for j in range(i, len(people)):
            if people[i] > 0 and people[j] < 0 or people[i] < 0 and people[j] > 0 and people[j] != prev:
                prev = people[j]
                people[j] += people[i] 
                res = min(res, 1 + self.backtrack(i+1, people))
                people[j] -= people[i]

        return 0 if res == float('inf') else res

    def minTransfers(self, transactions: List[List[int]]) -> int:
        ctr = Counter()
        for a, b, d in transactions:
            ctr[a] -= d
            ctr[b] += d
        
        people = list(ctr.values())
        return self.backtrack(0, people)
