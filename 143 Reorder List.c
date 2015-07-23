#include <stdio.h>
#include <stdlib.h>
/*
Reorder List
https://leetcode.com/problems/reorder-list/
*/
struct ListNode
{
    int rank;
    struct ListNode *next;
};
typedef struct ListNode lnode;

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

void rec(lnode** head, lnode* curr, int* stopped)
{
    if(curr->next != 0)
        rec(head,curr->next,stopped);

    if(*stopped == 0)
    {
        if((*head) == curr || (*head)->next == curr)
        {
            *stopped = 1;
            curr->next = 0;
        }
        else
        {
            curr->next = (*head)->next;
            (*head)->next = curr;
            *head = curr->next;
        }
    }
}
void reorderList(lnode* head)
{
    int stopped;
    if(head == 0 || head->next == 0) return;
    
    stopped = 0;
    rec(&head,head->next, &stopped);
}

void test(void)
{
    int arr[] = {1,2,3};
    int i;
    lnode* head = initList(arr,sizeof(arr)/sizeof(int));
    printList(head);

    reorderList(head);

    printList(head);
    freeList(head);
}
int main()
{
    test();
    return 0;
}
