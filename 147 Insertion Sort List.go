package main
/*
147 Insertion Sort List
https://oj.leetcode.com/problems/insertion-sort-list/
*/
/*
merge sort helper
*/
import (
	"fmt"
)

type node struct{
	val int64
	ptr *node
}

// constructor
func (p *node) initnode(val int64){
	p.val = val
	p.ptr = nil
}

// notice head will not be changed after print
func printnodes(head *node){
	for head != nil {
		fmt.Printf("%d ",head.val)
		head = head.ptr
	}
	fmt.Println()
}

/*
insertion sort
average: O(n^2)
best: O(n), already sorted
worst: O(n^2), reverse ordered
memory usage: 0 
*/
func insertionsort(head* node) *node{
	if head == nil {return head} // 0 element
	
	var curr *node = head // current
	if curr.ptr == nil {return head} // only 1 element
	var next *node = curr.ptr // next
	
	for next != nil {
		if next.val < curr.val { // needs insertion
			curr.ptr = next.ptr
			
			//start from head
			if next.val < head.val {
				next.ptr = head
				head = next
				next = curr.ptr
			} else {
				var prev *node = head // previous
				var comp *node = head.ptr // compare with next
				for prev != curr {
					if next.val < comp.val { // do insertion
						prev.ptr = next
						next.ptr = comp
						next = curr.ptr
						break
					} else {
						prev = comp
						comp = comp.ptr
					}
				}
			}
		} else { // do nothing
			curr = next
			next = next.ptr
		}
	}
	return head
}

// tester
func main() {   
}