#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <set>
/*
218 The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/

An example:
https://www.codeeval.com/open_challenges/120/
http://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/
*/
typedef std::string Str;
typedef std::pair<int,int> Pair;

#define PARSEINT(p,e,del)\
	while(*p!=del){\
		e = e*10 + *p -'0';\
		p++;\
	}p++;

/*
Parse the input following Codeeval.com format
Here the input format is (Li,Hi,Ri) (Li,Hi,Ri) ... 
*/	
void parse(std::string& in, std::vector<Pair>& out)
{
    std::istringstream iss(in);
    Str unit;
    out.clear();
    
    while(iss>>unit)
    {
        int x=0,y=0,h=0;
        char* p = &unit[1];//*(p-1) == '('
        PARSEINT(p,x,',')
        PARSEINT(p,h,',')
        PARSEINT(p,y,')')
        out.push_back(std::make_pair(x,h));
        out.push_back(std::make_pair(y,-h));//minus indicates end of building
    }

    std::stable_sort(out.begin(),out.end(),[](const Pair& x, const Pair& y)
    {
        return x.first < y.first;
    });
}
void compute(std::vector<Pair>& vec)
{
    if(vec.size()==2)
        std::cout<<vec.begin()->first<<" "<<vec.begin()->second<<" ";
    else
    {
        std::multiset<int> heights; // previous heights
        int prev; // previous max height
        
        heights.insert(0);
        prev = *heights.rbegin();
        
        for(auto i = vec.begin();i!=vec.end()-1;i++)
        {
            int p = i->first;
            int h = i->second;
            
            if(h>0) heights.insert(h);
            else heights.erase(-h);
            
            // if next building's position is not same as current's
            if((i+1)->first != p)
            {  
                // if $prev has changed
                if(prev != *heights.rbegin())
                    std::cout<<p<<" "<<*heights.rbegin()<<" ";
                prev = *heights.rbegin(); 
            }
        }
    }
    std::cout<<vec.rbegin()->first<<" 0\n";
}		
void test_skyline(void)
{
    std::vector<Str> input(10,"");
    input[0] = "(1,11,5)";
    input[1] = "(0,10,3) (1,15,2)";
    input[2] = "(1,2,3) (2,4,6) (4,5,5) (7,3,11) (9,2,14) (13,7,15) (14,3,17)";
    input[3] = "(1,11,5) (2,6,7) (3,13,9) (12,7,16), (14,3,25) (19,18,22) (23,13,29) (24,4,28)";
    
    input[4] = "(0,3,1) (0,2,2) (0,1,3)";
    input[5] = "(0,3,3) (0,2,2) (0,1,1)";
    
    std::vector<Pair> out;
    parse(input[5],out);
    /*
    for(auto i = out.begin();i!=out.end();i++)
        std::cout<<i->first<<" "<<i->second<<"\n";
    */
    compute(out);
}
int main()
{
    test_skyline();
    return 0;
}
