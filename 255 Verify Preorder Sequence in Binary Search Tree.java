/*
Verify Preorder Sequence in Binary Search Tree
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
You may assume each number in the sequence is unique.
*/
public class Solution {
    public boolean verifyPreorder(int[] preorder) {
        if(preorder.length < 3) return true;
        int minVal = preorder[0] < preorder[1] ? preorder[0] : Integer.MIN_VALUE;
        java.util.LinkedList<Integer> stack = new java.util.LinkedList<Integer>();
        stack.push(preorder[0]);
        for(int i = 1;i<preorder.length;i++){
            int v = preorder[i];
            if(v < preorder[i-1]){
                if(v < minVal) return false;
            }
            else{
                while(stack.size() > 0 && stack.peekLast() < v){
                    minVal = stack.pollLast();
                }
            }
            stack.offerLast(v);
        }
        return true;
    }
}
