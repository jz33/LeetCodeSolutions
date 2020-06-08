/*
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Use a fake head to make code shorter
        ListNode fakeHead = new ListNode();
        ListNode writer = fakeHead;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val){
                writer.next = l1;
                l1 = l1.next;
            } else {
                writer.next = l2;
                l2 = l2.next;
            }
            writer = writer.next;
        }

        // Attach remaining tail
        if (l1 != null) {
            writer.next = l1;
        }
        if (l2 != null) {
            writer.next = l2;
        }
        
        ListNode res = fakeHead.next;
        fakeHead.next = null;
        return res;
    }
}
