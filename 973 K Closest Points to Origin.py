'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
'''
class MinHeap:
    '''
    A simple fixed-sized minimun binary heap implemented on array

    Supports:
        push
        pop
        pushpop
        empty
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.count = 0

    def push(self, v):
        if self.count == len(self.arr):
            raise IndexError('')

        # Append to tail first
        self.arr[self.count] = v

        # Then lift up
        lift(self.arr, self.count)

        self.count += 1

    def pop(self):
        if self.count < 1:
            raise IndexError('')

        arr = self.arr
        count = self.count
        ret = arr[0]
        
        # Move last element to top
        arr[0] = arr[count - 1]
        arr[count - 1] = None

        # Then sink it
        sink(arr, 0, count - 1)

        self.count -= 1
        return ret

    def pushpop(self,v):
        if self.count < 1:
            return v

        arr = self.arr      
        ret = arr[0]
        if v < ret:
            return v

        arr[0] = v
        sink(arr, 0, self.count)
        return ret

    def empty(self) -> bool:
        return self.count == 0

def heapify(arr) -> MinHeap:
    '''
    Transform list x into a heap, in-place, in linear time.
    '''
    n = len(arr)
    h = MinHeap(n)

    for i in range((n >> 1) - 1, -1, -1):
        sink(arr, i, n);

    h.arr = arr
    h.count = n

    return h

def lift(arr, i):
    '''
    Lift up value at index i
    '''
    while True:
        p = getparent(i)
        if p != i and arr[p] > arr[i]:
            arr[p],arr[i] = arr[i],arr[p]
            i = p
        else:
            break

def sink(arr, i, count):
    '''
    Push down arr[i] in arr[:count] boundary
    '''
    while True:
        '''
        Find if any children element is smaller than p
        '''
        smallest = i
        lt = getleft(i)
        if lt < count and arr[lt] < arr[smallest]: 
            smallest = lt
        rt = getright(i)
        if rt < count and arr[rt] < arr[smallest]: 
            smallest = rt

        if smallest == i:
            break

        arr[i],arr[smallest] = arr[smallest],arr[i]
        i = smallest

def getleft(i):
    '''
    Index of left child
    '''
    return (i << 1) + 1

def getright(i):
    '''
    Index of right child
    '''
    return (i + 1) << 1

def getparent(i):
    '''
    Index of parent
    '''
    return (i - 1) >> 1 if i != 0 else 0
        
class EuclideanWrapper:
    def __init__(self, point: List[int]):
        self.point = point
        self.length = point[0]**2 + point[1]**2
        
    def __lt__(self, that) -> bool:
        return self.length < that.length
    
    def __gt__(self, that) -> bool:
        return self.length > that.length
    
    def __eq__(self, that) -> bool:
        return self.length == that.length
    
    def __str__(self) -> str:
        return str(self.point) + ", " + str(self.length)
    
class Solution:
    '''
    Use my own implementation of heap
    '''
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        arr = [EuclideanWrapper(point) for point in points]
        
        heap = heapify(arr)
        
        # Need to find all points with same smallest distance!
        poped = []
        for i in range(K):
            poped.append(heap.pop().point)
 
        return poped



from heapq import heappush, heappop
class Solution:
    '''
    Use python's heap
    '''
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [] # max heap
        for p in points:
            d = p[0] * p[0] + p[1] * p[1]
            heappush(heap, (-d, p))
            if len(heap) > K:
                heappop(heap)
        
        # No order required for return
        return [point for _, point in heap]
