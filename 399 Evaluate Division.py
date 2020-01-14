'''
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number
(floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
'''
from typing import Tuple

class Solution:
    def getDenominator(self, node: str, graph) -> Tuple[str, float]:
        '''
        Essentially, node is a numerator, keep finding the denominator
        '''
        division = 1
        while True:
            parent, value = graph[node]
            if parent == node:
                return node, division
            division *= value
            node = parent
        
        raise ValueError('Not reachable')
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Build Union Find graph
        # 1. Put in all the vertices
        graph = {} # {numerator : (denominator, division result)}
        for f, t in equations:
            graph[f] = (f, 1)
            graph[t] = (t, 1)

        # 2. Union Edges
        for i in range(len(equations)):
            f = equations[i][0]
            t = equations[i][1]
            v = values[i]

            df, wf = self.getDenominator(f, graph)
            dt, wt = self.getDenominator(t, graph)
            if df != dt:                          
                # f / df = wf
                # t / dt = wt
                # => df / dt = f / t * wt / wf = v * wf / wt
                graph[df] = (dt, v * wt / wf)

        # 3. Handle queries
        res = [-1.0] * len(queries)
        for i, query in enumerate(queries):
            f = query[0]
            t = query[1]
            if f not in graph or t not in graph:
                continue

            df, wf = self.getDenominator(f, graph)
            dt, wt = self.getDenominator(t, graph)
            if df == dt:
                # f / df = wf
                # t / dt = wt
                # => f / t =  wf / wt * df / dt = wf / wt
                res[i] = wf / wt

        return res   
