'''
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
    1 <= task.length <= 104
    tasks[i] is upper-case English letter.
    The integer n is in the range [0, 100].
'''
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], minGap: int) -> int:
        counter = Counter(tasks)
        
        # Get the most frequent task's count and how many such task is
        topTaskFrequency = 0
        topTaskRepeat = 0
        for frequency in counter.values():
            if frequency > topTaskFrequency:
                topTaskFrequency = frequency
                topTaskRepeat = 1
            elif frequency == topTaskFrequency:
                topTaskRepeat += 1

        # Assume 'A' is the top task, we want separate A as much as possible, like:
        # A .. A ... A 
        # Now figure out the how many gap needed:
        gapCount = topTaskFrequency - 1
        # If topTaskRepeat = 1, then minGap is the required gap width.
        # If more than 1 top tasks, the gap width can be smaller, like:
        # A B ... A B ... A B
        gapWidth = minGap - (topTaskRepeat - 1)
        # The slots needs to fill between top tasks
        slots = gapCount * gapWidth
        # Use other task to fill the slots
        idlesNeeded = max(0, slots - (len(tasks) - topTaskFrequency * topTaskRepeat))
        return len(tasks) + idlesNeeded