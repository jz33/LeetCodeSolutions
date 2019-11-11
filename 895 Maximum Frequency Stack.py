'''
895 Maximum Frequency Stack
https://leetcode.com/problems/maximum-frequency-stack/

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
'''
from collections import Counter

class FreqStack:
    def __init__(self):
        # The map is to map the value to its count
        self.mapper = Counter()  
        
        # The self.stacks is a stack of stacks
        self.stacks = []

    def push(self, x: int) -> None:
        self.mapper[x] += 1
        count = self.mapper[x]
        if count > len(self.stacks):
            self.stacks.append([x])
        else:
            self.stacks[count-1].append(x)

    def pop(self) -> int:
        if not self.stacks:
            return -1
        
        x = self.stacks[-1].pop()
        self.mapper[x] -= 1
        
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        
        return x
