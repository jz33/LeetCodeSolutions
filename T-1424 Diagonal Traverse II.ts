/*
1424. Diagonal Traverse II
https://leetcode.com/problems/diagonal-traverse-ii/

Given a list of lists of integers, nums,
return all elements of nums in diagonal order as shown in the below images.
 
Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]

Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]
*/
function findDiagonalOrder(nums: number[][]): number[] {
    let res: number[] = []
    const rowCount: number = nums.length

    let colCount: number = 0
    for (let row of nums) {
        colCount = Math.max(colCount, row.length)
    }

    // How many bottom-left to top-right strips?
    const stripCount = rowCount + colCount - 1

    for (let s = 0; s < stripCount; ++s) {
        // Use 'i' as row index, then column index j = s - i
        // Clearyly, it must satisfy i > -1 && j < colCount, which got
        // i > Math.max(s - colCount, -1)
        for (let i = Math.min(s, rowCount - 1); i > Math.max(s - colCount, -1); --i) {
            let v: number | undefined = nums[i][s-i]
            if (v !== undefined) {
                res.push(v)
            }
        }
    }
    return res
}
