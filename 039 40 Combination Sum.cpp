#include <iostream>
#include <vector>
#include <algorithm>
/*
Combination Sum I
https://leetcode.com/problems/combination-sum/
Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

http://bangbingsyb.blogspot.com/2014/11/leetcode-combination-sum-i-ii.html
*/
void dumpVec(std::vector<int>& in){
    for(std::vector<int>::iterator i = in.begin();i!=in.end();i++)
        std::cout<<*i<<" ";
    printf("\n");
}
/*
Has duplicates
*/
void findCombSum(std::vector<int>& input, std::vector<int>& sofar, int start, int tag)
{
    if(tag == 0)
        dumpVec(sofar);
    else if(tag > 0)
    {
        for(int i = start;i<input.size();i++)
        {
            if(i>start && input[i] == input[i-1]) 
                continue;
            if(input[i] <= tag)
            {
                sofar.push_back(input[i]);
                findCombSum(input, sofar, i,tag - input[i]);
                sofar.pop_back();
            }
        }
    }
}
void combinationSum(std::vector<int>& input, const int tag)
{
    std::stable_sort(input.begin(),input.end());
	std::vector<int> sofar;
    findCombSum(input,sofar,0,tag);
}
/*
Without duplicates
*/
void findCombSum2(std::vector<int>& input, std::vector<int>& sofar, int start, int tag)
{
    if(tag == 0)
        dumpVec(sofar);
    else if(tag > 0)
    {
        for(int i = start;i<input.size();i++)
        {
            if(i>start && input[i] == input[i-1]) 
                continue;
            if(input[i] <= tag)
            {
                sofar.push_back(input[i]);
                findCombSum2(input, sofar, i+1,tag - input[i]);
                sofar.pop_back();
            }
        }
    }
}
void combinationSum2(std::vector<int>& input, const int tag)
{
    std::stable_sort(input.begin(),input.end());
	std::vector<int> sofar;
    findCombSum2(input,sofar,0,tag);
}
// test Combination Sum
void test1(){
    int arr[] = {2,3,6,7};
    std::vector<int> input(arr,arr+sizeof(arr)/sizeof(int));
    combinationSum(input,7);
	printf("\n");
}
// test Combination Sum II
void test2(){
    int arr[] = {10,1,2,2,4,7,6,1,5};
    std::vector<int> input(arr,arr+sizeof(arr)/sizeof(int));
    combinationSum2(input,8);
	printf("\n");
}
int main(int argc, char** argv){   
    test1();
    test2();
    return 0;
}
