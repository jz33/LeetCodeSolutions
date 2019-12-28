'''
450. Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 1. Find the target (to-be-deleted) node
        parent = None
        target = root  
        while target:
            if target.val == key:
                break          
            parent = target
            target = target.left if key < target.val else target.right
        
        if not target:
            # key not in tree
            return root
        
        # 2. Get next node of the target node in target node's child tree
        nextNode = target.right
        if nextNode:      
            while nextNode.left:
                nextNode = nextNode.left
        
        # 3. Delete target node
        if not parent:
            if not nextNode:
                # Delete root node, no right branch
                return root.left
            else:
                # Delete root node, has right branch
                nextNode.left = root.left
                return root.right
        else:
            targetIsOnLeft = (parent.left == target)
            # Delete the node, re-assign target's left & right
            if not nextNode:
                if targetIsOnLeft:
                    parent.left = target.left
                else:
                    parent.right = target.left
            else:
                nextNode.left = target.left
                if targetIsOnLeft:
                    parent.left = target.right
                else:
                    parent.right = target.right
                    
        return root
