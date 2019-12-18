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
           
int countNodes(Node* root)
{
    int depth = getLeftDepth(root);
    if (depth <= 1)
    {
        return depth;
    }
    
    // The total node count of complete tree is the sum of
    // inner node count + last row node count
    // To count last row node, it needs to find the "break point",
    // which is last node of the tree
    int lastRowCount = 0;
    Node* p = root;
    for (int d = depth-1; d > 0; --d)
    {
        // Check if left branch of p is full tree
        // by checking left branch's right depth
        int rightDepth = getRigthDepth(p->left);
        if (rightDepth == d)
        {
            // P's left branch is full tree, then non-full tree
            // can only exist in p->right
            // Add the node count of last row of left branch.
            lastRowCount += (1 << (d - 1));
            p = p->right;
        }
        else
        {
            // P's left branch is not full tree, move to left
            p = p->left;
        }
    }
    
    // Now p is on last row, either the last node of the tree or null
    if (p)
    {
        lastRowCount++;
    }
 
    // Plus inner complete tree node count
    return (1 << (depth - 1)) - 1 + lastRowCount;
}
