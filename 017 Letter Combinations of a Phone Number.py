'''
Letter Combinations of a Phone Number 
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Time and Space Complexity: 3^6 * 4^2
'''
class FixedArray:
    def __init__(self, size: int):
        self.buf = [None] * size
        self.i = 0

    def add(self, v: object):
        self.buf[self.i] = v
        self.i += 1
    
    def pop(self):
        self.buf[self.i] = None
        self.i -= 1
        
    def toString(self, size: int) -> str:
        return ''.join(self.buf[:size])

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pool = []
        if len(digits) == 0: return pool
        
        def digitToCharList(i: str) -> List[str]:
            if i == '2':
                return ['a','b','c']
            elif i == '3':
                return ['d','e','f']
            elif i == '4':
                return ['g','h','i']
            elif i == '5':
                return ['j','k','l']
            elif i == '6':
                return ['m','n','o']
            elif i == '7':
                return ['p','q','r','s']
            elif i == '8':
                return ['t','u','v']
            elif i == '9':
                return ['w','x','y','z']
  
        def recursive(buf: FixedArray, di: int):
            if di == len(digits):
                pool.append(buf.toString(len(digits)))
                return
            
            for c in digitToCharList(digits[di]):
                buf.add(c)
                recursive(buf, di+1)
                buf.pop()
        
        # Give 1 more char room
        buffer = FixedArray(len(digits)+1)
        recursive(buffer, 0)
        
        return pool
