import random
'''
32 Longest Valid Parentheses
https://oj.leetcode.com/problems/longest-valid-parentheses/
'''
# generate a random Parentheses string with size n
def randParentheses(n):
    return ''.join(random.choice('('+')') for _ in range(n))
 
def longestValidParentheses(sent):
    '''
    Notations for 'buf' :
    '-1': invalid from here till end of string
    '0' : currently paired
    >0  : num of '(' - num of ')'
    '''
    buf = -1
    lt  = 0
    rt  = -1
     
    for i in range(0,len(sent)-1):
        if sent[i] == ')': continue
         
        buf = 1
        for j in range(i+1,len(sent)):
            if sent[j] == ')':
                buf -= 1
                if buf < 0 : 
                    i = j # speed-up
                    break
            else: buf += 1
                 
            # update result
            if buf == 0:
                if j - i > rt - lt :
                    rt = j
                    lt = i
    print lt, rt
       
def main():
    repeat = 5
    for i in range(0,repeat):
        sent = randParentheses(10)
        print sent
        longestValidParentheses(sent)
     
if __name__ == "__main__":
    main()
