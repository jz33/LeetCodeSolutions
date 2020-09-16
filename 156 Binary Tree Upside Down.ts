/*
156. Binary Tree Upside Down
https://leetcode.com/problems/binary-tree-upside-down/

Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.


The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.

Example 1:


Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Constraints:

The number of nodes in the tree will be in the range [0, 10].
1 <= Node.val <= 10
Every node has either 0 or 2 children.
*/
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function upsideDownBinaryTree(root: TreeNode | null): TreeNode | null {
    let newHead: TreeNode | null = root
    if (!root || root.left === null) {
        return newHead
    }

    let stack: Array<TreeNode | null> = [root]
    let p: TreeNode | null = root.left
    while (p) {
        stack.push(p)
        p = p.left
    }

    newHead = stack.pop()!
    p = newHead
    while (stack.length !== 0) {
        let q: TreeNode | null = stack.pop()!
        p.left = q.right
        p.right = q

        q.left = null
        q.right = null
        p = q
    }

    return newHead
}
