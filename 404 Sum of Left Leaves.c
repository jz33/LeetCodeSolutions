/*
404 Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves
*/
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct TreeNode Node;

void rec(Node* p, int toLeft, int* sum)
{
    if (p == 0) return;
    if (p->left == 0 && p->right == 0)
    {
        if(toLeft) *sum = *sum + p->val;
        return;
    }
    rec(p->left, 1, sum);
    rec(p->right, 0, sum);
}

int sumOfLeftLeaves(Node *root)
{
    int sum = 0;
    rec(root,0,&sum);
    return sum;
}
