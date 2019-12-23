'''
1051. Height Checker
https://leetcode.com/problems/height-checker/

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.
(This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hs = sorted(heights) + [0]
        book = {hs[0] : [0, None]} # {height : [left index, right index]}
        for i in range(1, len(hs)):
            h = hs[i]
            p = hs[i-1]
            if h != p:
                book[p][1] = i-1
                book[h] = [i, None]
                
        return sum(not (book[h][0] <= i <= book[h][1]) for i, h in enumerate(heights))
