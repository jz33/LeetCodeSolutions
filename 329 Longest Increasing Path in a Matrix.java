/*
329. Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
*/
class Solution {
    public int longestIncreasingPath(int[][] mat) {
        int rowCount = mat.length;
        if (rowCount == 0) {
            return 0;
        }
        int colCount = mat[0].length;
        if (colCount == 0) {
            return 0;
        }
        
        // A matrix records longest path visited on (i,j)
        // visited[i][j] == 0 means not visitet yet
        int[][] visited = new int[rowCount][colCount]; 
        int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};

        for (int i = 0;i < rowCount;i++) {
            for (int j = 0;j < colCount;j++) {
                if (visited[i][j] == 0) {
                    Queue<Integer[]> queue = new LinkedList<Integer[]>();
                    queue.add(new Integer[]{i,j});
                    int depth = 1;
                    while (queue.size() > 0) {
                        depth++;
                        int size = queue.size();
                        for (int k = 0;k < size;k++) {
                            Integer[] from = queue.poll();
                            int i1 = from[0];
                            int j1 = from[1];
                            for (int[] inc : directions) {
                                int i2 = i1 + inc[0];
                                if (i2 > -1 && i2 < rowCount) {
                                    int j2 = j1 + inc[1];
                                    if (j2 > -1 && j2 < colCount) {
                                        if (mat[i2][j2] > mat[i1][j1] && depth > visited[i2][j2]) {
                                            visited[i2][j2] = depth;
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
        
        int maxDepth = 1;
        for (int i = 0;i < rowCount;i++) {
            for (int j = 0;j < colCount;j++) {
                maxDepth = Math.max(maxDepth, visited[i][j]);
            }
        }
        return maxDepth;
    }
}
