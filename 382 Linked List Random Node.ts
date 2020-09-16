/*
382. Linked List Random Node
https://leetcode.com/problems/linked-list-random-node/

Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly.
Each element should have equal probability of returning.
solution.getRandom();
*/
class ListNode {
    val: number
    next: ListNode | null

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

class Solution {
    head: ListNode | null

    constructor(head: ListNode | null) {
        this.head = head
    }

    getRandom(): number {
        if (!this.head) {
            return 0
        }
        let node: ListNode = this.head
        let val: number = node.val
        for (let i = 1; node.next !== null; ++i) {
            node = node.next
            if (Math.round(Math.random() * (i + 1)) === i) {
                val = node.val
            }
        }
        return val
    }
}
