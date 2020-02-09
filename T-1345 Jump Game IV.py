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
Explanation: Start index is the last index. You don't need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Example 4:

Input: arr = [6,1,9]
Output: 2

Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
'''
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        book = defaultdict(list) # {value : [indexed]}
        for i, e in enumerate(arr):
            book[e].append(i)
            
        visited = [True] + [False] * (len(arr) - 1)
        queue = deque([0])
        steps = 1
        End = len(arr) - 1
        
        def push(i):
            nonlocal visited, queue
            visited[i] = True
            queue.append(i)
        
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                
                if visited[i+1] is False:
                    if i+1 == End:
                        return steps
                    push(i+1)
                
                if i > 0 and visited[i-1] is False:
                    push(i-1)
                    
                v = arr[i]
                for togo in book[v]:
                    if togo != i and visited[togo] is False:
                        if togo == End:
                            return steps
                        push(togo)
                        
                # Remove from map to improve performance
                book.pop(v) 
                
            steps += 1       
        return steps
                    
