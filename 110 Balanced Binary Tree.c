/*
Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
An approach based on "Maximun depth of Binary Tree"
*/
typedef struct TreeNode node;

int depth(node* n)
{
    int lt,rt;
    if(n == 0) return 0;
  
    lt = depth(n->left);
    if(lt == -1) return -1;
    
    rt = depth(n->right);
    if(rt == -1) return -1;
    
    if(lt - rt > 1 || rt - lt > 1) return -1;
    else return (lt > rt ? lt : rt ) + 1;
}

bool isBalanced(node* root)
{
    return depth(root) != -1;
}
