'''
1105. Filling Bookcase Shelves
https://leetcode.com/problems/filling-bookcase-shelves/

We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

We want to place these books in order onto bookcase shelves that have total width shelf_width.

We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width),
then build another level of shelf of the bookcase so that the total height of the bookcase has increased by
the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

Note again that at each step of the above process, the order of the books we place is the same order as
the given sequence of books.  For example, if we have an ordered list of 5 books,
we might place the first and second book onto the first shelf, the third book on the second shelf,
and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Example 1:

Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
'''
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:      
        # dp[i] is the minimun total heights after put in i books
        dp = [0] * (len(books)+1)
        
        for i in range(len(books)):
            width = books[i][0]
            height = books[i][1]
            
            # Put books[i] into a new row
            dp[i+1] = dp[i] + height
            
            # Or try squeeze previous books together
            for j in range(i-1,-1,-1):
                if books[j][0] + width > shelf_width:
                    break
                width += books[j][0]
                height = max(height, books[j][1])
                dp[i+1] = min(dp[i+1], height + dp[j])
        
        return dp[-1]
