/*
86. Partition List
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
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
    public ListNode partition(ListNode head, int x) {
        ListNode smallHead = new ListNode();
        ListNode s = smallHead;
        
        ListNode bigHead = new ListNode();
        ListNode b = bigHead;
        
        ListNode p = head;
        while (p != null) {
            // Extract p
            ListNode n = p.next;
            p.next = null;
            
            // Append to small or big list
            if (p.val < x) {
                s.next = p;
                s = p;
            } else {
                b.next = p;
                b = p;
            }
            
            // Move p
            p = n;
        }
        
        s.next = bigHead.next;
        return smallHead.next;
    }
}
