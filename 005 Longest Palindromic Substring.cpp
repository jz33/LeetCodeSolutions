#include <iostream>
#include <sstream>
#include <vector>
/*
05 Longest Palindromic Substring.c
https://oj.leetcode.com/problems/longest-palindromic-substring/
*/
/*
O(n^2)
http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html
*/
void longestPalindromicSubstring(const char* in){
    int rs = 0,maxLen = 1; // result
    int i,l,r,n = strlen(in);
    
    for(i=1;i<n-1;i++){
        l = i, r = i;
        while(l >= 0 && r < n && in[l] == in[r]) {
            l--;
            r++;
        }
        if(r-l-1 > maxLen){
            rs = l+1;
            maxLen = r-l-1; 
        }
        l = i, r = i+1;
        while(l >= 0 && r < n && in[l] == in[r]) {
            l--;
            r++;
        }
        if(r-l-1 > maxLen){
            rs = l+1;
            maxLen = r-l-1; 
        }
    }

    // print result
    printf("%u,%u\n",rs,maxLen);
    for(i=0;i<maxLen;i++) printf("%c",in[i+rs]);
    printf("\n");
}

/*
Manacher’s Algorithmm O(n)
http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
This method can also used for listing all palidromic substrings
*/
#define MIN(a,b) (a)<(b)?(a):(b)

std::string preProcess(std::string s)
{
    if(s.size() == 0) return "^$";
    std::string ret = "^";
    for(size_t i = 0;i < s.size();i++)
        ret += "#" + s.substr(i, 1);
    ret += "#$";
    return ret;
}
void manacher(std::string& s)
{
    std::string T = preProcess(s);
    size_t size = T.size();
    std::vector<int> P(size,0);
    int C = 0, R = 0;
    
    for(size_t i = 1;i < size-1;i++)
    {
        int i_mirror = 2*C-i; // equals to i' = C - (i-C)
        P[i] = (R > i) ? MIN(R-i, P[i_mirror]) : 0;

        // Attempt to expand palindrome centered at i
        while (T[i + 1 + P[i]] == T[i - 1 - P[i]])
            P[i]++;

        // If palindrome centered at i expand past R,
        // adjust center based on expanded palindrome.
        if (i + P[i] > R)
        {
            C = i;
            R = i + P[i];
        }
    }

    // Find the maximum element in P.
    int maxLen = 0;
    int centerIndex = 0;
    for(size_t i = 1;i < size-1;i++)
    {
        if (P[i] > maxLen)
        {
            maxLen = P[i];
            centerIndex = i;
        }
    }
    std::cout<< s.substr((centerIndex - 1 - maxLen)/2, maxLen)<<"\n";
}
int main(){
    std::string in = "abmcdefggfedcba";
    std::cout<<in<<"\n";
    longestPalindromicSubstring(in.c_str());
    manacher(in);
    return 0;  
}
