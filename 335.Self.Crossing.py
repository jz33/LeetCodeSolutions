'''
Self Crossing
https://leetcode.com/problems/self-crossing/
'''
def isSelfCrossing(dirs):
    if len(dirs) == 0: return False
    s = set()
    c = (0,0)
    s.add(c)
    for i,d in enumerate(dirs):
        r = i % 4
        for _ in xrange(d):           
            if r == 0:
                c = (c[0]-1,c[1])
            elif r == 1:
                c = (c[0],c[1]-1)
            elif r == 2:
                c = (c[0]+1,c[1])
            else:
                c = (c[0],c[1]+1)
            if c in s:
                return True
            s.add(c)
    return False

dirs = [1, 2, 3, 4]
print isSelfCrossing(dirs)
