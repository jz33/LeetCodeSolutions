#include <stdio.h>
/*
136 Single Number
https://oj.leetcode.com/problems/single-number/
137 Single Number II
https://oj.leetcode.com/problems/single-number-ii/
*/

// 136
int singleNumber(int* arr, int n)
{
    int res = arr[0];
    int i;
    for(i=1;i<n;i++) res ^= arr[i];
    return res;
}
// 137
//http://www.acmerblog.com/leetcode-single-number-ii-5394.html
int singleNumber3(int A[], int n) {
    int ones = 0, twos = 0, threes = 0, i=0;
    for(i = 0; i < n; i++)
    {
        twos |= ones & A[i];
        ones ^= A[i];
        threes = ones & twos;
        ones &= ~threes;
        twos &= ~threes;
    }
    return ones;
}

int main(int argc, char** argv)
{
    int arr[] = {1,2,3,1,3};
    printf("%d\n",singleNumber(arr,sizeof(arr)/sizeof(int)));
    
    int ar2[] = {1,2,3,1,3,1,3};
    printf("%d\n",singleNumber3(ar2,sizeof(ar2)/sizeof(int)));

    return 0;
}