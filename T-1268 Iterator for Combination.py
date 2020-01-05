'''
1286. Iterator for Combination
https://leetcode.com/problems/iterator-for-combination/

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and
a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
'''
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.pool = []
        self.pos = 0
        
        if combinationLength == len(characters):
            self.pool.append(characters)
        else:
            self.backtrack(characters, combinationLength, 0, [])
            
        
    def backtrack(self, characters: str, combinationLength: int, i: int, sofar: List[str]):
        if len(sofar) == combinationLength:
            self.pool.append(''.join(sofar))
        else:
            for j in range(i, len(characters)):
                sofar.append(characters[j])
                self.backtrack(characters, combinationLength, j+1, sofar)
                sofar.pop()


    def next(self) -> str:
        r = self.pool[self.pos]
        self.pos += 1
        return r
    

    def hasNext(self) -> bool:
        return self.pos < len(self.pool)
