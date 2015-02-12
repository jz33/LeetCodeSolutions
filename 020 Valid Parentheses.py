'''
20 Valid Parentheses
https://oj.leetcode.com/problems/valid-parentheses/
'''
def validParentheses(arg):
    if len(arg) < 2: return False
    stack = []
    for i in range(0,len(arg)):
        curr = arg[i]
        if curr == '(' or curr == '[' or curr == '{':
            stack.append(curr)
        else:
            if len(stack) == 0 : return False
            prev = stack[len(stack)-1]
            if curr == ')':
                if prev == '(': stack.pop()
                else: return False
            elif curr == ']':
                if prev == '[': stack.pop()
                else: return False
            elif curr == '}':
                if prev == '{': stack.pop()
                else: return False
            else: return False
            
    return True if len(stack) == 0 else False

def main():
    s = r"{[()]}"
    print validParentheses(s)
    s = r"{[(]]}"
    print validParentheses(s)
    s = r"{[("
    print validParentheses(s)
    s = r"a{[()]}"
    print validParentheses(s)
    
if __name__ == "__main__":
    main()
