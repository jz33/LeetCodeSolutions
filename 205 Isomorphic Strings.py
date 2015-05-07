'''
207 Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/ 
'''
def isIsomorphic(x,y):
    if len(x) != len(y): 
        return False
        
    map = {}
    for i in xrange(0,len(x)):
        if x[i] in map:
            if y[i] != map[x[i]]:
                return False
        else:
            map[x[i]] = y[i]
            
    return True
    
def main():
    print isIsomorphic('egg','add')
    print isIsomorphic('foo','bar')
    print isIsomorphic('paper','title')
    print isIsomorphic('ppper','ptper')
    
if __name__ == '__main__':
    main()
            
