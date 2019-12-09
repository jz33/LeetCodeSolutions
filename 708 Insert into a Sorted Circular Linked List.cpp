/*
708. Insert into a Sorted Circular Linked List
https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

Given a node from a Circular Linked List which is sorted in ascending order,
write a function to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list,
and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null),
you should create a new single circular list and return the reference to that single node.
Otherwise, you should return the original given node.

Example 1:

Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements.
You are given a reference to the node with value 3, and we need to insert 2 into the list.
The new node should be inserted between node 1 and node 3.
After the insertion, the list should look like this, and we should still return node 3.

Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and
return the reference to that single node.

Example 3:

Input: head = [1], insertVal = 0
Output: [1,0]
*/
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;

    Node() {}

    Node(int _val) {
        val = _val;
        next = NULL;
    }

    Node(int _val, Node* _next) {
        val = _val;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* insert(Node* start, int insertVal)
    {
        if (!start)
        {
            auto n = new Node(insertVal);
            n->next = n;
            return n;
        }
        
        /*
        3 cases:
        1. insertVal is bigger than anyone in list
        2. insertVal is smaller than anyone in list
        3. insertVal is in middle
        */
        
        auto tail = start;
        auto prev = start;
        do
        {
            auto next = prev->next; // next cannot be null for circular linkedlist
            
            // Case 3 ?
            if (insertVal >= prev->val && insertVal <= next->val)
            {
                auto n = new Node(insertVal);
                prev->next = n;
                n->next = next;
                return start;
            }
            
            // Try find tail -> head
            if (next->val < prev->val)
            {
                tail = prev;
                
                // Case 1 or 2 ?
                if (insertVal >= tail->val || insertVal <= tail->next->val)
                {
                    break;
                }
            }
            
            prev = next;
        }
        while (prev != start);
        
        // Case 1 or 2
        auto n = new Node(insertVal);
        n->next = tail->next;
        tail->next = n;
        return start;        
    }
};
