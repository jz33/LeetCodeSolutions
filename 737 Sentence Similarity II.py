'''
737. Sentence Similarity II
https://leetcode.com/problems/sentence-similarity-ii/

Given two sentences words1, words2 (each represented as an array of strings),
and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar,
if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar,
and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"],
pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words.
So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
'''
from typing import Tuple

class Solution:
    def getParent(self, graph, node) -> Tuple[str, int]:
        depth = 0
        parent = node
        while node in graph:
            parent = graph[node]
            node = parent
            depth += 1
        return parent, depth
        
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        l1 = len(words1)
        l2 = len(words2)
        if l1 != l2:
            return False
        
        # Build Union-Find graph
        graph = {}
        for a,b in pairs:
            ra,da = self.getParent(graph, a)
            rb,db = self.getParent(graph, b)
            if ra != rb:
                if da <= db:
                    graph[rb] = ra
                else:
                    graph[ra] = rb
            
        # Test
        for i in range(l1):
            w1 = words1[i]
            w2 = words2[i]
            r1,_ = self.getParent(graph, w1)
            r2,_ = self.getParent(graph, w2)
            if r1 != r2:
                return False
        
        return True
