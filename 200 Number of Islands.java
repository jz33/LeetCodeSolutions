import java.util.*;

class Pair {
    public Pair(int i, int j) {
        this.i = i;
        this.j = j;
    }

    public int i;
    public int j;
}

class Solution {
    private Pair[] Dirs = {new Pair(0, 1), new Pair(0, -1), new Pair(1, 0), new Pair(-1, 0)};
    
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int rowCount = grid.length;
        int colCount = grid[0].length;
        
        boolean[][] visited = new boolean[rowCount][colCount];
        int island = 0;
        
        for (int i = 0; i < rowCount; ++i) {
            for (int j = 0; j < colCount ; ++j) {
                if (grid[i][j] == '1' && visited[i][j] == false) {
                    Queue<Pair> queue = new LinkedList<>();
                    queue.offer(new Pair(i, j));
                    visited[i][j] = true;
                    
                    while (!queue.isEmpty()) {
                        Pair p = queue.poll();                  
                        for (Pair d : Dirs) {
                            int x = p.i + d.i;
                            int y = p.j + d.j;
                            if (x >= 0 && x < rowCount && y >= 0 && y < colCount && grid[x][y] == '1' && visited[x][y] == false) {
                                queue.offer(new Pair(x, y));
                                visited[x][y] = true;
                            }
                        }
                    }
                    
                    island++;
                }
            }
        }
        return island;
    }
}
