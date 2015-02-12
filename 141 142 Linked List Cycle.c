#include <stdio.h>
#include <stdlib.h>
/*
141 Linked List Cycle
142 Linked List Cycle II
https://oj.leetcode.com/problems/linked-list-cycle/
https://oj.leetcode.com/problems/linked-list-cycle-ii/
*/
struct LinkedListNode{
    int rank;
    struct LinkedListNode* next;
};
typedef struct LinkedListNode node;

#define NEWNODE \
	(node*)malloc(sizeof(node))

#define ASSIGN(p, val) \
	p->rank = val;\
	p->next = 0;
    
/*
Detect if a linked list has a cycle. and return the starting node
http://yucoding.blogspot.com/2013/12/leetcode-question-linked-list-cycle-ii.html
Author: junzhengrice@gmail.com

Notice that the normal approach is not perfect

Let's denote the staring point as S, cycle staring point as C
meeting point as M, and assume there exists a cylce;
if it is a pure circular list, S=C=M; if not, it has a previous 
straight part, then enters the cycle, as:

S    C
->->->->->
	 /	  \
	|	   | M
	 \	  /
	  <-<-

As a classic slower & faster pointer approach (denoted as ps, pf, 
and pf moves 2 steps each time, ps moves 1 step), because there is a cylce, 
they will eventually meet, and ps has travelled less than 1 cycle after
entering C, and pf travelled exactly 1 more cycle than ps (because pf cannot 
bypass ps by no means);

Assume s denotes the distance ps has travelled, c is the cycle length, then:

ps    pf
s =  (s + c)/2 = total travel time

Notice that S != C, and M not necessarliy be C. 
Therefore the distance ps has travelled is same as 
the cycle length, then we can either record the length, 
or let 1 pointer travel from S, another one from M, 
after c - (M-C) steps, they will meet at C
*/
node* detect(node* head)
{
    node *ps, *pf;
    if(head == 0) return 0;
	
    ps = head;
    pf = head;
    while(pf->next != 0 && pf->next->next != 0)
    {
        ps = ps->next;
        pf = pf->next->next;
		
        if(ps == pf)
        {
	        // pure circular list
	        if(ps == head)
                return head;
            else
            {
                pf = head;
                while(ps != pf)
                {
                    ps = ps->next;
                    pf = pf->next;
                }
                return pf;
            }
        }
    }
    // not a circular list
    return 0;
}

/*
   0->1->2->3->4->5
         |
-1->-2->-3
*/
int main()
{
#define NUM 10

    int array[NUM] = {0,1,2,3,4,5,6,7,8,9};
    int i;
    node* cir = NEWNODE;
    node* nor = NEWNODE;
    node *p, *q,*res;

    // a pure circular list
    ASSIGN(cir,array[0]);
    p = cir;

    for(i = 1;i<NUM;i++){
        p->next = NEWNODE;
        p = p->next;
        ASSIGN(p,array[i]);
    }
    p->next = cir;

    res = detect(cir);
    printf("result value: %d\n",res->rank);

    // normal cycle list
    ASSIGN(nor,array[0]);
    p = nor;

    for(i = 1;i<NUM;i++){
        p->next = NEWNODE;
        p = p->next;
        ASSIGN(p,array[i]);
        
        if(i == 4) {q = p;}
    }
    p->next = q;

    res = detect(nor);
    printf("result value: %d\n",res->rank);
    return 0;
}