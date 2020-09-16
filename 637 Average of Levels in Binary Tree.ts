/*
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]

Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
*/
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function averageOfLevels(root: TreeNode | null): number[] {
    if (!root) {
        return []
    }
    
    let stack: Array<TreeNode | null> = [root]
    let res: number[] = []
    while (stack.length > 0) {
        let newStack: Array<TreeNode | null> = []
        let total: number = 0
        for (let node of stack) {
            total += node!.val
            if (node!.left) {
                newStack.push(node!.left)
            }
            if (node!.right) {
                newStack.push(node!.right)
            }
        }
        res.push(total / stack.length)
        stack = newStack
    }
    return res
};
