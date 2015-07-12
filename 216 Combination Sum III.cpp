#include <iostream>
#include <vector>
/*
Combination Sum III
https://leetcode.com/problems/combination-sum-iii/
*/
typedef std::vector<std::vector<int> > MAT;

MAT pool;
int target_size;

void dumpVec(std::vector<int>& in){
    for(std::vector<int>::iterator i = in.begin();i!=in.end();i++)
        std::cout<<*i<<" ";
    printf("\n");
}

void recursive(std::vector<int>& input, std::vector<int>& sofar, int start, int tag)
{
    if(sofar.size() <= target_size)
    {
        if(tag == 0)
        {
            if(sofar.size() == target_size) pool.push_back(sofar);
        }
        else if(tag > 0)
        {
            for(int i = start;i<input.size();i++)
            {
                if(i>start && input[i] == input[i-1]) 
                    continue;
                if(input[i] <= tag)
                {
                    sofar.push_back(input[i]);
                    recursive(input,sofar,i+1,tag - input[i]);
                    sofar.pop_back();
                }
            }
        }
    }
}
MAT combinationSum(int k, int n)
{
    pool.clear();
    
    int arr[] = {1,2,3,4,5,6,7,8,9};
    std::vector<int> input(arr,arr+sizeof(arr)/sizeof(int));
    std::vector<int> sofar;
    
    target_size = k;
    recursive(input,sofar,0,n);
    
    return pool;
}
void test(void)
{
    int k = 3;
    int n = 9;
    combinationSum(k,n);
    
    for(auto i = pool.begin();i!=pool.end();i++)
        dumpVec(*i);
}
int main()
{   
    test();
    return 0;
}
