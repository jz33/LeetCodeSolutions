# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNode(self, node: TreeNode) -> int:
        if not node:
            return 0
        return self.countNode(node.left) + self.countNode(node.right) + 1
    
    def findNode(self, node: TreeNode, target: int) -> TreeNode:
        if not node:
            return None
        
        if node.val == target:
            return node
        
        return self.findNode(node.left, target) or self.findNode(node.right, target)
        
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        mine = self.findNode(root, x)
        left = self.countNode(mine.left)
        right = self.countNode(mine.right)
        top = n - left - right - 1
        
        # In order for player 2 to win, he needs to choose the biggest branch who's node count
        # is bigger than rest 2 together
        return top > left + right or left > top + right or right > top + left
