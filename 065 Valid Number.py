'''
065 Valid Number
https://leetcode.com/problems/valid-number/
See DFA figure:
dg : digit

   --- S0 
  |     |  \ 
  |    +,-  \ dot
  |     |    \
  dg   S1-dot-S6     S3 - +,- - S5
  |     |     |     /  \       /
  |    dg     dg  exp  dg    dg
  |     |     |  /       \  /
   --- S2-dot-S7          S4
      /  \   /  \        /  \
      -dg-   -dg-        -dg-
      
      S2 -- exp -- S3
'''
ORD_0 = ord('0')
ORD_9 = ord('9')

def isNumber(input):
    state = 0
    input = input.strip()
    for char in input:
        if char == '+' or char == '-':
            if state == 0: state = 1
            elif state == 3: state = 5
            else: return False
        elif char == '.':
            if state == 0: state = 6
            elif state == 1: state = 6
            elif state == 2: state = 7
            else: return False
        elif char == 'e':
            if state == 2: state = 3
            elif state == 7: state = 3
            else: return False
        elif ord(char) >= ORD_0 and ord(char) <= ORD_9:
            if state == 0: state = 2
            elif state == 1: state = 2
            elif state == 2: state = 2
            elif state == 3: state = 4
            elif state == 4: state = 4
            elif state == 5: state = 4
            elif state == 6: state = 7
            elif state == 7: state = 7
            else: return False
        else: return False
    return state == 2 or state == 4 or state == 7
    
print isNumber('.e1')
