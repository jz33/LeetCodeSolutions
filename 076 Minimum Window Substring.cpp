#include <iostream>
#include <string>
#include <limits.h>
/*
76 Minimum Window Substring
https://oj.leetcode.com/problems/minimum-window-substring/
*/
typedef std::string STR;
typedef std::size_t INT;

STR minWin(STR src, STR tag){
    INT i,j;
    INT mask[256] = {0}; 
    INT found[256] = {0};
    INT minLen = INT_MAX;
    INT winlen = 0;
    INT count = 0;
    STR win = "-1";
    
    for(i =0;i<tag.size();i++) mask[tag[i]]++;
    i = 0;
    j = 0;
    for(;i<src.size();i++){
        if(mask[src[i]] > 0){
            found[src[i]]++;
            if(found[src[i]] <= mask[src[i]]) count++;
            
            //If found a candidate, shrink
            if(count == tag.size()){
                for(;mask[src[j]]==0 || found[src[j]] > mask[src[j]];j++)
                    if(found[src[j]] > mask[src[j]]) found[src[j]]--;
                
                //Update min win
                winlen = i-j+1;
                if(minLen > winlen){
                    minLen = winlen;
                    win = src.substr(j,winlen);
                }
            }
        }
    }
    return win;
}
    
int main(int argc, char** argv)
{
    STR S = "ADOBECODEBANC";
    STR T = "ABC";
    std::cout<<minWin(S,T)<<"\n";
    return 0;
}