'''
Topological sort on a valid tree graph, print all possible combinations
'''
from typing import List
from copy import deepcopy

class Solution:
    def __init__(self, houses, edges):
        self.results = []
        self.houseCount = len(houses)
        self.build(houses, edges)

    def build(self, houses: List[str], edges):
        graph = {}
        degrees = {}
        for h in houses:
            graph[h] = set()
            degrees[h] = 0
        for f, t in edges:
            graph[f].add(t)
            degrees[t] += 1

        self.graph = graph
        self.degrees = degrees

    def dfs(self, queue: List[str], degrees, result: List[str]):
        if len(result) == self.houseCount:
            self.pool.append(result)
            return
            
        for i, h in enumerate(queue):
            newResult = result + [h]
            newQueue = queue[:i] + queue[i+1:]
            newDegrees = deepcopy(degrees)

            # Try find if there can be new queue element
            for togo in self.graph[h]:
                newDegrees[togo] -= 1
                if newDegrees[togo] == 0:
                    newQueue.append(togo)

            self.dfs(newQueue, newDegrees, newResult)
                    
    def showHouse(self) -> List[List[str]]:
        self.pool = []

        queue = [h for h,c in self.degrees.items() if c == 0]
        self.dfs(queue, self.degrees, [])

        return self.pool

houses = ['a', 'b', 'c', 'd', 'e']
edges = [['a', 'b'], ['c', 'd']]
sol = Solution(houses, edges)
print(sol.showHouse())
