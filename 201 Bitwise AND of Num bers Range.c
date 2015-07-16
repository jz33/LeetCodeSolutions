/*
Bitwise AND of Num bers Range
https://leetcode.com/problems/bitwise-and-of-numbers-range/
https://leetcode.com/discuss/43070/three-solution-explanation-loops-recursion-extra-variable
*/
int compute(int l,  int r)
{
    unsigned int x = l ^ r;
    x |= (x >> 1);
    x |= (x >> 2);
    x |= (x >> 4);
    x |= (x >> 8);
    x |= (x >> 16);
    return l & ~x;
}  
