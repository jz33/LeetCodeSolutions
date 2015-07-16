#include<iostream>
#include<sstream>
#include<vector>
using namespace std;
/*
Repeated DNA Sequences 
https://leetcode.com/problems/repeated-dna-sequences/
*/
#define SIZE 0x100000
#define SIZE_1 0xFFFFF

/*
How to avoid switch:
'A' - 64 : 1 : 00001 : 001 : 00
'C' - 64 : 3 : 00011 : 011 : 01
'G' - 64 : 7 : 00111 : 111 : 11
'T' - 64 :20 : 10100 : 100 : 10
*/
std::vector<std::string> findRepeatedDnaSequences(std::string src)
{
    size_t i,length;
    char c;
    int hash;
    std::vector<std::string> ret;
    if(src.size() <= 10) return ret;
    
    char table[SIZE] = {0};
    hash = 0;
    length = src.size();
    for(i = 0;i<10;i++)
    {
        c = src[i];
        hash = ((hash << 2) | ((c - 64 & 6) >> 1));
    }
    table[hash] = 1;
    
    for(;i<length;i++)
    {
        c = src[i];
        hash = (((hash << 2) | ((c - 64 & 6) >> 1)) & SIZE_1);
        if(table[hash] == 1)
        {
            ret.push_back(src.substr(i-9,10));
            table[hash] = 2;
        }
        else if(table[hash] == 0)
        {
            table[hash] = 1;
        }
    }
    return ret;
}

int main()
{
    std::string src = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
    std::vector<std::string>  ret = findRepeatedDnaSequences(src);
    for(auto i = ret.begin();i!=ret.end();i++)
        std::cout<<*i<<endl;
    return 0;
}
