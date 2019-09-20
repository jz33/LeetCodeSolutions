'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
         
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <queue>
#include <algorithm>

class Solution
{
public:
    TreeNode* invertTree(TreeNode* root)
    {
        if (!root)
        {
            return root;
        }
        
        std::queue<TreeNode*> queue;
        queue.emplace(root);
        
        while (!queue.empty())
        {
            auto node = queue.front();
            queue.pop();
            
            std::swap(node->left, node->right);
            
            if (node->left)
            {               
                queue.emplace(node->left);
            }
            
            if (node->right)
            {               
                queue.emplace(node->right);
            }
        }
        return root;
    }
};
