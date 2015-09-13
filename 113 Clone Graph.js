"use strict";
/*
Clone Graph
https://leetcode.com/problems/clone-graph/

DFS, UNTESTED
*/
var HashMap = require('hashmap');

function UndirectedGraphNode(label){
    this.label = label;
    this.neighbors = [];
}

var map = new HashMap();
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
