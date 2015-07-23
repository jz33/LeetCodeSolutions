#include <stdio.h>
#include <stdlib.h>
/*
138 Copy List with Random Pointer
https://oj.leetcode.com/problems/copy-list-with-random-pointer/
*/
struct RandomListNode
{
    int rank;
    struct RandomListNode* next;
    struct RandomListNode* jump;
};
typedef struct RandomListNode lnode;

#define NEWNODE (lnode*)malloc(sizeof(lnode))

lnode* initList(int* arr, int size)
{
    int i;
    lnode *head,*p;
    if(size < 1) return 0;
    
    head = NEWNODE;
    head->rank = arr[0];
    head->next = 0;
    p = head;
    for(i=1;i<size;i++)
    {
       p->next = NEWNODE;
       p->jump = p->next;
       p = p->next;
       p->rank = arr[i];
    }
    p->next = 0;
    p->jump = head;
    return head;
}
void printList(lnode* p)
{
    while(p != 0)
    {
        printf("%d ",p->rank);
        if(p->jump != 0) printf("%d ",p->jump->rank);
        printf("\n");
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
lnode* copyRandom(lnode* old)
{
    lnode *res, *pold, *pnew;
    if(old == 0) return 0;
    
    res = NEWNODE;
    pold = old;
    pnew = res;
    
    // 0. insert new nodes
    while(pold != 0)
    {
        if(pnew != res) pnew = NEWNODE;
        
        //copy
        pnew->rank = pold->rank;
        pnew->next = pold->next;
        pnew->jump = pold->jump;
        
        // insert & move
        pold->next = pnew;  
        pold = pnew->next;
        pnew = 0;
    }
    
    //printList(res);
    
    // 1. modify jump nodes
    pnew = old;
    while(pnew != 0)
    {
        pnew = pnew->next; // now at new node
        if(pnew->jump != 0) 
            pnew->jump = pnew->jump->next;
        pnew = pnew->next; // now at old node or NULL
    }
    
    // 2. split
    pold = old;
    pnew = res;
    while(pnew->next != 0)
    {
        pold->next = pnew->next;
        pold = pold->next;
        pnew->next = pold->next;
        pnew = pnew->next;
    }
    pold->next = 0;
    return res;
}

void test(void)
{
    int arr[] = {1,2,3};
    int i;
    lnode* head = initList(arr,sizeof(arr)/sizeof(int));
    lnode* pnew;
    printList(head);

    pnew = copyRandom(head);

    printList(pnew);
    freeList(head);
}
int main()
{
    test();
    return 0;
}
