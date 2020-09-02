/*
60. Permutation Sequence
https://leetcode.com/problems/permutation-sequence/

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"
*/
function getPermutation(n: number, k: number): string {
    // 1. Build string array like ['1', '2', '3'...]
    let arr: string[] = []
    for (let i = 1; i < n + 1; ++i) {
        arr.push(i.toString())
    }

    // 2. Get factorial of n
    let fact: number = 1
    for (let i = 2; i < n + 1; ++i) {
        fact *= i 
    }

    // 3. Compute
    k -= 1
    let res: string[] = []
    for (let i = n; i > 0; --i) {
        fact = fact / i
        let r = Math.floor(k / fact)
        k = k % fact
        
        res.push(arr[r])
        arr.splice(r, 1) // Remove arr[r]
    }
        
    return res.join('')
};
