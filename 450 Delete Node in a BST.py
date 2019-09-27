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
from typing import Tuple

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def getNextNode(n: TreeNode) -> TreeNode:
            '''
            Get next node of n, return found node
            '''
            found = n.right
            if not found:
                return None
      
            while found.left:
                found = found.left

            return found
        
        def searchNode(root: TreeNode) -> Tuple[TreeNode, TreeNode]:
            '''
            Search key in BST, return found node and its parent
            '''
            parent = None
            found = root
            
            while found:
                if found.val == key:
                    break
           
                parent = found

                if key < found.val:            
                    found = found.left
                else:
                    found = found.right
                    
            return found, parent
        
        # Main body
        if not root:
            return root
        
        toDelete, toDeleteParent = searchNode(root)
        if not toDelete:
            return root
                
        nextNode = getNextNode(toDelete)
 
        if not toDeleteParent:
            # Found in root
            if not nextNode:
                return root.left
            else:
                nextNode.left = root.left
                return root.right       
        else:
            if toDeleteParent.left is toDelete:
                # found in left
                if not nextNode:
                    toDeleteParent.left = toDelete.left
                else:
                    nextNode.left = toDelete.left
                    toDeleteParent.left = toDelete.right
            else:
                # found in right
                if not nextNode:
                    toDeleteParent.right = toDelete.left
                else:
                    nextNode.left = toDelete.left
                    toDeleteParent.right = toDelete.right
            return root
