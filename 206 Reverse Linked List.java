/*
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
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
    
    // Recursively
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode newHead = dfs(head);
        head.next = null;
        return newHead;
    }
    
    /**
    *@node: != null
    *@return: new head of the reversed list
    */
    private ListNode dfs(ListNode node) {
        if (node.next == null) {
            return node;
        }
        
        ListNode newHead = dfs(node.next);
        
        // Redirect
        node.next.next = node;
        
        return newHead;
    }
}

class Solution {
    
    // Iteratively
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode p1 = head.next;
        head.next = null;
        while (p1.next != null) {
            
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
