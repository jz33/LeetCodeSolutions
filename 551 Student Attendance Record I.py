'''
551. Student Attendance Record I
https://leetcode.com/problems/student-attendance-record-i/

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        ca = 0
        cl = 0
        for e in s:
            if e == 'A':
                ca += 1
                cl = 0
            elif e == 'L':
                cl += 1
            else:
                cl = 0
                
            if ca > 1 or cl > 2:
                return False
        
        return True
