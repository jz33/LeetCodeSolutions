'''
Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome/
'''
def shortestPalindrome(ori):
    rev = ori[::-1]
    ndl = ori + '#' + rev;
    
    #build KMP table
    T = [0] * len(ndl)
    T[0] = -1
    i = 0
    j = 2
    while j < len(ndl):
        if ndl[j-1] == ndl[i]:
            i += 1
            T[j] = i
            j += 1
        elif i > 0:
            i = T[i]
        else:
            T[j] = 0
            j += 1
    
    print T
    # return
    return rev[:len(ori) - (T[-1]+1)] + ori; 
