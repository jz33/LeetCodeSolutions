/*
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
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
#include <algorithm> 

class Solution {
public:
    // The method returns the maximum sum from this root to down to ONE OF its leaves
    int getBranchSumRecursively(TreeNode* node, int* totalSum)
    {
        if (!node)
        {
            return 0;
        }

        auto leftBranchSum = getBranchSumRecursively(node->left, totalSum);
        auto rightBranchSum = getBranchSumRecursively(node->right, totalSum);
        
        // The maximum sum is either:
        // 1. Value of current node
        // 2. Current node value + left branch sum
        // 3. Current node value + right branch sum
        // 4. Current node value + left branch sum + right branch sum
        // The maximum of top 3 is the return value (called singleChoice)
        
        int singleChoiceArray[] = {node->val, node->val + leftBranchSum, node->val + rightBranchSum};
        int singleChoice = *std::max_element(singleChoiceArray, singleChoiceArray + 3);
        
        int totalSumArray[] = {*totalSum, singleChoice, node->val + leftBranchSum + rightBranchSum};
        *totalSum = *std::max_element(totalSumArray, totalSumArray + 3);
        
        return singleChoice;
    }
     
    int maxPathSum(TreeNode* root)
    {
        if (!root)
        {
            return 0;
        }
        
        int totalSum = root->val;
        
        getBranchSumRecursively(root, &totalSum);     
        return totalSum;
    }
};
