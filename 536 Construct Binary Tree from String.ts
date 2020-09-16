/*
536. Construct Binary Tree from String
https://leetcode.com/problems/construct-binary-tree-from-string/

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example 1:

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]

Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
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

function str2tree(s: string): TreeNode | null {
    if (!s) {
        return null
    }
    let val: number = NaN
    let sign: number = 1
    let stack: TreeNode[] = []
    for (const c of s) {
        if (c === '(' || c === ')') {
            if (!isNaN(val)) {
                let node: TreeNode = new TreeNode(val * sign)
                val = NaN
                sign = 1

                if (stack.length > 0) {
                    let parent = stack[stack.length - 1]

                    // As request by this problem always try assign
                    // left child first, but in reality, it is possible
                    // for the string to represents a node with no left
                    // child but having right child, like: 4(2()(3))

                    if (parent.left === null) {
                        parent.left = node
                    }
                    else {
                        parent.right = node
                    }
                }

                stack.push(node)
            }

            if (c === ')') {
                stack.pop()
            }
        }
        else if (c === '-') {
            sign = -1
        }
        else { // [0-9]
            if (isNaN(val)) {
                val = +c
            }
            else {
                val = val * 10 + (+c)
            }
        }
    }

    // Root only case like "-5"
    if (!isNaN(val)) {
        return new TreeNode(val * sign)
    }
    else { // Normal case
        return stack[0]
    }
};
