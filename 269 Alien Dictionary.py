import pprint
pp = pprint.PrettyPrinter(indent=4)

class Graph(object):
    def __init__(self):
        self.indes = {} # in degrees
        self.edges = {} # edges
        
    def add(self, w):
        indes = self.indes
        edges = self.edges
        for i,e in enumerate(w):
            if e not in edges:
                edges[e] = []
            if i == 0:
                indes[e] = indes.get(e,0)
            else: 
                prev = w[i-1]
                if e != prev:   
                    if e not in edges[prev]:
                        indes[e] = indes.get(e,0) + 1
                        edges[prev] += [e]              
    
    def debug(self):
        pp.pprint(self.indes)
        pp.pprint(self.edges)

    def topologicalSort(self):
        indes = self.indes
        edges = self.edges
        res = []
        q = []
        for i,v in indes.iteritems():
            if v == 0:
                q.append(i)
        while len(q) > 0:
            node = q.pop(0)
            res.append(node)
            for togo in edges[node]:
                d = indes[togo]
                if d == 1:
                    q.append(togo)
                indes[togo] = d - 1
        return res
        
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = Graph()
        for w in words:
            graph.add(w)
        return ''.join(graph.topologicalSort())


words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

sol = Solution()
pp.pprint(sol.alienOrder(words))
