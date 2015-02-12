#include <stdio.h>
#include <stdlib.h>
/*
24 Swap Nodes in Pairs
https://oj.leetcode.com/problems/swap-nodes-in-pairs/
More tricky than it looks like
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

void printList(node* p){
    while(p != 0){
        printf("%d ",p->rank);
        p = p->next;
    }
    printf("\n");
}

/*
 0->1->2->3->4->5 => 1->0->3->2->5->4
 0->1->2->3->4    => 1->0->3->2->4
 prev even oddy next
*/
node* swapPairs(node* even){
    node *prev = 0, *oddy, *next, *ret;
	if(even == 0 || even->next == 0) return even;
	ret = even->next;

	oddy = even->next;
	next = oddy->next;
	oddy->next = even;
    prev = even;
    even = next;

    while(even != 0){
        oddy = even->next;
        if(oddy == 0){
            prev->next = even;
            return ret;
        }
        prev->next = oddy;
        next = oddy->next;
        oddy->next = even;
        prev = even;
        even = next;
    }
	prev->next = 0;
    return ret;
}

int main(){
	int repeat = 6;
    //int repeat = 3;
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

    printList(head);
    head = swapPairs(head);
    printList(head);
    
    //free
    while(head != 0){
        p = head->next;
        free(head);
        head = p;
    }
    return 0; 
}