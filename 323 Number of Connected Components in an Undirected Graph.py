'''
Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
'''
def getParent(tree,i):
    '''
    @tree: List[int]
    @i: int
    @return: (int,int)
    '''
    d = 0 # depth
    while tree[i] != -1:
        i = tree[i]
        d += 1
    return i,d
    
def countComponents(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    tree = [-1] * n
    for ed in edges:
        n0, n1 = ed[0],ed[1]
        (p0,d0) = getParent(tree,n0)
        (p1,d1) = getParent(tree,n1)
        if p0 != p1:
            if d0 < d1:
                tree[p0] = p1
            else:
                tree[p1] = p0
    return sum(1 for n in tree if n == -1)
    
n = 10
edges = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
print countComponents(n,edges)
