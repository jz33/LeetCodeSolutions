#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
/*
218 The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/
http://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/
*/
#define MAKE std::make_pair

typedef long long LONG; // in case of int32_t overflow
typedef std::vector<LONG> VEC;
typedef std::vector<VEC> MAT;
typedef std::pair<LONG,LONG> PAIR;
typedef std::map<LONG,LONG> MAP;

void dump(std::vector<PAIR>& res)
{
    for(auto i = res.begin();i!=res.end();i++)
    {
        std::cout<<"["<<i->first<<","<<i->second<<"],";
    }
    std::cout<<"\n";
}

void dumpMat(MAT& res)
{
    for(auto i = res.begin();i!=res.end();i++)
    {
        std::cout<<"[";
        for(auto j = i->begin();j!=i->end();j++)
        {
            std::cout<<*j<<" ";
        }
        std::cout<<"]\n";
    }
}

void parse(MAT& in, std::vector<PAIR>& out)
{
    LONG li,ri,hi;
    
    out.clear();
    for(auto i = in.begin();i!=in.end();i++)
    {
        li = (*i)[0];
        ri = (*i)[1];
        hi = (*i)[2];
        out.push_back(MAKE(li,hi));
        out.push_back(MAKE(ri,-hi));//minus indicates end of building
    }

    std::stable_sort(out.begin(),out.end(),[](const PAIR& x, const PAIR& y)
    {
        return x.first < y.first;
    });
}

std::vector<PAIR> getSkyline(MAT& buildings)
{
    std::vector<PAIR> res;
    std::vector<PAIR> vec;
    parse(buildings,vec);
    
    if(vec.size() == 0)
        return res;
        
    if(vec.size() == 2)
    {
        res.push_back(MAKE(vec.begin()->first,vec.begin()->second));
    }
    else
    {
        MAP heights; // previous heights, possible duplicates
        LONG prev; // previous max height
        
        heights.insert(MAKE(0,0));
        prev = 0;
        
        for(auto i = vec.begin();i!=vec.end()-1;i++)
        {
            LONG p = i->first;
            LONG h = i->second;
            
            if(h>0){
                heights[h]++;
            }
            else{
                heights[-h]--;
                if(heights[-h] == 0) heights.erase(-h);
            }
            
            // if next building's position is not same as current's
            if((i+1)->first != p)
            {  
                // if $prev has changed
                if(prev != heights.rbegin()->first)
                {
                    res.push_back(MAKE(p,heights.rbegin()->first));
                }
                prev = heights.rbegin()->first; 
            }
        }
    }
    res.push_back(MAKE(vec.rbegin()->first,0));
    return res;
}

void test(void)
{
    MAT buildings;
    LONG arr[] = {0,3,3,1,5,3,2,4,3,3,7,3};
    for(int i =0;i<(sizeof(arr)/sizeof(LONG)/3);i++)
    {
        VEC v(arr+i*3,arr+(i+1)*3);
        buildings.push_back(v);
    }
    std::vector<PAIR> res = getSkyline(buildings);
    dump(res);
}
void test1(void)
{
    MAT buildings;
    LONG arr[] = {1,2,1,2147483646,2147483647,2147483647};
    for(int i =0;i<(sizeof(arr)/sizeof(LONG)/3);i++)
    {
        VEC v(arr+i*3,arr+(i+1)*3);
        buildings.push_back(v);
    }
    dumpMat(buildings);
    
    std::vector<PAIR> res = getSkyline(buildings);
    dump(res);
}
int main()
{
    test();
    return 0;
}
