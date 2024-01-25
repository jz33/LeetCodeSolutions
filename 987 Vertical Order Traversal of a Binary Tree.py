'''
987. Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col),
its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively.
The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of
top-to-bottom orderings for each column index starting from the leftmost column and
ending on the rightmost column. There may be multiple nodes in the same row and same column.
In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Example 3:

Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 1000
'''
import collections

class Solution:
    '''
    Nearly same approach as 314. Binary Tree Vertical Order Traversal
    Time complexity: O(w * n/w * log(n/w)) = O(n(log(n/w)))
    '''
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        nodes = [(root, 0)] # [(node, x offset)]
        book = collections.defaultdict(list) # {x offset : [values]}
        minOffset = 0
        maxOffset = 0
        while nodes:
            newNodes = []
            # Use an inner book to track values as it requires the values
            # on same row on same offset to be sorted
            newBook = collections.defaultdict(list)
            for node, offset in nodes:
                newBook[offset].append(node.val)
                minOffset = min(minOffset, offset)
                maxOffset = max(maxOffset, offset)
                if node.left:
                    newNodes.append((node.left, offset - 1))
                if node.right:
                    newNodes.append((node.right, offset + 1))
            
            nodes = newNodes
            for offset, values in newBook.items():
                book[offset] += sorted(values)
            
        # User min/max offset to avoid sorting
        result = []
        for offset in range(minOffset, maxOffset + 1):
            result.append(book[offset])
        return result

class Solution2:
    '''
    DFS
    '''
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        book = collections.defaultdict(list) # {offset : [(depth, val)]}
        minOffset = 0
        maxOffset = 0

        def preorder(node: TreeNode, depth: int, offset: int):
            nonlocal minOffset, maxOffset
            book[offset].append((depth, node.val))
            minOffset = min(minOffset, offset)
            maxOffset = max(maxOffset, offset)
            if node.left:
                preorder(node.left, depth + 1, offset - 1)
            if node.right:
                preorder(node.right, depth + 1, offset + 1)

        preorder(root, 0, 0)
            
        # User min/max offset to avoid sorting
        result = []
        for offset in range(minOffset, maxOffset + 1):
            # Different to 314: sort by depths and values
            result.append([val for _, val in sorted(book[offset])])
        return result