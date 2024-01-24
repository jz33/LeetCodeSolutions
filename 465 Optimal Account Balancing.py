'''
465. Optimal Account Balancing
https://leetcode.com/problems/optimal-account-balancing/

You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that
the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example 2:

Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.

Constraints:
    1 <= transactions.length <= 8
    transactions[i].length == 3
    0 <= fromi, toi < 12
    fromi != toi
    1 <= amounti <= 100
'''
from collections import Counter

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = Counter() # {person : balance}
        for fromPerson, toPerson, money in transactions:
            balances[fromPerson] -= money
            balances[toPerson] += money
        
        def backtrack(payId: int, debts: List[int]) -> int:
            '''
            @payId: index of the person who will pay debt to others
            @debts: current debts, after some previous transactions
            @return: minimum transaction count
            '''
            while payId < len(debts) and debts[payId] == 0:
                # The payId person might have 0 balance, if so, skip
                payId += 1

            maxTransactionCount = len(debts)
            result = maxTransactionCount
            visitedDebts = set()
            for getId in range(payId + 1, len(debts)):
                if debts[payId] > 0 and debts[getId] < 0 or debts[payId] < 0 and debts[getId] > 0 and debts[getId] not in visitedDebts:
                    visitedDebts.add(debts[getId])
                    debts[getId] += debts[payId] # let payId pays getId person
                    result = min(result, 1 + backtrack(payId + 1, debts))
                    debts[getId] -= debts[payId]

            return 0 if result == maxTransactionCount else result

        return backtrack(0, list(balances.values()))