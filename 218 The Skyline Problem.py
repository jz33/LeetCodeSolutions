class MinHeap:
    '''
    A simple fixed-sized minimun binary heap implemented on array
    '''
    def __init__(self, capacity: int, comp: "less than comparator" = None):
        self.arr = [None] * capacity
        self.comp = comp
        self.count = 0

    def push(self, v):
        if self.count == len(self.arr):
            raise IndexError('')

        # Append to tail first
        self.arr[self.count] = v

        # Then lift up
        self.lift(self.count)

        self.count += 1

    def pop(self):
        if self.count < 1:
            raise IndexError('')

        self.count -= 1 
        ret = self.arr[0]

        # Move last element to top
        self.arr[0] = self.arr[self.count]
        self.arr[self.count] = None

        # Then sink it     
        self.sink(0)

        return ret

    def pushpop(self,v):
        if self.count < 1:
            raise IndexError('')

        top = self.arr[0]
        self.arr[0] = v
        self.sink(0)
        return top

    def top(self):
        if self.count < 1:
            raise IndexError('')

        return self.arr[0]

    def empty(self) -> bool:
        return self.count == 0

    def lift(self, i):
        '''
        Lift up value at i
        '''
        arr = self.arr

        while True:
            p = self.getParent(i)
            if p != i and self.lessThan(arr[i], arr[p]):
                arr[p],arr[i] = arr[i],arr[p]
                i = p
            else:
                break

    def sink(self, i):
        '''
        Push down value at i
        '''
        arr = self.arr
        count = self.count

        while True:
            '''
            Find if any children element is smaller than p
            '''
            smallest = i

            lt = self.getLeft(i)
            if lt < count and self.lessThan(arr[lt], arr[smallest]): 
                smallest = lt

            rt = self.getRight(i)
            if rt < count and self.lessThan(arr[rt], arr[smallest]):
                smallest = rt

            if smallest == i:
                break

            arr[i],arr[smallest] = arr[smallest],arr[i]
            i = smallest

    # Comparision helper
    def lessThan(self, a, b) -> bool:
        if self.comp:
            return self.comp(a, b)
        else:
            return a < b

    # Index helpers
    def getLeft(self, i):
        '''
        Get left child index of i
        '''
        return (i << 1) + 1

    def getRight(self, i):
        '''
        Get right child index of i
        '''
        return (i + 1) << 1

    def getParent(self, i):
        '''
        Get parent index of i
        If i is root or less then 0, return i
        '''
        return ((i - 1) >> 1) if i > 0 else i

# Not used
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

class BuildingWrapper:
    '''
    A wrapped-up class for heap usage
    '''
    def __init__(self, right, height):
        self.right = right
        self.height = height

    def __lt__(self, that) -> bool:
        # Revesed comparison, as Max Heap is needed
        return self.height > that.height

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        buidings: [[left, right, height]]
        '''
        size = len(buildings)      
        heap = MinHeap(size) # BuildingWrapper
        skyline = [] 

        i = 0      
        while i < size or not heap.empty():
            nextIndex = 0
            
            # 1. Need to push
            if heap.empty() or i < size and buildings[i][0] <= heap.top().right:
                nextIndex = buildings[i][0]

                # Push in all buildings with same left bound
                while i < size and buildings[i][0] == nextIndex:
                    heap.push(BuildingWrapper(buildings[i][1], buildings[i][2]))
                    i += 1
        
            # 2. Or need to pop
            else:
                nextIndex = heap.top().right
                # Pop all elements with right bound smaller or equal to "right"
                # Because they are no longer needed
                while not heap.empty() and heap.top().right <= nextIndex:
                    heap.pop()

            height = 0 if heap.empty() else heap.top().height

            # Do not add duplicate height
            if len(skyline) == 0 or height != skyline[-1][1]:
                skyline.append([nextIndex, height])

        return skyline

# Test cases
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
[[2,9,10],[9,12,15]]
[[1,2,1],[1,2,2],[1,2,3]]
[[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]]
