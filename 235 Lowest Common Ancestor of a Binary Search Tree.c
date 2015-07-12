struct TreeNode 
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct TreeNode node;

/*
Natively, assume $p, $q are in tree
*/
node* lowestCommonAncestor(node* root, node* p, node* q)
{
    node *lt, *rt;
    if(root == 0) return 0;
    
    lt = lowestCommonAncestor(root->left,p,q);
    rt = lowestCommonAncestor(root->right,p,q);
    
    if(root == p || root == q)
    {
        return root;
    }
    
    if(lt != 0 && rt != 0) return root;
    else if(lt != 0 && rt == 0) return lt;
    else if(lt == 0 && rt != 0) return rt;
    else return 0;
}

int main()
{
    return 0;
}
