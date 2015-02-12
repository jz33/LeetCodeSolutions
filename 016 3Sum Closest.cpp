#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
/*
16 3Sum Closest
https://oj.leetcode.com/problems/3sum-closest/
*/
int threeSumClosest(std::vector<int>& num, int target){
    if(num.size() == 0) return -1;
	std::size_t j,k;
    std::stable_sort(num.begin(),num.end());
    
    int diff = INT_MAX, sum = INT_MIN;
    int newDiff, newSum, e1;
    std::size_t len = num.size();
    for(std::size_t i = 0;i!=len;i++){
        e1 = num[i];
        j = i+1;
        k = len - 1;
        for(;j < k;j++,k--){
			newSum = e1+num[j]+num[k];
            newDiff = target - newSum;
            if(newDiff == 0) return newSum;
            if(newDiff >0 && newDiff < diff){
                diff = newDiff;
				sum = newSum;
            } else if (newDiff <0 && -newDiff < diff){
                diff = -newDiff;
				sum = newSum;
            }
            while((j+1)!= k && num[j] == num[j+1]) j++;
            while((k-1)!= j && num[k] == num[k-1]) k--;
        }
        while((i+1)!= len && num[i+1] == e1) i++;
    }
    return sum;
}               
// tester
int main(int argc, char** argv){
    int arr[] = {-1,2,1,-4};
    int len = sizeof(arr)/sizeof(int);
    const int target = 1;
	std::vector<int> num(len);

	std::copy(arr,arr+len,num.begin());
    std::cout<<threeSumClosest(num,target)<<"\n";
    return 0;
}