"use strict";
/*
Clone Graph
https://leetcode.com/problems/clone-graph/

DFS, UNTESTED
*/
function UndirectedGraphNode(label){
    this.label = label;
    this.neighbors = [];
}

/*
Standard built-in "Map" object
Alternaitvely in Node.js, use:
var HashMap = require('hashmap');
*/
var map = new Map();
var cloneGraph = function(n) {
    if(n === undefined) return undefined;
    if(map.has(n) === false) {
        var branch = new UndirectedGraphNode(n.label);
        map.set(n, branch);
        n.neighbors.forEach(function(v,i,a){
            map.get(n).neighbors.push(cloneGraph(v));
        });
    }
    return map.get(n);
}
