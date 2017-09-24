/*
Lowest Common Ancestor of a Binary Tree 
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
*/

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

 /*
 Assume $p, $q are in tree
 */
typedef struct TreeNode node;
node* rec(node* r, node* p, node* q, int* sofar)
{
    node *lt, *rt;
    if (r == 0) return 0;
    if (*sofar == 2) return 0; // found in other branch
    
    lt = rec(r->left, p,q,sofar);
    rt = rec(r->right,p,q,sofar);
    
    if (r == p || r == q)
    {
        *sofar = *sofar + 1;
        return r;
    }
    
    if(lt != 0)
    {
        if(rt != 0) return r;
        else return lt;
    }
    else
    {
        if(rt != 0) return rt;
        else return 0;
    }
}

node* lowestCommonAncestor(node* root, node* p, node* q)
{
    int sofar = 0;
    return rec(root,p,q,&sofar);
}
