'''
913. Cat and Mouse
https://leetcode.com/problems/cat-and-mouse/

A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.
For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in 3 ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated (ie. the players are in the same position as a previous turn,
and it is the same player's turn to move), the game is a draw.
Given a graph, and assuming both players play optimally, return 1 if the game is won by Mouse,
2 if the game is won by Cat, and 0 if the game is a draw.

Example 1:

Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Explanation:
4---3---1
|   |
2---5
 \ /
  0

Note:

3 <= graph.length <= 50
It is guaranteed that graph[1] is non-empty.
It is guaranteed that graph[2] contains a non-zero element. 
'''
from collections import deque, Counter

DRAW, MOUSE, CAT = 0, 1, 2

class Solution:
    def getParents(self, graph, m, c, t):
        '''
        get parent states of (m, c, t)
        '''
        if t == MOUSE:
            return [(m, p, 3-t) for p in graph[c] if p != 0]
        elif t == CAT:
            return [(p, c, 3-t) for p in graph[m] if p != 0]

    def catMouseGame(self, graph):
        '''
        Let (m,c,t) be the state of the game. m is the mouse location,
        c is cat location, t is 1 means it's mouse's turn, 
        t is 2 means it's cat' turn.
        Then the algorithm is to mark all the states to 3 colors.
        '''
        # childrenCount[s] : the number of children state of this state
        childrenCount = {}
        for m in range(len(graph)):
            for c in range(len(graph)):
                # mouse can move to anywhere
                childrenCount[m,c,MOUSE] = len(graph[m]) 
                # cat cannot move to 0
                childrenCount[m,c,CAT] = len(graph[c]) if 0 not in graph[c] else len(graph[c]) - 1

        # Mark colors of initial states.
        # Default color is DRAW
        colors = Counter() # {[m,c,t] : color}
        
        # mouse at node 0, mouse wins
        for i in range(len(graph)):
            colors[0, i, MOUSE] = MOUSE
            colors[0, i, CAT] = MOUSE 

        # mouse and cat at same node other that 0, cat wins
        for i in range(1, len(graph)):
            colors[i, i, MOUSE] = CAT
            colors[i, i, CAT] = CAT

        # starting nodes are already determined states
        queue = deque(colors.keys()) 

        # Iterate, mark colors
        while queue:
            m, c, t = queue.popleft()
            color = colors[m, c, t]

            for pm, pc, pt in self.getParents(graph, m, c, t):
                if colors[pm, pc, pt] == DRAW:
                    
                    # If parent node is mouse to move and current node is mouse win, or
                    # parent node is cat to move and current node is cat win, parent's is a win
                    if pt == color:
                        colors[pm, pc, pt] = color
                        queue.append((pm, pc, pt))

                    # Otherwise, if parent's all children cannot determine its color,
                    # its color, it is lost, which is to mark its color as opposite of turn
                    else:
                        childrenCount[pm, pc, pt] -= 1
                        if childrenCount[pm, pc, pt] == 0:
                            colors[pm, pc, pt] = 3 - pt
                            queue.append((pm, pc, pt))

        # Mouse starts at 1, cat starts at 2, mouse moves first
        return colors[1, 2, 1]
