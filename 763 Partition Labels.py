class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        book = {} # {char : last appeared index}
        for i, c in enumerate(S):
            book[c] = i
        
        left = 0
        last = 0
        res = []
        for i,c in enumerate(S):
            last = max(last, book[c])                         
            if i == last:
                res.append(i - left + 1)
                left = i + 1
        return res
