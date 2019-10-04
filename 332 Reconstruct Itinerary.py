'''
332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries,
you should return the itinerary that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''
from collections import defaultdict

class Solution:
    def dfs(self, itinerary):
        '''
        Do dfs/back tracking, reture True if all route is iterated
        '''
        if len(itinerary) == self.total:
            return True
        
        f = itinerary[-1]
        for t in self.graph[f]:
            if t[1] == False:
                itinerary.append(t[0])
                t[1] = True
                
                if self.dfs(itinerary):
                    return True
                
                # Back track, reset
                itinerary.pop()
                t[1] = False
    
        return False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build graph, sort togo by lexical order
        graph = defaultdict(list) # {from : [[togo, whether this edge is visited]]}
        for f, t in tickets:
            graph[f].append([t, False])
        
        for f in graph.keys():
            graph[f].sort(key = lambda x : x[0])
            
        self.total = len(tickets) + 1
        self.graph = graph
        
        itinerary = ['JFK']
        self.dfs(itinerary)
        return itinerary
