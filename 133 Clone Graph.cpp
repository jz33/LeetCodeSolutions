#include <iostream>
#include <unordered_map>
using namespace std;
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     std::vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
 
 /*
 DFS
 https://leetcode.com/discuss/26440/9-line-c-dfs-solution
 */

std::unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> map;

UndirectedGraphNode* cloneGraph(UndirectedGraphNode* n) {
   if (!n) return NULL;
   if(map.find(n) == map.end()) {
       map[n] = new UndirectedGraphNode(n->label);
       for (auto x : n->neighbors) {
            (map[n]->neighbors).push_back(cloneGraph(x));
       }
   }
   return map[n];
}
