/*
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
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
    public ListNode reverseKGroup(ListNode inputHead, int k) {
        ListNode fakeHead = new ListNode();
        ListNode prev = fakeHead; // last node of previous k group
        ListNode tail = inputHead;
        
        while (tail != null) {
            // Try find a k group
            ListNode head = tail;
            int count = 0;
            for (;tail != null && count < k; ++count) {
                tail = tail.next;
            }
            
            if (count == k) {
                prev.next = reverse(head, tail);
                prev = head;
                head.next = tail;
            } 
        }
        return fakeHead.next;
    }
    
    // Reverse from head (inclusive) till tail (exclusive)
    private ListNode reverse(ListNode head, ListNode tail) {
        if (head == tail || head.next == tail) {
            return head;
        }
        
        ListNode p0 = head.next;
        head.next = null;
        
        while (p0.next != tail) {
            ListNode p1 = p0.next;
            p0.next = head;
            head = p0;
            p0 = p1;
        }
        
        p0.next = head;
        return p0;
    }
}
