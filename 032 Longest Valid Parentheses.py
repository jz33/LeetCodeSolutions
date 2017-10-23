import random
'''
32 Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/description/
O(n), 2 paths
'''
# generate a random Parentheses string with size n
def randParentheses(n):
    return ''.join(random.choice('('+')') for _ in range(n))
 
def longestValidParentheses(src):
    if len(src) < 2: return 0
    res = 0
    '''
    Notations for 'buf' :
    '0' : currently paired
    >0  : num of '(' - num of ')'
    <0  : invalid (abort)
    '''
    buf = 0        
    s = 0 # start index
    for i in xrange(len(src)):
        if src[i] == '(':
            buf += 1
        else:
            buf -= 1
            if buf == 0:
                res = max(res, i - s + 1)
            elif buf < 0: # reset
                buf = 0
                s = i + 1
    '''
    Think the exmaple of (()( or )()) to understand why it needs 2 paths
    '''
    buf = 0
    s = len(src) - 1       
    for i in xrange(len(src)-1, -1, -1):
        if src[i] == ')':
            buf += 1
        else:
            buf -= 1
            if buf == 0:
                res = max(res, s - i + 1)
            elif buf < 0:
                buf = 0
                s = i - 1                 
    return res
       
def main():
    repeat = 5
    for i in xrange(repeat):
        sent = randParentheses(10)
        print sent, longestValidParentheses(sent)
     
if __name__ == "__main__":
    main()
