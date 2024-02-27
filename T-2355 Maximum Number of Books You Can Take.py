'''
2355. Maximum Number of Books You Can Take
https://leetcode.com/problems/maximum-number-of-books-you-can-take/

You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on the ith shelf of a bookshelf.

You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n. For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.

Return the maximum number of books you can take from the bookshelf.

Example 1:

Input: books = [8,5,2,7,9]
Output: 19
Explanation:
- Take 1 book from shelf 1.
- Take 2 books from shelf 2.
- Take 7 books from shelf 3.
- Take 9 books from shelf 4.
You have taken 19 books, so return 19.
It can be proven that 19 is the maximum number of books you can take.

Example 2:

Input: books = [7,0,3,4,5]
Output: 12
Explanation:
- Take 3 books from shelf 2.
- Take 4 books from shelf 3.
- Take 5 books from shelf 4.
You have taken 12 books so return 12.
It can be proven that 12 is the maximum number of books you can take.

Example 3:

Input: books = [8,2,3,7,3,4,0,1,4,3]
Output: 13
Explanation:
- Take 1 book from shelf 0.
- Take 2 books from shelf 1.
- Take 3 books from shelf 2.
- Take 7 books from shelf 3.
You have taken 13 books so return 13.
It can be proven that 13 is the maximum number of books you can take.

Constraints:
    1 <= books.length <= 105
    0 <= books[i] <= 105
'''
class Solution:
    '''
    Monotonic stack. LTE
    '''
    def maximumBooks(self, books: List[int]) -> int:
        stack = [books[0]] # book count array, monotonically increasing
        total = books[0]
        result = total

        def rebuildStack(currBookCount: int):
            '''
            Rebuild the stack when encounters a smaller element.
            Notice there are 3 possible terminal scenarios
            '''
            nonlocal stack, total
            smallerCount = currBookCount - 1 # how many previous book should pick
            newTotal = 0 # total of newly updated elements
            reduced = 0 # how many books reduced
            for i in range(len(stack)-1,-1,-1):
                if smallerCount <= 0:
                    # Case 1: no books are picked in [:i]
                    # Example: [4,5] + 2
                    stack = stack[i+1:]
                    total = newTotal
                    return
                
                prevBookCount = stack[i]
                if smallerCount >= prevBookCount:
                    # Case 2: can keep using all previous results. Done
                    # Example: [1,4,7] + 6
                    total -= reduced
                    return
                else:
                    # Update current book count. Keep going
                    stack[i] = smallerCount
                    reduced += prevBookCount - smallerCount
                    newTotal += smallerCount
                    smallerCount -= 1
            # Case 3: neither of above
            # Example: [5,6,7] + 4
            total = newTotal

        for i in range(1, len(books)):
            currBookCount = books[i]
            if currBookCount <= books[i-1]:
                rebuildStack(currBookCount)

            # Pick all books in current self
            stack.append(currBookCount)
            total += currBookCount
            result = max(result, total)
        return result
