/*
15. 3Sum
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/
type MovePredict = (it: number) => boolean

function threeSum(nums: number[]): number[][] {
    let result: number[][] = []
    
    // NOT: nums.sort(),
    // because for negative numbers it will be wrong
    nums.sort((x, y) => x - y);
    const size: number = nums.length
    
    function moveLeft(it: number, pred: MovePredict): number{
        it--;
        while (pred(it)) {
            it--;
        }
        return it;
    }
    
    function moveRight(it: number, pred: MovePredict): number{
        it++;
        while (pred(it)) {
            it++;
        }
        return it;
    }
    
    let i: number = 0;
    while (i < size - 2) {
        let a = nums[i]
        let j = i + 1
        let k = size - 1
        while (j < k) {
            let b = nums[j]
            let c = nums[k]
            let s = a + b + c
            if (s === 0) {
                result.push([a, b, c])
                
                j = moveRight(j, (v) => {return v < k && nums[v] === b})
                k = moveLeft(k, (v) => {return v > j && nums[v] === c})
            }
            else if (s < 0) {
                j = moveRight(j, (v) => {return v < k && nums[v] === b})
            }
            else {
                k = moveLeft(k, (v) => {return v > j && nums[v] === c})
            }
        }
        i = moveRight(i, (v) => {return v < size && nums[v] === a})
    }
    
    return result
};
