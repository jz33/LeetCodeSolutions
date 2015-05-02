#include <stdio.h>
#include <stdlib.h>
/*
19 Remove Nth Node From End of List
https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
*/
struct LinkedListNode
{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

void printList(node* p){
    while(p != 0){
        printf("%d ",p->rank);
        p = p->next;
    }
    printf("\n");
}
/*
Remove Nth node from end of a single linked list
http://yucoding.blogspot.ca/2013/04/leetcode-question-82-remove-nth-node.html
 0->1->2->3->4, 2  => 0->1->3->4
*/
void removeFromBackRec(node* head, int* counter, const int tag)
{
    node* t;
    if(head->next != 0) 
        removeFromBackRec(head->next,counter,tag);

    // notice the current node is 1 before to-be-deleted node
    if(*counter == tag)
    {
        t = head->next;
        head->next = t->next;
        t->next = 0;
        free(t);
    }
    *counter = *counter+1;
}
/*
tag = [1,2,3...]
*/
node* removeFromBack(node* head, const int tag)
{
    int counter = 0;
    node* t;
    if (head==0) 
        return 0;
    removeFromBackRec(head,&counter,tag);
    
    // if the head node is to be deleted
    if(counter == tag)
    {
        t = head->next;
        free(head);
        return t;
    }
    else return head;
}

int main(){
    int repeat = 6;
    int i,tag;
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
    printList(head);
    
    tag = 7;
    head = removeFromBack(head,tag);
    
    printList(head);
    
    //free
    while(head != 0){
        p = head->next;
        free(head);
        head = p;
    }
    return 0; 
}
