#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
/*
56 Merge Intervals
https://oj.leetcode.com/problems/merge-intervals/
*/
typedef std::pair<int,int> Interval;

bool compareIntevals(Interval i,Interval j)
{
    if(i.first != j.first) return i.first < j.first;
    else return i.second < j.second;
}
void dump(std::vector<Interval>& input)
{
    for(std::vector<Interval>::iterator i = input.begin();i!=input.end();i++)
    {
        std::cout<<"("<<i->first<<","<<i->second<<") ";
    }
    printf("\n");
}
std::vector<Interval> mergeIntevals(std::vector<Interval> input)
{
    std::stable_sort(input.begin(),input.end(),compareIntevals);
    std::vector<Interval> ret;
    std::vector<Interval>::iterator prev = input.begin();
    for(std::vector<Interval>::iterator i = input.begin()+1;i!=input.end();i++)
    {
        if(prev->second < i->first){
            ret.push_back(*prev);
            prev = i;
        } else if(prev->second <= i->second){
            prev->second = i->second;
        }
    }
    ret.push_back(*prev);
    return ret;
}
    
int main(int argc, char** argv)
{
    std::vector<Interval> input;
    input.push_back(std::make_pair(1,3));
    input.push_back(std::make_pair(2,6));
    input.push_back(std::make_pair(8,10));
    input.push_back(std::make_pair(15,18));
    
    std::vector<Interval> out = mergeIntevals(input);
    
    dump(input);
    dump(out);
    return 0;
}