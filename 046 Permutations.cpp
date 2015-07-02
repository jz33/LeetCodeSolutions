#include <iostream>
#include <vector>
#include <algorithm>
/*
Permutations
https://oj.leetcode.com/problems/permutations/
*/
typedef std::vector<int> VEC;

std::vector<VEC> pool;

void swap(int* x, int* y)
{
    int t = *x;
    *x = *y;
    *y = t ;
}
/*
Backtracing
*/
void perms(int* arr, int size, int lv)
{
    int i; 
    for(i = lv;i < size;i++){
        swap(arr+lv, arr+i);
        if(lv + 1 == size)
        {
            VEC v(arr,arr+size);
            pool.push_back(v);
        }
        else perms(arr, size, lv+1);
        swap(arr+lv, arr+i);
    }
}

std::vector<VEC> permute(VEC& in)
{
    pool.clear();
    std::stable_sort(in.begin(),in.end());

    int* arr = &in[0];
    int size = (int)in.size();
    perms(arr,size,0);

    return pool;
}

int main()
{   
    int arr[] = {0,1};
    int size = sizeof(arr)/sizeof(int);
    VEC in(arr,arr+size);
    permute(in);

    return 0;
}
