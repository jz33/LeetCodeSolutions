#include <iostream>
#include <vector>
#include <algorithm>
/*
Insert Interval
https://oj.leetcode.com/problems/insert-interval/
*/
#define DEBUG 0
#define NOT_FOUND -2

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
typedef std::vector<Interval> List;

void dump(List& input)
{
    for(List::iterator i = input.begin();i!=input.end();i++)
    {
        std::cout<<"("<<i->start<<","<<i->end<<") ";
    }
    printf("\n");
}
List insert(List& input, Interval tag)
{
    // right most interval that includes tag.start (include boundary)
    auto lo = std::lower_bound(input.begin(), input.end(), tag, [](const Interval& lt, const Interval& rt){
        return lt.end < rt.start;
    });

    // right first interval that excludes tag.end
    auto up = std::upper_bound(input.begin(), input.end(), tag, [](const Interval& lt, const Interval& rt){
        return lt.end < rt.start;
    });
    if (lo == up) 
        input.insert(lo, tag);
    else 
    {
        --up;
        tag.start = std::min(tag.start, lo->start);
        tag.end = std::max(tag.end, up->end);
        input.erase(lo, up+1);
        input.insert(lo, tag);
    }
    return input;
}
/*
[1,2],[3,5],[6,7],[8,10],[12,16] : [4,9] 
=> [1,2],[3,10],[12,16]
*/
void test02(void){
    List input;
    input.push_back(make_pair(1,2));
    input.push_back(make_pair(3,5));
    input.push_back(make_pair(6,7));
    input.push_back(make_pair(8,10));
    input.push_back(make_pair(12,16));
    Interval tag = make_pair(5,8);
    
    dump(input);
    insert(input, tag);
    dump(input);
}
int main(int argc, char** argv)
{
    test02();
    return 0;
}
