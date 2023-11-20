/*
2422. Merge Operations to Turn Array Into a Palindrome
https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

You are given an array nums consisting of positive integers.

You can perform the following operation on the array any number of times:

    Choose any two adjacent elements and replace them with their sum.
        For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].

Return the minimum number of operations needed to turn the array into a palindrome.

Example 1:

Input: nums = [4,3,2,1,2,3,1]
Output: 2
Explanation: We can turn the array into a palindrome in 2 operations as follows:
- Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,3,3,1].
- Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,4].
The array [4,3,2,3,4] is a palindrome.
It can be shown that 2 is the minimum number of operations needed.

Example 2:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We do the operation 3 times in any position, we obtain the array [10] at the end which is a palindrome.

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 106
    
*/
function minimumOperations(nums: number[]): number {
    let operations = 0;
    let left = 0;
    let right = nums.length - 1;
    let leftSum = nums[left];
    let rightSum = nums[right];
    while (left < right) {
        if (leftSum < rightSum) {
            left++;
            leftSum += nums[left];
            operations++;
        } else if (leftSum > rightSum) {
            right--;
            rightSum += nums[right];
            operations++;
        } else {
            left++;
            leftSum = nums[left];
            right--;
            rightSum = nums[right];
        }
    }
    return operations;
};
