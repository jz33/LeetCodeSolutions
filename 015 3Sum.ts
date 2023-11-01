/*
15. 3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
*/
function twoSum(nums: number[], target: number): [number, number][] {
    const result: [number, number][] = [];
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const leftVal = nums[left];
        const rightVal = nums[right];
        const total = leftVal + rightVal;
        if (total === target) {
            result.push([leftVal, rightVal]);
        }
        if (total <= target) {
            left++;
            while (left < right && nums[left] == leftVal) {
                left++;
            }
        }
        if (total >= target) {
            right--;
            while (left < right && nums[right] == rightVal) {
                right--;
            }
        }
    }
    return result;
}

function threeSum(nums: number[]): [number, number, number][] {
    let result: [number, number, number][] = [];

    // NOT nums.sort(),
    // because for negative numbers it will be wrong
    nums.sort((x, y) => x - y);

    let start = 0;
    while (start < nums.length - 2) {
        const startVal = nums[start];
        const twoSumResult = twoSum(nums.slice(start + 1), 0 - startVal);
        result = result.concat(
            twoSumResult.map((twoSum) => [startVal].concat(twoSum)) as [
                number,
                number,
                number,
            ][]
        );
        start++;
        while (start < nums.length - 2 && nums[start] == startVal) {
            start++;
        }
    }

    return result;
}
