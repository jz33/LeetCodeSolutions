from copy import deepcopy
'''
Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/
'''
pool = []

def isPalindrome(s):
    return s == s[-1::-1]

def allPalindromicSubstrings(src, st, r):
    global pool
    if st == len(src):
        pool.append(deepcopy(r))
    elif st < len(src):
        for i in range(st,len(src)):
            sub = src[st:i+1]
            if isPalindrome(sub):
                r.append(sub)
                allPalindromicSubstrings(src,i+1,r)      
                r.pop()
                
def partition(src):
    global pool
    r = []
    allPalindromicSubstrings(src,0,r)
    return pool
        
src = 'a'
r = []
partition(src)
print pool
