'''
44 Wildcard Matching
https://oj.leetcode.com/problems/wildcard-matching/
'?' matches any single char
'*' matches 0 or more any chars
https://leetcode.com/discuss/38645/128ms-o-1-space-python-solution
Accepted
'''
def isMatch(s, p):
    '''
    s: string
    p: pattern
    '''
    if not p: return not s
    si = 0
    pi = 0
    prev_s = 0
    prev_p = -1
    while si < len(s):
        if pi < len(p) and (p[pi] == '?' or p[pi] == s[si]):
            # normal match
            si += 1
            pi += 1
        elif pi < len(p) and p[pi] == '*':
            # '*' match 1 char
            prev_s = si
            prev_p = pi
            pi += 1
        elif prev_p > -1:
            # '*' match more than 1 char
            si = prev_s + 1
            pi = prev_p
            prev_s = si
        else:
            return False

    for i in xrange(pi,len(p)):
        if p[i] != '*':
            return False
    else:
        return True
