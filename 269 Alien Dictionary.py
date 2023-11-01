'''
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are
sorted lexicographically
by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules.
If there are multiple solutions, return any of them.

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:

Input: words = ["z","x"]
Output: "zx"

Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of only lowercase English letters.
'''
from typing import List, Tuple, Union

import pprint
pp = pprint.PrettyPrinter(indent=4)

class Graph(object):
    def __init__(self):
        self.ranks = {} # {char : reach count}
        self.edges = {} # {from char : set(togo chars)}
        
    def compare(self, a: str, b: str) -> Union[Tuple[str, str], None]:
        # Compare 2 words, return why a is in front of b
        size = min(len(a), len(b))
        for i in range(size):
            if a[i] != b[i]:
                return a[i], b[i]
        return None

    def build(self, words: List[str])-> bool:
        ranks = self.ranks
        edges = self.edges

        # Put all chars (nodes)
        for word in words:
            for char in word:
                if char not in ranks:
                    ranks[char] = 0
                    edges[char] = set()
                    
        # Compare each word with all its following words
        for i in range(len(words) - 1):
            pair = self.compare(words[i], words[i+1])
            if pair:
               fromChar, togoChar = pair[0], pair[1]
               if togoChar not in edges[fromChar]:
                  edges[fromChar].add(togoChar)
                  ranks[togoChar] += 1
            elif len(words[i]) > len(words[i+1]):
                # For cases like ['abc', 'ab'], 'abc' should never go in front of 'ab'
                return False
            
        return True
         
    def debug(self):
        pp.pprint(self.ranks)
        pp.pprint(self.edges)

    def topologicalSort(self) -> List[str]:
        ranks = self.ranks
        edges = self.edges
        
        # Get the starting nodes
        queue = [i for i,d in ranks.items() if d == 0]
        queueIndex = 0
        while queueIndex < len(queue):
            node = queue[queueIndex]

            for togo in edges[node]:
                reachCount = ranks[togo]
                if reachCount == 1:
                    queue.append(togo)
                ranks[togo] = reachCount - 1
            
            queueIndex += 1
    
        return queue if len(queue) == len(ranks) else []
    
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = Graph()
        if graph.build(words):
            return ''.join(graph.topologicalSort())
        return ''
