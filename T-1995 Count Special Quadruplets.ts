/*
1995. Count Special Quadruplets
https://leetcode.com/problems/count-special-quadruplets/

Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

    nums[a] + nums[b] + nums[c] == nums[d], and
    a < b < c < d
 

Example 1:

Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

Example 2:

Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].

Example 3:

Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
 

Constraints:

    4 <= nums.length <= 50
    1 <= nums[i] <= 100

*/
/**
 * Separate nums by b. Save all nums[a] + nums[b] for a in [0, b) to map.
 * get all nums[d] - nums[c], for c = b + 1, d in (c, length) for map.
 */
function countQuadruplets(nums: number[]): number {
    const sums = new Map<number, number>();
    let result = 0;
    for (let b = 1; b < nums.length - 2; b++) {
        for (let a = 0; a < b; a++) {
            const sum = nums[a] + nums[b];
            sums.set(sum, (sums.get(sum) ?? 0) + 1);
        }
        const c = b + 1;
        for (let d = c + 1; d < nums.length; d++) {
            const sub = nums[d] - nums[c];
            result += sums.get(sub) ?? 0;
        }
    }
    return result;
}
