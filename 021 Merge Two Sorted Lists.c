#include <stdio.h>
#include <stdlib.h>
/*
21 Merge Two Sorted Lists
https://oj.leetcode.com/problems/merge-two-sorted-lists/
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

node* mergeTwoSorted(node* la, node* lb){
    node *ret, *p;
    if(la == 0) return lb;
    if(lb == 0) return la;

    if(la->rank < lb->rank){
        ret = la;
        la = la->next;
    } else {
        ret = lb;
        lb = lb->next;
    }

    p = ret;
    while(la != 0 && lb != 0){
        if(la->rank < lb->rank){
            p->next = la;
            la = la->next;
        } else {
            p->next = lb;
            lb = lb->next;
        }
        p = p->next;
    }
    
    // notice here is different from "Merge 2 sorted array"
    if(la != 0) p->next = la;
    if(lb != 0) p->next = lb;
    return ret;
}

int main(){
    int repeat = 7; // will create repeat + 1 nodes
    int K;
    int i;
    node* head = (node*)malloc(sizeof(node));
    node* hea2 = (node*)malloc(sizeof(node));
    node* p;

    // init
    p = head;
    p->rank = 0;
    for(i=0;i<repeat;i++){
        p->next = (node*)malloc(sizeof(node));
        p = p->next;
        p->rank = i+1;
        p->next = 0;
    }
    printList(head);

    // init
    p = hea2;
    p->rank = 0;
    for(i=0;i<repeat;i++){
        p->next = (node*)malloc(sizeof(node));
        p = p->next;
        p->rank = i*2+1;
        p->next = 0;
    }
    printList(hea2);

    // test
    p = mergeTwoSorted(head,hea2);
    printList(p);

    //free
    head = p;
    while(head != 0){
        p = head->next;
        free(head);
        head = p;
    }
    return 0; 
}