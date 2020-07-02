/*
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Need to ask interviewer when n is invalid, what to do.
        // And meaning of "n", n is from 1 or 0
        
        // Use a front pointer from head, move n steps.
        ListNode front = head;
        for (int i = 0; i < n; ++i) {
            front = front.next;
        }
        
        // If front is null now, means the head is the one to remove
        if (front == null) {
            ListNode res = head.next;
            head.next = null;
            return res;
        }
        
        // Use a back pointer from head. Move front and back together
        // until front pointer reaches last node.
        ListNode back = head;
        while (front.next != null) {
            front = front.next;
            back = back.next;
        }
        
        // Back.next is the node to remove
        // Notice since n is valid, back != last node
        ListNode removal = back.next;
        back.next = removal.next;
        removal.next = null;
        return head;
    }
}
