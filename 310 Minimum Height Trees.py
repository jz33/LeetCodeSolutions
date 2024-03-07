'''
310. Minimum Height Trees
https://leetcode.com/problems/minimum-height-trees/

A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1,
and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is
an undirected edge between the two nodes ai and bi in the tree,
you can choose any node of the tree as the root.
When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h)) are called
minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between
the root and a leaf.

Example 1:

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Constraints:
    1 <= n <= 2 * 104
    edges.length == n - 1
    0 <= ai, bi < n
    ai != bi
    All the pairs (ai, bi) are distinct.
    The given input is guaranteed to be a tree and there will be no repeated edges.
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        The idea is to remove leaves layer by layer until
        there are no more inner nodes
        '''
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
                
        leaves = deque([i for i in range(n) if len(graph[i]) <= 1])
        innerNodeCount = n - len(leaves)
        
        while innerNodeCount > 0:
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                # Remove this leaf from the graph
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                
                # If parent becomes a new leaf, add to queue
                if len(graph[parent]) == 1:
                    leaves.append(parent)
            innerNodeCount -= len(leaves)

        return leaves
