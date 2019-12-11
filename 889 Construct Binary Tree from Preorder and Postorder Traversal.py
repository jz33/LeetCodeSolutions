'''
889. Construct Binary Tree from Preorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 
Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
'''
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        book = dict(zip(post, range(len(post))))

        root = TreeNode(pre[0])
        stack = [root]
        for i in range(1, len(pre)):
            curr = pre[i]
            n = TreeNode(curr)
            pos = book[curr]
            
            '''
            In preorder traversal output, if b is after a,
            it means b is child of a or one of its parent's right child;
            In postorder traversal output, if b is after a,
            if means b is a's parent or one of its parent's right child;
            '''
            if pos < book[stack[-1].val]:
                # Put n to left
                stack[-1].left = n
            else:
                # Put n to one of the parents' right
                stack.pop()
                while stack and pos > book[stack[-1].val]:
                    stack.pop()
                stack.pop().right = n
                
            stack.append(n)

        return root
