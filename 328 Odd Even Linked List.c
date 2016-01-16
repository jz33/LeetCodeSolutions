#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
/*
Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/
*/
struct LinkedListNode{
    int val;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode Node;

Node* newNode(int v){
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = v;
    n->next = 0;
    return n;
}

Node* oddEvenList(Node* head){
    Node *lt, *rt, *tag;
    if(head == 0) return head;
    lt = head;
    rt = lt->next;
    while(rt != 0 && rt->next != 0){
        tag = rt->next;
        rt->next = tag->next;
        tag->next = lt->next;
        lt->next = tag;
        lt = lt->next;
        rt = rt->next;
    }
    return head;
}

Node* fromArray(int* arr, int size){
    int i;
    Node* head, *p;
    assert(size > 0);
    head = newNode(arr[0]);
    p = head;
    for(i = 1;i<size;i++){
        p->next = newNode(arr[i]);
        p = p->next;
    }
    return head;
}

void deleteList(Node* head){
    Node* prev = 0;
    while(head != 0){
        prev = head;
        head = head->next;
        free(prev);
    }
}

void printList(Node* p){
    while(p != 0){
        printf("%d\n",p->val);
        p = p->next;
    }
}

int main(){
    int arr[] = {0,1,2,3,4,5,6,7};
    Node* head = fromArray(arr, sizeof(arr)/sizeof(int));
    printList(head);
    head = oddEvenList(head);
    printList(head);
    deleteList(head);
    return 0;
}
