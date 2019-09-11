/*
778. Swim in Rising Water
https://leetcode.com/problems/swim-in-rising-water/

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
*/
class ElevationPoint implements Comparable<ElevationPoint> {
    
    public int x; // Coordinate x
    public int y; // Coordinate y
    public int h; // height
    
    public ElevationPoint(int x, int y, int h) {
        this.x = x;
        this.y = y;
        this.h = h;
    }
    
    public int compareTo(ElevationPoint that) { 
        return this.h - that.h;
    } 
}

class Solution {

    // A classic 2-D matrix traversal problem using priority queue
    public int swimInWater(int[][] grid) {
        int rowCount = grid.length;
        if (rowCount == 0) {
            return 0;
        }
        
        int colCount = grid[0].length;
        if (colCount == 0) {
            return 0;
        }
        
        java.util.PriorityQueue<ElevationPoint> pq = new java.util.PriorityQueue<ElevationPoint>(rowCount * colCount);
        
        pq.add(new ElevationPoint(0,0,grid[0][0]));
        
        int visited = -1; // Used on grid to mark if the point is visited
        int t = 0;
        while (pq.size() > 0) {
            ElevationPoint top = pq.poll();
            int x = top.x;
            int y = top.y;
            int h = top.h;
            
            grid[x][y] = visited; // mark visited
            
            if (h > t) {
                t = h; // t += h - t
            }
            
            // Reached end?
            if (x == rowCount - 1 && y == colCount - 1) {
                break;
            }
            
            if (x+1 < rowCount && grid[x+1][y] != visited) {
                pq.add(new ElevationPoint(x+1, y, grid[x+1][y]));
            }
            if (x > 0 && grid[x-1][y] != visited) {
                pq.add(new ElevationPoint(x-1, y, grid[x-1][y]));
            }
            if (y+1 < colCount && grid[x][y+1] != visited) {
                pq.add(new ElevationPoint(x, y+1, grid[x][y+1]));
            }
            if (y > 0 && grid[x][y-1] != visited) {
                pq.add(new ElevationPoint(x, y-1, grid[x][y-1]));
            }
        }
        
        return t;        
    }
}
