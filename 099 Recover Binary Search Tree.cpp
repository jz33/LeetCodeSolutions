/*
99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
   
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
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
#include <algorithm>

class Solution {
public:
    void recoverTree(TreeNode* root)
    {
        // These 2 are the missplaced nodes
        // For an inorder traversal, result array is like:
        // ... -> left -> .... -> right ->...
        // therefore left > left + 1, right < right - 1
        TreeNode* left = nullptr;
        TreeNode* right = nullptr;
        int howManyAbnormalNodesFound = 0; // Should found 2
        
        std::stack<TreeNode*> stack;
        TreeNode* curr = root; // current node
        TreeNode* prev = nullptr; // previous node
        while (curr || !stack.empty() && howManyAbnormalNodesFound < 2)
        {
            if (curr)
            {
                stack.push(curr);
                curr = curr->left;
            }
            else
            {
                curr = stack.top();
                stack.pop();
                
                if (prev && curr->val < prev->val)
                {
                    // Found abnormal node
                    // Must found left first
                    
                    ++howManyAbnormalNodesFound;                
                    if (!left)
                    {
                        left = prev;
                        
                        // Assign right too, as right can be next node of left
                        right = curr; 
                    }
                    else
                    {
                        right = curr;
                    }                  
                }
                
                prev = curr;
                curr = curr->right;
            }
        }
        
        if (left && right)
        {
            std::swap(left->val, right->val);
        }
    }
};
