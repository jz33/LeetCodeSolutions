/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/*
Return true if all subtrees and self are same valued
*/
var rec = function(root, val, count){
    if (root === null)
        return true;
    if (!rec(root.left, root.val, count) | !rec(root.right, root.val, count))
        return false;
    count[0]++;
    return root.val === val;
}
/**
 * @param {TreeNode} root
 * @return {number}
 */
var countUnivalSubtrees = function(root) {
    if(root === null){
        return 0;
    }
    var count = [0];
    rec(root,0,count);
    return count[0];
};
