#include <stdio.h>
#include <stdlib.h>
/*
109 Convert Sorted List to Binary Search Tree
https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
http://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/
*/
#define MAX(a,b) (a)>(b)?(a):(b)
struct Linked_List_Node
{
    int rank;
    struct Linked_List_Node *next;
};
typedef struct Linked_List_Node lnode;

void push(lnode** head_ref, int new_data)
{
    lnode* new_node = (lnode*)malloc(sizeof(lnode));
    new_node->rank  = new_data;
    new_node->next  = *head_ref;
    *head_ref       = new_node;
}

struct Binary_Search_Tree_Node
{
    int rank;
    struct Binary_Search_Tree_Node *pl;
    struct Binary_Search_Tree_Node *pr;
};
typedef struct Binary_Search_Tree_Node node;

void preorder(node* n)
{
    if(n != 0) {
		printf("%d ", n->rank);
        preorder(n->pl);
		preorder(n->pr);
	}
}
void inorder(node* n)
{
	if(n != 0) {
		inorder(n->pl);
		printf("%d ", n->rank);
		inorder(n->pr);
	}
}
node* sortedLinkedList2BSTRec(lnode** list_head, int lt, int rt)
{
    int md;
    node *lc, *rc, *me;
    if(lt > rt) return 0;
    
    md = rt+lt>>1;
    lc = sortedLinkedList2BSTRec(list_head,lt,md-1);
    
    me = (node*)malloc(sizeof(node));
    me->rank = (*list_head)->rank;
    
    *list_head = (*list_head)->next;
    
    rc = sortedLinkedList2BSTRec(list_head,md+1,rt);
    
    me->pl  = lc;
    me->pr  = rc;
    return me;
}
/*
Need to know sizeo of linked list
*/
node* sortedLinkedList2BST(lnode** list_head, const int list_size)
{
    if(list_head == 0 || (*list_head) == 0 || list_size < 1) {return 0;}
    return sortedLinkedList2BSTRec(list_head,0,list_size-1);
}
// tester
int main()
{
    int i, NUM =7;
    lnode* head = 0;
	node* root;

    for(i=NUM;i>0;i--) push(&head, i);
    
    root = sortedLinkedList2BST(&head,NUM);
    preorder(root);putchar('\n');
    inorder(root); putchar('\n');
    
    return 0;
}