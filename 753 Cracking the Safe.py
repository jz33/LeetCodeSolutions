'''
753. Cracking the Safe
https://leetcode.com/problems/cracking-the-safe/

There is a box protected by a password. The password is a sequence of n digits where each digit can be one of
the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because
the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

Example 1:

Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.

Example 2:

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.

Note:

    n will be in the range [1, 4].
    k will be in the range [1, 10].
    k ^ n will be at most 4096.

'''
class Solution:
    '''
    Time complexity is K ^ N
    '''
    def crackSafe(self, n: int, k: int) -> str:
        '''
        Think about a graph, there are k ^ (n-1) nodes, each node
        has k different edges, so there are totally k ^ n edges.
        To find a path covering all the edges without visiting an edge twice,
        this is to find an Euler path.
        To further define the graph, if a Node is string s,
        then its edges are s + i for i in range(k), and its neighbor
        nodes are (s + i)[1:]
        '''
        visited = set() # visited edges
        path = []

        def dfs(node):
            for i in map(str, range(k)):
                edge = node + i
                if edge not in visited:
                    visited.add(edge)

                    newNode = edge[1:]
                    dfs(newNode)

                    path.append(i)

        startNode = '0' * (n-1)
        dfs(startNode)

        '''
        So adding the startNode, this is the full path if looking from back. 
        For example, if k = 2, n = 2, the result is 01100.
        This means the Euler path is from startNode 0, first to 
        0 node via 00 edge, then go to 1 node via 01, then go to
        1 node via 11, then go to 0 node via 10
        '''
        return "".join(path) + startNode
