from copy import deepcopy
'''
127 Word Ladder II
https://leetcode.com/problems/word-ladder-ii/
Double-sided BFS

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
A = ord('a')
width = 0 # word length
start = ""
ended = ""
book = set()
pool = [] # answers

def traceRec(node,path,result,history):
    parents = history.get(node,None)
    if parents == None:
        result.append(path)
    else:
        for p in parents:
            newPath = deepcopy(path)
            newPath.append(p)
            traceRec(p,newPath,result,history)
        
def trace(up,lo,history):
    '''
    Make sure $path has no cycles
    1 node can have multiple parents
    '''
    up_path = [up]
    up_result = []
    traceRec(up,up_path,up_result,history)
    
    lo_path = [lo]
    lo_result = []
    traceRec(lo,lo_path,lo_result,history)

    if up_result[0][-1] == ended:
        up_result,lo_result = lo_result,up_result
        
    for up_path in up_result:
        for lo_path in lo_result:
            pool.append(up_path[::-1] + lo_path)
   
            
def iterate():
    upper = set()
    upper.add(start)
    lower = set()
    lower.add(ended)
    
    # node : [parent1, parent2, ...]
    history  = {start : None, ended : None}
    
    found = False
    while found is False: 
        # make sure len(upper) <= len(lower)
        if len(upper) > len(lower):
            upper, lower = lower, upper
        
        row = set()
        for up in upper:
            ls = list(up)
            for i in xrange(0,width):
                ori = ls[i]
                for j in xrange(0,26):
                    ls[i] = chr(A + j)
                    if ls[i] == ori: continue
                    lo = ''.join(ls)
                    if lo in lower:
                        found = True
                        trace(up,lo,history)
                    elif lo in book:
                        row.add(lo)
                        parents = history.get(lo,None)
                        if parents == None:
                            history[lo] = [up]
                        else:
                            parents.append(up)
                ls[i] = ori
                
        if len(row) == 0: return
        upper, row = row, upper  
        
        for up in upper: book.discard(up)
        
        print "upper:", upper
        print "lower:", lower

        
def findLadders(beginWord, endWord, wordlist):
    global width, start, ended, book, pool
    width = len(beginWord)
    start = beginWord
    ended = endWord
    book = wordlist
    book.discard(start)
    book.discard(ended)
    pool = []
    iterate()
    return pool

'''    
beginWord = "hit"
endWord = "cog"
wordlist = set(["hot","dot","dog","lot","log"])
'''
beginWord = "hot"
endWord = "dog"
wordlist = set(["hot","dog","dot"])

beginWord = "hit"
endWord = "cog"
wordlist = set(["hot","cog","dot","dog","hit","lot","log"])

beginWord = "magic"
endWord = "pearl"
wordlist = set(["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]);

res = findLadders(beginWord, endWord, wordlist)
print res
print len(res)
