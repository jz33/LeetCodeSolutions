#include <stdio.h>
/*
Pow(x,n)
https://oj.leetcode.com/problems/powx-n/
http://www.programcreek.com/2012/12/leetcode-powx-n/

A divide-conquer approach,
very inpractical
*/
double _power(double x, int n){
    double v = 1;
	if (n == 0) return v;
 
	v = _power(x, n / 2);
 
	if (n % 2 == 0) {
		return v * v;
	} else {
		return v * v * x;
	}
}
 
double _pow(double x, int n){
	if (n < 0) {
		return 1 / _power(x, -n);
	} else {
		return _power(x, n);
	}
}

int main()
{
    printf("%d\n",_pow(12,12));
    return 0;
}