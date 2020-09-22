/*
1498. Number of Subsequences That Satisfy the Given Sum Condition
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

Given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that
the sum of the minimum and maximum element on it is less or equal than target.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Example 4:

Input: nums = [5,2,4,1,7,6,8], target = 16
Output: 127
Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6
*/
/**
 * The result is the same when array is sorted
 * @param nums 
 * @param target 
 */
function numSubseq(nums: number[], target: number): number {
    let res: number = 0
    const mod = 10 ** 9 + 7

    nums.sort(function (a: number, b: number): number {
        return a - b
    })

    // The pow of 2 needs to be pre-computed because it can be too big
    const pows: number[] = []
    pows[0] = 1
    for (let i = 1; i < nums.length; ++i) {
        pows[i] = pows[i - 1] * 2 % mod;
    }

    let left = 0
    let right = nums.length - 1
    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            // For an array of length n, its subsequence count is 2 ^ n
            res = (res + pows[right - left]) % mod
            left++
        }
        else {
            right--
        }
    }
    return res
}
