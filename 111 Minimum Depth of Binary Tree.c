typedef struct TreeNode node;
/*
The wrong answer
*/
int minDepthWrong(node* n)
{
    int lt,rt;
    if(n == 0)
    {
        return 0;
    }
    else
    {
        lt = minDepthWrong(n->left);
        rt = minDepthWrong(n->right);
        return  (lt < rt ? lt : rt) + 1;
    }
}

/*
The right answer
*/
int minDepth(node* n)
{
    int lt,rt;
    if(n == 0)
    {
        return 0;
    }
    else if(n->left != 0 && n->right != 0)
    {
        lt = minDepth(n->left);
        rt = minDepth(n->right);
        return  (lt < rt ? lt : rt) + 1;
    }
    else if(n->left != 0 && n->right == 0)
    {
        return minDepth(n->left) + 1;
    }
    else if(n->left == 0 && n->right != 0)
    {
        return minDepth(n->right) + 1;
    }
    else
    {
        return 1;
    }
}
