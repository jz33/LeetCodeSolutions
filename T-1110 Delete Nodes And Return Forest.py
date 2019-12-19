'''
1110. Delete Nodes And Return Forest
https://leetcode.com/problems/delete-nodes-and-return-forest/

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, node, parent):
        if node.left:
            self.postorder(node.left, node)
        if node.right:
            self.postorder(node.right, node)
            
        if node.val in self.to_delete_set:
            if node.left and node.left.val not in self.to_delete_set:
                self.result.append(node.left)
            if node.right and node.right.val not in self.to_delete_set:
                self.result.append(node.right)
        
            # Actually delete this node
            if parent:
                if node == parent.left:
                    parent.left = None
                elif node == parent.right:
                    parent.right = None
            
            node.left = None
            node.right = None
                    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        self.to_delete_set = set(to_delete)
        self.result = []
        if root.val not in self.to_delete_set:
            self.result.append(root)
        self.postorder(root, None)
        return self.result
