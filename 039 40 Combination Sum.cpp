#include <iostream>
#include <vector>
#include <algorithm>
/*
39 Combination Sum
https://oj.leetcode.com/problems/combination-sum/
40 Combination Sum II
https://oj.leetcode.com/problems/combination-sum-ii/

39 is inspired from C++ version of "combinations",
40 is from "combinations without duplicates"
*/
int getSum(std::vector<int>& in){
    int res = 0;
    for(std::vector<int>::iterator i = in.begin();i!=in.end();i++)
        res += *i;
    return res;
}
void dumpVec(std::vector<int>& in){
    for(std::vector<int>::iterator i = in.begin();i!=in.end();i++)
        std::cout<<*i<<" ";
    printf("\n");
}
bool compareInt(int i, int j){
  return (i==j);
}
void combinationSumRec(std::vector<int>& in, std::vector<int>& pattern, const int tag)
{
    int sum = getSum(pattern);
    if(sum==tag){
		dumpVec(pattern);
	} else if (sum < tag){
		for(std::size_t i = 0;i < in.size();i++)
		{
			std::vector<int> newPattern(pattern);
			newPattern.push_back(in[i]);
        
			std::vector<int> newInput(in.size()-i);
			std::copy(in.begin()+i,in.end(),newInput.begin());
        
			combinationSumRec(newInput, newPattern, tag);
		}
	}
}
void combinationSum(std::vector<int> in, const int tag)
{
    std::stable_sort(in.begin(),in.end());
	std::vector<int> pattern;
    combinationSumRec(in, pattern, tag);
}
void combinationSum2Rec(const int tag,std::vector<int>& src,std::vector<int>& cur)
{
    int sum = getSum(cur);
    if(sum == tag){
		dumpVec(cur);
	} else if (sum < tag){
    
        // "prev" is used to eliminate duplicates
        std::vector<int> prev;  
		for(std::size_t i = 0;i < src.size()-1;i++)
		{
			std::vector<int> newCur(cur);
			newCur.push_back(src[i]);
            if(	prev.size() == 0 ||
				!std::equal(newCur.begin(),newCur.end(),prev.begin(),compareInt)){
                prev = newCur;
                std::vector<int> newSrc(src.size()-i-1);
                std::copy(src.begin()+i+1,src.end(),newSrc.begin());
                combinationSum2Rec(tag, newSrc, newCur);
            }
		}
	}
}
void combinationSum2(std::vector<int> src, const int tag)
{
    std::stable_sort(src.begin(),src.end());
	std::vector<int> cur;
    combinationSum2Rec(tag,src,cur);
}
// test Combination Sum
void test1(){
    int arr[4];
    arr[0] = 2;arr[1] = 3;arr[2] = 6;arr[3] = 7;
    std::vector<int> in(arr,arr+sizeof(arr)/sizeof(int));
    combinationSum(in,7);
	printf("\n");
}
// test Combination Sum II
void test2(){
    int arr[7];
    arr[0] =10;arr[1] = 1;arr[2] = 2;arr[3] = 7;
    arr[4] = 6;arr[5] = 1;arr[6] = 5;
    std::vector<int> in(arr,arr+sizeof(arr)/sizeof(int));
    combinationSum2(in,8);
	printf("\n");
}
int main(int argc, char** argv){   
    test1();
    test2();
    return 0;
}