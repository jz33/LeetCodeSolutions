'''
420. Strong Password Checker
https://leetcode.com/problems/strong-password-checker/

A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.

It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.

It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong,
assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input,
and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
'''
from heapq import heappush, heappop, heapify

class Solution:
    def getRepetitionCost(self, reps: List[int], toDelete: int) -> int:
        '''
        If password is longer than 20, some chars need to be deleted.
        To be greedy, delete chars on repetition substrings.
        Which repetition to delete?
        Notice eventually, the minimum cost to modify repetition strings
        to make them valid is sum(r // 3 for r in reps), therefore, 
        choose those whose mod % 3 value is closest to 0
        '''
        if not reps:
            return 0
        if len(reps) == 1:
            return (max(0, reps[0] - toDelete)) // 3
        
        heap = [(r % 3, r) for r in reps]
        heapify(heap)
        for _ in range(toDelete):
            if not heap:
                return 0
            _,r = heappop(heap)
            r -= 1
            if r >= 3:
                heappush(heap, (r % 3, r))
        return sum(r // 3 for _, r in heap)
            
    def strongPasswordChecker(self, s: str) -> int:
        # Parsing the string, get information
        counts = [0,0,0] # for lowerCount, upperCount, digitCount
        repCount, repChar = 0, None
        reps = [] # [repetion count]
        for i, e in enumerate(s):
            if e.isdigit():
                counts[0] += 1
            elif e.islower():
                counts[1] += 1
            elif e.isupper():
                counts[2] += 1

            if i == 0:
                repCount, repChar = 1, e
            elif e == repChar:
                repCount += 1
            else:
                if repCount >= 3:
                    reps.append(repCount)
                repCount, repChar = 1, e

        if repCount >= 3:
            reps.append(repCount)

        # Change count needed to add/modify for missing lower, upper, digit
        missed = sum(max(0, 1-c) for c in counts)

        size = len(s)
        if size <= 20:
            # Only add chars if size < 6, or modify or add
            # chars to break missings and repetitions
            breaks = sum(r // 3 for r in reps)
            return max(6 - size, missed, breaks)
        else:
            # Delete chars on repetitions
            toDelete = size - 20
            breaks = self.getRepetitionCost(reps, toDelete)
            return toDelete + max(breaks, missed)
