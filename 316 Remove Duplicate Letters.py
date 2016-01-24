class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        A = ord('a')
        
        # Build char counter array
        counter = [0]*26
        for ch in s:
            counter[ord(ch) - A] += 1
        
        stack = []
        added = set()
        for i,c in enumerate(s):
            if c not in added:
                # If current char is smaller than top char and top char is not the last one
                while len(stack) > 0 and stack[-1] > c and counter[ord(stack[-1])-A] > 0:
                    added.remove(stack[-1])
                    stack.pop()
                stack.append(c)
                added.add(c)
            counter[ord(c) - A] -= 1
        return ''.join(stack)
