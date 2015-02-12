package main
/*
150 Evaluate Reverse Polish Notation
https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
*/
import (
	"fmt"
    "strconv"
)
func evalReversePolishNotation(list []string) int64 {
	var stack []int64 = make([]int64,len(list)) // should use stack
	var j int = 0
	
	for _,v := range(list) {
		val,err := strconv.ParseInt(v,10,64)
		if err == nil {
			stack[j] = val
			j++
		} else {
			switch v{
			case "+": stack[j-2] = stack[j-2]+stack[j-1]
			case "-": stack[j-2] = stack[j-2]-stack[j-1]
			case "*": stack[j-2] = stack[j-2]*stack[j-1]
			case "/": stack[j-2] = stack[j-2]/stack[j-1]
			default: panic("unrecognized operator")
			}
			j--
		}
	}
	return stack[j-1]
}
func main() {
    ls := []string{"2", "1", "+", "3", "*"}
    fmt.Printf("%v\n",evalReversePolishNotation(ls))
    
    ls = []string{"4", "13", "5", "/", "+"}
    fmt.Printf("%v\n",evalReversePolishNotation(ls))
}