/*
148. Sort List
https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        // Merge Sort. 
        // Split list into 2 sections
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null; // Previous node of slow
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;

        // Sort left & right separately
        ListNode left = sortList(head);
        ListNode right = sortList(slow);

        // Merge
        return merge(left, right);
    }
    
    private ListNode merge(ListNode left, ListNode right) {
        if (left == null) {
            return right;
        }
        if (right == null) {
            return left;
        }
        
        // Determine return head
        ListNode head = null;
        if (left.val <= right.val) { // Use <= to stable sort
            head = left;
            left = left.next;
        } else {
            head = right;
            right = right.next;
        }

        ListNode p = head;
        while (left != null && right != null) {
            if (left.val <= right.val) {
                p.next = left;
                left = left.next;
            } else {
                p.next = right;
                right = right.next;
            }
            p = p.next;
        }
        
        if (left != null ) {
            p.next = left;
        }
        
        if (right != null) {
            p.next = right;
        }
        
        return head;
    }
}
