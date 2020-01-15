'''
604. Design Compressed String Iterator
https://leetcode.com/problems/design-compressed-string-iterator/

Design and implement a data structure for a compressed string iterator.
It should support the following operations:next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer
representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter;
Otherwise return a white space.

hasNext() - Judge whether there is any letter needs to be uncompressed.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
'''
class StringIterator:

    def __init__(self, compressedString: str):
        ls = []
        num = 0
        char = None
        for c in compressedString:
            if c.isalpha():
                if num > 0 and char is not None:
                    ls.append((char, num))
                char = c
                num = 0
            else:
                num = num * 10 + int(c)
                
        if num > 0 and char is not None:
            ls.append((char, num))
            
        self.ls = ls
        self.i = 0 # iterator through ls
        self.j = 0 # iterator through ls[i]

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        r = self.ls[self.i][0]
        
        self.j += 1
        if self.j == self.ls[self.i][1]:
            self.i += 1
            self.j = 0
        
        return r

    def hasNext(self) -> bool:
        return self.i < len(self.ls)
