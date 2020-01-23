'''
440. K-th Smallest in Lexicographical Order
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
'''
class Solution:
    def getGap(self, n: int, node: int) -> int:
        '''
        Compute how many nodes between node and its next sibling
        '''
        gap = 0
        sibling = node + 1
        while node <= n:
            # The gap of node and its sibling on a level is just
            # slibling - gap. Notice slibing can go out of bound
            # Use n + 1 not n because n itself is counted
            gap += min(n + 1, sibling) - node;
            
            # Both go deeper
            node *= 10
            sibling *= 10  
            
        return gap
    
    def findKthNumber(self, n: int, k: int) -> int:
        '''
        Similar to 386. Lexicographical Numbers
        This is essentially preorder traversal on 10-ary tree
        '''
        node = 1
        steps = 1
        while steps < k:
            gap = self.getGap(n, node)
            
            if steps + gap <= k:
                # If the gap is small, go to next sibling
                node += 1
                steps += gap
            else:
                # If the gap is too big, it means the target is in subtree, go to child
                node *= 10
                steps += 1
                
        return node
