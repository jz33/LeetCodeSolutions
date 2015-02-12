package main
/*
Pascal's Triangle
Pascal's Triangle II
https://oj.leetcode.com/problems/pascals-triangle/
https://oj.leetcode.com/problems/pascals-triangle-ii/
*/
import (
	"fmt"
)

func generate(level int) (res [][]int, err bool){
    if level < 1 {
        err = true
        return nil, err
    } 
    
	res = make([][]int,level)
	res[0] = make([]int,1)
	res[0][0] = 1
	
	for i := 1;i<level;i++{
	    res[i] = make([]int,i+1)
	    res[i][0] = 1
	    res[i][i] = 1
	    for j := 1;j<i;j++{
	        res[i][j] = res[i-1][j-1]+res[i-1][j]
	    }
	}
	
	return res,err
}

func dumpMat(res [][]int){
    for i := 0;i<len(res);i++{
        for j := 0;j<len(res[i]);j++{
            fmt.Printf("%5v",res[i][j])
        }
        fmt.Println()
    }
}

func combination(base, up int) (res int, err bool) {
    if up > base || base < 0 || up < 0{
        err = true
        return 0, err
    }
    res = 1
    for i := base;i > up;i-- {
        res *= i
    }
    for i := base-up;i > 1;i-- {
        res /= i
    }
    return res,err
}

func getRow(level int) (res []int, err bool){
    if level < 1 {
        err = true
        return nil, err
    }
    
    res = make([]int,level)
    var mid int = level /2
    
    for i := 0;i<mid;i++{
        res[i],_ = combination(level-1,i)
    }
    for i := mid;i<level;i++{
        res[i] = res[level-i-1]
    }
    
    if level % 2 == 1 {
        res[mid],_ = combination(level-1,mid)
    }
    
    return res,err
}

func dumpArr(res []int){
    for i := 0;i<len(res);i++{
        fmt.Printf("%5v",res[i])
    }
    fmt.Println()
}

func main() {
    var level int = 10 // 1,2,3,4...
    res,_ := generate(level)
    dumpMat(res)
    
    res2,_:= getRow(9)
    dumpArr(res2)
    res3,_:= getRow(8)
    dumpArr(res3)
}