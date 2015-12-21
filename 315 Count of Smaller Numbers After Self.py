from copy import deepcopy
'''
Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
'''
'''
lt    m      rt
0 1 2 3 4 5 6 7
'''
def merge(arr, buf, inv, lt, mid, rt):
    i = mid
    j = rt
    k = rt
    while i >= lt and j > mid:
        if arr[i][1] <= arr[j][1]:
            buf[k] = arr[j]
            k -= 1
            j -= 1     
        else:
            inv[arr[i][0]] += j - mid
            buf[k] = arr[i]
            k -= 1
            i -= 1

    while j > mid:
        buf[k] = arr[j]
        k -= 1
        j -= 1
                
    for i in xrange(lt,rt+1):
        arr[i] = buf[i]
 
def mergesort(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    size = len(nums)
    arr = list(enumerate(nums))
    buf = deepcopy(arr)
    inv = [0] * size;

    stride = 2
    while stride < size * 2:
        for lt in xrange(0,size,stride):
            mid = min(lt + (stride >> 1) - 1,size - 1);
            rt  = min(lt + stride - 1,size - 1);
            merge(arr,buf,inv,lt,mid,rt);
        stride <<= 1
    return inv


nums = [7,6,5,4,3]
print mergesort(nums)
