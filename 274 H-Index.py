'''
274. H-Index
https://leetcode.com/problems/h-index/

Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have at least h citations each,
and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
    
Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        right = len(citations)
        left = 0
        hIndex = -1
        while left <= right:
            h = left + (right - left) // 2          
            moreThan = sum(c >= h for c in citations)
            lessThan = sum(c <= h for c in citations)
            
            '''
            This question description should be clearer.
            There can be more than h paper whose citation is at least h,
            similary there can be more than h paper whose citation is equal or less than h
            '''
            if moreThan >= h:
                if lessThan >= len(citations) - h:
                    hIndex = h
                left = h + 1
            else:
                right = h - 1
                
        return hIndex
