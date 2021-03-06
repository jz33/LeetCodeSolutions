/*
117. Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
*/
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() {}

    Node(int _val, Node* _left, Node* _right, Node* _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
public:

    // Exactly same solution as 116. Populating Next Right Pointers in Each Node
    Node* connect(Node* root) {
        
        if (!root)
        {
            return root;
        }
        
        std::queue<Node*> queue;
        queue.push(root);
        
        while (!queue.empty())
        {
            const size_t length = queue.size();
            Node* curr = nullptr;
            Node* prev = nullptr;

            for (int i = 0; i< length; i++)
            {
                curr = queue.front();
                queue.pop();
                
                if (prev)
                {
                    prev->next = curr;
                }
                prev = curr;
                
                if (curr->left)
                {
                    queue.emplace(curr->left);
                }
                if (curr->right)
                {
                    queue.emplace(curr->right);
                }
            }
        }
        
        return root;
    }
};
