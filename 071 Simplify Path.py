'''
Simplify Path
https://leetcode.com/problems/simplify-path/
'''
def simplifyPath(input):
    stack = []
    for e in input.split('/'):
        if e == '.' or e == '': continue
        if e == '..' and len(stack) > 0:
            stack.pop()
        elif e != '..':
            stack.append(e)
    return '/' if len(stack) == 0 else '/' + '/'.join(stack)
        
input = "/../"
print simplifyPath(input)
