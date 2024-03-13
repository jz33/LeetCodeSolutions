'''
1522. Diameter of N-Ary Tree
https://leetcode.com/problems/diameter-of-n-ary-tree/description/

Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree.
This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value.
 
Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Diameter is shown in red color.

Example 2:

Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4

Example 3:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7

Constraints:
    The depth of the n-ary tree is less than or equal to 1000.
    The total number of nodes is between [1, 104].
'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def getTop2(values: List[int]):
    top1 = max(values[0], values[1])
    top2 = min(values[0], values[1])
    for i in range(2, len(values)):
        val = values[i]
        if val >= top1:
            top1, top2 = val, top1
        elif top1 > val > top2:
            top2 = val
    return top1, top2

class Solution:
    '''
    Same idea as 543. Diameter of Binary Tree
    '''
    def diameter(self, root: 'Node') -> int:
        if not root:
            return 0
        
        maxNodeCount = 1
        def postorder(node: 'Node') -> int:
            nonlocal maxNodeCount
            childrenDepths = [postorder(child) for child in node.children]
            if len(childrenDepths) == 0:
                return 1
            elif len(childrenDepths) == 1:
                maxNodeCount = max(maxNodeCount, childrenDepths[0] + 1)
                return childrenDepths[0] + 1
            else:
                top1, top2 = getTop2(childrenDepths)
                maxNodeCount = max(maxNodeCount, top1 + top2 + 1)
                return top1 + 1
        
        postorder(root)
        return maxNodeCount - 1