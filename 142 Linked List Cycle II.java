/*
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Follow-up:
Can you solve it without using extra space?
*/
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
/*
Let's denote the head of list as point as H, cycle staring point as C
meeting point as M, and assume there exists a cylce;
if it is a pure circular list, H=C=M; if not, it has a previous 
straight part, then enters the cycle, like:
H    C
->->->->->
     /    \
    |      | M
     \    /
      <-<-
User 2 pointers, slow and fast, slow moves 1, fast moves 2, 
they will eventually meet in M. At M, fast pointer travels exactly 1 more cycle
than slow pointer (because fast cannot skip over slow without meet slow).
If c denotes the cycle length, then:
    HM =  (HM + c) / 2 = total distance slow pointer traveled
This means:
    c = HM
So slow pointer traverlled exactly the size of circle. It also has:
    MC = c - CM = HM - CM = HC 
So the distance from M to C is same as H to C. Let 1 pointer move from
M, another from H, in same speed, they will meet in C.
*/
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                fast = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return fast;
            }
        }
        return null;
    }
}
