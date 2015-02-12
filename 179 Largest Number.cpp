#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
/*
179 Largest Number
https://oj.leetcode.com/problems/largest-number/
*/
std::string largestNumber(std::vector<int> &num) {
    std::stable_sort(num.begin(),num.end(),[](const int& oa, const int& ob) -> bool{
		int a = oa, b = ob;
        int da = 10,db = 10;
        while(da<a) da *= 10;
        while(db<b) db *= 10;
        da /= 10;
        db /= 10;
        while(da > 0 && db > 0){
            int ra = a / da;
            int rb = b / db;
            if(ra<rb){
                return true;
            } else if (ra>rb){
                return false;
            }
            a = a % da;
            b = b % db;
            da /= 10;
            db /= 10;
        }
        if(da > 0 || db > 0){
            int ra = oa % 10;
            int rb = ob % 10;
            return ra < rb;
        }
        return false;
    });
	std::string ret;
	char buffer [32];
	for(auto i = num.rbegin();i!=num.rend();i++){
		sprintf(buffer, "%d", *i);
		ret += std::string(buffer);
	}
	return ret;
}

// tester
int main(int argc, char** argv){
    int arr[] = {3, 30, 34, 992, 99, 2223, 222};
    int len = sizeof(arr)/sizeof(int);
	std::vector<int> num(len);

	std::copy(arr,arr+len,num.begin());
    std::cout<<largestNumber(num)<<"\n";
    return 0;
}