'''
839. Similar String Groups
https://leetcode.com/problems/similar-string-groups/

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar,
but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
Notice that "tars" and "arts" are in the same group even though they are not similar.
Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

Example 1:

Input: ["tars","rats","arts","star"]
Output: 2
Note:

A.length <= 2000
A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
'''
from collections import defaultdict

class UnionFind:
    def __init__(self, size: int):
        self.roots = [i for i in range(size)]

    def find(self, node: int) -> int:
        '''
        Pay attention to this "Find".
        It returns node's root, and also all node's parent's root to root
        '''
        if self.roots[node] != node:
            self.roots[node] = self.find(self.roots[node])
        return self.roots[node]

    def union(self, a: int, b: int):
        self.roots[self.find(a)] = self.find(b)

    def rootCount(self) -> int:
        return sum(1 for i in range(len(self.roots)) if self.roots[i] == i)

class Solution(object):
    def areSimilar(self, a: str, b: str) -> bool:
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
            if diff > 2:
                return False
        return True

    def numSimilarGroups(self, A):
        wordCount = len(A)
        wordSize = len(A[0])
        graph = UnionFind(wordCount)

        # If few words, then check for pairwise similarity: O(wordCount^2 * wordSize)
        if wordCount < wordSize * wordSize: 
            for (i, wa), (j, wb) in itertools.combinations(enumerate(A), 2):
                if self.areSimilar(wa, wb):
                    graph.union(i, j)

        # # If many words, check all neighbors: O(wordCount * wordSize ^3)
        else:
            neighbors = defaultdict(set)
            for wi, word in enumerate(map(list, A)):
                for i, j in itertools.combinations(range(wordSize), 2):
                    word[i], word[j] = word[j], word[i]
                    neighbors["".join(word)].add(wi)
                    word[i], word[j] = word[j], word[i]

            for wi, word in enumerate(A):
                for ni in neighbors[word]:
                    graph.union(wi, ni)

        return graph.rootCount()
