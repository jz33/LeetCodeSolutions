#include <stdio.h>
#include <stdlib.h>
/*
Count Primes
https://leetcode.com/problems/count-primes/

Regular Eratosthenes method
*/
int eratosthenes(int x){
    int i,j;
    char* bc = (char*)calloc(x+1,sizeof(char)); // 0 means prime
    int counter = 0;
    
    bc[0] = 1;
    bc[1] = 1;
    for(i = 2;i<=x;i++)
        if(bc[i]==0){
            counter++;
            for(j = i*i;j<=x;j += i)
                bc[j]=1;
        }
    free(bc);
    return counter;
}
int main()
{
    // 100 -> 25
    printf("%d\n",eratosthenes(100));
    return 0;
}
