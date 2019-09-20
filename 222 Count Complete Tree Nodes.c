'''
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode Node;

int getLeftDepth(Node* n)
{
    int d = 0;
    while (n)
    {
        n = n->left;
        d++;
    }
    return d;
}

int getRigthDepth(Node* n)
{
    int d = 0;
    while (n)
    {
        n = n->right;
        d++;
    }
    return d;
}

// Get node count of full complete tree
int getFullTreeNodeCount(int depth)
{
    return (1 << depth) - 1;
}

// Get last row node count of complete tree
int getFullTreeLastRowNodeCount(int depth)
{
    return (1 << (depth - 1));
}
                
int countNodes(struct TreeNode* root)
{
    int d, rightDepth, lastRowCount;
    Node* p = root;
    int depth = getLeftDepth(root);
    if (depth <= 1)
        return depth;
    
    // The total node count of complete tree is the sum of
    // inner node count + last row node count
    // To count last row node, it needs to find the "break point",
    // which is last node of the tree
    lastRowCount = 0;
    for (d = depth-1; d > 0; --d)
    {
        // First check if left node of p is full tree
        rightDepth = getRigthDepth(p->left);
        if (rightDepth == d)
        {
            // The p->left is full tree, then non-full tree
            // can only exist in p->right
            lastRowCount += getFullTreeLastRowNodeCount(d);
            p = p->right;
        }
        else
        {
            // The p->left is non-full tree, move to left,
            // try find break point
            p = p->left;
        }
    }
    
    // Now p is on last row.
    // The p should be the last node of the tree or
    // the next node of last node of the tree
    if (p)
    {
        lastRowCount++;
    }
 
    return getFullTreeNodeCount(depth-1) + lastRowCount;
}
