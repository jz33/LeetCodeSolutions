'''
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted array, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
'''
class Solution:
    def getInsertionPoint(self, arr: List[int], target: int) -> int:
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
        
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ip = self.getInsertionPoint(arr, x)
        if ip == len(arr):
            # out of right bound
            return arr[-k:]
        if ip == 0:
            # out of left bound
            return arr[:k]
        
        left = ip - 1
        right = ip
        dq = collections.deque()
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
        return list(dq)
