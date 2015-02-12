#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
/*
86 Partition List
https://oj.leetcode.com/problems/partition-list/
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

void dumpList(node* p){
    while(p != 0){
        printf("%d ",p->rank);
        p = p->next;
    }
    printf("\n");
}

node* allocNode(int rank){
    node* p = (node*)malloc(sizeof(node));
    p->rank = rank;
    p->next = 0;
    return p;
}

node* createFromArray(int* arr, const int N){
    int i;
    node *head, *p;
    assert(N>0);

    head = allocNode(*arr++);
    p = head;
    
    for(i =1;i<N;i++){
        p->next = allocNode(*arr++); 
        p = p->next;
    }
    return head;
}

// return new head node
node* partition(node* lls, int tag){
    node *tail, *grow, *ret, *curr;
    assert(lls != 0);
    
    // find tail. tail is fixed
    tail = lls;
    while(tail->next != 0) tail = tail->next;
    grow = tail;
    
    // find return node
    curr = lls;
    if(lls->rank < tag){
        ret = lls;
    } else {
        while(curr->next != 0 && curr->next->rank >= tag){
            curr = curr->next;
        }
        if(curr->next == 0){
            return lls;
        } else {
            ret = curr->next;

            grow->next = lls;
            grow = curr;
            grow->next = 0;
            curr = ret;
        }
    }  
    
    // body      
    while(curr->next != tail){
        if(curr->next->rank >= tag){            
            grow->next = curr->next;
            grow = curr->next;
            curr->next = grow->next;
            grow->next = 0;
        } else {
            curr = curr->next;
        }
    } 
    
    // end
    if(tail->rank >= tag){
        grow->next = tail;
        grow = tail;
        curr->next = grow->next;
        grow->next = 0;
    }
    
    return ret;
}

int main(){
    int i,tag = 3;
    int arr[] = {7,8,2,3,2,5};
    
    // init
    node* head = createFromArray(arr,6);
    node* p = head;
    
    dumpList(head);    
    
    // test
    head = partition(head,tag);
    dumpList(head);    

    //free
    while(head != 0){
        p = head->next;
        free(head);
        head = p;
    }
    return 0; 
}