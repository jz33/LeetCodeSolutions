/*
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:
    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104
*/
function threeSumClosest(nums: number[], target: number): number {
    // NOT nums.sort(),
    // because for negative numbers it will be wrong
    nums.sort((x, y) => x - y);

    let start = 0;
    let closestResult: number | undefined = undefined;
    while (start < nums.length - 2) {
        const startVal = nums[start];
        let left = start + 1;
        let right = nums.length - 1;
        while (left < right) {
            const leftVal = nums[left];
            const rightVal = nums[right];
            const total = startVal + leftVal + rightVal;
            if (total === target) {
                return total;
            }

            if (
                closestResult === undefined ||
                Math.abs(total - target) < Math.abs(closestResult - target)
            ) {
                closestResult = total;
            }

            if (total < target) {
                left++;
                while (left < right && nums[left] == leftVal) {
                    left++;
                }
            }
            if (total > target) {
                right--;
                while (left < right && nums[right] == rightVal) {
                    right--;
                }
            }
        }
        start++;
        while (start < nums.length - 2 && nums[start] == startVal) {
            start++;
        }
    }
    return closestResult!;
}
