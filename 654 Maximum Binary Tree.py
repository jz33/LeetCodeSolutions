'''
654. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
'''
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # The stack is same as in-order traversal, which holds the nodes from root to leaf
        # Each node is at most pushed/poped of stack for 1 time, so time complexity is O(n)
        stack = []        
        for n in nums:
                        
            lastPoped = None # last poped node from stack            
            while stack and n > stack[-1].val:
                lastPoped = stack.pop()
            
            node = TreeNode(n)
            node.left = lastPoped
            
            if stack:
                stack[-1].right = node
                 
            stack.append(node)

        return stack[0] if stack else None
