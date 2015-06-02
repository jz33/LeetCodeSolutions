#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
/*
214 Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome/
*/
/* 
Build KMP table
http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
*/
std::vector<int> buildKMPTable(std::string& ndl)
{
	size_t n_len = ndl.size();
	std::vector<int> T(n_len, 0);
    
	T[0] = -1;
	T[1] = 0;

	int i = 2; // iterate ndl
	int j = 0; // iterate over T
	while (i < n_len)
	{
		if (ndl[i - 1] == ndl[j])
			T[i++] = ++j;
		else if (j>0)
			j = T[j];
		else
			T[i++] = 0;
	}
	return T;
}
std::string shortestPalindrome(std::string& ori)
{
	// get reverse string
	std::string rev = ori;
	std::reverse(rev.begin(), rev.end());

	// add a delimiter in center
	std::string t = ori + "#" + rev;

	// build KMP table
	std::vector<int> T = buildKMPTable(t);

	return rev.substr(0, ori.size() - (*T.rbegin()+1)) + ori;
}
int main()
{
	char* tests[] = { \
		"aacecaaa", \
		"abcd", \
		"aabaa", \
		"abaa", \
		"abbaa", \
		"aabbaa", \
	};
	for (int i = 0; i<sizeof(tests) / sizeof(char*); i++)
	{
		std::string s = tests[i];
		std::cout << s << " : " << shortestPalindrome(s) << "\n";
	}
	return 0;
}
