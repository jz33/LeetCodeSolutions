/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode node;

int maxDepth(node* n)
{
    int lt,rt;
    if(n == 0)
    {
        return 0;
    }
    else if(n->left != 0 && n->right != 0)
    {
        lt = maxDepth(n->left);
        rt = maxDepth(n->right);
        return  (lt > rt ? lt : rt) + 1;
    }
    else if(n->left != 0 && n->right == 0)
    {
        return maxDepth(n->left) + 1;
    }
    else if(n->left == 0 && n->right != 0)
    {
        return maxDepth(n->right) + 1;
    }
    else
    {
        return 1;
    }
}
