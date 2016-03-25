import java.util.LinkedList;
import java.util.Queue;
/*
Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
*/
public int longestIncreasingPath(int[][] mat) {
    int R = mat.length;
    if(R == 0) return 0;
    int C = mat[0].length;
    if(C == 0) return 0;
    int[][] ref = new int[R][C];
    
    int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
    int maxDepth = 1;
    
    for(int i = 0;i<R;i++){
        for(int j = 0;j<C;j++){
            if(ref[i][j] == 0){
                Queue<Integer[]> queue = new LinkedList<Integer[]>();
                queue.add(new Integer[]{i,j});
                int depth = 1;
                while(queue.size() > 0){
                    depth++;
                    int size = queue.size();
                    for(int k = 0;k<size;k++){
                        Integer[] from = queue.poll();
                        int i1 = from[0];
                        int j1 = from[1];
                        for(int d=0;d<4;d++){
                            int i2 = i1 + directions[d][0];
                            if(i2 > -1 && i2 < R){
                                int j2 = j1 + directions[d][1];
                                if(j2 > -1 && j2 < C){
                                    if(mat[i2][j2] > mat[i1][j1] && depth > ref[i2][j2]){
                                        ref[i2][j2] = depth;
                                        maxDepth = Math.max(maxDepth,depth);
                                        queue.add(new Integer[]{i2,j2});
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return maxDepth;
}
