#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
/*
99 Recover Binary Search Tree
https://oj.leetcode.com/problems/recover-binary-search-tree/

Inspired by "Validate Binary Search Tree"
*/
struct Binary_Search_Tree_Node{
    int rank;
    struct Binary_Search_Tree_Node *pl;
    struct Binary_Search_Tree_Node *pr;
};
typedef struct Binary_Search_Tree_Node node;

node* emptyNode(){
    node* n = (node*)malloc(sizeof(node));
    n->rank = -1;
    n->pl = 0;
    n->pr = 0;
    return n;
}
void initInOrder(node* n, int* arr, int start, int end){
	int mid = (start+end)>>1;
	n->rank = arr[mid];
	
	if(start <= mid-1) {
		n->pl = emptyNode();
		initInOrder(n->pl, arr, start, mid-1);
	}
	if(mid+1 <= end) {
		n->pr = emptyNode();
		initInOrder(n->pr, arr, mid+1, end);
	}
}
void destroyInOrder(node* n) {
	if(n != 0){
		destroyInOrder(n->pl);
		destroyInOrder(n->pr);
        free(n);
	}
}
// standard inorder traversal, recursively
void inorder(node* n) {
	if(n != 0) {
		inorder(n->pl);
		printf("%d ", n->rank);
		inorder(n->pr);
	}
}
void minMax(node* head, int minRank, int maxRank, node** lt, node** rt){
    if(head != 0 && (*lt == 0 || *rt == 0)){
        if(head->rank < minRank){
            *rt = head;
        }
        if(head->rank > maxRank){
            *lt = head;
        } 
        if(*lt == 0 || *rt == 0){
            minMax(head->pl, minRank, head->rank, lt,rt);
            minMax(head->pr, head->rank, maxRank, lt,rt);
        }
    }
}
void recover(node* head){
    node *lt,*rt;
    int minRank,maxRank,t;
    if(head == 0) return;
    
    lt = 0;
    rt = 0;
    minRank = INT_MIN;
    maxRank = INT_MAX;
    minMax(head,minRank,maxRank,&lt,&rt);
    
    if(lt != 0 && rt != 0){
        t = lt->rank;
        lt->rank = rt->rank;
        rt->rank = t;
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
    arr[2] = 5;
    arr[5] = 2;
    initInOrder(n,arr,0,NUM-1);
    inorder(n);putchar('\n');
    
    recover(n);
    inorder(n);putchar('\n');
    
    destroyInOrder(n);
    return 0;
}