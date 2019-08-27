class Solution:
    def checkValidString(self, s: str) -> bool:
        
        minL = 0 # Only count '(' as left
        maxL = 0 # Count '(' and '*' as left  
        
        for c in s:
            if c == '(':
                minL += 1
                maxL += 1
            elif c == ')':
                minL -= 1
                maxL -= 1
            else:
                minL -= 1
                maxL += 1
            
            # If total '(' + '*' is less than ')', it must be invalid
            if maxL < 0: return False
            
            # If left is exhausted, convert a '*' to '('
            minL = max(minL, 0)
        
        # There should not be outstanding '('
        return minL == 0
            
