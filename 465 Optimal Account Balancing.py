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
    def backtrack(self, payId: int, debts: List[int]) -> int:
        '''
        Similar backtrack method like 40 Combination Sum II
        @payId: index of the person who will pay debt to others
        @return: minimum transaction count
        '''
        debtSize = len(debts)
        while payId < debtSize and debts[payId] == 0:
            payId += 1

        minTrans = float('inf')
        prevPaidDebt = 0
        for getId in range(payId + 1, debtSize):
            if debts[payId] > 0 and debts[getId] < 0 or debts[payId] < 0 and debts[getId] > 0 and debts[getId] != prevPaidDebt:
                prevPaidDebt = debts[getId]
                debts[getId] += debts[payId] 
                minTrans = min(minTrans, 1 + self.backtrack(payId + 1, debts))
                debts[getId] -= debts[payId]

        return 0 if minTrans == float('inf') else minTrans

    def minTransfers(self, transactions: List[List[int]]) -> int:
        ctr = Counter()
        for pa, pb, money in transactions:
            ctr[pa] -= money
            ctr[pb] += money
        
        debts = list(ctr.values())
        return self.backtrack(0, debts)
