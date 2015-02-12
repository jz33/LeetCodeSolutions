#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
/*
124 Binary Tree Maximum Path Sum
https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/
*/
#define MAX(a,b) (a)>(b)?(a):(b)
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
int maxPathSum(node* n, int* sum){
    int lt,rt,singleChoice;
    if(n==0) return 0;
    
    lt = maxPathSum(n->pl,sum);
    rt = maxPathSum(n->pr,sum);
	/*
	"singleChoice" is to choose one of the children 
	plus current node value
	*/
    singleChoice = MAX(n->rank,MAX(lt,rt)+n->rank);

	/*
	"sum" is either "singleChoice" or use current node as
	root plus both children
	*/
    *sum = MAX(*sum,MAX(singleChoice,lt+rt+n->rank));
    return singleChoice;
}

// tester
int main()
{
#define NUM 7
    int arr[NUM];
    int i,sum;
    node* n = assign(-1);
    for(i=0;i<NUM;i++){
        arr[i] = i;
    }
    initInOrder(n,arr,0,NUM-1);
	inorder(n);printf("\n");

    sum = INT_MIN;
    maxPathSum(n,&sum);
    printf("%d\n",sum);
    
    destroyPostOrder(n);
    return 0;
}