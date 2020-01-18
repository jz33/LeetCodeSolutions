'''
914. X of a Kind in a Deck of Cards
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible
to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 
Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.

Example 3:

Input: [1]
Output: false
Explanation: No possible partition.

Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]

Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
'''
def getGcd(a: int, b: int) -> int:
    '''
    Get greatest common divisor of a & b
    '''
    while a:
        a, b = b % a, a
    return b

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        ctr = collections.Counter(deck)
        
        # Get the counts, find whether their greateset common divisor
        # is greated than 1
        counts = sorted(ctr.values())
        if len(counts) == 1:
            return counts[0] > 1
        
        gcd = getGcd(counts[0], counts[1])
        if gcd < 2:
            return False
        
        for i in range(2, len(counts)):
            gcd = getGcd(gcd, counts[i])
            if gcd < 2:
                return False
        
        return True
