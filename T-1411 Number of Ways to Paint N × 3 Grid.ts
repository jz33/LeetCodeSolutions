/*
1411. Number of Ways to Paint N × 3 Grid
https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours:
Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54

Example 3:

Input: n = 3
Output: 246

Example 4:

Input: n = 7
Output: 106494

Example 5:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000
*/
/**
 * Consider n == 1 case:
 * Total 12 combinations, 6 combs have 3 colors, 2 combs have 2 colors
 * Adding new level, discussing 2 / 3 colors cases separately
 * 
 * 3 colors + 3 colors, example:
 * r y g: y g r, g r y # *2
 * 
 * 3 colors + 2 colors:
 * r y g: g r y, y r g # *2
 * 
 * 2 colors + 3 colors:
 * r y r: g r y, y r g # *2
 * 
 * 2 colors + 2 colors:
 * r y r: g r g, y g y, y r y # *3
 * 
 * Therefore, at n == 2, there are:
 * 2 colors combs = 6 * 2 + 6 * 3 = 30
 * 3 colors combs = 6 * 2 + 6 * 2 = 24
 * Total 54
 * This is Constate State Dynamic Programming
 */
function numOfWays(n: number): number {
    const mod: number = 10**9 + 7
    let c2: number = 6
    let c3: number = 6

    for (let i = 1; i < n; ++i) {
        let newC2 = c2 * 3 + c3 * 2
        let newC3 = c2 * 2 + c3 * 2
        c2 = newC2 % mod
        c3 = newC3 % mod
    }

    return (c2 + c3) % mod
}
