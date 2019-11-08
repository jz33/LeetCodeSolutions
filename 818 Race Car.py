'''
818. Race Car
https://leetcode.com/problems/race-car/
'''
from collections import deque

class Solution:
    def addQueue(self, position, speed, queue, visited):
        pair = str(position) + "|" + str(speed)
        if pair not in visited:
            # Notice the boundary
            if -(self.target << 1) < position < (self.target << 1) :
                queue.append((position, speed))
                visited.add(pair)

    def racecar(self, target: int) -> int:
        self.target = abs(target)

        queue = deque() # (position, speed)  
        visited = set() # visited position speed pairs
        self.addQueue(0, 1, queue, visited)

        steps = 0
        while queue:
            for _ in range(len(queue)): 
                position, speed = queue.popleft()
                if position == target:
                    return steps

                # Keep going
                self.addQueue(position + speed, (speed << 1), queue, visited)

                # Reverse
                self.addQueue(position, -1 if speed > 0 else 1, queue, visited)

            steps += 1

        return -1
