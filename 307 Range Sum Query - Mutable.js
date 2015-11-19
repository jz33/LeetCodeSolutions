"use strict";
/*
Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/
http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
*/
function TreeNode(val, lr, rr, lc, rc){
    /*
    val : value on node
    lr: left range of array inclusive
    rr: right range of array inclusive
    lc: left child
    rc: right child
    */
    this.val = val;
    this.lr = lr;
    this.rr = rr;
    this.lc = typeof lc !== undefined ? lc : null;
    this.rc = typeof rc !== undefined ? rc : null;      
}

var getInit = function(){
    var initRec = function(arr, lr, rr){
        if(lr === rr)
            return new TreeNode(arr[lr], lr, rr);
        else{
            var mid = (lr + rr >> 1);
            var node = new TreeNode(-1,lr,rr);
            node.lc = initRec(arr, lr, mid);
            node.rc = initRec(arr, mid + 1, rr);
            node.val = node.lc.val + node.rc.val;
            return node;
        }
    }
    return initRec;
}    

var getUpdate = function(){  
    var updateRec = function(i, val, node){
        if(node.lr === i && node.rr === i) 
            node.val = val;
        else{
            var mid = (node.lr + node.rr >> 1);
            if(i <= mid)
                updateRec(i,val,node.lc);
            else
                updateRec(i,val,node.rc);
            node.val = node.lc.val + node.rc.val;
        }
    }
    return updateRec;
}      

var getSumRange = function(){     
    var sumRangeRec = function(i, j, node){
        if(node.lr === node.rr)
            return node.val
        else{
            var mid = (node.lr + node.rr >> 1)
            if(j <= mid)
                return sumRangeRec(i,j,node.lc);
            else if(i >= mid + 1)
                return sumRangeRec(i,j,node.rc);
            else
                return sumRangeRec(i,j,node.lc) + sumRangeRec(i,j,node.rc);
        }
    }
    return sumRangeRec;
}

function NumArray(arr){
    if(arr === null || arr.length === 0) this.root = null;
    else this.root = getInit()(arr, 0, arr.length - 1);
}

NumArray.prototype.update = function(i, val){
    if(this.root === null) return;
    getUpdate()(i,val,this.root)
}

NumArray.prototype.sumRange = function(i, j){
    if(this.root === null) return 0;
    return getSumRange()(i,j,this.root)
}
      
var arr = [1,3,5,7,9,11];
var sol = new NumArray(arr);
console.log(sol.sumRange(1,3));
sol.update(1,10);
console.log(sol.sumRange(1,3));
