'''
489. Robot Room Cleaner
https://leetcode.com/problems/robot-room-cleaner/

You are controlling a robot that is located somewhere in a room.
The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty,
and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room).
The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle,
and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

Note that the initial direction of the robot will be facing up.
You can assume all four edges of the grid are all surrounded by a wall.

Custom testing:

The input is only given to initialize the room and the robot's position internally.
You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.

Example 1:

Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
Output: Robot cleaned all rooms.
Explanation: All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

Example 2:

Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms.

Constraints:
    m == room.length
    n == room[i].length
    1 <= m <= 100
    1 <= n <= 200
    room[i][j] is either 0 or 1.
    0 <= row < m
    0 <= col < n
    room[row][col] == 1
    All the empty cells can be visited from the starting position
'''
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
from typing import Tuple

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
def getNextPosition(direction: int, position: Tuple[int, int]):
    if direction == UP:
        return (position[0]-1, position[1])
    if direction == RIGHT:
        return (position[0], position[1]+1)
    if direction == DOWN:
        return (position[0]+1, position[1])
    if direction == LEFT:
        return (position[0], position[1]-1)           
        
class Solution:
    def cleanRoom(self, robot):
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
                         
        visited = set()
        def backTrack(position: Tuple[int, int], direction: int):
            robot.clean()
            
            for _ in range(4):
                # It can only get next direction from the previous direction,
                # and from Up->Right->Down->Left order, as the robot already has a facing
                nextPosition = getNextPosition(direction, position)
                if nextPosition not in visited and robot.move():
                    visited.add(nextPosition)
                    backTrack(nextPosition, direction)
                    goBack() # backtrack
                
                robot.turnRight()
                direction = (direction + 1) % 4
                
        visited.add((0,0))
        backTrack((0,0), UP)

'''
This real Facebook interview question is similar:
https://leetcode.com/discuss/interview-question/633689/facebook-phonevideo-find-cheese

Given a mouse with 2 APIs in a maze.
Design an algorithm to find a cheese in the maze using only the 2 given APIs shown below.
'''
class Mouse:
	# Moves to one of the directions (left, right, up, down) and returns false if you can't move and true if you can.
	def move(self, direction: int) -> bool:
        pass
        
	# Returns true if there is a cheese in the current cell.
	def hasCheese(self) -> bool:
        pass
        
def getCheese(mouse: 'Mouse'):
    visited = set() # {visited (x, y)}
    cheesePosition = None

    def backTrack(position: Tuple[int, int], fromDirection: int) -> bool:
        '''
        @return: if found cheese or not. This is for early return to avoid go to other branches.
        '''
        nonlocal cheesePosition
        if mouse.hasCheese():
            cheesePosition = position
            return True
        
        for direction in range(4):
            nextPosition = getNextPosition(direction, position)
            if nextPosition not in visited and mouse.move(direction):
                visited.add(nextPosition)
                if backTrack(nextPosition, direction):
                    return True
                
        # Needs to go back, if cannot move further or not find the cheese.
        # The grip shape is unknown, so it is possible to stuck, so it needs to go back
        if fromDirection == UP:
            mouse.move(DOWN)
        elif fromDirection == DOWN:
            mouse.move(UP)
        elif fromDirection == LEFT:
            mouse.move(RIGHT)
        elif fromDirection == RIGHT:
            mouse.move(LEFT)
        return False
                            
    backTrack((0,0), UP)
    return cheesePosition
