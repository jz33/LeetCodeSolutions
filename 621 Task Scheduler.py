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
Explanation: A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle.
'''
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get sorted histogram
        ctr = Counter(tasks)
        histo = sorted(ctr.values(), key = lambda x : -x)

        # 1. About top n + 1 tasks, they might need idle cycle
        idles = 0
        top = histo[0]
        for i in range(1, n+1):
            ci = histo[i] if i < len(histo) else 0
            diff = top - ci
            if diff > 0:
                idles += diff - 1

        # 2. However, histo[n+1:] tasks are free to schedule,
        # therefore scheudle them to idle slots
        return len(tasks) + max(0, idles - sum(histo[n+1:]))
