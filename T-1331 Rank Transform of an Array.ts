/*
1331. Rank Transform of an Array
https://leetcode.com/problems/rank-transform-of-an-array/

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

    Rank is an integer starting from 1.
    The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    Rank should be as small as possible.

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.

Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]

Constraints:

    0 <= arr.length <= 105
    -109 <= arr[i] <= 109

*/
function arrayRankTransform(arr: number[]): number[] {
    // Build a [(value, original index)] array, sort by values
    const sortedPairs = arr
        .map((value, index) => [value, index])
        .sort((a, b) => a[0] - b[0]);

    const result = new Array(arr.length);
    let rank = 0;
    for (let i = 0; i < sortedPairs.length; i++) {
        const [value, originalIndex] = sortedPairs[i];
        // Only increase the rank when neighbors are different
        if (i === 0 || value !== sortedPairs[i - 1][0]) {
            rank++;
        }
        result[originalIndex] = rank;
    }
    return result;
}
