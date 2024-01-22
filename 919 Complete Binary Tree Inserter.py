'''
919. Complete Binary Tree Inserter
https://leetcode.com/problems/complete-binary-tree-inserter/

A complete binary tree is a binary tree in which every level, except possibly the last,
is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the CBTInserter class:

CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.

int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that
the tree remains complete, and returns the value of the parent of the inserted TreeNode.

TreeNode get_root() Returns the root node of the tree.

Example 1:

Input
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
Output
[null, 1, 2, [1, 2, 3, 4]]

Explanation
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // return 1
cBTInserter.insert(4);  // return 2
cBTInserter.get_root(); // return [1, 2, 3, 4]

Constraints:
    The number of nodes in the tree will be in the range [1, 1000].
    0 <= Node.val <= 5000
    root is a complete binary tree.
    0 <= val <= 5000
    At most 104 calls will be made to insert and get_root.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def countNode(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return countNode(root.left) + countNode(root.right) + 1

class CBTInserter:
    '''
    O(log(depth)) insertion, O(1) space
    '''
    def __init__(self, root: Optional[TreeNode]):
        '''
        '''
        # Root is non-null
        self.root = root
        self.count = countNode(root)

    def insert(self, val: int) -> int:
        '''
        The insertion takes O(log(depth)) time
        '''
        self.count += 1
        # Bit operation. Ignore most significant bit (must be 1).
        # From 2nd bit and before last bit, if '0', go left; if '1', go right.
        # The last bit determines to put the node in left or right
        parent = self.root
        countBinary = "{0:b}".format(self.count)
        for i in range(1, len(countBinary) - 1):
            if countBinary[i] == '0':
                parent = parent.left
            else: # countString[i] == '1'
                parent = parent.right
        
        if countBinary[-1] == '0':
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return parent.val
    
    def get_root(self) -> Optional[TreeNode]:
        return self.root

class CBTInserter2:
    '''
    O(1) insertion, O(N) space
    '''
    def __init__(self, root: Optional[TreeNode]):
        tree = [root]
        ti = 0
        while ti < len(tree):
            node = tree[ti]
            if node.left:
                tree.append(node.left)
            if node.right:
                tree.append(node.right)
            ti += 1
        self.tree = tree

    def insert(self, val: int) -> int:
        node = TreeNode(val)

        newIndex = len(self.tree) # index of the new node
        parentIndex = (newIndex - 1) >> 1
        if newIndex & 1:
            self.tree[parentIndex].left = node
        else:
            self.tree[parentIndex].right = node

        self.tree.append(node)
        return self.tree[parentIndex].val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree[0]
