#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
/*
92 Reverse Linked List II
https://oj.leetcode.com/problems/reverse-linked-list-ii/
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

void dumpList(node* p){
    while(p != 0){
        printf("%d ",p->rank);
        p = p->next;
    }
    printf("\n");
}

node* allocNode(int rank){
    node* p = (node*)malloc(sizeof(node));
    p->rank = rank;
    p->next = 0;
    return p;
}

node* createFromArray(int* arr, const int N){
    int i;
    node *head, *p;
    assert(N>0);

    head = allocNode(*arr++);
    p = head;
    
    for(i =1;i<N;i++){
        p->next = allocNode(*arr++); 
        p = p->next;
    }
    return head;
}
/*
Reverse first "rt" nodes
Original head node will point to rt+1 node
*/
node* reverseTo(node* lls, int rt){
    node *p,*q,*head;
    int i;
    assert(lls != 0 && rt > 0);
    
    head = lls;
    p = head->next;
    q = 0;
    i = 1;
    while(i++ < rt){
        q = p->next;
        if(q == 0) break;
        p->next = head;
        head = p;
        p = q;
    }
    lls->next =  p->next; // NOTICE !
    p->next = head;
    return p;
}
/*
Notice lt & rt is index + 1
*/
node* reverseRange(node* lls, int lt, int rt){
    node *ret, *head;
    int i;
    assert(lls != 0 && lt > 0 && lt <= rt);
    
    if(lt == rt) return lls;
    
    if(lt == 1){
        ret = reverseTo(lls,rt-lt); 
    } else {
        ret = lls;
        i = 1;
        head = lls;
        while(i++ < lt-1) head = head->next;
        head->next = reverseTo(head->next,rt-lt); 
    }
    return ret;
}

int main(){
    int i;
	int lt = 2;
	int rt = 4;
    int arr[] = {0,1,2,3,4,5};
    
    // init
    node* head = createFromArray(arr,sizeof(arr)/sizeof(int));
    node* p = head;
    
    dumpList(head);    
    
    // test
    head = reverseRange(head,lt,rt);
    dumpList(head);    

    //free
    while(head != 0){
        p = head->next;
        free(head);
        head = p;
    }
    return 0; 
}