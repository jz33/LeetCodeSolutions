/*
172 Factorial Trailing Zeros
https://oj.leetcode.com/problems/factorial-trailing-zeroes/
*/
int trailingZeroes(int n)
{
    int count = 0;
    while(n /= 5) count += n;
    return count;
}
