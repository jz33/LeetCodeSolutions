"use strict";
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
    var p,len;
    var res = [];
    if(root === null) return res;
    var queue = [];
    queue.push(root);
    
    while(queue.length > 0){
        len = queue.length;
        for(;len > 0;len--){
            p = queue.shift();
            if(p.left  !== null) queue.push(p.left);
            if(p.right !== null) queue.push(p.right);
        }
        res.push(p.val); 
    }
    return res;
};
