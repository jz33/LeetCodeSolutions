/*
23 Merge k Sorted Lists
https://oj.leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <queue>

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
