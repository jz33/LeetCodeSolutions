#include <stdio.h>
#include <stdint.h>
/*
Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Hamming Weight
http://en.wikipedia.org/wiki/Hamming_weight
*/
const uint64_t m1  = 0x5555555555555555;
const uint64_t m2  = 0x3333333333333333;
const uint64_t m4  = 0x0f0f0f0f0f0f0f0f;
const uint64_t m8  = 0x00ff00ff00ff00ff;
const uint64_t m16 = 0x0000ffff0000ffff;
const uint64_t m32 = 0x00000000ffffffff;
const uint64_t h01 = 0x0101010101010101;
 
const uint32_t s1  = 0x55555555; //01010101010101010101010101010101
const uint32_t s2  = 0x33333333; //00110011001100110011001100110011
const uint32_t s4  = 0x0f0f0f0f; //00001111000011110000111100001111
const uint32_t s8  = 0x00ff00ff; //00000000111111110000000011111111
const uint32_t s16 = 0x0000ffff; //00000000000000001111111111111111
 
#define COMB32(b,x) x = (x & s##b ) + ((x >> b) & s##b );
uint32_t popcount32(uint32_t x)
{
    COMB32(1,x)
    COMB32(2,x)
    COMB32(4,x)
    COMB32(8,x)
    COMB32(16,x)
    return x;
}
 
//This is a naive implementation, shown for comparison,
//and to help in understanding the better functions.
//It uses 24 arithmetic operations (shift, add, and).
#define COMB64(b,x) x = (x & m##b ) + ((x >> b) & m##b );
uint64_t popcount64(uint64_t x)
{
    COMB64(1,x)
    COMB64(2,x)
    COMB64(4,x)
    COMB64(8,x)
    COMB64(16,x)
    COMB64(32,x)
    return x;
}
 
//This uses fewer arithmetic operations than any other known
//implementation on machines with slow multiplication.
//It uses 17 arithmetic operations.
uint64_t popcount64_2(uint64_t x)
{
    x -= (x >> 1) & m1;             //put count of each 2 bits into those 2 bits
    x = (x & m2) + ((x >> 2) & m2); //put count of each 4 bits into those 4 bits
    x = (x + (x >> 4)) & m4;        //put count of each 8 bits into those 8 bits
    x += x >>  8;  //put count of each 16 bits into their lowest 8 bits
    x += x >> 16;  //put count of each 32 bits into their lowest 8 bits
    x += x >> 32;  //put count of each 64 bits into their lowest 8 bits
    return x & 0x7f;
}
 
//This uses fewer arithmetic operations than any other known
//implementation on machines with fast multiplication.
//It uses 12 arithmetic operations, one of which is a multiply.
uint64_t popcount64_3(uint64_t x)
{
    x -= (x >> 1) & m1;             //put count of each 2 bits into those 2 bits
    COMB64(2,x)//put count of each 4 bits into those 4 bits
    x = (x + (x >> 4)) & m4;        //put count of each 8 bits into those 8 bits
    return (x * h01)>>56;  //returns left 8 bits of x + (x<<8) + (x<<16) + (x<<24) + ...
}
 
//This is better when most bits in x are 0
//It uses 3 arithmetic operations and one comparison/branch per "1" bit in x.
uint64_t popcount64_4(uint64_t x)
{
    uint64_t count;
    for (count=0; x; count++)
        x &= x-1;
    return count;
}
 
int main(int argc, char* argv[])
{
    uint32_t x = 8;
	printf("%u\n",popcount32(x));
    return 0;
}
