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
        # Get the key number information from first pair
        nodes = []
        if A[0] == B[0]:
            nodes = [KeyNode(A[0], 1, 1)]
        else:
            nodes = [KeyNode(A[0], 1, 0), KeyNode(B[0], 0, 1)]
            
        for i in range(1, len(A)):
            a = A[i]
            b = B[i]
            if len(nodes) == 2:
                key0Matched = self.match(nodes[0], A[i], B[i])                
                key1Matched = self.match(nodes[1], A[i], B[i])
 
                if not key0Matched and not key1Matched:
                    return -1
                
                if not key0Matched:
                    nodes = nodes[1:]
     
                if not key1Matched:
                    nodes = nodes[:1]
                    
            else: # len(nodes) == 1
                keyMatched = self.match(nodes[0], A[i], B[i]) 
                if not keyMatched:
                    return -1

        if len(nodes) == 2:
            # If there are 2 keys, then these 2 numbers are just periodically appeared
            # on A or B. Counts of nodes[0] and nodes[1] are exactly opposite
            return min(nodes[0].countFromA, nodes[0].countFromB)
        
        else: # len(nodes) == 1
            # Notice the key count can be larger than array size, which means
            # on some pair, the key appears both on A and B
            return min(nodes[0].countFromA, nodes[0].countFromB) - (nodes[0].countFromA + nodes[0].countFromB - len(A))
