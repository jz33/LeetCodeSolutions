#include <stdio.h>
#include <limits.h>
/*
Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
https://leetcode.com/discuss/11358/simple-o-log-n-2-c-solution
O(log(upper) ^ 2)
*/
void printBinary(int x)
{
    char bin[32];
    int i;
    char *p = bin,*st = bin;
    
    for(i = 2147483648; i > 0; i >>= 1) *p++ = (x & i) ? '1': '0';
    while(st != p) printf("%c",*st++);
    printf("\n");
}

long long labs(int x)
{
    return x >= 0 ? x : -x;
}

int add(int x,int y){
    int a,b;
    do{
        a=x&y;
        b=x^y;
        x=a<<1;
        y=b;
    }while(a);
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
    if(x<0){
        x=negate(x);
        y=negate(y);
    }
 
    while(x>=m && y) {
        if(x & m) z=add(y,z);
        y <<= 1; m<<= 1;
    }
    return z;
}

int div(int upper, int lower)
{
    int sign,re;
    long long up,lo,t,m;
    if (lower == 0 || (upper == INT_MIN && lower == -1))
        return INT_MAX;
        
    sign = (upper < 0) ^ (lower < 0) ? -1 : 1;
    up = labs(upper);
    lo = labs(lower);
    re = 0;
    
    // move bits of upper, so log(upper) loops
    while (up >= lo)
    { 
        t = lo;
        m = 1;
        while ((t << 1) < up)
        {
            t <<= 1;
            m <<= 1;
        }
        up -= t;
        re += m;
    }
    return sign == 1 ? re : -re; 
}

int main(){
    int x = -24;
    int y = 10;
    printf("add: %d\n",add(x,y));
    printf("sub: %d\n",sub(x,y));
    printf("mul: %d\n",mul(x,y));
    printf("div: %d\n",div(x,y));
    return 0;
}
