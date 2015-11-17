'''
Number of Islands II
https://leetcode.com/problems/number-of-islands-ii/

Union-Find
https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
'''
def getParent(parents,pt):
    '''
    :type parents: {(int,int):(int,int)} 
    :type pt: (int,int)
    :rtype: ((int,int),int)
    '''
    steps = 0
    pa = parents.get(pt,None)
    while pa != None:
        pt = pa
        pa = parents.get(pt,None)
        steps += 1
    return pt,steps

def update(parents,i,j,res):
    neighbors = []
    maxDepth, maxDepthRoot = 0, None
    for node in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
        if node in parents:
            root,depth = getParent(parents,node)
            if maxDepthRoot is None or depth > maxDepth:
                maxDepth, maxDepthRoot = depth, root
            neighbors.append(root)

    # root that has largest depth
    parents[(i,j)] = maxDepthRoot

    # union, and get unique root count
    s = set()
    for node in neighbors:
        if node != maxDepthRoot:
            parents[node] = maxDepthRoot
        s.add(node)

    res.append(res[-1] + 1 - len(s))

def numIslands2(m, n, points):
    """
    :type m: int
    :type n: int
    :type points: List[List[int]]
    :rtype: List[int]
    """
    parents = {}
    res = [0]
    for x,y in points:
        if (x,y) in parents: continue
        update(parents,x,y,res)   
    return res[1:]

points = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
r = numIslands2(3,3,points)
print r
