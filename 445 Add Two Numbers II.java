/*
445. Add Two Numbers II
https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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
    
    /**
    * A solution without extra memory
    * 7 -> 2 -> 4 -> 3, 5 -> 6 -> 4
    * => 7 <- 7 <- 10 <- 7
    * => 7 <- 8 <- 0 <- 7
    * => 7 -> 8 -> 0 -> 7
    */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int size1 = getSize(l1);
        if (size1 == 0) {
            return l2;
        }
        
        int size2 = getSize(l2);
        if (size2 == 0) {
            return l1;
        }
        
        // 1. Build a reversed result list
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode head = null;
        int s1 = size1;
        int s2 = size2;
        while (!(s1 == 0 && s2 == 0)) {
            ListNode newNode = null;
            if (s1 == s2) {
                newNode = new ListNode(p1.val + p2.val);
                p1 = p1.next;
                p2 = p2.next;
                s1 -= 1;
                s2 -= 1;
            } else if (s1 > s2) {
                newNode = new ListNode(p1.val);
                p1 = p1.next;
                s1 -= 1;
            } else {
                newNode = new ListNode(p2.val);
                p2 = p2.next;
                s2 -= 1;
            }
            
            // Add newNode in front of head
            newNode.next = head;
            head = newNode;
        }
        
        // 2. Deal carries
        ListNode p = head;
        int carry = 0;
        while (p != null) {
            int val = p.val + carry;
            p.val = val % 10;
            carry = val >= 10 ? 1 : 0;
            
            // Last
            if (carry > 0 && p.next == null) {
                p.next = new ListNode(1);
                break;
            }
            p = p.next;
        }
        
        // 3. Reverse list
        if (head.next == null){
            return head;
        }

        p1 = head.next;
        head.next = null;
        while (p1.next != null) {
            p2 = p1.next;
            p1.next = head;
            head = p1;
            p1 = p2;
        }
        p1.next = head;
        return p1;
    }
    
    private int getSize(ListNode l1) {
        int count = 0;
        while (l1 != null) {
            count += 1;
            l1 = l1.next;
        }
        return count;
    }
}
