#include <iostream>
#include <stack>
/*
103 Binary Tree Zigzag Level Order Traversal
https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
*/
#define MAX(a,b) (a)>(b)?(a):(b)
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
void inorder(node* n) {
	if(n != 0) {
		inorder(n->pl);
		printf("%d ", n->rank);
		inorder(n->pr);
	}
}
//102
int getHeight(node* n){
    if(n == 0){return 0;}
    return MAX(getHeight(n->pl),getHeight(n->pr))+1;
}
void levelorderRec(node* n, int level){
    if(n == 0 || level < 1){return;}
    if(level == 1){printf("%d ",n->rank);}
    levelorderRec(n->pl,level-1);
    levelorderRec(n->pr,level-1);
}
void levelorder(node* n){
    int height = getHeight(n);
    int i;
    for(i=1;i<=height;i++){
        levelorderRec(n,i);
        printf("\n");
    }
    printf("\n");
}
//103
void zigzag(node* root){
    if(root==0) return;
    std::stack<node*> even;
    std::stack<node*> oddy;
    int isEvenLevel = 1;
    node* t;
    even.push(root);
    
    /*
    Notice for belowing implementation,
    the 2nd level is printed from rt -> lt.
    If 2nd level is required printed from lt -> rt,
    starts iteration from 2nd level
    */
    while(!even.empty() || !oddy.empty()){
        if(isEvenLevel){
            while(!even.empty()){
                t = even.top();
                even.pop();
                printf("%d ",t->rank);
                if(t->pl != 0) oddy.push(t->pl);
                if(t->pr != 0) oddy.push(t->pr);
            }
            isEvenLevel = 0;
        } else{
            while(!oddy.empty()){
                t = oddy.top();
                oddy.pop();
                printf("%d ",t->rank);
				// Notice here push pr first!
				if(t->pr != 0) even.push(t->pr);
                if(t->pl != 0) even.push(t->pl);    
            }
            isEvenLevel = 1;
        }
		printf("\n");
    }
}

// tester
int main(int argc, char** argv){
#define NUM 15
    int arr[NUM];
    int i;
    node* n = emptyNode();
    for(i=0;i<NUM;i++){
        arr[i] = i;
    }
    initInOrder(n,arr,0,NUM-1);
    inorder(n);putchar('\n');
    
    levelorder(n);
    zigzag(n);
    
    destroyInOrder(n);
    return 0;
}