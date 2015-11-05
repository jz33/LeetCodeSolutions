'''
Remove Invalid Parentheses
https://leetcode.com/problems/remove-invalid-parentheses/
https://leetcode.com/discuss/67908/java-bfs-solution-16ms-avoid-generating-duplicate-strings
'''
class Solution(object):
    def isValid(self,s):
        ctr = 0
        for ch in s:
            if ch == '(': ctr += 1
            elif ch == ')': ctr -= 1
            if ctr < 0: return False
        return ctr == 0
    
    def trim(self,ls):
        length = len(ls)
        i = 0
        while i < length and ls[i] == ')': i += 1
        ls = ls[i:]
        length = len(ls)
        i = length - 1
        while i > -1 and ls[i] == '(': i -= 1
        return ls[:i+1]
    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ls = self.trim(list(s))
        if self.isValid(ls): return [''.join(ls)]

        ans = []        
        # The queue only contains invalid middle steps
        queue = []
        # The 3-Tuple is (string, startIndex, lastRemovedChar)
        queue.append((ls, 0, ')'))
        while len(queue) > 0:
            (ls,start,removed) = queue.pop(0)
            
            # Observation 2, start from last removal position
            for i in xrange(start,len(ls)):
                ch = ls[i]
                if ch != '(' and ch != ')': continue
                # Observation 1, do not repeatedly remove from consecutive parentheses
                if i != start and ls[i-1] == ch: continue            
                #Observation 3, do not remove a pair of valid parentheses
                if removed == '(' and ch == ')': continue
                
                ls2 = ls[:i] + ls[i+1:]
                if self.isValid(ls2):
                    ans.append(''.join(ls2))                   
                # Avoid adding children
                elif len(ans) == 0:
                    queue.append((ls2, i, ch));
        return ans
        
sol = Solution()
s = "a"
r = sol.removeInvalidParentheses(s)
print r


