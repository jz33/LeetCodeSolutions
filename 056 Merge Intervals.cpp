#include <iostream>
#include <vector>
#include <algorithm>
/*
Merge Intervals
https://oj.leetcode.com/problems/merge-intervals/
*/
struct Interval {
    int start;
    int end;
};
Interval make_pair(int x,int y)
{
    Interval r;
    r.start = x;
    r.end = y;
    return r;
}
void dump(std::vector<Interval>& input)
{
    for(std::vector<Interval>::iterator i = input.begin();i!=input.end();i++)
    {
        std::cout<<"("<<i->start<<","<<i->end<<") ";
    }
    printf("\n");
}

bool compareIntevals(Interval i,Interval j)
{
    if(i.start != j.start) return i.start < j.start;
    else return i.end < j.end;
}

std::vector<Interval> mergeIntevals(std::vector<Interval>& input)
{
    std::vector<Interval> ret;
    if(input.size() == 0) return ret;
    
    std::stable_sort(input.begin(),input.end(),compareIntevals);
    
    std::vector<Interval>::iterator prev = input.begin();
    for(std::vector<Interval>::iterator i = input.begin()+1;i!=input.end();i++)
    {
        if(prev->end < i->start){
            ret.push_back(*prev);
            prev = i;
        } else if(prev->end <= i->end){
            prev->end = i->end;
        }
    }
    ret.push_back(*prev);
    return ret;
}
    
int main(int argc, char** argv)
{
    std::vector<Interval> input;
    input.push_back(make_pair(1,3));
    input.push_back(make_pair(2,6));
    input.push_back(make_pair(8,10));
    input.push_back(make_pair(15,18));
    
    std::vector<Interval> out = mergeIntevals(input);
    
    dump(input);
    dump(out);
    return 0;
}
