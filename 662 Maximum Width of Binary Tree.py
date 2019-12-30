# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque() # [(node, position)]
        queue.append((root, 0)) # position starts from 0
        maxWidth = 0
        while queue:
            maxWidth = max(maxWidth, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                node, pos = queue.popleft()
                
                # Positions on 1st row is [0]
                # 2nd row is [0,1]
                # 3rd row is [0,1,2,3], so on
                if node.left:
                    queue.append((node.left, (pos << 1)))
                if node.right:
                    queue.append((node.right, (pos << 1) + 1))
        return maxWidth
