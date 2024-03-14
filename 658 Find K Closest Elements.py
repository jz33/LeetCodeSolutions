'''
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
    1 <= k <= arr.length
    1 <= arr.length <= 104
    arr is sorted in ascending order.
    -104 <= arr[i], x <= 104
'''
def getInsertionPoint(arr: List[int], target: int):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Check len(arr) < k case

        insertionPoint = getInsertionPoint(arr, x)
        if insertionPoint == len(arr):
            # out of right bound
            return arr[-k:]
        if insertionPoint == 0:
            # out of left bound
            return arr[:k]
        
        left = insertionPoint - 1
        right = insertionPoint
        dq = deque()
        while left >=0 and right < len(arr) and len(dq) < k:
            le = arr[left]
            re = arr[right]
            if abs(x - le) <= abs(re - x):
                dq.appendleft(le)
                left -= 1
            else:
                dq.append(re)
                right += 1

        missedCount = k - len(dq)
        if missedCount > 0:        
            if left >=0:
                return arr[left - missedCount + 1 : left+1] + list(dq)
            else: # right < len(arr)
                return list(dq) + arr[right : right + missedCount]
        else:
            return list(dq)
        
class Solution:
    '''
    Simple heap method
    '''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [] # [(-dist, val)]
        for val in arr:
            heappush(heap, (-abs(val-x), -val))
            if len(heap) > k:
                heappop(heap)
        return sorted(-v for _,v in heap)
