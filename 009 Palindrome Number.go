package main
/*
09 Palindrome Number
https://oj.leetcode.com/problems/palindrome-number/
*/
import (
	"fmt"
	"math"
)
/*
Tell if a decimal int64 number is palindrome 
without extra space
Negative number is treated as positive
Iterative way
*/
func isPalindromicDecimal(x int64) bool {
	if x > math.MaxInt64 || x < math.MinInt64 {return false}
	if x < 0 {x = -x}
    if x >=0 && x < 10 {return true}
	
    var digit float64 = 1
    var t int64 = x 
    for t >= 10 {
        digit += 1
        t = int64(t/10)
    }
	
    for digit > 1 {
        var div int64 = int64(math.Pow(10,digit-1))
        var left  int64 = int64(x/div)
        var right int64 = int64(math.Mod(float64(x),10))
        if left != right  {return false}
        x = int64((x - div*left-right)/10)
        digit -=2
    }
    return true
}

func main() {
    var x int64 = 123454321
    fmt.Printf("%v,%v\n",x,isPalindromicDecimal(x))  
}