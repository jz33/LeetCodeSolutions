'''
1146. Snapshot Array
https://leetcode.com/problems/snapshot-array/

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]

Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
'''
class SnapshotArray:
    def __init__(self, length: int):
        # Matrix of arrays, each stores (snap_id, value) tuples
        self.matrix = [[(-1,0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        arr = self.matrix[index]            
        arr.append((self.snap_id, val))

    def snap(self) -> int:
        r = self.snap_id
        self.snap_id += 1
        return r

    def get(self, index: int, snap_id: int) -> int:
        arr = self.matrix[index]
        
        # Search upper bound
        left = 0
        right = len(arr) - 1
        bound = 0
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= snap_id:
                bound = mid
                left = mid + 1        
            else:
                right = mid - 1
        
        return arr[bound][1]
