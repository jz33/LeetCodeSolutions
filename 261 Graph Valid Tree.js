"use strict";
/*
Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

Union-Find
https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
O(N + MlogN), M : edges
*/
/**
 * @param {number[]} list
 * @param {number} i
 * @return {number[]}[parent,steps]
 */
var getParent = function(list,i){
    var c = 0;
    while(list[i] != -1){
        i = list[i];
        c++;
    }
    return [i,c];
}
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var validTree = function(n, edges){
    var i,p0,p1;
    // list[i] is i's parent
    var list = []; 
    for(i = 0;i<n;i++) list.push(-1);
    
    var m = edges.length;
    for(i = 0;i < m;i++){
        console.log(list);
        p0 = getParent(list,edges[i][0]);
        p1 = getParent(list,edges[i][1]);
        if(p0[0] === p1[0]){
            return false;
        } 
        // Set shallow tree's parent to deep tree
        if(p0[1] < p1[1]){
            list[p0[0]] = p1[0];
        } else {
            list[p1[0]] = p0[0];
        }
    }    
    // Check if all nodes connected by counting "-1"
    console.log("check: " + list);
    p0 = 0;
    for(i = 0;i<n;i++){
        if(list[i] == -1) p0++;
        if(p0 > 1) return false;
    }
    return true;
};

var n = 5;
var edges = [[0,1],[0,2],[2,3],[2,4]];
console.log(validTree(n,edges));
