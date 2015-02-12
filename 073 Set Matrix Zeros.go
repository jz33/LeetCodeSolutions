package main
/*
73 Set Matrix Zeros
https://oj.leetcode.com/problems/set-matrix-zeroes/
http://yucoding.blogspot.com/2013/04/leetcode-question-97-set-matrix-zeros.html
Use first row and col as recorders
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

func setZeros(mat [][]int64){
    fr0 := false
    fc0 := false
     
    for i:=0;i<len(mat[0]) && !fr0;i++{
        if mat[0][i]==0 {fr0 = true}
    }
    for i:=0;i<len(mat) && !fc0;i++{
        if mat[i][0]==0 {fc0 = true}
    }
    
    for i:=1;i<len(mat);i++{
        for j:=0;j<len(mat[i]);j++{
            if mat[i][j]==0{
                mat[i][0]=0
                mat[0][j]=0
            }
        }
    }
    
    for i:=1;i<len(mat);i++{
        if mat[i][0]==0{
            for j:=0;j<len(mat[i]);j++{
                mat[i][j]=0
            }
        }
    }
    for j:=1;j<len(mat[0]);j++{
        if mat[0][j]==0{
            for i:=0;i<len(mat);i++{
                mat[i][j]=0
            }
        }
    }
     
    if fr0{
        for j:=0;j<len(mat[0]);j++{
            mat[0][j]=0
        }
    }
    if fc0{
        for i:=0;i<len(mat);i++{
            mat[i][0]=0
        }
    }
}

func main(){
    //TODO: test
}