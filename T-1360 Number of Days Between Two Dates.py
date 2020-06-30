'''
1360. Number of Days Between Two Dates
https://leetcode.com/problems/number-of-days-between-two-dates/

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''
monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def daysFromStartOfYear(year: int, month: int, day: int) -> int:
    for m in range(1, month):
        if m == 2 and isLeapYear(year):
            day += 1
        day += monthDays[m]
    return day

def daysDiffOfTwoYears(year1: int, year2: int) -> int:
    '''
    year1 < year2
    '''
    days = 0
    for y in range(year1, year2):
        if isLeapYear(y):
            days += 366
        else:
            days += 365
    return days

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = [int(s) for s in date1.split('-')]
        y2, m2, d2 = [int(s) for s in date2.split('-')]
        if y1 == y2:
            return abs(daysFromStartOfYear(y1, m1, d1) - daysFromStartOfYear(y2, m2, d2))
        elif y1 < y2:
            return daysDiffOfTwoYears(y1, y2) + daysFromStartOfYear(y2, m2, d2) - daysFromStartOfYear(y1, m1, d1)
        else:
            return daysDiffOfTwoYears(y2, y1) + daysFromStartOfYear(y1, m1, d1) - daysFromStartOfYear(y2, m2, d2)
