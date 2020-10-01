/*
6. ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
*/
function convert(s: string, numRows: number): string {
    if (numRows <= 1 || s.length === 0) {
        return s; 
    }

    let res: string[] = []
    for (let r = 0; r < numRows; ++r) {
        // For each row, compute the "stride", aka,
        // the distance of current char to next char
        let strides: number[] = []
        if (r === 0 || r === numRows - 1) {
            strides = [(numRows - 1) * 2]
        }
        else {
            strides = [(numRows - 1 - r) * 2, r * 2]
        }

        let c: number = r
        let si = 0 // index of strides
        while (c < s.length) {
            res.push(s[c])
            c += strides[si]
            si = (si + 1) % strides.length 
        }
    }
    return res.join('')
}
