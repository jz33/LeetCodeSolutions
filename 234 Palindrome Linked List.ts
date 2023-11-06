/*
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?

*/
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

/**
 * Get middle node of the linked list
 * 0->1->2->3->4 => 2
 * 0->1->2->3 => 1
 */
function getMiddle(head: ListNode): ListNode {
    let slow: ListNode = head;
    let fast: ListNode | null = head;
    while (fast?.next?.next) {
        fast = fast.next.next;
        slow = slow.next!;
    }
    return slow;
}

/**
 * Classic way to reverse a linked list
 */
function reverse(head: ListNode | null): ListNode | null {
    if (!head?.next) {
        return head;
    }
    let p0: ListNode = head;
    let p1: ListNode = head.next;
    p0.next = null;
    while (p1.next) {
        const p2 = p1.next;
        p1.next = p0;
        p0 = p1;
        p1 = p2;
    }
    p1.next = p0;
    return p1;
}

/**
 * Compare 2 linked lists from beginning if all values are identical
 */
function compare(a: ListNode, b: ListNode): boolean {
    let pa: ListNode | null = a;
    let pb: ListNode | null = b;
    while (pa && pb) {
        if (pa.val !== pb.val) {
            return false;
        }
        pa = pa.next;
        pb = pb.next;
    }
    return true;
}

function isPalindrome(head: ListNode | null): boolean {
    if (!head?.next) {
        return true;
    }
    const middle = getMiddle(head);
    const reversedHead = reverse(middle.next)!;
    middle.next = null;

    const result = compare(head, reversedHead);

    // Recover the list
    middle.next = reverse(reversedHead);

    return result;
}
