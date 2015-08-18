/*
Convert Sorted Array to Binary Search Tree 
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
*/
struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct TreeNode node;

void getBST(node* n, int* arr, int lt, int rt)
{
    int m = ((lt + rt) >> 1);
    n->val = arr[m];
    
    if(lt <= m-1)
    {
        n->left  = (node*)malloc(sizeof(node));
        getBST(n->left, arr,lt,m-1);
    }
    else 
        n->left = 0;
    
    if(m+1 <= rt)
    {
        n->right = (node*)malloc(sizeof(node));
        getBST(n->right,arr,m+1,rt);
    }
    else
        n->right = 0;
}

node* sortedArrayToBST(int* arr, int size)
{
    node* n = 0;
    if(size < 1) return n;
    
    n = (node*)malloc(sizeof(node));
    getBST(n,arr,0,size-1);
    
    return n;
}
