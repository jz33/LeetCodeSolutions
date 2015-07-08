#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
/*
4Sum
https://leetcode.com/problems/4sum/
O(n^3)
*/
typedef std::vector<int> VEC;
typedef std::vector<VEC> MAT;

MAT fourSum(VEC& nums,int target){
    MAT pool;
    int diff;
    size_t i,j,x,y;
    size_t size = nums.size();
    
    if(size < 4) return pool;
    std::stable_sort(nums.begin(),nums.end());
    
    VEC row(4,-1);
    i = 0;
    while(i < size - 3){
        row[0] = nums[i];
        j = i + 1;
        while(j < size - 2){
            row[1] = nums[j];
            x = j + 1;
            y = size - 1;
            while(x < y){
                row[2] = nums[x];
                row[3] = nums[y];
                diff = row[0]+row[1]+row[2]+row[3] - target;
                if(diff == 0){
                    pool.push_back(row);
                    x += 1;
                    while (x < y && nums[x] == row[2]) x += 1;
                    y -= 1;
                    while (y > x && nums[y] == row[3]) y -= 1;
                }
                else if(diff < 0){   
                    x += 1;
                    while (x < y && nums[x] == row[2]) x += 1;
                }
                else{
                    y -= 1;
                    while (y > x && nums[y] == row[3]) y -= 1;
                }
            }
            j += 1;         
            while(j < size - 2 && nums[j] == row[1]) j += 1;
        }
        i += 1;      
        while(i < size - 3 && nums[i] == row[0]) i += 1;
    }
    return pool;
}

int main(){
    int arr[] = {-3,-2,-1,0,0,1,2,3};
    VEC nums(arr,arr+sizeof(arr)/sizeof(int));
    int target = 0;
    MAT pool = fourSum(nums,target);
    
    return 0;
}
