'''
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/

There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Example 1:

Input:
[ "wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"

Example 2:

Input:
["z", "x"]
Output: "zx"

Example 3:

Input:["z", "x", "z"] 
Output: "" 

Explanation: The order is invalid, so return "".

Example 4:

Input:["z", "z"] 
Output: "z" 

Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''
from typing import List, Tuple
from collections import defaultdict, Counter, deque

import pprint
pp = pprint.PrettyPrinter(indent=4)

class Graph(object):
    def __init__(self):
        self.ranks = Counter() # How many time the node is reached?
        self.edges = defaultdict(set) # {from char: set(togo chars)}
        
    def compare(self, a: str, b: str) -> Tuple[str, str]:
        '''
        Compare 2 words, return why a is in front of b
        '''
        size = min(len(a), len(b))
        for i in range(size):
            ca = a[i]
            cb = b[i]
            if ca != cb:
                return ca, cb

        return None

    def add(self, words: List[str]):
        ranks = self.ranks
        edges = self.edges

        # 1. Put all chars (nodes)
        for word in words:
            for c in word:
                if c not in ranks:
                    ranks[c] = 0
                    edges[c] = set()

        # 2. Add edges
        for i in range(len(words)):
            wi = words[i]
            for j in range(i+1, len(words)):
                wj = words[j]
                pair = self.compare(wi, wj)
                if pair:
                    f, t = pair[0], pair[1]
                    if t not in edges[f]:
                        edges[f].add(t)
                        ranks[t] += 1
 
     
    def debug(self):
        pp.pprint(self.ranks)
        pp.pprint(self.edges)

    def topologicalSort(self) -> List[str]:
        ranks = self.ranks
        edges = self.edges
        res = []
        
        queue = deque([i for i,d in ranks.items() if d == 0])    
        while queue:
            # Notice size of queue can be bigger than 1,
            # which means more than 1 possible order
            node = queue.popleft()
            res.append(node)

            for togo in edges[node]:
                d = ranks[togo]
                if d == 1:
                    queue.append(togo)
                ranks[togo] -= 1
    
        return res if len(res) == len(ranks) else ''
    
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = Graph()
        graph.add(words)
        return ''.join(graph.topologicalSort())
