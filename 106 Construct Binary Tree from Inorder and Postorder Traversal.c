#include <stdio.h>
#include <stdlib.h>
/*
106 Construct Binary Tree from Inorder and Postorder Traversal
https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
*/
struct Binary_Search_Tree_Node{
    int rank;
    struct Binary_Search_Tree_Node *pl;
    struct Binary_Search_Tree_Node *pr;
};
typedef struct Binary_Search_Tree_Node node;

void destroyInOrder(node* n) {
	if(n != 0){
		destroyInOrder(n->pl);
		destroyInOrder(n->pr);
        free(n);
	}
}
void preorder(node* n){
    if(n != 0) {
		printf("%d ", n->rank);
        preorder(n->pl);
		preorder(n->pr);
	}
}
void inorder(node* n) {
	if(n != 0) {
		inorder(n->pl);
		printf("%d ", n->rank);
		inorder(n->pr);
	}
}
void postorder(node* n) {
	if(n != 0) {
		postorder(n->pl);
        postorder(n->pr);
		printf("%d ", n->rank);
	}
}
// find the index from an array, naive
int findIndex(int* arr, int lt, int rt, int tag){
    int i;
    for(i=lt;i<=rt;i++)
        if(arr[i]==tag) return i;
    return -1;
}
node* initFromInorderPostorder(int* in, int in_lt, int in_rt, int* post, int post_lt, int post_rt){
    node* n;
    int find;
    if(in_lt>in_rt || post_lt>post_rt) return 0;
    
    n = (node*)malloc(sizeof(node));
    n->rank = post[post_rt];
    if(in_lt==in_rt || post_lt==post_rt){
        n->pl = 0;
        n->pr = 0;
        return n;
    }
    find = findIndex(in,in_lt,in_rt,post[post_rt]);
    n->pl = initFromInorderPostorder(in,in_lt,find-1,post,post_lt,post_lt+find-in_lt-1);
    n->pr = initFromInorderPostorder(in,find+1,in_rt,post,post_rt-(in_rt-find),post_rt-1);
    return n;
}
// tester
int main(int argc, char** argv){
#define NUM 7
	int pre[NUM]  = {3,1,0,2,5,4,6};
    int in[NUM]   = {0,1,2,3,4,5,6};
    int post[NUM] = {0,2,1,4,6,5,3};
    node* n;

    n = initFromInorderPostorder(in,0,NUM-1,post,0,NUM-1);
    preorder(n);printf("\n");
    inorder(n);printf("\n");
    postorder(n);printf("\n");
    destroyInOrder(n);
    
    return 0;
}