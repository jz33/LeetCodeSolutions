#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
/*
23 Merge k Sorted Lists
https://oj.leetcode.com/problems/merge-k-sorted-lists/
*/
typedef std::vector<int> VEC;
typedef std::vector<VEC> MAT;

int randLimit(const int limit){
    int div = RAND_MAX/(limit+1);
    int res = -1;
    do{ 
        res = rand() / div;
    }while (res > limit);
    return res;
}
template<typename T>
void dump(T& a)
{
    for(auto i = a.begin();i!=a.end();i++) printf("%d ",*i);
    printf("\n");
}
/*
Custom less
*/
struct CustomLess 
{
  bool operator()(const VEC::iterator& x, const VEC::iterator&  y) const
  {
    return *x < *y;
  }
};
/*
std::multimap<vector::iterator, vector::end()>
*/
typedef std::multimap<VEC::iterator, VEC::iterator, CustomLess> CustomMap;
/*
Merge first N elements from sorted arrays
*/
VEC mergeSorted(MAT& input)
{ 
    // size of buf is no more than input.size()
    CustomMap buf;
	VEC res;
    
	// insert each array's begin() iterator to buf
    for(size_t i = 0;i<input.size();i++){
		VEC& v = input[i];
		if(v.size()>0) buf.insert(std::make_pair(v.begin(),v.end()));
	}
    
	// extract first element from buf, push back to res,
	// then find next element in corresponding array
	while(!buf.empty()){
		CustomMap::iterator it = buf.begin();
		res.push_back(*(it->first));//dump<VEC>(res);
        
		if(it->first+1 != it->second) 
            buf.insert(std::make_pair(it->first+1, it->second));
		buf.erase(it);
	}
    return res;
}

#define NUM 3
int main(int argc, char* argv[]){ 
	MAT mat;
	for(int i=0;i<NUM;i++)
	{
		VEC v;
		int size = randLimit(NUM)+1;
		for(int j =0;j<size;j++) v.push_back(randLimit(NUM));
		std::stable_sort(v.begin(),v.end());
		mat.push_back(v);
	}
    
    VEC r1 = mergeSorted(mat);
	dump<VEC>(r1);
    return 0;
}