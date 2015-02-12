#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <functional>
/*
N-Queens 
https://oj.leetcode.com/problems/n-queens/
N-Queens II
https://oj.leetcode.com/problems/n-queens-ii/
*/
/*
Notice how each solution is recorded
DIM == 4, total = 2, unique = 1
0100 => 2,4,1,3
0001
1000
0010

0010 => 3,1,4,2
1000
0001
0100
*/
typedef std::vector<std::vector<int> > MAT;
typedef std::vector<int> ROW;

struct CustomHash{
    // override
    std::size_t operator()(ROW const& x) const 
    {
		std::size_t h=0;
		for(ROW::const_iterator i = x.begin();i!=x.end();i++)
			h ^= (*i)*100;
		return h;
    }
};

struct CustomEqual{
    // vertical reflection, i.e., reverse vector
    ROW verticalReflect(ROW const& x) const
    {
        ROW r(x.size());
        std::reverse_copy(x.begin(), x.end(), r.begin());
        return r;
    }
    
    // horizontal reflection
    ROW horizontalReflect(ROW const& x) const
    {
        ROW r(x.size());
        int S = (int)(x.size()-1);
        for(auto i = 0;i<x.size();i++)
            r[i] = S-x[i];
        return r;
    }
    
    // rotate 90 counterclockwise
    ROW rot90(ROW const& x) const
    {
        ROW r(x.size());
        int S = (int)(x.size()-1);
        for(auto i = 0;i<x.size();i++)
            r[S-x[i]] = i;
        return r;
    }
    
    // rotate 180 counterclockwise
    ROW rot180(ROW const& x) const
    {
        ROW r(x.size());
        int S = (int)(x.size()-1);
        for(auto i = 0;i<x.size();i++)
            r[S-i] = S-x[i];
        return r;
    }
    
    // rotate 270 counterclockwise
    ROW rot270(ROW const& x) const
    {
        ROW r(x.size());
        int S = (int)(x.size()-1);
        for(auto i = 0;i<x.size();i++)
            r[x[i]] = S-i;
        return r;
    }
    
    // override
    bool operator()(ROW const& x, ROW const& y) const 
    {   
        if(std::equal(x.begin(), x.end(), y.begin())) return true;
        ROW r,s;
        
        r = verticalReflect(x);
        if(std::equal(r.begin(), r.end(), y.begin())) return true;
        
        r = horizontalReflect(x);
        if(std::equal(r.begin(), r.end(), y.begin())) return true;
        
        r = rot90(x);
        if(std::equal(r.begin(), r.end(), y.begin())) return true;
        
        r = rot180(x);
        if(std::equal(r.begin(), r.end(), y.begin())) return true;
        
        r = rot270(x);
        if(std::equal(r.begin(), r.end(), y.begin())) return true;
        
        s = rot90(x); r = horizontalReflect(s);
        if(std::equal(r.begin(), r.end(), y.begin())) return true;
        
        s = rot270(x);r = horizontalReflect(s);
        if(std::equal(r.begin(), r.end(), y.begin())) return true;
        
        return false;
    }
};

int abs(int a,int b){return a>b? a-b:b-a;}

// curr = current row = buf.size()
void rec(MAT& res, ROW& buf, const int DIM, int curr){
    if(curr == DIM){
        res.push_back(buf);
        return;
    }
    
    // check current row
    for(int i=0;i<DIM;i++)
    {
        bool isValid = true;
        for(int j=0;j<curr && isValid;j++){
            // (j, buf[j]) vs (curr, i)
            if(buf[j] == i || abs(j,curr)==abs(buf[j],i)) isValid = false;
        }
        if(isValid){
            ROW newbuf(buf);
            newbuf[curr] = i;
            rec(res,newbuf,DIM,curr+1);
        }
    }
}

MAT queens(const int DIM){
    MAT res;
    if(DIM==1){
        ROW r;
        r.push_back(1);
        res.push_back(r);
        return res;
    }
    
    for(int i=0;i<DIM;i++)
    {
        ROW buf(DIM);// recursion buffer
        buf[0] = i;
        
        // start from 2nd row
        rec(res,buf,DIM,1);
    }
    return res;
}

/*
  Filter total solutions to get unique solutions.
  This can be magically achieved by a carefully designed
  set, i.e., a set whose hash function treats solution
  with its rotations & reflection as one same solution.
*/
typedef std::unordered_set<ROW, CustomHash, CustomEqual> SET;
SET unique(MAT& mat){
    SET filter;
    for(size_t i=0;i<mat.size();i++){
			filter.insert(mat[i]);
	}
    return filter;
}

void dumpMat(MAT& mat, const int DIM){
	printf("Number of Queens: %d\n",DIM);
    printf("Total number of the solutions: %u\n",mat.size());
    for(size_t i=0;i<mat.size();i++){
        printf("%u: ",i);
        for(size_t j=0;j<mat[i].size();j++)
            printf("%d ",mat[i][j]);
        printf("\n");
    }
    printf("\n");
}

void dumpSet(SET& mat, const int DIM){
    printf("Number of Queens: %d\n",DIM);
    printf("Unique solutions: %u\n",mat.size());
	size_t x = 0;
    for(auto i=mat.begin();i !=mat.end();i++){
        printf("%u: ",x++);
        for(size_t j=0;j<i->size();j++)
            printf("%d ",(*i)[j]);
        printf("\n");
    }
    printf("\n");
}

void dumpROW(ROW& mat){
    for(auto i=mat.begin();i !=mat.end();i++) printf("%d ",*i);
    printf("\n");
}

int main(int argc, char* argv[]){
    for(int i=4;i<=8;i++){
        auto res = queens(i);
        dumpMat(res,i);
        dumpSet(unique(res),i);
    }
	return 0;
}