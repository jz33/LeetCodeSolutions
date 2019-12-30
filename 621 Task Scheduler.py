'''
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/

Given a char array representing tasks CPU need to do.
It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order. Each task could be done in one interval.
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Example 2:
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get sorted histogram
        ctr = collections.Counter(tasks)
        histo = sorted(ctr.values(), key = lambda x : -x)

        # So we separate top tasks, set each top task with at least
        # n empty slot to each other.
        # Then fill other tasks to the empty slots.
        topTaskCount = histo[0]
        emptySlots = (topTaskCount - 1) * n
        filled = 0
        for i in range(1, len(histo)):
            count = histo[i]
            filled += min(count, topTaskCount - 1)
            if filled >= emptySlots:
                break
        
        # If all empty slots are filled, no need for idle cycles
        # Otherwise, need idel cycles for the empty slots.
        return len(tasks) + max(0, emptySlots - filled)
