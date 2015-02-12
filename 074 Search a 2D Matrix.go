package main
/*
74 Search a 2D Matrix
https://oj.leetcode.com/problems/search-a-2d-matrix/
http://yucoding.blogspot.com/2013/04/leetcode-question-92-search-2d-matrix.html

Each row is sorted left to right;
Each col is sorted up to down;

Notice that first integer of each row is not necessary to be 
greater than the last integer of the previous row

x is row, y is col, 0 is left, 1 is right

Test:
-2 0 5 7 15
-1 10 11 16 20
0 23 30 34 50
*/
import (
	"fmt"
)
func dump(mat [][]int64){
    for i:=0;i<len(mat);i++{
        for j:=0;j<len(mat[i]);j++{
            fmt.Printf("%v ",mat[i][j])
        }
        fmt.Println()
    } 
    fmt.Println()
}

func matSearch(mat [][]int64, tag int64, x0,x1,y0,y1 int) (rx,ry int, isExisted bool){
    if x0>x1 || y0>y1 {return rx,ry,isExisted}
    if x0==x1 && y0==y1{
        if mat[x0][y0] == tag{
            return x0,y0,true
        } else {
            return rx,ry,isExisted
        }
    }
    var mx,my int
        
    if x0==x1 && y0<y1{
        mx = x0
        my = (y0+y1)>>1

        if mat[mx][my] == tag {
            return mx,my,true
        } else if mat[mx][my] < tag {
            return matSearch(mat,tag,x0,x1,my+1,y1) //right
        } else {
            return matSearch(mat,tag,x0,x1,y0,my-1) //left
        }
    } 
    if x0<x1 && y0==y1 {
        mx = (x0+x1)>>1
        my = y0

        if mat[mx][my] == tag {
            return mx,my,true
        } else if mat[mx][my] < tag {
            return matSearch(mat,tag,mx+1,x1,y0,y1)//down
        } else {
            return matSearch(mat,tag,x0,mx-1,y0,y1)//up
        }
    }

    // x0<x1 && y0<y1
    mx = (x0+x1)>>1
    my = (y0+y1)>>1

    if mat[mx][my] == tag {
        isExisted = true
        rx = mx
        ry = my
        return rx,ry,isExisted
    } else if mat[mx][my] < tag {
        rx,ry,isExisted = matSearch(mat,tag,x0,x1,my+1,y1)//right
        if isExisted {return rx,ry,isExisted}
        rx,ry,isExisted = matSearch(mat,tag,mx+1,x1,y0,my)//lower left
        if isExisted {return rx,ry,isExisted}
    } else {
        rx,ry,isExisted = matSearch(mat,tag,x0,x1,y0,my-1)//left
        if isExisted {return rx,ry,isExisted}
        rx,ry,isExisted = matSearch(mat,tag,x0,mx-1,my,y1)//upper right
        if isExisted {return rx,ry,isExisted}
    }
    return rx,ry,isExisted
}

func main(){
    //TODO: test
}