'''
20 Valid Parentheses
https://oj.leetcode.com/problems/valid-parentheses/
'''
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    buf = [-1]
    for c in s:
        if c == '(': 
            buf.append(0)
        elif c == '{':
            buf.append(1)
        elif c == '[':
            buf.append(2)
        elif c == ')':
            if buf[-1] != 0: 
                return False
            else:
                buf.pop()
        elif c == '}':
            if buf[-1] != 1:
                return False
            else:
                buf.pop()
        elif c == ']':
            if buf[-1] != 2:
                return False
            else:
                buf.pop()
        else:
            return False
    return len(buf) == 1
