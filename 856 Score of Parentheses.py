class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # The buf contains score at previous '('
        buf = [0] # for convenience
        for c in s:
            if c == '(':
                buf.append(0)
            else:
                # When buf[-1] = 0, it means it is a newly closed brackets
                ss = 1
                # Else, there are already a score on buf[-1], double it
                if buf[-1] != 0:
                    ss = buf[-1] * 2
                # Previous '(' must be pop
                buf.pop()
                # Save score to previous '('
                buf[-1] += ss
        
        return buf[0]
                    
