/*
694. Number of Distinct Islands
https://leetcode.com/problems/number-of-distinct-islands/

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if
one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

Example 1:

Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:

Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.

*/
function dfsPath(
    grid: number[][],
    visited: boolean[][],
    path: number[],
    root: number[]
) {
    const rowCount = grid.length;
    const colCount = grid[0].length;
    const [fx, fy] = root;

    const togos = [
        [fx + 1, fy],
        [fx - 1, fy],
        [fx, fy + 1],
        [fx, fy - 1],
    ];
    for (let ti = 0; ti < 4; ti++) {
        const tx = togos[ti][0];
        const ty = togos[ti][1];
        if (
            tx >= 0 &&
            tx < rowCount &&
            ty >= 0 &&
            ty < colCount &&
            grid[tx][ty] === 1 &&
            !visited[tx][ty]
        ) {
            visited[tx][ty] = true;
            path.push(ti);
            dfsPath(grid, visited, path, togos[ti]);
        }
    }
    path.push(4);
}

/**
 * Similar to 200. Number of Islands
 * Also record the visit path for dedup
 * It has to use DFS, somehow BFS paths cannot dedup for some cases
 */
function numDistinctIslands(grid: number[][]): number {
    const rowCount = grid.length;
    const colCount = grid[0].length;

    const visited: boolean[][] = [];
    for (let r = 0; r < rowCount; r++) {
        visited.push(new Array(colCount).fill(false));
    }

    const uniquePaths = new Set<string>();
    for (let r = 0; r < rowCount; r++) {
        for (let c = 0; c < colCount; c++) {
            if (grid[r][c] === 1 && !visited[r][c]) {
                visited[r][c] = true;
                // Record the path from [r ,c].
                // '0' means down, '1' means up, '2' means right, '3' means left, '4' is delimiter
                const path: number[] = [];
                dfsPath(grid, visited, path, [r, c]);
                uniquePaths.add(path.join(''));
            }
        }
    }
    return uniquePaths.size;
}
