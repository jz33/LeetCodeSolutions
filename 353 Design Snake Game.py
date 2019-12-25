'''
353. Design Snake Game
https://leetcode.com/problems/design-snake-game/

Design a Snake game that is played on a device with screen size = width x height.
Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food,
its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until
the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
'''
from typing import Tuple

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        
        snake = collections.deque()
        snake.append((0,0)) # last element of deque is head of snake
        self.snake = snake
        
        self.food = collections.deque()
        for f in food:
            self.food.append((f[0], f[1]))

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake[-1]
        inc = self.getDirection(direction)
        nextPos = (head[0] + inc[0], head[1] + inc[1])
        if nextPos[0] < 0 or nextPos[0] == self.height or nextPos[1] < 0 or nextPos[1] == self.width:
            # Hit boundary
            return -1
        
        if self.food and nextPos == self.food[0]:
            self.food.popleft()
        else:
            # Test if snake hits self only after pop tail!
            self.snake.popleft()
            if nextPos in self.snake:
                return -1
            
        self.snake.append(nextPos)
        return len(self.snake) - 1
    
    def getDirection(self, direction: str) -> Tuple[int, int]:
        if direction == 'U':
            return (-1,0)
        elif direction == 'L':
            return (0,-1)
        elif direction == 'R':
            return (0,1)
        elif direction == 'D':
            return (1,0)
