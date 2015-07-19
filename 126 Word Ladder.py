'''
126 Word Ladder
https://leetcode.com/problems/word-ladder/

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
   
This implementation exceeds time limit,
but is right
'''
level = 2
book = set()
width = 0

def isLinked(src, tag):
    global width
    diff = 0
    i = 0 
    j = 0
    while i < width and j < width and diff < 2:
        if tag[i] != src[j]: diff += 1
        i += 1
        j += 1
    return diff == 1
    
def iterate(upper,lower):
    '''
    @upper: set[node]
    @lower: set[node]
    '''
    global level,book
    
    if len(upper & lower) > 0:
        level -= 1 # connected !
        return
        
    if len(book) == 0: 
        level = 0 #unconnected
        return
    
    # iterate upper
    newUpper = set()
    for e in upper:
        for b in book:
            if isLinked(e,b):
                newUpper.add(b)
                
    if len(newUpper) == 0:
        level = 0 # unconnected
        return
    
    print "newUpper: ", newUpper
    
    # iterate lower
    newLower = set()
    for e in lower:
        for b in book:
            if isLinked(e,b):
                newLower.add(b)
    
    if len(newLower) == 0:
        level = 0 # unconnected
        return
      
    print "newLower: ", newLower
                 
    # clean $book
    for e in newUpper:
        book.discard(e)
    for e in newLower:
        book.discard(e)
     
    # clean current levels
    upper.clear()
    lower.clear()
    
    # next iteration
    level += 2
    iterate(newUpper,newLower)
    
def ladderLength(start, ended, wordDict):
    global level,book,width
    if len(wordDict) == 0: return 0
    
    for w in wordDict:
        width = len(w)
        break
        
    book = wordDict
    
    newUpper = set([start])
    newLower = set([ended])
    iterate(newUpper,newLower)
    
    return level
    
# test
wordDict = set(["a","b","c"])
start = "a"
ended = "c"
print ladderLength(start, ended, wordDict)
