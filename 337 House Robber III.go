/*
337. House Robber III
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again. There is only one entrance to this area,
called the "root." Besides the root, each house has one and only one parent house. After a tour,
the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func Max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

/**
*@return: [max cash if current node is NOT stolen,
max cash at current node (does not matter current is stolen or not)]
*/
func postorder(node *TreeNode) (int, int) {
    if node == nil {
        return 0, 0
    }
    
    leftNo, leftMax := postorder(node.Left)
    rightNo, rightMax := postorder(node.Right)
    
    maxValNo := leftMax + rightMax
    maxValHas := node.Val + leftNo + rightNo
    
    return maxValNo, Max(maxValNo, maxValHas)
}

func rob(root *TreeNode) int {
    _, max := postorder(root)
    return max
}
