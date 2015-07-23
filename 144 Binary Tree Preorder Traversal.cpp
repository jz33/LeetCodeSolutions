#include <stack>
#include <vector>

Struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
};

vector<int> preorderTraversal(TreeNode* root)
{
    std::vector<int> ret;
    if(root == 0) return ret;
    
    std::stack<TreeNode*> st;
    TreeNode* p = root;
    while(!st.empty() || p != 0)
    {
        if(p != 0)
        {
            ret.push_back(p->val);
            st.push(p);
            p = p->left; 
        }
        else
        {
            p = st.top();
            st.pop();
            p = p->right;
        }
    }
    return ret;
}
