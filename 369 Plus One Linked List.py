'''
369. Plus One Linked List
https://leetcode.com/problems/plus-one-linked-list/

Given a non-negative integer represented as non-empty a singly linked list of digits,
plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
'''
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        p = head
        while p.next != None:
            if p.val == 9:
                stack.append(p)
            else:
                stack = [p]
            p = p.next
        
        # p is tail now
        stack.append(p)       
        for i in range(len(stack)-1,-1,-1):
            p = stack[i]
            if p.val != 9:
                p.val += 1
                break
            p.val = 0
        else:
            # all stack is poped, check if we poped head
            if head.val == 0:
                p = ListNode(1)
                p.next = head
                head = p
        
        return head
