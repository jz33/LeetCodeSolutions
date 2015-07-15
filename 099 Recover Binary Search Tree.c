#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
/*
99 Recover Binary Search Tree
https://oj.leetcode.com/problems/recover-binary-search-tree/
Inspired by "Validate Binary Search Tree"
*/
struct Binary_Search_Tree_Node{
    int val;
    struct Binary_Search_Tree_Node *left;
    struct Binary_Search_Tree_Node *right;
};
typedef struct Binary_Search_Tree_Node node;

node* emptyNode(){
    node* n = (node*)malloc(sizeof(node));
    n->val = -1;
    n->left = 0;
    n->right = 0;
    return n;
}
void initInOrder(node* n, int* arr, int start, int end){
	int mid = (start+end)>>1;
	n->val = arr[mid];
	
	if(start <= mid-1) {
		n->left = emptyNode();
		initInOrder(n->left, arr, start, mid-1);
	}
	if(mid+1 <= end) {
		n->right = emptyNode();
		initInOrder(n->right, arr, mid+1, end);
	}
}
void destroyInOrder(node* n) {
	if(n != 0){
		destroyInOrder(n->left);
		destroyInOrder(n->right);
        free(n);
	}
}
// standard inorder traversal, recursively
void inorder(node* n) {
	if(n != 0) {
		inorder(n->left);
		printf("%d ", n->val);
		inorder(n->right);
	}
}
/*
1 2 3 4 5 6 7
1 5 3 4 2 6 7 => 5 3 4 2 => 5 2
1 4 3 2 5 6 7 => 4 3 3 2 => 4 2
1 2 3 4 5 7 6 => 7 6 => 7 6
*/
void find(node* n, int* prev_val, node** prev, node** lt, node** rt)
{
    if(n != 0)
    {
        find(n->left,prev_val,prev,lt,rt);
        if(n->val < *prev_val)
        {
            if(*lt == 0)
            {
                *lt = *prev;
                *rt = n;
            }
            else
            {
                *rt = n;
                return;
            }
        }
        *prev = n;
        *prev_val = n->val;

        find(n->right,prev_val,prev,lt,rt);
    }
}
void recover(node* head)
{
    node *prev,*lt,*rt;
    int t,prev_val;
    if(head == 0) return;
    
    lt = 0;
    rt = 0;
    prev = 0;

    prev_val = INT_MIN;

    find(head,&prev_val,&prev,&lt,&rt);
    
    if(lt != 0)
    {
        t = lt->val;
        lt->val = rt->val;
        rt->val = t;
    }
}

#define NUM 7

int main(int argc, char** argv){

    int arr[NUM];
    int i;
    node* n = emptyNode();
    for(i=0;i<NUM;i++){
        arr[i] = i;
    }

    // twists
    arr[6] = 5;arr[5] = 6;
    //arr[0] = 6;arr[6] = 0;
    //arr[5] = 3;arr[3] = 5;
    //arr[5] = 1;arr[1] = 5;

    initInOrder(n,arr,0,NUM-1);
    inorder(n);putchar('\n');
    
    recover(n);
    inorder(n);putchar('\n');
    
    destroyInOrder(n);
    return 0;
}
