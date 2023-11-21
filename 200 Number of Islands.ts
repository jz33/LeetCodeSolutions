/*
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
*/
function numIslands(grid: string[][]): number {
    const rowCount = grid.length;
    const colCount = grid[0].length;

    const visited: boolean[][] = [];
    for (let r = 0; r < rowCount; r++) {
        visited.push(new Array(colCount).fill(false));
    }

    let islandCount = 0;
    for (let r = 0; r < rowCount; r++) {
        for (let c = 0; c < colCount; c++) {
            if (grid[r][c] === '1' && !visited[r][c]) {
                visited[r][c] = true;
                let row = [[r, c]];
                while (row.length) {
                    const newRow: number[][] = [];
                    for (const [fx, fy] of row) {
                        for (const [tx, ty] of [
                            [fx + 1, fy],
                            [fx - 1, fy],
                            [fx, fy + 1],
                            [fx, fy - 1],
                        ]) {
                            if (
                                tx >= 0 &&
                                tx < rowCount &&
                                ty >= 0 &&
                                ty < colCount &&
                                grid[tx][ty] === '1' &&
                                !visited[tx][ty]
                            ) {
                                visited[tx][ty] = true;
                                newRow.push([tx, ty]);
                            }
                        }
                    }
                    row = newRow;
                }
                islandCount++;
            }
        }
    }
    return islandCount;
}
