/*
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode fakeHead = new ListNode(0, head);
        
        // Find the prev node, which is the node before m-th node
        ListNode prev = move(fakeHead, m - 1);
        ListNode mNode = prev.next;
        
        // Find the tail node, which the next node of n-th node
        ListNode tail = move(head, n);

        // Reverse, get nNode
        ListNode nNode = reverseBeforeTail(mNode, tail);
        
        // Link
        prev.next = nNode;
        mNode.next = tail;
        
        return fakeHead.next;
    }
    
    // Move a node n steps
    private ListNode move(ListNode node, int n) {
        for (int i = 0; i < n ; ++i) {
            node = node.next;
        }
        return node;
    }
    
    // Reverse from head to tail (exclusive)
    private ListNode reverseBeforeTail(ListNode head, ListNode tail) {
        if (head == tail || head.next == tail) {
            return head;
        }
        
        ListNode p1 = head.next;
        head.next = null;
        while (p1.next != tail) {
            // Assign
            ListNode p2 = p1.next;
            
            // Redirect
            p1.next = head;
            
            // Move
            head = p1;
            p1 = p2;
        }
        p1.next = head;
        return p1;
    } 
}
