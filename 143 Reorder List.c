/*
143. Reorder List
https://leetcode.com/problems/reorder-list/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
*/

struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode Node;
Node* reverse(Node* h)
{
    Node *p0,*p1;
    if (h == 0 || h->next == 0) return h;
    
    p0 = h->next;
    h->next = 0;
    while(p0->next != 0)
    {
        p1 = p0->next;
        p0->next = h;
        h = p0;
        p0 = p1;
    }
    p0->next = h;
    return p0;
}

void combine(Node *p0, Node *p1)
{
    Node *p;
    while (p0 != 0 && p1 != 0)
    {
        p = p0->next;
        p0->next = p1;
        p0 = p;
        p = p1->next;
        p1->next = p0;
        p1 = p;
    }
}

int getSize(Node* h)
{
    int i = 0;
    while(h != 0)
    {
        h = h->next;
        i++;
    }
    return i;
}

void reorderList(Node* head) {
    Node *p,*r;
    int size,half,i;
    if (head == 0 || head->next == 0 || head->next->next == 0)
        return;
    /*
    Decouple
    Reverse
    Combine
    */
    size = getSize(head);
    half = ((size - 1) >> 1);
        
    p = head;
    for(i = 0;i<half;i++){
        p = p->next;
    }
    r = reverse(p->next);
    p->next = 0;
    
    combine(head,r);
}
