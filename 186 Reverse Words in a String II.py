def reverseRange(ls,j,i):
    while j < i:
        ls[i],ls[j] = ls[j],ls[i]
        i -= 1
        j += 1
            
class Solution(object):
    def reverseWords(self, ls):
        ls.reverse()
        i = 0
        j = 0
        while i < len(ls):
            if ls[i] == ' ':
                reverseRange(ls,j,i-1)
                j = i + 1
            i += 1
        reverseRange(ls,j,i-1)
