#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
/*
Permutations II
https://oj.leetcode.com/problems/permutations-ii/
*/
typedef std::vector<int> VEC;
/*
A custom set for std::vector<int>
*/
typedef std::set<VEC, std::less<VEC> > SET;

void copySet(SET& tag, SET& src)
{
    for(SET::iterator i = src.begin();i!=src.end();i++)
        tag.insert(tag.end(),*i);
}
void swap(VEC::iterator i, VEC::iterator j)
{
	int t = *i;
	*i = *j;
	*j = t;
}

std::vector<VEC> pool;
bool compareInt(int i, int j)
{
    return (i==j);
}

/*
An iterative approach using set
"filter" is used to record current level's candidates
*/
std::vector<VEC> perms(VEC& src)
{   
    SET prev, filter;
    std::size_t size = src.size();
    std::size_t lv,i;
    VEC curr;

    prev.insert(src);
    for(lv = 0;lv < size - 1;lv++)
    {
        filter.clear();
        for(SET::iterator j = prev.begin();j!=prev.end();j++)
        {
            curr = *j;
            for(i = lv;i<size;i++)
            {
                swap(curr.begin()+lv,curr.begin()+i);
                filter.insert(curr);
                swap(curr.begin()+lv,curr.begin()+i);
            }
        }
        prev.clear();
        copySet(prev,filter); 
    }
    
    std::vector<VEC> res;
    for(SET::iterator j = prev.begin();j!=prev.end();j++)
        res.push_back(*j);
    return res;
}
std::vector<VEC> permuteUnique(VEC& in)
{
    return perms(in);  
}
/*
A recursive c++ version of permutation considering duplicates
*/
void permutationsDupRec(size_t size,VEC& src,VEC& cur)
{
    if(cur.size() == size) pool.push_back(cur);
    else
	{
        // "prev" is used to eliminate duplicates
        VEC prev;
        for(std::size_t i=0;i < src.size();i++)
        {   
            VEC newCur(cur);
            newCur.push_back(src[i]);
            
            if(	prev.size() == 0 ||
                !std::equal(newCur.begin(),newCur.end(),prev.begin(),compareInt))
            {
                prev = newCur;
                VEC newSrc(src.size()-1);            
                std::copy(src.begin(),src.begin()+i,newSrc.begin());
                std::copy(src.begin()+i+1,src.end(),newSrc.begin()+i);
                permutationsDupRec(size, newSrc, newCur);
            }
        }
    }
}
void permutationsDup(VEC& in)
{
    pool.clear();
    std::stable_sort(in.begin(),in.end());
	VEC cur;
	std::size_t size = in.size();
    permutationsDupRec(size,in,cur);
}
int main()
{   
    int arr[] = {1,1,2};
    int size = sizeof(arr)/sizeof(int);
    VEC in(arr,arr+size);
    
    std::vector<VEC> iter = permuteUnique(in);
    permutationsDup(in);
    
    return 0;
}
