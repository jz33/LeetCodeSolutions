#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
/*
57 Insert Intervals
https://oj.leetcode.com/problems/insert-interval/
*/
typedef std::pair<int,int> Interval;
typedef std::vector<Interval> List;
typedef std::vector<Interval>::iterator Iter;

const int ERROR = -1;

void dump(List& input)
{
    for(List::iterator i = input.begin();i!=input.end();i++)
    {
        std::cout<<"("<<i->first<<","<<i->second<<") ";
    }
    printf("\n");
}
/*
Notice the "pos" notation,
first is index, second is:
before : -1
in : 0
after : 1
*/
void findInsertPlace(List& input, int lt, int rt, const int val, Interval& pos)
{
    if(lt >= rt) return;
    if(lt + 1 == rt){
        if(val < input[lt].first)
            pos = std::make_pair(lt, -1);
        else if (val >= input[lt].first && val <= input[lt].second) 
            pos = std::make_pair(lt, 0);
        else if (val > input[lt].second && val < input[rt].first) 
            pos = std::make_pair(lt, 1);
        else if (val >= input[rt].first && val <= input[rt].second) 
            pos = std::make_pair(rt, 0);
        else
            pos = std::make_pair(rt, 1);
        return;
    }
    
    int mid = (lt+rt)>>1;
    if(val < input[mid].first)
        findInsertPlace(input,lt,mid-1,val,pos);
    else if(val >= input[mid].first && val <= input[mid].second)
        pos = std::make_pair(mid,0);
    else
        findInsertPlace(input,mid+1,rt,val,pos);
}

void insert(List& input, Interval tag)
{
    std::stable_sort(input.begin(),input.end(),[](const Interval& i, const Interval& j)->bool{
        if(i.first != j.first) return i.first < j.first;
        else return i.second < j.second;
    });
        
    Interval ltPos = std::make_pair(ERROR,ERROR);
    Interval rtPos = std::make_pair(ERROR,ERROR);
    findInsertPlace(input,0,input.size()-1,tag.first, ltPos);
    findInsertPlace(input,0,input.size()-1,tag.second,rtPos);
    
    if(ltPos.first == ERROR || rtPos.first == ERROR){
        std::cout<<"ERROR!\n";return;
    }
    
    // debug
    std::cout<<"("<<ltPos.first<<","<<ltPos.second<<")\n";
    std::cout<<"("<<rtPos.first<<","<<rtPos.second<<")\n";
    
    int ltRm, rtRm;
    if(ltPos.second == -1){
        ltRm = ltPos.first;
        input[ltRm].first = tag.first;
    } else if(ltPos.second == 0){
        ltRm = ltPos.first;
    } else if(ltPos.second == 1){
        ltRm = ltPos.first + 1;
        input[ltRm].first = tag.first;
    }
    
    if(rtPos.second == -1){
        rtRm = rtPos.first - 1;
        input[rtRm].second = tag.second;
    } else if(rtPos.second == 0){
        rtRm = rtPos.first;
    } else if(rtPos.second == 1){
        rtRm = rtPos.first;
        input[rtRm].second = tag.second;
    }
        
    // merge interval ltRm (included) till rtRm (included)
    input[ltRm].second = input[rtRm].second;
    input.erase(input.begin()+ltRm+1,input.begin()+rtRm+1);
}
/*
[1,3],[6,9] : [2,5] => [1,5],[6,9]
*/
void test01(void){
    List input;
    input.push_back(std::make_pair(1,3));
    input.push_back(std::make_pair(6,9));
    Interval tag = std::make_pair(2,5);
    
    dump(input);
    insert(input, tag);
    dump(input);
}
/*
[1,2],[3,5],[6,7],[8,10],[12,16] : [4,9] 
=> [1,2],[3,10],[12,16]
*/
void test02(void){
    List input;
    input.push_back(std::make_pair(1,2));
    input.push_back(std::make_pair(3,5));
    input.push_back(std::make_pair(6,7));
    input.push_back(std::make_pair(8,10));
    input.push_back(std::make_pair(12,16));
    Interval tag = std::make_pair(4,9);
    
    dump(input);
    insert(input, tag);
    dump(input);
}
int main(int argc, char** argv)
{
    test01();
    test02();
    return 0;
}