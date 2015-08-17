#include <stdio.h>
#include <stdlib.h>
/*
105 Construct Binary Tree from Preorder and Inorder Traversal
https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
*/
typedef struct TreeNode node;
int findIndex(int* arr, int lt, int rt, int tag){
    int i;
    for(i=lt;i<=rt;i++)
        if(arr[i]==tag) return i;
    return -1; // not reachable 
}

node* initFromPreorderInorder(int* in, int in_lt, int in_rt, int* pre, int pre_lt, int pre_rt)
{
    node* n;
    int find;
    if(in_lt > in_rt || pre_lt > pre_rt) return 0;
    
    n = (node*)malloc(sizeof(node));
    n->val = pre[pre_lt];
    if(in_lt == in_rt || pre_lt==pre_rt)
    {
        n->left = 0;
        n->right = 0;
        return n;
    }
    find = findIndex(in,in_lt,in_rt,pre[pre_lt]);
    n->left  = initFromPreorderInorder(in, in_lt,  find-1, pre, pre_lt+1,            pre_lt+find-in_lt);
    n->right = initFromPreorderInorder(in, find+1, in_rt,  pre, pre_lt+find-in_lt+1, pre_rt);
    return n;
}

node* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize)
{
    node* n = initFromPreorderInorder(inorder, 0, inorderSize - 1, preorder, 0, preorderSize -1);
    return n;
}
