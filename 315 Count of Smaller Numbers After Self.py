'''
315. Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 

Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''
from copy import deepcopy

def brutal(arr):
    inv = [0] * len(arr)
    for i in xrange(len(arr)-1):
        for j in xrange(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv[i] += 1
    return inv
    
def merge(arr, buf, inv, lt, mid, rt):
    '''
    lt      m        rt
    0 1 2 3 4 5 6 7
    '''
    i = mid - 1
    j = rt - 1
    k = rt - 1
    while i >= lt and j >= mid:
        if arr[i][1] <= arr[j][1]:
            buf[k] = arr[j]
            k -= 1
            j -= 1
        else:
            inv[arr[i][0]] += j - mid + 1
            buf[k] = arr[i]
            k -= 1
            i -= 1
    while j >= mid:
        buf[k] = arr[j]
        k -= 1
        j -= 1
    for i in xrange(lt,rt): arr[i] = buf[i]
 
def countSmaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    size = len(nums)
    arr = list(enumerate(nums))
    buf = deepcopy(arr)
    inv = [0] * size;
    bound = (size << 1)
    stride = 2
    while stride < bound:
        for lt in xrange(0,size,stride):
            mid = min(lt + (stride >> 1),size);
            rt  = min(lt + stride,       size);
            merge(arr,buf,inv,lt,mid,rt);
        stride <<= 1
    return inv

'''
New Python3 recursive code
'''
def merge(arr, left, mid, right, buf):
    '''
    Regular mergo for mergesort, merge from back.
    left, mid is from left array.
    mid+1, right is from right array
    '''
    i = mid
    j = right
    k = right
    while i >= left and j > mid:
        if arr[i][1] <= arr[j][1]:
            buf[k] = arr[j]
            k -= 1
            j -= 1
        else:
            buf[k] = arr[i]
            k -= 1
            i -= 1
    
    # Put rest of right array
    while j > mid:
        buf[k] = arr[j]
        k -= 1
        j -= 1

    # Copy back
    arr[left : right+1] = buf[left : right+1]

def mergesort(arr, left, right, buf, res):
    if left >= right:
        return

    mid = left + (right - left) // 2
    mergesort(arr, left, mid, buf, res)
    mergesort(arr, mid + 1, right, buf, res)

    # Count smaller numbers
    midBegin = mid + 1
    j = midBegin
    for i in range(left, midBegin):
        while j <= right and arr[i][1] > arr[j][1]:
            j += 1
        res[arr[i][0]] += j - midBegin

    merge(arr, left, mid, right, buf);

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = list(enumerate(nums)) # [(index, value)]
        buf = deepcopy(arr)
        res = [0] * len(arr)
        mergesort(arr, 0, len(arr)-1, buf, res)
        return res
