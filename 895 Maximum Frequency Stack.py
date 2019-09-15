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
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.numberToCount = defaultdict(int) # number : count    
        
        # The stacks is stack of stacks
        # Each stack is a stack of numbers associate with a count,
        # which is index of stacks + 1
        self.stacks = []

    def push(self, key: int) -> None:
        stacks = self.stacks

        c = self.numberToCount[key] + 1
        self.numberToCount[key] = c

        # Push key to stacks[c-1]
        if c > len(stacks):
            stacks.append([key])
        else:
            stacks[c-1].append(key)

    def pop(self) -> int:
        stacks = self.stacks
        
        if len(stacks) == 0:
            return -1
          
        # Pop from last element from last stack
        res = stacks[-1].pop()
        if len(stacks[-1]) == 0:
            stacks.pop()
        
        self.numberToCount[res] -= 1
        return res
