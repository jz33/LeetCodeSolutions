#include <vector>
using namespace std;
/*
Maximal Square
https://leetcode.com/problems/maximal-square/
*/
int min3(int a,int b,int c){
    int m = a < b ? a : b;
    return m < c ? m : c;
}

int maximalSquare(vector<vector<char> >& mat){
    size_t row,col,i,j;
    int maxv,v;
    
    row = mat.size();
    if(row == 0) return 0;
    
    col = mat[0].size();
    
    maxv = 0;
    for(i=0;i<row;i++){
        if(mat[i][0] == '1'){
            maxv = 1;
            break;
        }
    }
    if(maxv != 1){
        for(i=1;i<col;i++){
            if(mat[0][i] == '1'){
                maxv = 1;
                break;
            }
        }
    }
    /*
    Use the input as buffer
    */
    for(i=1;i<row;i++){
        for(j=1;j<col;j++){
            if(mat[i][j] != '0'){
                v = min3(mat[i-1][j]-'0',mat[i-1][j-1]-'0',mat[i][j-1]-'0')+1;
                mat[i][j] = v + '0';
                maxv = maxv >= v ? maxv : v ;
            }
        }
    }
    return maxv * maxv;
    
int main(){
    return 0;
}
