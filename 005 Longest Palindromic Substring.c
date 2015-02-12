#include <stdio.h>
#include <string.h>
/*
05 Longest Palindromic Substring.c
https://oj.leetcode.com/problems/longest-palindromic-substring/
http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html
*/
/*
O(n^2)
just print result
*/
void longestPalindromicSubstring(char* in){
    size_t rs = 0,maxLen = 1; // result
    size_t i,l,r,n = strlen(in);
    
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
}

int main(){
    char* in = "abmcdefggfedcba";puts(in);
    longestPalindromicSubstring(in);
    return 0;  
}