#include <stdio.h>
/*
89 Gray Code
https://oj.leetcode.com/problems/gray-code/
// http://en.wikipedia.org/wiki/Gray_code
*/
int binaryToGray(int num)
{
    return (num >> 1) ^ num;
}

int main(int argc, char** argv){
    int i,n,bits;

    bits = 3;
    n = 1 << bits;
	
    for(i = 0; i < n; i++){
        printf("%d ", i);
        printf("%d\n", binaryToGray(i));
    }
    return 0;
}