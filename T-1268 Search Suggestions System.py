class Solution:
    def lowerBound(self, arr: List[str], startIndex: int, target: str):
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
                startIndex = self.lowerBound(products, startIndex, prefix)
                if startIndex is None:
                    res.append([])
                else:
                    res.append([s for s in products[startIndex : startIndex + 3] if s.startswith(prefix)])
        return res
