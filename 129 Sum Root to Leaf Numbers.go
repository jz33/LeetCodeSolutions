package main
/*
129 Sum Root to Leaf Numbers.go
https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
*/
import (
	"fmt"
)
type node struct {
	val int64
	pl  *node
	pr  *node
}

// constructor
func (n *node) initnode(val int64) {
	n.val = val
	n.pl = nil
	n.pr = nil
}
/*
initialize a tree from an array as inorder
start is 0, end is len(arr)-1
*/
func (n *node) initInOrder(arr []int64, start,end int){
	mid := (start+end)>>1
	n.val = arr[mid]
	
	if start <= mid-1 {
		n.pl = new(node)
		n.pl.initInOrder(arr, start, mid-1)
	}
	if mid+1 <= end {
		n.pr = new(node)
		n.pr.initInOrder(arr, mid+1, end)
	}
}
/*
A specific traversal methods, e.g.,
        0
	   /  \
      1    2
     / \   
    3   4   
=>
[
[0 1 3] = 13
[0 1 4] = 14
[0 2] = 2
]
=> 29
*/
func toMatrixRec(sum *int64, buf int64, n *node){
    if n == nil {return}
    buf = buf * 10 + n.val
    
    if n.pl == nil && n.pr == nil {
        *sum = *sum + buf
    } else {
        toMatrixRec(sum, buf, n.pl)
        toMatrixRec(sum, buf, n.pr)
    }
}
func main(){
    const cap int = 7
	var arr []int64 = make([]int64,cap)
	for i := 0;i<cap;i++{
		arr[i] = int64(i)
	}
    var in *node = new(node)
	in.initInOrder(arr,0,len(arr)-1)
    
    var sum int64 = 0
    toMatrixRec(&sum,0,in); 
    fmt.Println(sum); // sum == 1332
}