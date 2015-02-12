package main
/*
148 Sort list
https://oj.leetcode.com/problems/sort-list/
*/
import (
	"fmt"
    "log"
	"bufio"
	"os"
	"strconv"
	"strings"
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
func mergesort_merge(a *node, b *node) *node{
	if a == nil {return b}
	if b == nil {return a}
	
	var head *node
	if a.val < b.val {
		head = a
		a = a.ptr
	} else {
		head = b
		b = b.ptr
	}
	
	var t *node = head
	for a != nil && b != nil{
		if a.val < b.val {
			t.ptr = a
			a = a.ptr
		} else {
			t.ptr = b
			b = b.ptr
		}
		t = t.ptr
	}
	if a != nil {t.ptr = a}
	if b != nil {t.ptr = b}

	return head
}
func mergesort_split(head *node) (aRef, bRef *node){
	var slow *node
	var fast *node
	
	aRef = head
	if head == nil || head.ptr == nil {	
		bRef = nil
	} else {
		slow = head
		fast = head
		
		for fast != nil && fast.ptr != nil {
			fast = fast.ptr.ptr
			if fast == nil {break} // this is important
			slow = slow.ptr
		}

		bRef = slow.ptr
		slow.ptr = nil
	}
	return aRef, bRef
}
/*
merge sort
average: O(nlogn)
best: O(nlogn)
worst: O(nlogn)
memory usage: 0 
*/
func mergesort(head *node) *node{
	if head == nil || head.ptr == nil {return head}
	
	aRef, bRef := mergesort_split(head)
	aRef = mergesort(aRef)
	bRef = mergesort(bRef)
	head = mergesort_merge(aRef,bRef)
	
	return head
}

// tester, input like :
// 3 8 9 4 5 7 2
func main() {
    file, err := os.Open(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }   
    defer file.Close()
    scanner := bufio.NewScanner(file)
	
	var line_num int = 0
    for scanner.Scan() {
		line_num++
		
		var list []string = strings.Fields(scanner.Text())
		var listi []int64 = make([]int64,len(list))
		for i,v := range(list){
			listi[i],_ = strconv.ParseInt(v,10,64)
		}
		
		var head *node = new(node)
		head.initnode(listi[0])
		var p *node = head
		
		for i := 1;i<len(listi);i++{
			p.ptr = new(node)
			p = p.ptr
			p.initnode(listi[i])
		}
		
		fmt.Printf("line: %d, input: \n",line_num)
		printnodes(head)
		
		head = mergesort(head)
		
		fmt.Printf("line: %d, result: \n",line_num)
		printnodes(head)
    }   
}