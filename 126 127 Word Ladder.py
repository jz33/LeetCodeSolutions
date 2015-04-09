'''
126 Word Ladder
127 Word Ladder II

Double-sided BFS
Try to find the shorted solutions

Input sample:
hit
cog
hot dot dog lot log

   hit => start
    |
   hot => entries   \
  /   \
dot    lot           tree                       
|       |
dog    log => exits /
  \   /
   cog => ended
'''

pool = []
EMPTY = '-1'

class node:
    '''
    Assume one node has only one daddy
    '''
    def __init__(self,name):
        self.name = name
        self.dady = None
    
def isLinked(src, tag):
    '''
    @src: str
    @tag: str
    '''
    diff = 0
    i = 0 
    j = 0
    while i < len(tag) and j < len(src) and diff < 2:
        if tag[i] != src[j]: diff += 1
        i += 1
        j += 1
    return diff == 1

def hasCommon(upper,lower):
    global pool
    '''
    @upper: list[node]
    @lower: list[node]
    '''
    found = False
    for u in upper:
        for l in lower:
            if isLinked(u.name,l.name):
                seq = [u,l]
                p = u.dady
                while p is not None:
                    seq.insert(0,p)
                    p = p.dady
                p = l.dady
                while p is not None:
                    seq.append(p)
                    p = p.dady
                pool.append(seq)
                found = True
    return found
    
def iterate(remains,upper,lower):
    '''
    @remains: list[str]
    @upper: list[node]
    @lower: list[node]
    '''
    global EMPTY
    if hasCommon(upper,lower): return
    
    newUpper = []
    newLower = []
    
    for i,r in enumerate(remains):
        linked = False
        if r != EMPTY:
            for u in upper:
                if isLinked(r,u.name):
                    n = node(r)
                    n.dady = u
                    newUpper.append(n)
                    linked = True
                    break
            if linked == True: continue
            for l in lower:
                if isLinked(r,l.name):
                    n = node(r)
                    n.dady = l
                    newLower.append(n)
                    linked = True
                    break    
        if linked: remains[i] = EMPTY
        
    if len(newUpper) == 0 and len(newLower) == 0:
        return
    elif len(newUpper) == 0:
        del lower[:]
        iterate(remains,upper,newLower)
    elif len(newLower) == 0:
        del upper[:]
        iterate(remains,newUpper,lower)
    else:
        del upper[:]
        del lower[:]
        iterate(remains,newUpper,newLower)

def main():
    file = open('small.in','r')
    cases = file.readlines()
    lineId = 0
    caseId = 0
    while lineId < len(cases):
        caseId += 1
        
        del pool[:]
        
        s = cases[lineId].strip()
        start = node(s)
        
        s = cases[lineId+1].strip()
        ended = node(s)
        
        remains = cases[lineId+2].strip().split(' ')
        upper = [start]
        lower = [ended]
        
        iterate(remains,upper,lower)
        
        print 'Case #%d:' % (caseId)
        if len(pool) == 0:
            print 'IMPOSSIBLE' 
        else:
            for seq in pool:
                for s in seq:
                    print s.name,
                print
                
        lineId += 3
    file.close()

if __name__ == '__main__':
    main()
