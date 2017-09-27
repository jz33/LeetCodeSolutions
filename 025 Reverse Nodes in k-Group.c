#include <stdio.h>
#include <stdlib.h>
/*
25 Reverse Nodes in k-Group
https://oj.leetcode.com/problems/reverse-nodes-in-k-group/
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

node* reverse(node* head, node* tail) // tail exclusive
{
    node *p0, *p1;
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
/*
 0->1->2->3->4->5, 2 => 1->0->3->2->5->4
 0->1->2->3->4->5, 3 => 2->1->0->5->4->3
 0->1->2->3->4->5, 4 => 3->2->1->0->4->5
*/
node* reverseKGroup(node* head, int k) {
    node *prev, *tail, *t;
    int i, firstTime;
    
    prev = head;
    tail = prev;  
    firstTime = 1;
    while (tail != 0)
    {
        for(i=0;tail != 0 && i < k;i++)
        {
            tail = tail->next;
        }
        if (i == k)
        {                      
           if (firstTime != 0) 
           {
               firstTime = 0;       
               head = reverse(prev,tail);
               prev->next = tail;
           }
           else
           {
                t = prev->next;
                prev->next = reverse(t,tail);
                t->next = tail;
                prev = t;
           }
           //printf("%d,%d,%d\n",prev->val,tail == 0? -1 : tail->val, head->val);
        } 
    }
    return head;
}


int main(){
    int repeat = 7; // will create repeat + 1 nodes
    int K;
    int i;
    node* head = (node*)malloc(sizeof(node));
    node* p = head;
    
    // init
    head->rank = 0;
    for(i=0;i<repeat;i++){
        p->next = (node*)malloc(sizeof(node));
        p = p->next;
        p->rank = i+1;
        p->next = 0;
    }
    
    // print
    p = head;
    while(p != 0){
        printf("%d ",p->rank);
        p = p->next;
    }
    printf("\n");
    
	// test K = [1,repeat]
	for(K=1;K<=repeat+1;K++){
		head = reverseK(head,K);
		// print
		p = head;
		while(p != 0){
			printf("%d ",p->rank);
			p = p->next;
		}
		printf("\n");
	}
    
    //free
    while(head != 0){
        p = head->next;
        free(head);
        head = p;
    }
    return 0; 
}
