'''
139 Word Break
140 Word Ladder II
https://oj.leetcode.com/problems/word-break/
https://oj.leetcode.com/problems/word-break-ii/

http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/
'''
'''
# 0. A normal recursive approach
'''
def isWordBreakRec(tag, book):
    if len(tag) == 0: return True
        
    for i in xrange(0,len(tag)):
        prefix = tag[0:i+1]
        suffix = tag[i+1:]
        if prefix in book and isWordBreakRec(suffix, book):
            return True;
    return False
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
    book = {"mobile","samsung","sam","sung","man","mango",\
    "icecream","and","go","i","like","ice","cream"}
    
    tag = 'ilikesamsung'
    test(tag,book)
    tag = 'iiiiiiii'
    test(tag,book)
    tag = ''
    test(tag,book)
    tag = 'ilikelikeimangoiii'
    test(tag,book)
    tag = 'samsungandmango'
    test(tag,book)
    tag = 'samsungandmangok'
    test(tag,book)
      
if __name__ == "__main__":
    main()