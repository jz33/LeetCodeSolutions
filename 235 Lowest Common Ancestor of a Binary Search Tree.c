/*
Lowest Common Ancestor of a Binary Search Tree 
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
*/
struct TreeNode 
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct TreeNode node;

node* lowestCommonAncestor(node* r, node* p, node* q)
{
    node* t;
    if(p->val > q->val)
    {
        t = p;
        p = q;
        q = t;
    }
    
    while(r != 0)
    {
        if(r->val < p->val) r = r->right;
        else if(r->val > q->val) r = r->left;
        else return r;
    }
    return r;
}

int main()
{
    return 0;
}
