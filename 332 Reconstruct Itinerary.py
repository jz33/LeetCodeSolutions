'''
332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent
the departure and the arrival airports of one flight.
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus,
the itinerary must begin with "JFK".
If there are multiple valid itineraries,
you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
    1 <= tickets.length <= 300
    tickets[i].length == 2
    fromi.length == 3
    toi.length == 3
    fromi and toi consist of uppercase English letters.
    fromi != toi
'''
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build the source : [targets] graph, which targets reversely sorted,
        # as the last target wants to pop first
        graph = {} # { src : [targets]}
        for src, tag in sorted(tickets)[::-1]:
            graph[src] = graph.get(src, []) + [tag]
        
        itinerary = []

        def dfs(airport):
            '''
            The idea of finding Euler path is dfs until stuck,
            put the stuck point as the last node in the path.
            '''
            while graph.get(airport, []):
                # Remove visited edge
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs('JFK')
        return itinerary[::-1]


sol = Solution()
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(sol.findItinerary(tickets))
