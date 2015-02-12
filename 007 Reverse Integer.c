#include <stdio.h>
/*
07 Reverse Integer
https://oj.leetcode.com/problems/reverse-integer/
*/
/*
int can be minus !
*/
int reverseInt(int x){
    int sign = x < 0? -1:1;
    int lt = 10;
    int y = 0;
    
    x = x*sign;
    while(lt<x) lt *= 10;
    lt /= 10;
    while(x>0){
        y += lt*(x%10);
        lt /= 10;
        x /= 10;
    }
    return sign*y;
}

int main(){
    int x = -123456789;
    printf("%d\n",reverseInt(x));
    return 0;  
}