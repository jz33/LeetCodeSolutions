package main
/*
91 Decode Ways
https://oj.leetcode.com/problems/decode-ways/
*/
import (
	"fmt"
)
func vocabularyComposeCount(in string, curr int) int {
    if curr > len(in)-1 {return 1}
    c0 := in[curr]
    if c0 == '0' {return 0}
    if curr == len(in)-1 {return 1}
    
    r0 := vocabularyComposeCount(in,curr+1)
    r1 := 0
    
    c1 := in[curr+1]
    n1 := int(c0-'0')*10+int(c1-'0')
    if n1 < 27 {
        r1 = vocabularyComposeCount(in,curr+2)
    }
    return r0+r1
}
func test_vocabularyComposeCount(){
    var t0 string = "1313";
    var t1 string = "13013";
    var t2 string = "131313";
    var t3 string = "111111";
    fmt.Printf("%v\n",vocabularyComposeCount(t0,0));
    fmt.Printf("%v\n",vocabularyComposeCount(t1,0));
    fmt.Printf("%v\n",vocabularyComposeCount(t2,0));
    fmt.Printf("%v\n",vocabularyComposeCount(t3,0));
}
func main() {
    test_vocabularyComposeCount();
}