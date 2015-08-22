#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stdint.h>
using namespace std;

void dump(vector<int>& num)
{
    for(auto i = num.begin();i!=num.end();i++)
    {
        cout<<*i<<" ";
    }
    cout<<"\n";
}

string largestNumber(vector<int>& num)
{
    bool allZero = true;
    for(auto i = num.begin();i!=num.end();i++)
    {
        if(*i != 0)
        {
            allZero = false;
            break;
        }
    }
    if(allZero == true) return "0";
    
    std::stable_sort(num.begin(),num.end(),[](const int& a, const int& b) -> bool
    {
        int da = 10,db = 10;
        while(da <= a) da *= 10;
        while(db <= b) db *= 10;
 
        int64_t x = (int64_t)a * (int64_t)db + (int64_t)b;
        int64_t y = (int64_t)a + (int64_t)da * (int64_t)b;
        
        return x < y;
    });
    
    dump(num);
    
    std::string ret;
    char buffer[32] = {0};
    for(auto i = num.rbegin();i!=num.rend();i++)
    {
        sprintf(buffer, "%d", *i);
        ret += std::string(buffer);
    }
    return ret;
}

int main()
{
    //int arr[] = {2,10};
    //int arr[] = {3,30,34,5,9};
    int arr[] = {999999998,999999997,999999999};
    //int arr[] = {0,0,0};
    vector<int> vec(arr,arr+sizeof(arr)/sizeof(int));
    cout<<largestNumber(vec)<<"\n";
    return 0;
}
