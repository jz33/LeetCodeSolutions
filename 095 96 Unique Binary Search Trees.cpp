#include <iostream>
/*
95 Unique Binary Search Trees
https://oj.leetcode.com/problems/unique-binary-search-trees/
96 Unique Binary Search Trees II
https://oj.leetcode.com/problems/unique-binary-search-trees-ii/

96:
Tree can be constructed using recursion, 
then by level order traverse, 
it will convert to OJ's notation
*/
/*
95
http://yucoding.blogspot.com/2013/04/leetcode-question-114-unique-binary.html

The uniqueness number is actually Catalan number
PI((n+k)/k), 2<=k<=n
=(n+2)*(n+3)*...*(n+n)/(2*3*...*n)
= factorial(2*n)/factorial(n+1)/factorial(n)
*/
int uniqueness(int n){
    int up,dn,i;
	if(n == 0 || n == 1){return 1;}
    
    up = 1;
	for(i=n+2;i<=n*2;i++) up *= i;
    dn = 1;
	for(i=2;i<=n;i++) dn *= i;
	return up/dn;
}

int main(){
    std::cout<<uniqueness(3)<<"\n";
    return 0; 
}