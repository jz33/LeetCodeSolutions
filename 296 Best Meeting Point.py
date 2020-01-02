'''
296. Best Meeting Point
https://leetcode.com/problems/best-meeting-point/

A group of two or more people wants to meet and minimize the total travel distance.
You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
'''
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # 1. Find all people
        # Notice the iteration order, i is before j
        people = [(i,j) for i in range(rowCount) for j in range(colCount) if grid[i][j] == 1]
        if not people:
            return 0
                
        # 2. Get middle row index
        # Notice people coordinates are already sorted by row
        mr = people[len(people) // 2][0]
        
        # 3. Get middle colunm index
        people.sort(key = lambda x : x[1])
        mc = people[len(people) // 2][1]
        
        # 4. Sum
        return sum(abs(i-mr) + abs(j-mc) for i,j in people)
