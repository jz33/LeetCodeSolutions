/*
10 Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
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
#include <queue>
#include <utility>

class Solution {
public:
    
    // An iterative method
    bool isSymmetric(TreeNode* root)
    {
        if (!root)
        {
            return true;
        }
        
        std::queue<std::pair<TreeNode*, TreeNode*>> queue;
        queue.emplace(root->left, root->right);
        
        while (!queue.empty())
        {
            auto pair = queue.front();
            queue.pop();
            
            auto left = pair.first;
            auto right = pair.second;
            
            if ((!left && right) || (left && !right))
            {
                return false;
            }
            if (left && right)
            {
                if (left->val != right->val) 
                {
                    return false;
                }
                
                queue.emplace(left->left, right->right);
                queue.emplace(left->right, right->left);
            }
        }
        return true;
    }
};
