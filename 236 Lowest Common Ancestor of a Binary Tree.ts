/*
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that
has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
    
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of
itself according to the LCA definition.
 
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
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

function isTargetExisting(root: TreeNode, target: TreeNode): boolean {
  // Standard preorder traversal to find a node
  let curr: TreeNode | null = root;
  let stack: TreeNode[] = [];
  while (curr || stack.length) {
    if (curr) {
      if (curr.val === target.val) {
        return true;
      }
      stack.push(curr);
      curr = curr.left;
    } else {
      curr = stack.pop().right;
    }
  }
  return false;
}

function lowestCommonAncestor(
  root: TreeNode,
  p: TreeNode,
  q: TreeNode
): TreeNode | null {
  // Find the 1st node. The Find 2nd node from the 1st node or 1st node's parent nodes.
  // The LCA is either 1st node or 1st node's parents.

  // First node that is found in 1st travesal
  let firstNode: TreeNode | null = null;

  // Second node that is to found in 2nd travesal
  let secondNode: TreeNode | null = null;

  // Preorder traversal to find 1st node
  let curr: TreeNode | null = root;
  let stack: TreeNode[] = [];
  while (curr || stack.length) {
    if (curr) {
      if (curr.val === p.val) {
        firstNode = p;
        secondNode = q;
        break;
      } else if (curr.val === q.val) {
        firstNode = q;
        secondNode = p;
        break;
      }
      stack.push(curr);
      curr = curr.left;
    } else {
      curr = stack.pop().right;
    }
  }

  // Not even found 1st node, no LCA
  if (!firstNode) {
    return null;
  }

  // The 1st node can be the LCA if 2nd node is found in its children
  if (isTargetExisting(firstNode, secondNode)) {
    return firstNode;
  }

  // The LCA can be a parent of 1st node
  while (stack.length) {
    const lca = stack.pop();
    if (isTargetExisting(lca, secondNode)) {
      return lca;
    }
  }

  // Not found 2nd node, no LCA
  return null;
}

