#include <stdio.h>
#include <stdlib.h>
/*
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
*/
struct ListNode
{
    int val;
    struct ListNode* next;
};
typedef struct ListNode lnode;

lnode* initList(int* arr, int size)
{
    int i;
    lnode *head,*p;
    if(size < 1) return 0;
    
    head = (lnode*)malloc(sizeof(lnode));
    head->val = arr[0];
    head->next = 0;
    p = head;
    for(i=1;i<size;i++)
    {
       p->next = (lnode*)malloc(sizeof(lnode));
       p = p->next;
       p->val = arr[i];
    }
    p->next = 0;
    return head;
}
void printList(lnode* p)
{
    while(p != 0){
        printf("%d ",p->val);
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
void printReversely(lnode* p)
{
    if(p == 0) return;
    printReversely(p->next);
    printf("%d ",p->val);
}
/*
1 2 3 3 2 1
1 2 3 4 3 2 1
*/
lnode* initPalindromicList(void)
{
    lnode* head = (lnode*)malloc(sizeof(lnode));
    lnode* p = head;
    int i,repeat = 3;
    for(i=0;i<repeat;i++)
    {   
        p->val = i+1;
        p->next = (lnode*)malloc(sizeof(lnode));
        p = p->next;
    }
    
    p->val = i+1;
    p->next = (lnode*)malloc(sizeof(lnode));
    p = p->next;
     
    for(i=repeat;i>1;i--)
    {   
        p->val = i;
        p->next = (lnode*)malloc(sizeof(lnode));
        p = p->next;
    }
    p->val = 1;
    p->next = 0;
    return head;
}
/*
Get middle node of linked list
0->1->2->3->4 => 2
0->1->2->3 => 2
*/
lnode* middle(lnode* head)
{
    lnode* f = head;
    while(f != 0 && f->next != 0)
    {
        f = f->next->next;;
        head = head->next;
    }
    return head;
}
/*
Reverse linked list, iteratively
*/
lnode* reverse(lnode* src)
{
    lnode *p1, *p2;
    if(src == 0) return 0;
    if(src->next == 0) return src;
    
    p1 = src->next;
    src->next = 0;
    p2 = p1->next;
    while(p2 != 0)
    {
        p1->next = src;
        src = p1;
        p1 = p2;
        p2 = p1->next;
    }
    p1->next = src;
    return p1;
}
/*
If palindromic list, iterative way
*/
int isPalindrome(lnode* src)
{
    lnode *mid, *rev;
    if(src == 0 || src->next == 0) return 1;
    mid = middle(src);
    rev = reverse(mid);
    
    while(src != mid && rev != mid)
    {
        if(src->val != rev->val)
            return 0;
        src = src->next;
        rev = rev->next;
    }
    return src->val == rev->val ? 1:0; 
}
void test_isPalindromicList(void)
{
    int status;
    lnode* head = initPalindromicList();
     
    printList(head);
    printReversely(head); printf("\n");
  
    status = isPalindrome(head);
    printf("Iterative status: %d\n",status);
}
int main()
{
    test_isPalindromicList();
    return 0;
}
