'''
22 Generate Parentheses
https://oj.leetcode.com/problems/generate-parentheses/
Just print
'''
ctr = 0 #count each output
def generateParenthesesRec(buf,lt,rt):
    global ctr
    if lt == 0 and rt == 0 :
        print buf
        ctr += 1
    elif lt == rt:
        generateParenthesesRec(buf + '(',lt-1,rt)
    elif lt < rt:
        if lt > 0:
            generateParenthesesRec(buf + '(',lt-1,rt)
        generateParenthesesRec(buf + ')',lt,rt-1)
            
def generateParentheses(n):
    generateParenthesesRec('',n,n)

repeat = 6
for i in range(1,repeat):
    ctr = 0
    print("repeat: {0}".format(i))
    generateParentheses(i)
    print("count: {0}\n".format(ctr))
