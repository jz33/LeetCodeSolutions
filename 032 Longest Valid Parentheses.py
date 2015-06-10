import random
'''
32 Longest Valid Parentheses
https://oj.leetcode.com/problems/longest-valid-parentheses/

O(n)
'''
# generate a random Parentheses string with size n
def randParentheses(n):
    return ''.join(random.choice('('+')') for _ in range(n))
 
def longestValidParentheses(sent):
    if len(sent) < 2:
        return 0
    '''
    Notations for 'buf' :
    '0' : currently paired
    >0  : num of '(' - num of ')'
    '''
    buf = 0
    max_len = 0
    start = 0
    for i in xrange(0, len(sent)):
        if sent[i] == '(':
            buf += 1
        else:
            buf -= 1
            if buf == 0:
                max_len = max(max_len, i - start + 1)
            elif buf < 0:
                start = i + 1
                buf = 0

    end = len(sent) - 1
    buf = 0
    for i in xrange(len(sent)-1, -1,-1):
        if sent[i] == ')':
            buf += 1
        else:
            buf -= 1
            if buf == 0:
                max_len = max(max_len, end - i + 1)
            elif buf < 0:
                end = i - 1
                buf = 0
    return max_len
       
def main():
    repeat = 5
    for i in range(0,repeat):
        sent = randParentheses(10)
        print sent, longestValidParentheses(sent)
     
if __name__ == "__main__":
    main()
