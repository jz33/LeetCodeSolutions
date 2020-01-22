'''
894. All Possible Full Binary Trees
https://leetcode.com/problems/all-possible-full-binary-trees/

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.
Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Example 1:

Input: 7
Output:
[[0,0,0,null,null,0,0,null,null,0,0],
[0,0,0,null,null,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,null,null,null,null,0,0],
[0,0,0,0,0,null,null,0,0]]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, N: int) -> List[TreeNode]:
        if N in self.computed:
            return self.computed[N]

        res = []
        for i in range(1, N-1):
            j = N - 1 - i
            lefts = self.postorder(i)
            rights = self.postorder(j)
                             
            for left in lefts:
                for right in rights:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        
        self.computed[N] = res
        return res
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        self.computed = collections.defaultdict(list) # {node count : [nodes]}
        self.computed[1] = [TreeNode(0)]
        return self.postorder(N)
