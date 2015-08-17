#include <stdio.h>
#include <stdlib.h>
/*
106 Construct Binary Tree from Inorder and Postorder Traversal
https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
*/
typedef struct TreeNode node;
int findIndex(int* arr, int lt, int rt, int tag){
	int i;
	for(i=lt;i<=rt;i++)
	    if(arr[i]==tag) return i;
	return -1; // not reachable 
}

node* initFromInorderPostorder(int* in, int in_lt, int in_rt, int* post, int post_lt, int post_rt){
    node* n;
    int find;
    if(in_lt > in_rt || post_lt > post_rt) return 0;
    
    n = (node*)malloc(sizeof(node));
    n->val = post[post_rt];
    if(in_lt == in_rt || post_lt == post_rt){
        n->left = 0;
        n->right = 0;
        return n;
    }
    find = findIndex(in,in_lt,in_rt,post[post_rt]);
    n->left  = initFromInorderPostorder(in, in_lt , find-1, post, post_lt, post_lt+find-in_lt-1);
    n->right = initFromInorderPostorder(in, find+1, in_rt,  post, post_lt+find-in_lt, post_rt-1);
    return n;
}

node* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize)
{
	node* n = initFromInorderPostorder(inorder, 0, inorderSize - 1, postorder, 0, postorderSize -1);
	return n;
}
