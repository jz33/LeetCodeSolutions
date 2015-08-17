def getDepth(n):
    '''
    Make sure to go left
    '''
    d = 0
    while n is not None:
        n = n.left
        d += 1
    return d

def getMid(n,d):
    '''
    @n: node != None
    @d: depth, >= 1
    @return: can be None
    '''
    n = n.left
    if d == 1: return n
    while d > 1:
        n = n.right
        d -= 1
    return n

def countNodes(n):
    depth = getDepth(n)
    if depth <= 1 : return depth
    
    lastRow = 0
    for i in xrange(depth - 1, 0, -1):
        leaf = getMid(n,i)
        if leaf is None:
            n = n.left
        else:
            lastRow += (1 << (i - 1))
            n = n.right
    if n is not None: lastRow += 1
    
    uponLastRow = (1 << (depth -1)) - 1
    return uponLastRow + lastRow
