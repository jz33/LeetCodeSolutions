/*
114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <stack>

class Solution {
public:
    
    // Solution is based on pre-order traversal
    void flatten(TreeNode* root)
    {
        // Unlike ususual pre-order traversal, which remembers previous visited node,
        // in this question, the right branch of previous visisted node is remembered
        std::stack<TreeNode*> stack;
        TreeNode* curr = root;
        TreeNode* prev = nullptr;
        
        while (curr || !stack.empty())
        {
            if (curr) 
            {
                if (prev)
                {
                    prev->left = nullptr;
                    prev->right = curr;                   
                }
                prev = curr;
                stack.emplace(curr->right);
                curr = curr->left;
            }
            else
            {
                curr = stack.top();
                stack.pop();
            }
        }
    }
};
