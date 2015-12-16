/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <unordered_map>

class Solution {
public:
    void dumpVec(vector<int> vec){
        for(auto i = vec.begin();i!=vec.end();i++){
            std::cout<<*i<<" ";
        }
        std::cout<<"\n";
    }

    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root == 0) return res;
        unordered_map<int, vector<int>> map;
        
        int minLevel = 0;
        int maxLevel = 0;
        queue<pair<int,TreeNode*>> q;
        q.emplace(0,root);
        
        while(!q.empty()){
            auto p = q.front();
            int level = p.first;
            TreeNode* t = p.second;
            q.pop();
            
            minLevel = level < minLevel ? level : minLevel;
            maxLevel = level > maxLevel ? level : maxLevel;
            
            if(map.find(level) == map.end()){
                vector<int> row;
                row.push_back(t->val);
                map[level] = row;
            } else {
                map[level].push_back(t->val);
            }
            
            if(t->left  != 0) q.emplace(level - 1, t->left );
            if(t->right != 0) q.emplace(level + 1, t->right);
        }
        for(int i = minLevel;i <= maxLevel;i++){
            if(map.find(i) != map.end()){
                res.push_back(map[i]);
            }
        }
        return res;
    }
};
