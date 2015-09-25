/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if(head == null) return null;
        ListNode prev = new ListNode(-1);
        prev.next = head;
        
        ListNode p = prev;
        for(;p.next != null;){
            if(p.next.val == val){
                ListNode q = p.next;
                p.next = q.next;
                q.next = null;
            }
            else
                p = p.next;
        }
        return prev.next;
    }
}
