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

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''
from typing import List, Tuple

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Union Find graph: {node: (parent, weight)}
        '''
        graph = {}

        def getRoot(i : str) -> Tuple[str, int]:
            '''
            Return root of i and total weight
            Notice this question is not optimized by steps
            '''
            weight = 1
            while i in graph:
                p, w = graph[i]
                if p == i:
                    # Get self, means i is root
                    return i, weight
                weight *= w
                i = p
            return i, weight

        # Build Union Find graph
        # 1. Put in all the vertices
        for eq in equations:
            f = eq[0]
            t = eq[1]
            graph[f] = (f, 1)
            graph[t] = (t, 1)

        # 2. Union Edges
        for i in range(len(equations)):
            f = equations[i][0]
            t = equations[i][1]
            v = values[i]

            # Union from -> togo
            rf, wf = getRoot(f)
            rt, wt = getRoot(t)
            
            if rf != rt:
                graph[rf] = (rt, wt / wf * v) # think why

        # 3. Handle queries
        size = len(queries)
        res = [-1.0] * size
        for i, query in enumerate(queries):
            f = query[0]
            t = query[1]
            if f not in graph or t not in graph:
                continue

            rf, wf = getRoot(f)
            rt, wt = getRoot(t)
            if rf != rt:
                # f and t are not connected
                continue

            res[i] = wf / wt

        return res
