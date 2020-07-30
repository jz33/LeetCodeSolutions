/*
354. Russian Doll Envelopes
https://leetcode.com/problems/russian-doll-envelopes/
*/
import (
    "sort"
)

func getInsertionIndex(arr []int, tag int) int {
    left := 0
    right := len(arr) - 1       
    for left <= right {
        mid := left + ((right - left) >> 1)
        if arr[mid] == tag {
            return mid
        }
        if arr[mid] < tag {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return left
}

func maxEnvelopes(envelopes [][]int) int {
    sort.SliceStable(envelopes, func(i, j int) bool {
        if envelopes[i][0] != envelopes[j][0] {
            return envelopes[i][0] < envelopes[j][0]
        } else {
            return envelopes[i][1] > envelopes[j][1]
        }
    })
    
    var arr []int // arr is ascending
    for _, env := range envelopes {
        h := env[1]
        i := getInsertionIndex(arr, h)
        if i >= len(arr) {
            arr = append(arr, h)
        } else {
            arr[i] = h
        }
    }
    return len(arr)
}
