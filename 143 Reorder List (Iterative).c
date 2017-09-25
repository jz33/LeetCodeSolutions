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
