/*
Pow(x,n)
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
*/
double myPow(double x, int n)
{
    double answer = 1;
    double base = x;
    long long exponent = n;
    
    if (exponent < 0)
    {
        exponent = -exponent;
        base = 1 / base;
    }
        
    while (exponent != 0)
    {
        /*
        Let i be the iteration count, then
        base is the product component needed on exponent[i]
        */
        if (exponent & 1)
        {
            answer *= base;
        }
        
        exponent >>= 1;
        base *= base;
    }
    
    return answer;
}
