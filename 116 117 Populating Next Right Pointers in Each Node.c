#include <stdio.h>
#include <stdlib.h>
/*
Populating Next Right Pointers in Each Node
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
Populating Next Right Pointers in Each Node II
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
*/
#define MAX(a,b) (a)>(b)?(a):(b)
struct Binary_Search_Tree_Node_WITH_NEXT
{
    int rank;
    struct Binary_Search_Tree_Node_WITH_NEXT *pl;
    struct Binary_Search_Tree_Node_WITH_NEXT *pr;
    struct Binary_Search_Tree_Node_WITH_NEXT *nt;
};
typedef struct Binary_Search_Tree_Node_WITH_NEXT node;

node* assign(int rank)
{
    node* n = (node*)malloc(sizeof(node));
    n->rank = rank;
    n->pl = 0;
    n->pr = 0;
    n->nt = 0;
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
void destroyInOrder(node* n)
{
	if(n != 0){
		destroyInOrder(n->pl);
		destroyInOrder(n->pr);
        free(n);
	}
}
// Notice pr is traversed before pl
void* connect2Next(node* root)
{
    node *p, *q;
    if(root == 0) return;
    if(root->nt == 0){
        if(root->pr != 0){root->pr->nt = 0;}
        if(root->pl != 0){root->pl->nt = root->pr;}
    } else {
        p = root->nt;
        q = 0;
        while(p != 0){
            if(p->pl != 0){q = p->pl; break;}
            if(p->pr != 0){q = p->pr; break;}
            p = p->nt;
        }
        if(root->pr != 0){root->pr->nt = q;}
        if(root->pl != 0 && root->pr != 0){root->pl->nt = root->pr;}
        if(root->pl != 0 && root->pr == 0){root->pl->nt = q;}
    }
    connect2Next(root->pr);
    connect2Next(root->pl);
}
// tester
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

    connect2Next(n);
    destroyInOrder(n);
    return 0;
}