'''
752. Open the Lock
https://leetcode.com/problems/open-the-lock/

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around:
for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1
'''
class Solution:
    def getNexts(self, node: int) -> List[int]:
        res = []
        for i in range(4):
            w = 10**i
            d = (node // w) % 10
            cs = [d-1, d+1]
            if d == 0:
                cs = [9, 1]
            elif d == 9:
                cs = [8, 0]
                
            res.append(node - d * w + cs[0] * w)
            res.append(node - d * w + cs[1] * w)
            
        return res
             
    def openLock(self, deadends: List[str], target: str) -> int:
        dest = int(target)
        visited = [False] * 10000
        for d in deadends:
            visited[int(d)] = True
            
        if visited[0] == True:
            # '0000' is in deadends
            return -1
        
        visited[0] = True      
        queue = collections.deque()
        queue.append(0)
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == dest:
                    return steps
                for togo in self.getNexts(node):
                    if visited[togo] is False:
                        visited[togo] = True
                        queue.append(togo)
            steps += 1
        return -1
