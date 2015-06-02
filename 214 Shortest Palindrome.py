'''
214 Shortest Palindrome 
https://leetcode.com/problems/shortest-palindrome/
'''
def isPalindromic(input,lt,rt):
    # left side might be incomplete
    while lt > -1:
        if input[lt] != input[rt]:
            return False
        lt -= 1
        rt += 1
    return True
'''
Notion of initial $lt, $rt:
     lt rt
a a c e c a a a
   lt
a b a a a

return shorted length
'''
def compute(input):
    lt = (len(input)- 1) >> 1
    rt =  len(input) >> 1
    
    while lt > -1:
        if isPalindromic(input,lt,rt):
            return len(input) - rt - 1 - lt
        if rt > lt :
            rt = lt
        else:
            lt -= 1

def main():
    tests = [\
        'aacecaaa',\
        'abcd',\
        'aabaa',\
        'abaa',\
        'abbaa',\
        'aabbaa',\
        ]
    for t in tests:
        print t, compute(t)
    
if __name__ == "__main__":
    main()
