'''
65. Valid Number
https://leetcode.com/problems/valid-number

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
'''
'''
DFA:
State # can only stay or increase
   --- S0 --------
  |     |         |
  |    +,-       dot
  |     |         |
  dg   S1 - dot - S2     S5 - +,- - S6
  |     |         |     /  \       /
  |    dg         dg  exp  dg    dg
  |     |         |  /       \  /
   --- S3 - dot - S4          S7
      /  \       /  \        /  \
      -dg-       -dg-        -dg-
      
      S3 -- exp -- S5
   
Final state should be in 3, 4, 7
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        state = 0;
        s = s.strip() # strip spaces
        for c in s:
            if c == '+' or c == '-':
                if state == 0: state = 1
                elif state == 5: state = 6
                else: return False
                
            elif c == '.':
                if state == 0 or state == 1: state = 2
                elif state == 3: state = 4
                else: return False
                
            elif c == 'e':
                if state == 3 or state == 4: state = 5
                else: return False
                
            elif ord('0') <= ord(c) <= ord('9'):
                if state == 0 or state == 1 or state == 3: state = 3
                elif state == 2 or state == 4: state = 4
                elif state == 5 or state == 6 or state == 7: state = 7
                else: return False
                
            else:
                return False
    
        return (state == 3 or state == 4 or state == 7)
