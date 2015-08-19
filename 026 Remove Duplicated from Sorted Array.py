'''
Remove Duplicated from Sorted Array
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
WIDTH = 1
def removeDuplicates(arr):
    i = 0
    for n in arr:
        if i < WIDTH or n > arr[i - WIDTH]:
            arr[i] = n
            i += 1
    return i
