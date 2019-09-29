'''
170. Two Sum III - Data structure design
https://leetcode.com/problems/two-sum-iii-data-structure-design/

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
'''
from collections import Counter

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.book = Counter() 

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.book[number] += 1      

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        book = self.book
        for k in book.keys():
            m = value - k
            if m in book and (m != k or book[m] > 1):
                return True
