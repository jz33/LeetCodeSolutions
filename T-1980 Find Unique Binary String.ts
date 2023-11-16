/*
1980. Find Unique Binary String
https://leetcode.com/problems/sentence-screen-fitting/

Given an array of strings nums containing n unique binary strings each of length n,
return a binary string of length n that does not appear in nums.
If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:
    n == nums.length
    1 <= n <= 16
    nums[i].length == n
    nums[i] is either '0' or '1'.
    All the strings of nums are unique.
*/
function findDifferentBinaryString(nums: string[]): string {
    const width = nums.length;
    const upperBound = 1 << width;
    const visitedNums = new Set<number>(
        nums.map(num => parseInt(num, 2))
    );
    let start = 0;
    while (start < upperBound) {
        if (!visitedNums.has(start)) {
            return start.toString(2).padStart(width, '0');
        }
        start++;
    }
    return '';
};
