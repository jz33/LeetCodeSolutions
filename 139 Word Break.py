'''
139 Word Break
https://oj.leetcode.com/problems/word-break/
'''
'''
A recursive approach with prefix check
'''
def isWordBreakRec(tag, book):
    if tag == '': return True
    
    # At least 1 prefix is in dict
    i = len(tag) - 1
    while i > -1:
        if tag[i:] in book: break
        i -= 1
            
    # Not found        
    if i == -1:return False
    
    # Loop each prefix
    i = 0
    while i < len(tag)-1:
        prefix = tag[:i+1]
        if prefix in book:
            suffix = tag[i+1:]
            if isWordBreakRec(suffix,book) == True:
                return True
        i += 1
    return tag in book
    
'''
A DP approach
'''
def isWordBreak(tag,book):
    size = len(tag)
    if size == 0: return True
    if tag in book: return True # optional
    
    # 'buf[i]' indicates whether tag[0:i] is work break
    buf = [False for i in xrange(0,size+1)]
    buf[0] = True
    for i in xrange(1,size):
        if buf[i] == False and tag[0:i] in book:
            buf[i] = True
        if buf[i] == True:
             for j in xrange(i+1,size+1):
                if buf[j] == False and tag[i:j] in book:
                    buf[j] = True

    return buf[len(tag)] == True

def test(tag,book):
    print isWordBreakRec(tag,book), ' ', isWordBreak(tag,book)

def main():
    book = set(["mobile","samsung","sam","sung","man","mango",\
    "icecream","and","go","i","like","ice","cream"])
    
    cases = [\
        'ilikesamsung',\
        'iiiiiiii',\
        '',\
        'ilikelikeimangoiii',\
        'samsungandmango',\
        'samsungandmangok',\
        ]
        
    for tag in cases:
        print isWordBreakRec(tag,book), ' ', isWordBreak(tag,book)
      
if __name__ == "__main__":
    main()
