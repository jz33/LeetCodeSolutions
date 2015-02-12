#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
/*
88 Merge Sorted Array
https://oj.leetcode.com/problems/merge-sorted-array/
*/
typedef std::vector<int> VEC;

void dumpVec(VEC& A)
{
    std::size_t i;
    for(i=0;i<A.size();i++) printf("%d ",A[i]);
    printf("\n");
}

int randInt(int leftLimit, int rightLimit)
{
    int div = RAND_MAX/(rightLimit - leftLimit + 1);
    int res = -1;
    do{ 
        res = rand() / div;
    } while (res <= leftLimit || res >= rightLimit);
    return res;
}

VEC randVec(int size,int leftLimit, int rightLimit)
{
    VEC ret(size,0);
    int i;
    for(i=0;i<size;i++) ret[i] = randInt(leftLimit,rightLimit);
    return ret;
}

void merge(VEC& A, VEC& B)
{
    int i = (int)A.size() - 1;
    int j = (int)B.size() - 1;
    int k = i + j + 1;

    A.resize(i+j+2);

    while(i > -1 && j > -1)
        if(A[i] > B[j]) A[k--] = A[i--];
        else A[k--] = B[j--];
    while(j > -1)
        A[k--] = B[j--];
}

int main(int argc, char** argv)
{
    int leftLimit = 0;
    int rightLimit = 32;

    VEC A = randVec(16,leftLimit,rightLimit);
    std::stable_sort(A.begin(),A.end(),[](int i,int j)->bool{
        return i<j;
    });
    dumpVec(A);
    VEC B = randVec(8,leftLimit,rightLimit);
    std::stable_sort(B.begin(),B.end(),[](int i,int j)->bool{
        return i<j;
    });
    dumpVec(B);

    merge(A,B);
    dumpVec(A);
    return 0;
}