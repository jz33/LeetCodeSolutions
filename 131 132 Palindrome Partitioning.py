'''
131 Palindrome Partitioning
132 Palindrome Partitioning II
https://oj.leetcode.com/problems/palindrome-partitioning/
https://oj.leetcode.com/problems/palindrome-partitioning-ii/
'''
# 132 https://oj.leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space.
def minCut(s):
    n = len(s)
    cut = [] # number of cuts for the first k characters
    for i in range(0,n+1): cut.append(i-1)
    for i in range(0,n):
        j = 0
        while i-j > -1 and i+j < n and s[i-j] == s[i+j]:
            cut[i+j+1] = min(cut[i+j+1],1+cut[i-j])
            j += 1
            
        j = 1
        while i-j+1 > -1 and i+j < n and s[i-j+1] == s[i+j]:
            cut[i+j+1] = min(cut[i+j+1],1+cut[i-j+1])
            j += 1
            
    return cut[n]

# 131, back tracking
def isPalindrome(s):
    return s == s[-1::-1]

def allPalindromicSubstrings(s, st, r):
        if st>= len(s):
            print r
        else:
            for i in range(st,len(s)):
                sub = s[st:i+1]
                if isPalindrome(sub):
                    r.append(sub)
                    allPalindromicSubstrings(s,i+1,r)      
                    r.pop()
   
def main():
    s = "aabbccc"
    print minCut(s)

    r = []
    allPalindromicSubstrings(s,0,r)
    
if __name__ == "__main__":
    main()
