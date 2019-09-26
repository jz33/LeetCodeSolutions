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

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:       
        if not root:
            return []
        
        to_delete_set = set(to_delete)
        stack = [(root, None)] # [(Node, parent node)], if parent node is none, it is deleted
        newRoots = []
        
        # Level order travsersal
        while stack:
            node, parent = stack.pop()
            
            # Update newRoots
            isCurrentNodeDeleted = node.val in to_delete_set
            if not parent and not isCurrentNodeDeleted:
                newRoots.append(node)
            
            # Next round
            if node.left:
                stack.append((node.left, None if isCurrentNodeDeleted else node))
            if node.right:
                stack.append((node.right, None if isCurrentNodeDeleted else node))
                
            # Actually delete the node
            if isCurrentNodeDeleted:
                if parent:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                        
                node.left = None
                node.right = None
                
        return newRoots  
