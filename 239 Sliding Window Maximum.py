from collections import deque
'''
Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
'''
def maxSlidingWindow(arr, width):
    if len(arr) == 0: return []
    ret = [0] * (len(arr) - width + 1)
    
    dq = deque()
    for i in xrange(0,width):
        while len(dq) > 0 and arr[i] > arr[dq[-1]]:
            dq.pop()
        dq.append(i)
            
    for i in xrange(width,len(arr)):
        ret[i-width] = arr[dq[0]]
        while len(dq) > 0 and arr[i] > arr[dq[-1]]:
            dq.pop()
        while len(dq) > 0 and dq[0] <= i - width:
            dq.popleft()
        dq.append(i)
        
    ret[-1] = arr[dq[0]]
    return ret
    

arr = [1,3,-1,-3,5,3,6,7]
width = 3

print maxSlidingWindow(arr,width)
    
