'''
Number of Islands II
https://leetcode.com/problems/number-of-islands-ii/

Union-Find
https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
'''
def getParent(tree,pt):
    '''
    :type tree: {(int,int):(int,int)} 
    :type pt: (int,int)
    :rtype: return root of pt. If pt itself is root, return itself
    pt must be in tree
    '''
    steps = 0
    t = tree.get(pt,None)
    while t is not None:
        pt = t
        t = tree.get(pt,None)
        steps += 1
    return pt,steps

def update(tree,i,j,res):
    neighbors = [] # root node of neighbors
    maxDepth, maxDepthRoot = 0, None
    
    # iterate neighbors, find the neighbor that has max depth root
    for node in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
        if node in tree:
            root,depth = getParent(tree,node)
            if maxDepthRoot is None or depth > maxDepth:
                maxDepth, maxDepthRoot = depth, root
            neighbors.append(root)

    tree[(i,j)] = maxDepthRoot # maxDepthRoot can be None

    # union all neighbors, and get unique root count
    s = set()
    for root in neighbors:
        if root != maxDepthRoot: # critical!
            tree[root] = maxDepthRoot # maxDepthRoot cannot be None
        s.add(root)

    res.append(res[-1] + 1 - len(s))

def numIslands2(m, n, points):
    """
    :type m: int
    :type n: int
    :type points: List[List[int]]
    :rtype: List[int]
    """
    '''
    Tree is defined as {child:parent}.
    If a child is root node, its parent is None
    '''
    tree = {}
    res = [0]
    for i,j in points:
        if (i,j) not in tree: 
            update(tree,i,j,res)   
    return res[1:]
    

m = 3
n = 3
points = [[0,0],[0,1],[1,2],[2,1]]
points = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
print numIslands2(m, n, points)
