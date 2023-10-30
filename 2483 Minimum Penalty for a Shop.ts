/*
2483. Minimum Penalty for a Shop
https://leetcode.com/problems/minimum-penalty-for-a-shop/

You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

    if the ith character is 'Y', it means that customers come at the ith hour
    whereas 'N' indicates that no customers come at the ith hour.

If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

    For every hour when the shop is open and no customers come, the penalty increases by 1.
    For every hour when the shop is closed and customers come, the penalty increases by 1.

Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

Example 1:

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.

Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

Constraints:
    1 <= customers.length <= 105
    customers consists only of characters 'Y' and 'N'.
*/
function bestClosingTime(customers: string): number {
    const customerSize = customers.length;

    // At nth hour, to compute the penalty, it needs to know
    // how many 'Y's on [, n], and how many 'Y's on [n+1, ]
    // Build a prefix array where yCounts[i] = # of 'Y's from [, i]
    const yCounts: number[] = new Array(customerSize).fill(0);
    for (let i = 0; i < customerSize; i++) {
        yCounts[i] =
            (i > 0 ? yCounts[i - 1] : 0) + (customers[i] === 'Y' ? 1 : 0);
    }

    // If closing before customer[0], the penalty is the # of 'Y's.
    const totalYs = yCounts[yCounts.length - 1];
    let minPenalty = totalYs;
    let minClosingIndex = -1;
    for (let i = 0; i < customerSize; i++) {
        const leftNs = i + 1 - yCounts[i];
        const rightYs = totalYs - yCounts[i];
        const penalty = leftNs + rightYs;
        if (penalty < minPenalty) {
            minPenalty = penalty;
            minClosingIndex = i;
        }
    }
    return minClosingIndex + 1;
}
