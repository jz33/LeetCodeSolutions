#include <stdio.h>
#include <stdint.h>
/*
Reverse Bits
https://leetcode.com/problems/reverse-bits/
*/
// Print
void print_uint32_t(uint32_t x)
{
    uint32_t pow31 = 2147483648;
    uint32_t z;
    
    for(z = pow31; z > 0; z >>= 1)
        printf("%c",(x & z) ? '1': '0');
    printf("\n");
}

// Binary string to binary
uint32_t to_uint32_t(char* in)
{
    uint32_t t = *in++ == '1' ? 1:0;
    while(*in != '\0')
    {
        t <<= 1;
        t ^= *in++ == '1' ? 1:0;
    }
    return t;
}

// Reverse 32 bits unsigned integer
uint32_t reverse(uint32_t x)
{
    int n = 32;
    int i,j,r,l;
    for(i=0;i < (n>>1);i++)
    {
        j = n-i-1;
        r = (x>>i) & 1;
        l = (x>>j) & 1;
        if(r^l) 
            x ^= ((1U << i) | (1U << j));
    }
    return x;
}

int main()
{
    char* x = "111000";
    uint32_t i = to_uint32_t(x);
    
    print_uint32_t(i);
    print_uint32_t(reverse(i));
    
    return 0;
}
