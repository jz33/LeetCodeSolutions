#include <stdio.h>
#include <stdlib.h>
/*
61 Rotate List
https://oj.leetcode.com/problems/rotate-list/
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

/*
Find "newEnd" node from end by K steps
"ctr" is init as 0
*/
void findNewEnd(node* st, const int K, int* ctr, node** newEnd){
    node* t;
	if(st->next != 0) findNewEnd(st->next,K,ctr,newEnd);

	if(*ctr == K){
	    *newEnd = st;
		*ctr += 1;
	} else if (*ctr < K) {
		*ctr = *ctr+1;
	} 
}
/*
 0->1->2->3->4->5, 2 => 4->5->0->1->2->3
 0->1->2->3->4->5, 3 => 3->4->5->0->1->2
 0->1->2->3->4->5, 4 => 2->3->4->5->0->1
*/
node* rotateK(node* st, const int K){
    node *newEnd, *newHead, *p;
    int ctr;
	
	if(K<1) return st;
    
    newEnd = 0;
    ctr = 0;
    findNewEnd(st,K,&ctr,&newEnd);
    if(newEnd==0) return st;
    
    newHead = newEnd->next;
    newEnd->next = 0;
    
    p = newHead;
    while(p->next != 0) p = p->next;
    p->next = st;
    
    return newHead;
}

int main(){
	int repeat = 7; // will create repeat + 1 nodes
    int K;
    int i;
    node* head = (node*)malloc(sizeof(node));
    node* p = head;
    
    // init
    head->rank = 0;
    for(i=0;i<repeat;i++){
        p->next = (node*)malloc(sizeof(node));
        p = p->next;
        p->rank = i+1;
        p->next = 0;
    }
    
    // print
    p = head;
    while(p != 0){
        printf("%d ",p->rank);
        p = p->next;
    }
    printf("\n");
    
	// test K = [1,repeat]
	for(K=1;K<=repeat+1;K++){
		head = rotateK(head,K);
		// print
		p = head;
		while(p != 0){
			printf("%d ",p->rank);
			p = p->next;
		}
		printf("\n");
	}
    
    //free
    while(head != 0){
        p = head->next;
        free(head);
        head = p;
    }
    return 0; 
}