'''
Remove Duplicated from Sorted Array
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
func removeDuplicates(nums []int) int {
    // The widht is the maximun allowd count for a distint value
    // Therefore if width is 2, this solution can be used for Remove Duplicates from Sorted Array II
    const WIDTH = 1
    
    // The n is the length of the return array
    n := 0
    for _, e := range nums {
        if n-WIDTH < 0 || nums[n-WIDTH] < e {
            nums[n] = e
            n++
        }
    }   
    return n
}
