from copy import deepcopy
'''
Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

Same problem as "Count Inversions"
'''
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
