#include <stdio.h>
/*
Pow(x,n)
https://oj.leetcode.com/problems/powx-n/
http://www.programcreek.com/2012/12/leetcode-powx-n/

A divide-conquer approach,
very impractical
*/
double myPow(double x, int n) {
    double ret = 1.0;
    unsigned long long p;
    if (n < 0) {
        p = -n;
        x = 1 / x;
    } else {
        p = n;
    }
    while (p) {
        if (p & 1)
            ret *= x;
        x *= x;
        p >>= 1;
    }
    return ret;
}

int main()
{
    return 0;
}
