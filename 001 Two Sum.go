package main
/*
01 Two Sum
https://oj.leetcode.com/problems/two-sum/
*/
import (
    "fmt"
)

func twoSum(numbers []int, target int) [2]int{
    var res [2]int
    for i := 0;i<len(numbers);i++ {
        r := target - numbers[i];
        if r>0 {
            for j := i+1;j<len(numbers);j++{
                if numbers[j]==r {
                    res[0] = i+1;
                    res[1] = j+1;
                    return res;
                }
            }
        }
    }
    return res;
}

func main(){
    numbers := []int{2,7,11,15};
    target := 9;
    res := twoSum(numbers, target);
    fmt.Println(res[0]);
    fmt.Println(res[1]);
}