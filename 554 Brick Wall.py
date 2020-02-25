'''
554. Brick Wall
https://leetcode.com/problems/brick-wall/

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks.
The bricks have the same height but different width.
You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing
the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed.
You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall,
in which case the line will obviously cross no bricks.

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2
'''
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ctr = collections.Counter() # {crevice position : crevice count}
        for row in wall:
            prefix = 0
            # End of row will not count
            for i in range(len(row)-1):
                prefix += row[i]
                ctr[prefix] += 1         
        return len(wall) - (ctr.most_common(1)[0][1] if ctr else 0)
