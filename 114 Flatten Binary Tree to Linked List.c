/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode node;

void preOrder(node* curr, node** prev)
{
    node* right;
    if(curr == 0) return;
    
    (*prev)->left  = 0;
    (*prev)->right = curr;
    *prev = curr;
    
    right = curr->right;
    preOrder(curr->left, prev);
    preOrder(right,prev);
} 

void flatten(node* curr)
{
    node *prev, *right;
    if(curr == 0) return;
    prev = curr;
    
    right = curr->right;
    preOrder(curr->left, &prev);
    preOrder(right,&prev);
}
