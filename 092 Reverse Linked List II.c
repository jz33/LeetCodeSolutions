struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode Node;
Node* reverse(Node* head, Node* tail) // tail exclusive
{
    Node *p0, *p1;
    if (head == tail || head->next == tail) return head;
    p0 = head->next;
    head->next = 0;
    while(p0->next != tail)
    {
        p1 = p0->next;
        p0->next = head;
        head = p0;
        p0 = p1;
    }
    p0->next = head;
    return p0;
}

Node* move(Node* p, int n)
{
    int i;
    for(i = 0;i<n;i++)
        p = p->next;
    return p;
}

Node* reverseBetween(Node* head, int m, int n) {
    Node *tail, *h, *r;
    tail = move(head, n);
    if (m == 1)
    {
        r = reverse(head, tail);
        head->next = tail;
        return r;
    }
    else
    {
        h = move(head, m-2);
        r = reverse(h->next, tail);
        h->next->next = tail;
        h->next = r;
        return head;
    }
}
