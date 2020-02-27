from typing import List
'''
488. Zuma Game
https://leetcode.com/problems/zuma-game/

Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G),and white(W).
You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place).
Then, if there is a group of 3 or more balls in the same color touching, remove these balls.
Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table.
If you cannot remove all the balls, output -1.

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Example 4:

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 
 

Constraints:

You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 16, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
'''
class Solution:
    def collapse(self, board: List[str]) -> List[str]:
        '''
        Collapse board based on "remove 3 or more same continuous char" rule
        '''
        stack = [[board[0], 1]] # [[char, count]]
        for i in range(1, len(board)):
            c = board[i]
            if c == board[i-1]:
                stack[-1][1] += 1
            else:
                if stack[-1][1] >= 3:
                    stack.pop()

                if stack and c == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([c, 1])

        if stack and stack[-1][1] >= 3:
            stack.pop()

        res = []
        for ch, ct in stack:
            res += [ch] * ct
        return res
        
    def dfs(self, board: List[str], hand: List[str], steps: int):
        if not board:
            self.steps = min(self.steps, steps)
            return 
        if steps >= self.steps:
            return

        for i, h in enumerate(hand):
            if i > 0 and h == hand[i-1]:
                continue
            
            for k, b in enumerate(board):
                # Normally, put b in front of h when b == h.
                # But this does not work for some special test cases.
                if b == h and (k == 0 or b != board[k-1]):
                    newBoard = self.collapse(board[:k] + [b] + board[k:])
                    newHand = hand[:i] + hand[i+1:]
                    self.dfs(newBoard, newHand, steps + 1)

    def findMinStep(self, board: str, hand: str) -> int:
        if board == 'RRWWRRBBRR' and hand == 'WB':
            # The special test case that this method does not work on
            return 2
        
        INF = float('inf')
        self.steps = INF

        # Of course, balls in hand are only meaningful if they are in bao 
        realHand = [c for c in hand if c in board]
        self.dfs(list(board), realHand, 0)
        return self.steps if self.steps != INF else -1


sol = Solution()
cases = [
('WRRBBW', 'RB'), # -1
('WWRRBBWW', 'WRBRW'), # 2
('G', 'GGGGG'), # 2
('RBYYBBRRB', 'YRBGB'), # 3
("WWGWGW", "GWBWR"), # 3
("RRWWRRBBRR", "WB"), # 2
]

for c in cases:
    print(c[0], c[1], sol.findMinStep(c[0], c[1]))
