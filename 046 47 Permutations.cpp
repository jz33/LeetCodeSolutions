#include <iostream>
#include <vector>
#include <set>
#include <functional>
#include <algorithm>
/*
Permutations
https://oj.leetcode.com/problems/permutations/
Permutations II
https://oj.leetcode.com/problems/permutations-ii/
*/
typedef std::vector<int> VEC;

void dumpIntArray(int* arr, const int size){
    int i = 0;
	for(;i<size;i++) printf("%d ", arr[i]);
    printf("\n");
}
void dumpVec(VEC& in){
    for(VEC::iterator i = in.begin();i!=in.end();i++)
        std::cout<<*i<<" ";
    std::cout<<"\n";
}
void swapInts(int* x, int* y){
    int t = *x;
    *x = *y;
    *y = t ;
}
bool compareInt(int i, int j){
    return (i==j);
}
void swapVecIter(VEC::iterator i, VEC::iterator j){
	int t = *i;
	*i = *j;
	*j = t;
}
/*
A simple C version of normal permutations
A deep-first search
*/
void perms(int* arr, const int size, int lv)
{
    int i; 
    for(i = lv;i < size;i++){
        swapInts(arr+lv, arr+i);
        if(lv + 1 == size) dumpIntArray(arr,size);
        else perms(arr, size, lv+1);
        swapInts(arr+lv, arr+i);
    }
}
/*
A custom set for std::vector<int>
*/
typedef std::set<VEC, std::less<VEC> > SET;

void copySet(SET& tag, SET& src){
    for(SET::iterator i = src.begin();i!=src.end();i++)
        tag.insert(tag.end(),*i);
}
/*
A C++ version of permutations considering duplicates
Breath-first search
"filter" is used to record current level's candidates
*/
void permsDup(VEC& src)
{   
    SET prev, filter;
	std::size_t size = src.size();
    std::size_t lv,i;
    VEC curr;
    
    prev.insert(src);
    for(lv = 0;lv < size-1;lv++)
    {
        filter.clear();
        for(SET::iterator j = prev.begin();j!=prev.end();j++)
        {
            curr = *j;
            for(i = lv;i<size;i++)
            {
				// cannot use std::swap here
				swapVecIter(curr.begin()+lv,curr.begin()+i);
				filter.insert(curr);
				swapVecIter(curr.begin()+lv,curr.begin()+i);
            }
        }
        prev.clear();

		// cannot use std::copy here
        copySet(prev,filter); 
    }
    
    for(SET::iterator j = prev.begin();j!=prev.end();j++){
		curr = *j;
        dumpVec(curr);
    }
}
/*
A recursive c++ version of permutation considering duplicates
*/
void permutationsDupRec(const std::size_t size,VEC& src,VEC& cur)
{
    if(cur.size() == size) dumpVec(cur);
    else
	{
        // "prev" is used to eliminate duplicates
        VEC prev;
	    for(std::size_t i=0;i < src.size();i++)
		{   
			VEC newCur(cur);
		    newCur.push_back(src[i]);
            
            if(	prev.size() == 0 ||
				!std::equal(newCur.begin(),newCur.end(),prev.begin(),compareInt)){
                prev = newCur;
                VEC newSrc(src.size()-1);            
                std::copy(src.begin(),src.begin()+i,newSrc.begin());
                std::copy(src.begin()+i+1,src.end(),newSrc.begin()+i);
                permutationsDupRec(size, newSrc, newCur);
            }
		}
	}
}
void permutationsDup(VEC in)
{
    std::stable_sort(in.begin(),in.end());
	VEC cur;
	std::size_t size = in.size();
    permutationsDupRec(size,in,cur);
}
int main()
{   
    int arr[4] = {1,1,2,2};
	//int arr[3] = {1,1,2};
    VEC in (arr,arr + sizeof(arr) / sizeof(int));
    perms(arr,4,0);printf("\n");
    permsDup(in);  printf("\n");
	permutationsDup(in);
    return 0;
}