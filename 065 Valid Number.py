'''
65. Valid Number
https://leetcode.com/problems/valid-number

A valid number can be split up into these components (in order):

    A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    One of the following formats:
        One or more digits, followed by a dot '.'.
        One or more digits, followed by a dot '.', followed by one or more digits.
        A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
    One or more digits.

For example, all the following are valid numbers: 
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
while the following are not valid numbers:
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false

Constraints:
    1 <= s.length <= 20
    s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
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
# State names
Initial = 0
Sign = 1
Dot = 2
Int = 3
Decimal = 4
Exp= 5
ExpSign = 6
ExpInt = 7

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        state = Initial
        for c in s:
            if c in ['+', '-']:
                if state == Initial:
                    state = Sign
                elif state == Exp:
                    state = ExpSign
                else:
                    return False
                
            elif c == '.':
                if state in [Initial, Sign]:
                    state = Dot
                elif state == Int:
                    state = Decimal
                else:
                    return False
                
            elif c in ['e', 'E']:
                if state in [Int, Decimal]:
                    state = Exp
                else:
                    return False
                
            elif c.isdigit():
                if state in [Initial, Sign, Int]:
                    state = Int
                elif state in [Dot, Decimal]:
                    state = Decimal
                elif state in [Exp, ExpSign, ExpInt]:
                    state = ExpInt
                else:
                    return False
                
            else:
                return False
    
        return state in [Int, Decimal, ExpInt]
