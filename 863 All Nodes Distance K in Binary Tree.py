'''
863. All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []

Constraints:
    The number of nodes in the tree is in the range [1, 500].
    0 <= Node.val <= 500
    All the values Node.val are unique.
    target is the value of one of the nodes in the tree.
    0 <= k <= 1000
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import Optional

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 1. Add parent pointers
        def addParent(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if node:
                node.parent = parent
                addParent(node.left, node)
                addParent(node.right, node)
        addParent(root, None)

        # 2. Iterate from target
        visited = set()
        result = []
        def preorder(node: Optional[TreeNode], distance: int):
            if not node or node in visited:
                return 

            visited.add(node)
            if distance == k:
                result.append(node.val)
                return

            preorder(node.parent, distance + 1)
            preorder(node.left, distance + 1)
            preorder(node.right, distance + 1)

        preorder(target, 0)
        return result

