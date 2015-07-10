struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct TreeNode node;

int target;
int result;
int counter;

void rec(node* root)
{
    if(root != 0 && counter < target)
    {
        rec(root->left);
        
        counter++;
        if(counter == target)
        {
            result = root->val;
        }
        
        rec(root->right);
    }
}

int kthSmallest(node* root, int k)
{
    target = k;
    result = -1;
    counter = 0;
    rec(root);
    return result;
}

int main()
{
  return 0;
}
