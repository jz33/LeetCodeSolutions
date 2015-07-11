#include <stdio.h>
#include <stdlib.h>
/*
Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
*/
struct Binary_Search_Tree_Node
{
    int rank;
    struct Binary_Search_Tree_Node *pl;
    struct Binary_Search_Tree_Node *pr;
};
typedef struct Binary_Search_Tree_Node node;

node* assign(int rank)
{
    node* n = (node*)malloc(sizeof(node));
    n->rank = rank;
    n->pl = 0;
    n->pr = 0;
    return n;
}
void initInOrder(node* n, int* arr, int start, int end)
{
    int mid = (start+end)>>1;
    n->rank = arr[mid];

    if(start <= mid-1) {
        n->pl = assign(-1);
        initInOrder(n->pl, arr, start, mid-1);
    }
    if(mid+1 <= end) {
        n->pr = assign(-1);
        initInOrder(n->pr, arr, mid+1, end);
    }
}
void inorder(node* n)
{
    if(n != 0){
        inorder(n->pl);
        printf("%d ",n->rank);
        inorder(n->pr);
    }
}
void destroyPostOrder(node* n)
{
    if(n != 0){
        destroyPostOrder(n->pl);
        destroyPostOrder(n->pr);
        free(n);
    }
}

void rec(node* n)
{
    node* t;
    if(n != 0)
    {
       t = n->pl;
       n->pl = n->pr;
       n->pr = t;
       
       rec(n->pl);
       rec(n->pr);
    }
}

node* invertTree(node* root)
{
    rec(root);
    return root;
}

int main()
{
#define NUM 7
    int arr[NUM];
    int i;
    node* n = assign(-1);
    for(i=0;i<NUM;i++){
        arr[i] = i;
    }
    initInOrder(n,arr,0,NUM-1);
    inorder(n);printf("\n");

    n = invertTree(n);
    inorder(n);printf("\n");
    
    destroyPostOrder(n);
    return 0;
}
