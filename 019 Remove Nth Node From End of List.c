#include <stdio.h>
#include <stdlib.h>
/*
19 Remove Nth Node From End of List
https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
*/
struct LinkedListNode
{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode lnode;

lnode* initList(int* arr, int size)
{
    int i;
    lnode *head,*p;
    if(size < 1) return 0;
    
    head = (lnode*)malloc(sizeof(lnode));
    head->rank = arr[0];
    head->next = 0;
    p = head;
    for(i=1;i<size;i++)
    {
       p->next = (lnode*)malloc(sizeof(lnode));
       p = p->next;
       p->rank = arr[i];
    }
    p->next = 0;
    return head;
}
void printList(lnode* p)
{
    while(p != 0){
        printf("%d ",p->rank);
        p = p->next;
    }
    printf("\n");
}
void freeList(lnode* head)
{
    lnode* p = head;
    while(p != 0){
        head = p->next;
        free(p);
        p = head;
    }
}
/*
Assume n is NOT necessarily valid
*/
lnode* removeNthFromEnd(lnode* head, int n)
{
    lnode *p,*r;
    int count;
    if(head == 0 || n < 1) return head;
    
    p = head;
    count = 0;
    while(p != 0 && count != n){
        p = p->next;
        count++;
    }
    
    // out of bound
    if(count < n) return head;
    
    r = head;
    
    // remove head
    if(p == 0)
    {
        head = head->next;
        free(r);
        return head;
    }
    
    while(p->next != 0)
    {
        p = p->next;
        r = r->next;
    }
    
    // remove
    p = r->next;
    r->next = p->next;
    free(p);
    
    return head;
}

void test(void)
{
    int arr[] = {0,1,2,3,4,5};
	int i;
    lnode* head = initList(arr,sizeof(arr)/sizeof(int));
    printList(head);
    
	head = removeNthFromEnd(head,6);
    
    printList(head);
    freeList(head);
}
int main()
{
    test();
    return 0;
}
