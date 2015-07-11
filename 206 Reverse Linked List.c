/*
Reverse Linked List 
https://leetcode.com/problems/reverse-linked-list/

Iterative way & recursive way
*/

struct ListNode {
    int val;
    struct ListNode *next;
};
typedef struct ListNode lnode;

// recursively
lnode* reverseList(lnode* curr)
{
    lnode* head;
    if(curr == 0 || curr->next == 0) return curr;
    if(curr->next->next != 0)
        head = reverseList(curr->next);
    else
        head = curr->next;
    curr->next->next = curr;
    curr->next = 0;
    return head;
}
// iteratively
/*
lnode* reverseList(lnode* head)
{
    lnode *p0,*p1;
    if(head == 0) return 0;
    if(head->next == 0) return head;
    
    p0 = head->next;
    head->next = 0;
    while(p0->next != 0)
    {
        p1 = p0->next;
        p0->next = head;
        head = p0;
        p0 = p1;
    }
    p0->next = head;
    return p0;
}
*/

int main()
{
  return 0;
}
