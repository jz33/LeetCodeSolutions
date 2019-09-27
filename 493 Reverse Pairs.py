'''
493. Reverse Pairs
https://leetcode.com/problems/reverse-pairs/

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
'''
from copy import deepcopy

class Solution:
    def upperBound(self, arr, tag, left, right)->int:
        '''
        Find the largest index i of arr where arr[i] * 2 < tag
        '''
        bound = None
        while left <= right:
            mid = left + ((right - left) >> 1)
            val = arr[mid]

            if val * 2 < tag:
                bound = mid
                left = mid + 1
            else:
                right = mid - 1
        return bound

    def merge(self, arr, buf, lt, mid, rt) -> int:
        '''
        Classic merge method for mergesort
        
        Merge from back (larger)
        lt     mid      rt
        0 1 2 3 4 5 6 7
        lt     mid    rt
        0 1 2 3 4 5 6
        
        left branch is arr[lt:mid]
        right branch is arr[mid:rt]
        '''

        # Compute inversion first
        inv = 0
        bound = rt - 1
        for i in range(mid-1, lt-1, -1): # iterate left branch
            bound = self.upperBound(arr, arr[i], mid, bound) # find bound in right branch
            if bound is None:
                break
            inv += bound - mid + 1
        
        # Do regular merge
        i = mid - 1
        j = rt - 1
        k = rt - 1
        while i >= lt and j >= mid:
            if arr[i] <= arr[j]:
                buf[k] = arr[j]
                k -= 1
                j -= 1
            else:
                buf[k] = arr[i]
                k -= 1
                i -= 1
                
        while j >= mid:
            buf[k] = arr[j]
            k -= 1
            j -= 1
            
        arr[max(lt, i):rt] = buf[max(lt, i):rt]
        return inv
 
    def reversePairs(self, arr: List[int]) -> int:
        # Use mergesort
        size = len(arr)
        buf = deepcopy(arr)
        inv = 0
        bound = (size << 1)
        stride = 2 # stride is half the size of array when calling merge    
        while stride < bound:
            for left in range(0, size, stride):
                mid = min(left + (stride >> 1), size);
                right = min(left + stride, size);
                inv += self.merge(arr,buf,left,mid,right);
            stride <<= 1
        return inv
