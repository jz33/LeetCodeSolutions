'''
1345. Jump Game IV
https://leetcode.com/problems/jump-game-iv/

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Constraints:
    1 <= arr.length <= 5 * 104
    -108 <= arr[i] <= 108
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        valueToIndexes = {}
        for i, e in enumerate(arr):
            # Avoid continuous duplicates, like 3 7 7 7 8, the middle 7 is meaningless
            if i > 0 and e == arr[i-1] and i < len(arr) - 1 and arr[i+1] == e:
                continue
            valueToIndexes[e] = valueToIndexes.get(e, []) + [i]
            
        visited = [True] + [False] * (len(arr) - 1)
        queue = [0]
        steps = 1

        def push(i: int, newQueue: List[int]) -> bool:
            '''
            Push-in new index. Check if reached end.
            '''
            if i == len(arr) - 1:
                return True
            newQueue.append(i)
            visited[i] = True

        while queue:
            newQueue = []
            for i in queue:            
                if visited[i+1] is False:
                    if push(i+1, newQueue):
                        return steps
                
                if i > 0 and visited[i-1] is False:
                    if push(i-1, newQueue):
                        return steps
                    
                val = arr[i]
                for togo in valueToIndexes.get(val, []):
                    if togo != i and visited[togo] is False:
                        if push(togo, newQueue):
                            return steps
                        
                # Remove from map to improve performance
                valueToIndexes.pop(val, None) 
                
            steps += 1
            queue = newQueue
             
        return steps