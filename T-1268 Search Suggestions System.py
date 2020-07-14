'''
268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/

Given an array of strings products and a string searchWord.
We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
'''
class Solution:
    def lowerBound(self, arr: List[str], target: str):
        bound = None
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid].startswith(target) or target < arr[mid]:
                bound = mid
                right = mid - 1
            else:
                left = mid + 1
        return bound
        
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ''
        startIndex = 0 # if startIndex is None, no more suggestions
        for c in searchWord:
            if startIndex is None:
                res.append([])
            else:
                prefix += c
                startIndex = self.lowerBound(products, prefix)
                if startIndex is None:
                    res.append([])
                else:
                    res.append([s for s in products[startIndex : startIndex + 3] if s.startswith(prefix)])
        return res
