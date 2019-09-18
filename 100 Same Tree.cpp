/*
100. Same Tree
https://leetcode.com/problems/same-tree/

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
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
};

// Recursive (C code)
bool isSameTree(struc TreeNode* p, struc TreeNode* q) {
    if(p == 0 && q == 0) return 1;
    if(p == 0 || q == 0) return 0;
    if(p->val != q->val) return 0;
    return isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
}
