package main
/*
125 Valid Palindrome
https://oj.leetcode.com/problems/valid-palindrome/
*/
import (
	"fmt"
    "bytes"
)
func isPalindromicString(y string) bool {
	var delimiters []uint8 = []uint8{' ',',','.',':',';'}
	var x []uint8 = []uint8(y)

	x = bytes.ToLower(x)
	i,j := 0,len(x)-1
	for i<=j{
		if bytes.IndexByte(delimiters,x[i]) != -1{
			i++
		} else if bytes.IndexByte(delimiters,x[j]) != -1{
			j--
		} else {
			if x[i] != x[j] {
				return false
			} else {
				i++
				j--
			}
		}
	}
    return true
}
func main() {
    ls := "A man, a plan, a canal: Panama"
    fmt.Printf("%v\n",isPalindromicString(ls))
    
    ls = "race a car"
    fmt.Printf("%v\n",isPalindromicString(ls))
}