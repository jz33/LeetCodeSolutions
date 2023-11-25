/*
1861. Rotating the Box
https://leetcode.com/problems/rotating-the-box/

You are given an m x n matrix of characters box representing a side-view of a box.
Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity.
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box.
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Example 1:

Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
         
Example 2:

Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
         
Example 3:

Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 
Constraints:
  m == box.length
  n == box[i].length
  1 <= m, n <= 500
  box[i][j] is either '#', '*', or '.'.
*/
function rotateTheBox(box: string[][]): string[][] {
    // For each row, iterate from right, try to move stones to right empty spots.
    const rowCount = box.length;
    const colCount = box[0].length;
    for (let ri = 0; ri < rowCount; ri++) {
        let sw = colCount - 1; // index to write the stones
        for (let ci = colCount - 1; ci > -1; ci--) {
            const value = box[ri][ci];
            if (value === '*') {
                // Meet obstacle, fill empties.
                // This part is similar to 283. Move Zeroes
                while (sw > ci) {
                    box[ri][sw] = '.';
                    sw--;
                }
                sw = ci - 1;
            } else if (value === '#') {
                // Put stones
                box[ri][sw] = '#';
                sw--;
            }
        }
        while (sw > -1) {
            box[ri][sw] = '.';
            sw--;
        }
    }
    // Then transpose the matrix closewise 90 degrees
    const resultMatrix: string[][] = new Array(colCount);
    for (let ci = 0; ci < colCount; ci++) {
        resultMatrix[ci] = new Array(rowCount);
    }
    for (let ri = 0; ri < rowCount; ri++) {
        for (let ci = 0; ci < colCount; ci++) {
            resultMatrix[ci][rowCount - ri - 1] = box[ri][ci];
        }
    }
    return resultMatrix;
}
