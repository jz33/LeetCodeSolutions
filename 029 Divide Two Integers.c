#include <stdio.h>
#include <limits.h>
/*
Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
*/
typedef long long LL;

int add(int x,int y){
    int a,b;
    do{
        a=x & y;
        b=x ^ y;
        x=a << 1;
        y=b;
    } while(a);
    return b;
}

int negate(int x){
    return add(~x,1);
}

int sub(int x,int y){
    return add(x,negate(y));
}

int mul(int x, int y){
    int m=1, z =0;
    if(x < 0){
        x = negate(x);
        y = negate(y);
    }
 
    while(x >= m && y){
        if(x & m) z=add(y,z);
        y <<= 1; 
        m <<= 1;
    }
    return z;
}

int divide(int dividend, int divisor){
    long long re,up,lo,mul,quo;
    if (!divisor || (dividend == INT_MIN && divisor == -1))
        return INT_MAX;
        
    up = (LL)dividend;
    up = up < 0 ? -up : up;
    lo = (LL)divisor;
    lo = lo < 0 ? -lo  : lo;
    re = 0;
    
    while (up >= lo){ 
        mul = lo;
        quo = 1;
        while ((mul << 1) < up){
            mul <<= 1;
            quo <<= 1;
        }
        up -= mul;
        re += quo;
    }
    return (dividend < 0) ^ (divisor < 0) ? (int)(-re) : (int)re; 
}
