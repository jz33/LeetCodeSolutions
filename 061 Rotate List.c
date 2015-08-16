/*
Rotate List
https://oj.leetcode.com/problems/rotate-list/
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

int getSize(node* head)
{
    int i = 0;
    while(head != 0)
    {
        head = head->next;
        i++;
    }
    return i;
}

node* getNewEnd(node* head, int size, int k)
{
    int i = 1;
    int ctr = size - k; // 0 < ctr < size
    while(i < ctr)
    {
        head = head->next;
        i++;
    }
    return head;
}
/*
 0->1->2->3->4->5, 1 => 5->0->1->2->3->4
 0->1->2->3->4->5, 2 => 4->5->0->1->2->3
 0->1->2->3->4->5, 3 => 3->4->5->0->1->2
 0->1->2->3->4->5, 4 => 2->3->4->5->0->1
 0->1->2->3->4->5, 5 => 1->2->3->4->5->0
 0->1->2->3->4->5, 6 => 0->1->2->3->4->5
*/
node* rotateRight(node* head, int k)
{
    node *newEnd, *newHead;
    int size;
    if(k < 1 || head == 0) return head;
    
    size = getSize(head);
    k = k % size;
    if(k == 0) return head;
    
    newEnd = getNewEnd(head,size,k);
    newHead = newEnd->next;
    newEnd->next = 0;
    
    // reuse $newEnd
    newEnd = newHead;
    while(newEnd->next != 0)
    {
        newEnd = newEnd->next;
    }
    newEnd->next = head;
    return newHead;
}
