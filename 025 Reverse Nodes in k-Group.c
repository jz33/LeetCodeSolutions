#include <stdio.h>
#include <stdlib.h>
/*
25 Reverse Nodes in k-Group
https://oj.leetcode.com/problems/reverse-nodes-in-k-group/
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

/*
Reverse list from st by K steps
Notice it is guarenteed p != 0
*/
node* reverse(node* st, const int K){
    node *p, *nt;
    int i;
    if(st == 0) return st;
    
    p = st->next;
    st->next = 0;
	for(i=1;i<K;i++){
        nt = p->next;
        p->next = st;
        st = p;
        p = nt;
    }
    return st;
}
/*
 0->1->2->3->4->5, 2 => 1->0->3->2->5->4
 0->1->2->3->4->5, 3 => 2->1->0->5->4->3
 0->1->2->3->4->5, 4 => 3->2->1->0->4->5
*/
node* reverseK(node* st, const int K){
    node *pv = 0, *p, *ret;
    int i;
	
	if(K<1) return st;
    p = st;
	for(i=0;i<K;i++){
        if(p == 0) return st;
        p = p->next;
    }
    ret = reverse(st,K);
    pv = st;
    st = p;

    while(st != 0){
        p = st;
        for(i=0;i<K;i++){
            if(p == 0){
				pv->next = st;
				return ret;
			}
            p = p->next;
        }
        pv->next = reverse(st,K);
        pv = st;
		st = p;
    }
    return ret;
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
		head = reverseK(head,K);
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