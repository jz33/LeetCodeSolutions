#include <stdio.h>
#include <stdlib.h>

int isPowerOfTwo(int n) {
    if(n <= 0) return 0;
    n--;
    while(n)
    {
        if((n & 1) == 0) return 0;
        n >>= 1;
    }
    return 1;
}

int main(int argc, char* argv[])
{
    int x;
    if(argc > 1)
    {
        x = (int)strtol(argv[1],0,10);
        printf("%d\n",isPowerOfTwo(x));
    }
    return 0;
}
