'''
314. Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal

Given the root of a binary tree,
return the vertical order traversal of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:

Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:

Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''
class Solution:
    '''
    Very similar to 987. Vertical Order Traversal of a Binary Tree
    '''
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        nodes = [(root, 0)] # [(node, x offset)]
        book = collections.defaultdict(list) # {x offset : [values]}
        minOffset = 0
        maxOffset = 0
        while nodes:
            newNodes = []
            for node, offset in nodes:
                book[offset].append(node.val)
                minOffset = min(minOffset, offset)
                maxOffset = max(maxOffset, offset)
                if node.left:
                    newNodes.append((node.left, offset - 1))
                if node.right:
                    newNodes.append((node.right, offset + 1))
            nodes = newNodes
            
        # User min/max offset to avoid sorting
        result = []
        for offset in range(minOffset, maxOffset + 1):
            result.append(book[offset])
        return result
