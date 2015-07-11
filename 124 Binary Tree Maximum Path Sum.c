#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
/*
124 Binary Tree Maximum Path Sum
https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/
*/
#define MAX(a,b) ((a)>(b)?(a):(b))
struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct TreeNode node;

int rec(node* n, int* sum)
{
    int lt,rt,singleChoice;
    if(n==0) return 0;
    
    lt = rec(n->left,sum);
    rt = rec(n->right,sum);
    
	/*
	"singleChoice" is to choose one of the children 
	plus current node value
	*/
    singleChoice = MAX(n->val,MAX(lt,rt) + n->val);

	/*
	"sum" is either "singleChoice" or use current node as
	root plus both children
	*/
    *sum = MAX(*sum, MAX(singleChoice,lt + rt + n->val));
    return singleChoice;
}
int maxPathSum(node* root)
{
    int sum;
    if(root == 0) return 0;
    sum = root->val;
    rec(root,&sum);
    return sum;
}
int main()
{
    return 0;
}
