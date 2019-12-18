'''
846. Hand of Straights
https://leetcode.com/problems/hand-of-straights/

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
'''
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        '''
        Similar to 659. Split Array into Consecutive Subsequences
        '''
        if len(hand) % W != 0:
            return False

        if W == 1:
            return True

        book = {} # max value : [counts]
        for card in sorted(hand):
            if card-2 in book:
                return False

            ls = book.get(card-1, [])
            if not ls:
                book[card] = book.get(card, []) + [1]
            else:
                ctr = ls.pop() + 1
                if not ls:
                    del book[card-1]
                if ctr < W:         
                    book[card] = book.get(card, []) + [ctr]
        
        return len(book) == 0
