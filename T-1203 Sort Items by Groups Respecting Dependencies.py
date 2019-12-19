'''
1203. Sort Items by Groups Respecting Dependencies
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

There are n items each belonging to zero or one of m groups where group[i] is
the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group.
The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

    The items that belong to the same group are next to each other in the sorted list.
    There are some relations between these items where beforeItems[i] is a list containing
    all the items that should come before the i-th item in the sorted array (to the left of the i-th item).

Return any solution if there is more than one solution and return an empty list if there is no solution.

Example 1:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]

Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

Constraints:

    1 <= m <= n <= 3*10^4
    group.length == beforeItems.length == n
    -1 <= group[i] <= m-1
    0 <= beforeItems[i].length <= n-1
    0 <= beforeItems[i][j] <= n-1
    i != beforeItems[i][j]
    beforeItems[i] does not contain duplicates elements
'''
from collections import deque

class Graph:
    '''
    The graph holds edges, from : [togos]
    If the node is integer, it is a real node;
    if the node is a str, it is the group id
    '''
    def __init__(self, gid):
        self.gid = gid
        self.edges = {}
        self.sortedList = []
    
    def add(self, f, t = None):
        '''
        Add either an edge (from, togo) or a single node
        '''
        edges = self.edges
        if f not in edges:
            edges[f] = set()
        if t is not None:
            edges[f].add(t)
            
    def sort(self) -> bool:
        '''
        Topological sort
        '''
        edges = self.edges

        # Compute in-degree ranks
        ranks = {}
        for node in edges.keys():
            if node not in ranks:
                ranks[node] = 0
            for togo in edges[node]:
                ranks[togo] = ranks.get(togo, 0) + 1 

        res = []
        queue = deque([i for i,d in ranks.items() if d == 0])    
        while queue:
            node = queue.popleft()
            res.append(node)

            for togo in edges[node]:
                d = ranks[togo]
                if d == 1:
                    queue.append(togo)
                ranks[togo] -= 1

        if len(res) != len(ranks):
            return False

        self.sortedList = res
        return True
    
    def __repr__(self):
        return str(self.gid) + " " + str(self.edges)
                     
        
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # build 2 graphs
        # 1. Has group id nodes, put into graphs identified by group id
        # 2. Overall group, includes group id nodes, and -1 group id nodes
        allGroups = [Graph(i) for i in range(m)]
        overall = Graph(-1)
        for i in range(n):
            gid = group[i]
            if gid == -1:
                overall.add(i)
            else:
                allGroups[gid].add(i)
                overall.add(str(gid))
                
            for b in beforeItems[i]:
                bgid = group[b]
                if gid != -1 and bgid != -1 and gid == bgid:
                    allGroups[gid].add(b, i)
                else:
                    overall.add(b if bgid == -1 else str(bgid), i if gid == -1 else str(gid))
                    
        for graph in allGroups:
            if not graph.sort():
                return []
            
        if not overall.sort():
            return []
        
        res = []
        for e in overall.sortedList:
            if isinstance(e, str):
                res += allGroups[int(e)].sortedList
            else:
                res.append(e)
        return res
