#include <iostream>
/*
74 Search a 2D Matrix
A naive version requires: 
"The first integer of each row is greater than the last integer of the previous row."
See:
https://oj.leetcode.com/problems/search-a-2d-matrix/
Can be simply done by binary search first column, then binary search at most 1 row

A more general case:
http://articles.leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html

Table[i][j] <= Table[i][j + 1] 
Table[i][j] <= Table[i + 1][j]
*/
#define COL_NUM 5

/*
Step-wise approach, starting from upper-right
Worst: O(n)
*/
int stepWise(int mat[COL_NUM][COL_NUM],int target,int& row,int& col)
{
    if(target < mat[0][0] || target > mat[COL_NUM-1][COL_NUM-1])
        return 0;

    row = 0;
    col = COL_NUM - 1;
    while(row <= COL_NUM -1 && col >= 0)
    {
        if(mat[row][col] < target) 
            row++;
        else if (mat[row][col] > target)
            col--;
        else
            return 0;
    }
    return 1;
}
/*
A binary search for ascending sorted array
Return insertion position, i.e.,
the index of the new element if is inserted
*/
int binary(int arr[], int tag, int lt, int rt)
{
    int mid;
    while(lt <= rt)
    {
        mid = (lt+rt) >> 1;
        if(arr[mid] == tag) return mid;
        
        // lt = rt - 1 or lt == rt
        if(mid == lt)
        {
            if(tag < arr[lt])
                return lt;
            else if (tag > arr[lt] && tag <= arr[rt])
                return lt + 1;
            else // (tag > arr[rt])
                return rt+1;
        }
        
        if(arr[mid] < tag) lt = mid + 1;
        else rt = mid - 1;
    }
    return -1; // error
}
/*
Binary Partition by row
O((lg n)^2)
*/
int partition(int mat[COL_NUM][COL_NUM],int tag,int lt,int rt,int up,int dn,int& row,int& col)
{
    if(lt > rt || up > dn)
        return 0;
    if(tag < mat[up][lt] || tag > mat[dn][rt])
        return 0;
    
    // binary search mid row
    int mid = (up + dn) >> 1;
    int index = binary(mat[mid],tag,lt,rt);
    if(index >= lt && index <= rt && mat[mid][index] == tag)
    {
        row = mid;
        col = index;
        return 1;
    }
    
    // go to upper right and lower left
    return \
        partition(mat, tag, index, rt,      up, mid-1, row, col) || \
        partition(mat, tag, lt,    index-1, mid+1, dn, row, col);
}
 
int binaryPartition(int mat[COL_NUM][COL_NUM],int tag,int &row,int &col)
{
    return partition(mat,tag,0,COL_NUM-1,0,COL_NUM-1,row,col);
}

int main()
{
    int mat[COL_NUM][COL_NUM] = {\
        { 1, 4, 5,11,15},\
        { 2, 5, 8,12,19},\
        { 3, 6, 9,16,22},\
        {10,13,14,17,24},\
        {18,21,23,26,30},\
    };
    int row = -1;
    int col = -1;
    
    int tag,r0,r1,i,j;
    for(i=0;i<COL_NUM;i++){
        for(j=0;j<COL_NUM;j++){
            tag = mat[i][j];
            row = -1,col = -1;
            
            r0 = stepWise(mat,tag,row,col);
            printf("(%d, %d) ",row,col);
            
            row = -1,col = -1;
            r1 = binaryPartition(mat,tag,row,col);
            if(r1 != 0){
                printf("(%d, %d)\n",row,col);
            } else {
                printf("Not found!\n");
            }
        }
    }    
    return 0;
}
