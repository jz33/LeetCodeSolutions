/*
660. Remove 9
https://leetcode.com/problems/remove-9/

Share
Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...

So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...

Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.

Example 1:

Input: 9
Output: 10
Hint: n will not exceed 9 x 10^8.
*/
// n is decimal, transfer to 9-based number
int newInteger(int n)
{
    int res = 0;
    long base = 1;
        
    while (n > 0)
    {
        res += n % 9 * base;
        n = (int)(n / 9);
        base *= 10L;
    }
    
    return res;
}
