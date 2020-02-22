'''
863. All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 
Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findParentChain(self, root: TreeNode, target: TreeNode):
        '''
        Find parent chain (including target node) of target node
        '''
        stack = [[root]]
        while stack:
            chain = stack.pop()
            node = chain[-1]
            if node == target:
                return chain
            if node.left:
                stack.append(chain + [node.left])
            if node.right:
                stack.append(chain + [node.right])
        return []
    
    def goDown(self, root: TreeNode, dist: int):
        if not root:
            return
        
        queue = collections.deque([root])
        depth = 0
        while queue and depth <= dist:
            for _ in range(len(queue)):
                node = queue.popleft()
                if depth == dist:
                    self.res.append(node.val)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            depth += 1
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        chain = self.findParentChain(root, target)
        pn = None # previous node
        self.res = []
        for i, n in enumerate(reversed(chain)):
            if i == 0:
                self.goDown(n, K)
            else:
                dist = K - i
                if dist < 0:
                    break
                if dist == 0:
                    self.res.append(n.val)
                else:              
                    if pn == n.left:
                        self.goDown(n.right, dist - 1)
                    else:
                        self.goDown(n.left, dist - 1)
            pn = n
        return self.res
