'''
536. Construct Binary Tree from String
https://leetcode.com/problems/construct-binary-tree-from-string/

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero,
one or two pairs of parenthesis.
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example 1:

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]

Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]

Constraints:
    0 <= s.length <= 3 * 104
    s consists of digits, '(', ')', and '-' only.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Similar to 428. Serialize and Deserialize N-ary Tree
    '''
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        val = None
        sign = 1 # +1 or -1
        stack = []
        for c in s:
            if c.isdigit():
                val = val * 10 + int(c) if val is not None else int(c)
            elif c == '-':
                sign = -1
            else: # c == '(' or ')'
                if val is not None:
                    node = TreeNode(val * sign)
                    val = None
                    sign = 1

                    if stack:
                        parent = stack[-1]
                        if not parent.left:
                            parent.left = node
                        else:
                            parent.right = node

                    stack.append(node)

                if c == ')':
                    stack.pop()
        if val is not None:
            # single number
            return TreeNode(val * sign)
        else:
            return stack[0]