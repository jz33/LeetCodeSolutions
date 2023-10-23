/*
314. Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
Examples 1:
Input: [3,9,20,null,null,15,7]
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 
Output:
[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:
Input: [3,9,8,4,0,1,7]
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 
Output:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:
Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
Output:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
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

function verticalOrder(root: TreeNode | null): number[][] {
  if (!root) {
    return [];
  }
  const offsetToValues = new Map<number, number[]>();

  // The offset is relative to root, minus if goes left, plus if goes right
  let nodeLevel: { node: TreeNode; offset: number }[] = [
    { node: root, offset: 0 },
  ];

  // It cannot use preorder traversal, as top nodes should show in front of lower nodes
  while (nodeLevel.length) {
    const newNodeLevel: { node: TreeNode; offset: number }[] = [];
    nodeLevel.map(({ node, offset }) => {
      offsetToValues.set(
        offset,
        (offsetToValues.get(offset) ?? []).concat([node.val])
      );
      if (node.left) {
        newNodeLevel.push({ node: node.left, offset: offset - 1 });
      }
      if (node.right) {
        newNodeLevel.push({ node: node.right, offset: offset + 1 });
      }
    });
    nodeLevel = newNodeLevel;
  }

  // It can either use sort, or record minimum / maximum offset to do linear iterations.
  // However, linear iteration is not necessarily faster as the tree can be sparse.
  return Array.from(offsetToValues)
    .sort((a, b) => a[0] - b[0])
    .map((row) => row[1]);
}
