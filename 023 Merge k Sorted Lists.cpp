#include<iostream>
#include<vector>
#include<set>
using namespace std;
/*
23 Merge k Sorted Lists
https://oj.leetcode.com/problems/merge-k-sorted-lists/
*/
/*
Generate a integer in [mini,maxi] inclusively
*/
int randLimit(int mini, int maxi)
{
    int limit = maxi - mini + 1;
    int div = RAND_MAX / limit;
    int res = -1;
    do
    { 
        res = rand() / div;
    } while (res > limit);
    return res + mini;
}
struct ListNode {
    int val;
    struct ListNode *next;
};
typedef struct ListNode node;

node* newNode()
{
    node* head = (node*)malloc(sizeof(node));
    head->val = -1;
    head->next = 0;
    return head;
}
node* randSortedList(int size)
{
    int i;
    node* head = newNode();
    node* p = head;
    int mini = 0;
    for(i=0;i < size - 1;i++)
    {
        p->val = randLimit(mini,mini+size);
        mini = p->val;
        p->next = newNode();
        p = p->next;
    }
    p->val = randLimit(mini,mini+size);
    return head;
}
void dumpList(node* h)
{
    while(h != 0)
    {
        printf("%d ",h->val);
        h = h->next;
    }
    printf("\n");
}
void deleteList(node* h)
{
    node* p;
    while(h != 0)
    {
        p = h->next;
        free(h);
        h = p;
    }
}
struct CustomLess 
{
    bool operator()(const node* x, const node* y) const
    {
        return x->val < y->val;
    }
};
typedef std::multiset<node*, CustomLess> CustomMap;
/*
Merge first N elements from sorted arrays
*/
node* mergeKLists(vector<node*>& input)
{ 
    // size of $buf is no more than input.size()
    CustomMap buf;
    node* res = newNode();
    node* p = res;
    node* v;

    // insert each head node
    for(size_t i = 0;i < input.size();i++)
    {
        v = input[i];
        if(v != 0) buf.insert(v);
    }

    // extract first element from buf, push back to res,
    // then find next element in corresponding list
    while(!buf.empty())
    {
        CustomMap::iterator it = buf.begin();
        v = *it;
    
        p->next = v;
        p = p->next;
    
        if(v->next != 0) buf.insert(v->next);
        buf.erase(it);
    }
    return res->next;
}

  
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <queue>

/*
Priority queue methods
*/
class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists)
    {
        auto* head = new ListNode(0); // NO const! or p will be const, cannot assign!
        
        const auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        
        std::priority_queue<ListNode* , std::vector<ListNode*>, decltype(cmp)> pq (cmp); // Has to put (cmp)
        
        for (const auto n : lists)
        {
            if (n)
            {
                pq.push(n);
            }
        }
        
        auto p = head;
        while (!pq.empty())
        {
            const auto n = pq.top();

            p->next = n;
            p = p->next;
            
            pq.pop();
            if (n->next)
            {
                pq.push(n->next);
            }
        }
        
        return head->next;
    }
};

int main()
{ 
    int size = 3,i;

    vector<node*> input;
    node* ls;

    for(i = 0;i<size;i++)
    {
        ls = randSortedList((i+1)*size);
        dumpList(ls);
        input.push_back(ls);    
    }

    ls = mergeKLists(input);
    dumpList(ls);
    deleteList(ls); 
    return 0;
}
