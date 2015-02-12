#include <stdio.h>
/*
29 Divide Two Integers
https://oj.leetcode.com/problems/divide-two-integers/
http://www.pixelstech.net/article/1344149505-Implementation-of-%2B---*-with-bitwise-operator
*/
// print a decimal int as a 32-bit binary string
void printBinary(int x){
    char bin[32];
    int i;
    char *p = bin,*st = bin;
    
    for(i = 2147483648; i > 0; i >>= 1) *p++ = (x & i) ? '1': '0';
    while(st != p) printf("%c",*st++);
    printf("\n");
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

int div(int x,int y){
    int c=0,sign=0;
 
    if(x<0){
        x=negate(x);
        sign^=1;
    }
    if(y<0){
        y=negate(y);
        sign^=1;
    }
    if(y!=0){
        while(x>=y){
            x=sub(x,y);
            ++c;
        }
    }
    if(sign){
        c=negate(c);
    }
    return c;
}

int main(){
    int x = -24;
    int y = 12;
    printf("add: %d\n",add(x,y));
    printf("sub: %d\n",sub(x,y));
    printf("mul: %d\n",mul(x,y));
    printf("div: %d\n",div(x,y));
    return 0;
}
