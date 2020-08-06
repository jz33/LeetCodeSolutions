'''
1361. Validate Binary Tree Nodes
https://leetcode.com/problems/validate-binary-tree-nodes/

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i],
return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:

Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false

Constraints:

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
'''
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ranks = [0] * n
        graph = [[] * n for _ in range(n)]
        
        # 1. Build graph and in-degrees
        def parse(childrenList: List[int]) -> bool:
            for p, c in enumerate(childrenList):
                if c != -1:
                    if ranks[c] != 0:
                        # A child can only have 1 parent
                        return False

                    if len(graph[p]) == 1 and graph[p][0] == c:
                        # A parent's left and right children should be different
                        return False

                    ranks[c] = 1
                    graph[p].append(c)
                    
            return True
        
        if not parse(leftChild) or not parse(rightChild):
            return False
        
        # 2. Topological sort
        stack = [i for i in range(n) if ranks[i] == 0]
        if len(stack) != 1:
            # Either no root or more than 1 root
            return False
        
        nodeCount = 1
        while stack:
            newStack = []
            for node in stack:
                for child in graph[node]:
                    if ranks[child] == 0:
                        # Reached this child again, i.e., cycled
                        return False
                    
                    ranks[child] = 0
                    newStack.append(child)
    
            stack = newStack
            nodeCount += len(stack)
            
        # All nodes must be reached
        return nodeCount == n
