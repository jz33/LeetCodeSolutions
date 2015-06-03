'''
212 Word Seach II
https://leetcode.com/problems/word-search-ii/
'''
root = None
VISITED = '#'

class TrieNode:
    '''
    struct TrieNode
    {
        string key
        hash_map<TrieNode> children
    }
    '''
    def __init__(self, key):
        self.key = key
        self.children  = {}

    '''
    Add $key to Trie
    '''
    def add(self,key,offset):
        if offset < len(key):
            char = key[offset]
            if char not in self.children:
                self.children[char] = TrieNode(key[:offset+1])
            self.children[char].add(key,offset+1)
       
    '''
    Check whether Trie contains whole $key
    '''
    def whole(self, key, offset):
        if offset == len(key):
            return key == self.key and len(self.children) == 0
        if offset <  len(key):
            char = key[offset]
            if char in self.children:
                return self.children[char].whole(key,offset+1)
        return False
    
    '''
    Check whether Trie contains a prefix of $key
    '''
    def prefix(self,key,offset):
        if offset == len(key):
            return key == self.key 
        if offset <  len(key):
            char = key[offset]
            if char in self.children:
                return self.children[char].prefix(key,offset+1)
        return False

def dfs(mat,str,row,col):
    if mat[row][col] == VISITED:
        return 
    
    ori = mat[row][col]
    str = str + ori
    
    if root.prefix(str,0) == False:
        return
    if root.whole(str,0):
        print str
        
    mat[row][col] = VISITED
    
    if row > 0: dfs(mat,str,row-1,col)
    if row < len(mat) - 1: dfs(mat,str,row + 1,col)
    if col > 0: dfs(mat,str, row,col - 1)
    if col < len(mat[0]) - 1: dfs(mat,str,row,col + 1)
    
    mat[row][col] = ori
        
def main():
    global root
    
    mat = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
    ]
    words = ['oath','pea','eat','rain']
    root = TrieNode('')
    for w in words:
        root.add(w,0)
    
    for i in xrange(0,len(mat)):
        for j in xrange(0,len(mat[i])):
            dfs(mat,'',i,j)

if __name__ == '__main__':
    main()
