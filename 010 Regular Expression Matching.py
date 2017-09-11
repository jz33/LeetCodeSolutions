def isMatch(st,si,pt,pi):
    '''
    st : string, si: string index
    pt : pattern, pi: pattern index
    Notice Python substring is deep copy
    '''
    # if pattern is empty, string must be empty
    if pi >= len(pt): # pi can be larger than len(pt)
        return si == len(st)
    
    # if string is empty, next pattern must be '*'
    if si == len(st):
        return pi+1 < len(pt) and pt[pi+1] == '*' and isMatch(st,si,pt,pi+2)
    
    # if next pattern is not '*' or pattern reached last char
    if pi+1 < len(pt) and pt[pi+1] != '*' or pi + 1 == len(pt):
        return (pt[pi] == '.' or pt[pi] == st[si]) and isMatch(st,si+1,pt,pi+1)
    
    # next pattern is '*': Skip '*' or assume '*' matches more than 1 chars
    return isMatch(st,si,pt,pi+2) or (pt[pi] == '.' or pt[pi] == st[si]) and isMatch(st,si+1,pt,pi)
