/*
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
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
    bool isSameTree(TreeNode* p, TreeNode* q)
    {
        std::queue<std::pair<TreeNode*, TreeNode*>> queue;
        queue.emplace(p, q);
        
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
                
                queue.emplace(left->left, right->left);
                queue.emplace(left->right, right->right);
            }
        }
        return true;
    }
    
    bool isSubtree(TreeNode* s, TreeNode* t)
    {
        // Level order traverse s
        std::queue<TreeNode*> queue;
        queue.emplace(s);

        while (!queue.empty())
        {
            auto node = queue.front();
            queue.pop();
            
            if (node->val == t->val && isSameTree(node, t))
            {
                return true;
            }
            
            if (node->left)
            {
                queue.emplace(node->left);
            }
            if (node->right)
            {
                queue.emplace(node->right);
            }
        }
        return false;
    }
};
