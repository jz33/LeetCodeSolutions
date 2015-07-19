#include<iostream>
#include<sstream>
#include<vector>
#include<unordered_map>
using namespace std;
/*
Letter Combinations of a Phone Number 
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

If needs to check if output string is in dictionary,
use Trie to pre-process dictionary, then add TrieNode 
to each recursive step
*/
vector<string> pool;
string input;
std::unordered_map<char,std::string> dial;

void recursive(string& buf, size_t i)
{
    if(i == input.size())
    {
        pool.push_back(buf);
    }
    else
    {
        char c = input[i];
        if(dial.find(c) == dial.end())
            return;
            
        string cands = dial[c];
        for(auto j = cands.begin();j!=cands.end();j++)
        {
            string next(buf);
            next += *j;
            recursive(next,i+1);
        }
    }
}

void initRef()
{
    dial.clear();
    for(int i = 2;i<=6;i++)
    {
        std::string val(1,(i - 2)*3 + 'a');
        val += (i - 2)*3 + 1 + 'a';
        val += (i - 2)*3 + 2 + 'a';
        dial[i +'0'] = val;
    }
    dial['7'] = "pqrs";
    dial['8'] = "tuv";
    dial['9'] = "wxyz";
    /*
    for(auto i = dial.begin();i!=dial.end();i++)
        std::cout<<i->first<<" "<<i->second<<"\n";
    */
}

vector<string> letterCombinations(string digits)
{
     pool.clear();
     if(digits.size() == 0) return pool;
     
     input = digits;
     
     string buf = "";
     size_t i = 0;
     
     initRef();
     
     recursive(buf,i);
     return pool;   
}

int main()
{
    string digits = "7";
    letterCombinations(digits);
    
    for(auto i = pool.begin();i!=pool.end();i++)
        std::cout<<*i<<"\n";
    return 0;
}
