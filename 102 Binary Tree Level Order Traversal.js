/*
Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
*/
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    var s = []; // stack
    var length = -1;
    var n = null;
    var res = [];
    var row = [];
    
    if(root === null) return res;
    s.push(root);
    for(;s.length > 0;){
        row.splice(0,row.length);
        for(length = s.length;length > 0;length--){
            n = s.splice(0,1)[0];
            row.push(n.val);
            if(n.left !== null) s.push(n.left);
            if(n.right !== null) s.push(n.right);
        }
        res.push(Array.prototype.concat([],row));
    }
    return res;
};
