/*
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        } 
        
        ListNode fakeHead = new ListNode(0, head);
        ListNode prev = fakeHead;

        while (head != null && head.next != null) {
            ListNode n1 = head.next;
            ListNode n2 = n1.next;
            
            prev.next = n1;
            n1.next = head;
            
            prev = head;
            head = n2;
        }
        prev.next = head;
        return fakeHead.next;
    }
}
