#include <iostream>
#include <vector>
#include <algorithm>
/*
120 Triangle
https://oj.leetcode.com/problems/triangle/
https://www.codeeval.com/open_challenges/89/
*/
typedef std::vector<int> VEC;
typedef std::vector<VEC> MAT;

#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)

int passTriangle(MAT& mat){
    if(mat.size() < 1) return -1;
    if(mat.size() == 1) return 1;
    VEC& prev = mat[0];
	
    for(std::size_t j = 1;j<mat.size();j++){
        VEC& curr = mat[j];
        
        curr[0] += prev[0];
		for(std::size_t i=0;i<prev.size()-1;i++)
			curr[i+1] += MIN(prev[i],prev[i+1]);
		curr[j] += prev[j-1];
		prev = curr;
    }
	return *std::min_element(prev.begin(),prev.end());
}
void insertRow(MAT& mat, int* arr, int size){
	VEC row(size);
	std::copy(arr,arr+size,row.begin());
	mat.push_back(row);
}
/*
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
*/
int main(int argc, char** argv){
    MAT mat;
	VEC row(4);
    int a0[] = {2};
    int a1[] = {3,4};
    int a2[] = {6,5,7};
    int a3[] = {4,1,8,3};

    insertRow(mat,a0,1);
	insertRow(mat,a1,2);
	insertRow(mat,a2,3);
	insertRow(mat,a3,4);

    printf("%d\n",passTriangle(mat));
	return 0;
}