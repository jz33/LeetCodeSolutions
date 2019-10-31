class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), k*2):
            # Should be familiar with the slice tricks
            res.append(s[i : min(i+k, len(s))][::-1])
            # 2nd string can be null.
            res.append(s[min(i+k, len(s)) : min(i+k*2, len(s))])
        return ''.join(res)
