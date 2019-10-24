'''
1007. Minimum Domino Rotations For Equal Row
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
'''
class KeyNode:
    def __init__(self, key: int, countFromA: int, countFromB: int):
        self.key = key
        self.countFromA = countFromA
        self.countFromB = countFromB

class Solution:
    def match(self, node: KeyNode, a: int, b: int) -> bool:
        matched = False
        if a == node.key:
            node.countFromA += 1
            matched = True
        if b == node.key:
            node.countFromB += 1
            matched = True
        return matched
    
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        '''
        Try write the method in more generic way
        '''
        # Get the key number information from first pair
        nodes = []
        if A[0] == B[0]:
            nodes = [KeyNode(A[0], 1, 1)]
        else:
            nodes = [KeyNode(A[0], 1, 0), KeyNode(B[0], 0, 1)]
            
        for i in range(1, len(A)):
            toRemove = []
            for j, node in enumerate(nodes):
                if not self.match(node, A[i], B[i]):
                    # If current pair does not match any keys,
                    # the key should be removed
                    toRemove.append(j)

            if len(toRemove) == len(nodes):
                return -1

            for j in toRemove:
                # There should only be 1 j in this question
                nodes.pop(j)

        # If there are 2 keys, then these 2 numbers are just periodically appeared
        # on A or B. Counts of nodes[0] and nodes[1] are exactly opposite,
        # and there will be no duplicates
        # If there is 1 key, notice the key count sum can be larger than array size,
        # which means on some pair, the key appears both on A and B
        return min(nodes[0].countFromA, nodes[0].countFromB) - (nodes[0].countFromA + nodes[0].countFromB - len(A))       
