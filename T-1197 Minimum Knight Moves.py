'''
1197. Minimum Knight Moves
https://leetcode.com/problems/minimum-knight-moves/

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below.
Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
'''
class Solution:
    def nextMoves(self, node):
        x,y = node
        return [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x-1, y+2), (x+1, y-2), (x-1, y-2)]
        
    def minKnightMoves(self, x: int, y: int) -> int:
        '''
        Since the move is symmetric for the 4 quarters,
        only consider top-right quarter (x, y are all positives)
        An example:

        0  3  2  3  2

        3  2  1  2  3
     
        2  1  4  3  2

        3  2  3  2  3

        2  3  2  3  4 
        '''
        target = (abs(x), abs(y))
        if target == (1, 1):
            # (1,1) is special case, because it needs to move out the top-right quarter
            return 2
        
        visited = {(0,0)}
        queue = collections.deque()
        queue.append((0,0))
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return steps
            
                for move in self.nextMoves(node):
                    if move[0] >= 0 and move[1] >= 0 and move not in visited:
                        # Constrain the move inside top-right quarter
                        visited.add(move)
                        queue.append(move)
            steps += 1
            
        return -1
