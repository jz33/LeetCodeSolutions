/*
470. Implement Rand10() Using Rand7()
https://leetcode.com/problems/implement-rand10-using-rand7/

Given the API rand7() that generates a uniform random integer in the range [1, 7],
write a function rand10() that generates a uniform random integer in the range [1, 10].
You can only call the API rand7(),
and you shouldn't call any other API. Please do not use a language's built-in random API.

Each test case will have one internal argument n,
the number of times that your implemented function rand10() will be called while testing.
Note that this is not an argument passed to rand10().

Example 1:

Input: n = 1
Output: [2]

Example 2:

Input: n = 2
Output: [2,8]

Example 3:

Input: n = 3
Output: [3,8,10]

Constraints:
    1 <= n <= 105

Follow up:
    What is the expected value for the number of calls to rand7() function?
    Could you minimize the number of calls to rand7()?
*/
/**
 * The rand7() API is already defined for you.
 * function rand7(): number {}
 * @return a random integer in the range 1 to 7
 */
/**
 * Rejection Sampling
 */
function rand10(): number {
    let sample = 41;
    while (sample > 40) {
        const col = rand7(); // [1, 7]
        const row = rand7() - 1; // [0, 6]
        sample = col + 7 * row; // [1, 49]
    }
    // Now sample is [1, 40]
    return sample % 10 + 1;
};