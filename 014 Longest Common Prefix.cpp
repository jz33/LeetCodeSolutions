#include <iostream>
#include <string>
#include <vector>
/*
14 Longest Common Prefix
https://oj.leetcode.com/problems/longest-common-prefix/
*/
std::string longestCommonPrefix(std::vector<std::string> &strs){
    if(strs.size()<1) return "";
    if(strs.size()<2) return strs[0];
    std::string p = strs[0];
    for(std::vector<std::string>::iterator i = strs.begin()+1;i!=strs.end();i++){
        std::string& t = *i;
		std::size_t j = 0;
        for(;j<p.size() && j<t.size();j++)
            if(p[j] != t[j])
                break;
        if(j<p.size()) p = p.substr(0,j);
    }
    return p;
}

int main(){
    std::vector<std::string> strs;
    strs.push_back("ABCD");
    strs.push_back("ABC");
    strs.push_back("AB");
    std::cout<<longestCommonPrefix(strs)<<"\n";
    return 0;  
}