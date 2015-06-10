#include <stdio.h>
#include <stdlib.h>
/*
148 Sort list
https://oj.leetcode.com/problems/sort-list/
*/
struct LinkedListNode
{
    int val;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode lnode;

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
/*
merge sort
average: O(nlogn)
best: O(nlogn)
worst: O(nlogn)
memory: O(1)
*/
lnode* merge(lnode* a, lnode* b){
    lnode *head,*t;
	if(a == 0) {return b;}
	if(b == 0) {return a;}

	if(a->val < b->val){
		head = a;
		a = a->next;
	} else {
		head = b;
		b = b->next;
	}
	
	t = head;
	while(a != 0 && b != 0){
		if(a->val < b->val){
			t->next = a;
			a = a->next;
		} else {
			t->next = b;
			b = b->next;
		}
		t = t->next;
	}
	if(a != 0) {t->next = a;}
	if(b != 0) {t->next = b;}
	return head;
}
lnode* split(lnode* head){
	lnode *slow, *fast, *mid;
	
	if(head == 0 || head->next == 0){	
		mid = 0;
	} else {
		slow = head;
		fast = head;
		
		while(fast != 0 && fast->next != 0){
			fast = fast->next->next;
			if(fast == 0){break;}
			slow = slow->next;
		}
		mid = slow->next;
		slow->next = 0;
	}
    return mid;
}
lnode* mergesort(lnode* head){
    lnode *mid;
	if(head == 0 || head->next == 0){return head;}
	
	mid  = split(head);
	head = mergesort(head);
	mid  = mergesort(mid);
	head = merge(head,mid);
	return head;
}
void test(void)
{
    int arr[] = {5,4,3,2,1,0};
    int i;
    lnode* head = initList(arr,sizeof(arr)/sizeof(int));
    printList(head);
    
    head = mergesort(head);
    
    printList(head);
    freeList(head);
}
int main()
{
    test();
    return 0;
}
