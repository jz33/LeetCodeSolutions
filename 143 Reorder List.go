package main
/*
143 Reorder list
https://oj.leetcode.com/problems/reorder-list/
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

/*
{1,2,3,4,5,6}   ---> {1,6,2,5,3,4}
{1,2,3,4,5,6,7} ---> {1,7,2,6,3,5,4}
*/
func reorder(head *node) *node {
	if head == nil {return head}
	if head.ptr == nil {return head}
	
	var p *node = head
	var q *node = head
	 
	//find the middle pointer
	for q.ptr != nil && q.ptr.ptr != nil {
		p = p.ptr
		q = q.ptr.ptr
	}
	 
	//now p is middle pointer
	//reverse p->next to end
	q = p.ptr
	var r *node = p.ptr
	for q.ptr != nil {
		r = p.ptr
		p.ptr = q.ptr
		q.ptr = q.ptr.ptr
		p.ptr.ptr = r
	}
	 
	//reorder
	q = head;
	r = p
	p = p.ptr
	r.ptr = nil
	
	for p != nil {
		r = p.ptr
		p.ptr = q.ptr
		q.ptr = p
		q = p.ptr
		p = r
	}
	return head;
}

// tester
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
		
		head = reorder(head)
		
		fmt.Printf("line: %d, result: \n",line_num)
		printnodes(head)
    }   
}