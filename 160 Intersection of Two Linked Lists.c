#include <stdio.h>
#include <stdlib.h>
/*
160 Intersection of Two Linked Lists
https://oj.leetcode.com/problems/intersection-of-two-linked-lists/
http://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

#define NEWNODE (node*)malloc(sizeof(node))

/*
Find "newEnd" node from end by K steps
"ctr" is init as 0
*/
node* findIntersection(node* x, node* y){
    int lx,ly,diff;
    node *p, *q;
    if(x == 0 || y == 0) return 0;
    
    // 0. count length of both lists
    lx = 0;
    p = x;
    while(p!=0) lx++,p=p->next;
	ly = 0;
    p = y;
    while(p!=0) ly++,p=p->next;
    
    // 1. move "diff" nodes from longer list
    diff = lx - ly;
	p = x;
	q = y;
	lx = 0; // re-use lx
    if(diff > 0){
		while(lx != diff) lx++,p=p->next;
	} else {
		while(lx != diff) lx--,q=q->next;
	}
    
    // 2. move both parallel, compare address
    while(p != 0 && q != 0){
        if(p==q) return p;
        p = p->next;
        q = q->next;
    }
    return 0;
}
/*
   0->1->2->3->4->5
         |
-1->-2->-3
*/
int main(){
    node* x = NEWNODE;
    node* y = NEWNODE;
    node *p, *intersection;
    int i;

    // init
    x->rank = 0;
    p = x;
    for(i=0;i<5;i++){
        p->next = NEWNODE;
        p = p->next;
        p->rank = i+1;
        p->next = 0;
    }
    
    y->rank = -1;
    p = y;
    for(i=0;i<2;i++){
        p->next = NEWNODE;
        p = p->next;
        p->rank = -i-2;
        p->next = 0;
    }
    p->next = x->next->next;
    
    // test
	intersection = findIntersection(x,y);
    
    // free
	while(y != intersection){
        p = y->next;
        free(y);
        y = p;
    }
    while(x != 0){
        p = x->next;
        free(x);
        x = p;
    }
    return 0; 
}