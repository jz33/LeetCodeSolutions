#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;
/*
Word Ladder
https://leetcode.com/problems/word-ladder/

Input sample:
hit
cog
hot dot dog lot log
   hit => start
    |
   hot => entries   \
  /   \
dot    lot           tree                       
|       |
dog    log => exits /
  \   /
   cog => ended
*/
#define DEBUG 0

typedef std::unordered_set<string> SET;

size_t WIDTH = 0;

template <typename T>
void dump(T& x)
{
    for(auto i = x.begin();i!=x.end();i++)
        cout<<*i<<" ";
    cout<<"\n";
}

int ladderLength(string s, string e, SET& dict)
{
    SET start,ended,newRow;
    start.insert(s);
    ended.insert(e);
    
    WIDTH = s.size();
    int length = 1;
    
    while(start.size() != 0 || ended.size() != 0)
    {
        /* 
        make sure start.size() <= ended.size()
        */
        if(start.size() > ended.size())
        {
            start.swap(ended);
        }
        if(DEBUG)
        {
            cout<<"before:\n";
            dump(start);
            dump(ended);
        }
        length += 1;
        
        // iterate through smaller set
        newRow.clear();
        for(auto i = start.begin();i != start.end();i++)
        {
            /*
            Notice the iteration strategy.
            Instead of iterating dictionary to find "linked",
            iterate through this string of its WIDTH and
            26 alphabets.
            */
            string tag = *i;
            for(size_t j = 0;j<WIDTH;j++)
            {
                char reserved = tag[j];
                for(int k = 0;k<26;k++)
                {
                    tag[j] = 'a' + k;
                    auto found = ended.find(tag);
                    if(found != ended.end())
                        return length;
                    found = dict.find(tag);
                    if(found != dict.end())
                    {
                        newRow.insert(tag);
                        dict.erase(found);
                    }
                }
                tag[j] = reserved;
            }
        }
        /*
        nothing new found
        */
        if(newRow.size() == 0) return 0;
        else start.swap(newRow);
        
        if(DEBUG)
        {
            cout<<"after: \n";
            dump(dict);
            dump(start);
            dump(ended);
        }
    }
    return length;
}

int main()
{
    // string s = "hit";
//     string e = "cog";
//     std::string input[] = {"hot","dot", "dog", "lot", "log"};
    
    string s = "hot";
    string e = "dog";
    std::string input[] = {"hot","dog"};
    
    SET dict;
    for(size_t i=0;i<sizeof(input)/sizeof(std::string);i++)
    {
        dict.insert(input[i]);
    }
    cout<<ladderLength(s,e,dict)<<"\n";
    return 0;
}
