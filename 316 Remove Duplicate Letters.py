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
        
        # Position of smallest char
        psc = 0 
        res = []
        i = 0
        while i < size:
            pc = ord(s[i]) - A
            
            # Current char is previously added
            if counter[pc] < 0:
                i += 1
                continue
            
            # If found a smaller char
            if pc < ord(s[psc]) - A:
                psc = i
            
            # Update counter as i move forward    
            counter[pc] -= 1
            
            if counter[pc] == 0:
                # Add to result and set invalid
                chosen = s[psc]
                counter[ord(chosen) - A] = - size
                res.append(chosen)
                
                # Move psc to valid position
                while psc < size and counter[ord(s[psc])-A] < 0:
                    psc += 1
                
                # Move i back so that psc == i
                while i >= psc:
                    counter[ord(s[i])-A] += 1
                    i -= 1
            i += 1
        return ''.join(res)
