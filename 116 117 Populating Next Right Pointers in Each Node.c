#include <stdio.h>
#include <stdlib.h>
/*
Populating Next Right Pointers in Each Node
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
Populating Next Right Pointers in Each Node II
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
*/
#define MAX(a,b) (a)>(b)?(a):(b)
struct TreeLinkNode {
    int rank;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
};
typedef struct TreeLinkNode node;

void connect(node *root) {
    node *p, *tag;
    if(root == 0) return;
    p = root->next;
    tag = 0;
    while(p != 0) {
        if(p->left != 0) {tag = p->left;  break;}
        if(p->right != 0){tag = p->right; break;}
        p = p->next;
    }
    if(root->right != 0) {
        root->right->next = tag; // tag can be 0
    }
    if(root->left != 0) {
        if (root->right != 0) {
            root->left->next = root->right;
        } else {
            root->left->next = tag;
        }
    }
    connect(root->right);
    connect(root->left);
}
