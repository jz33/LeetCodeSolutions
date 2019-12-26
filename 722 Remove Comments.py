/*
722. Remove Comments
https://leetcode.com/problems/remove-comments/

Remove c++ line comments ("//") and block comments ("/*...*/")
*/
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        buffer = []
        isInBlockComment = False
        for line in source:
            i = 0
            while i < len(line):
                c = line[i]
                if isInBlockComment:
                    # If in block comment, only care about */
                    if c == '*' and (i+1) < len(line) and line[i+1] == '/':
                        isInBlockComment = False
                        i += 1
                else:
                    if c == '/' and (i+1) < len(line) and line[i+1] == '*':
                        isInBlockComment = True
                        i += 1
                    elif c == '/' and (i+1) < len(line) and line[i+1] == '/':
                        break
                    else:
                        buffer.append(c)
                i += 1
            
            if buffer and not isInBlockComment:
                result.append(''.join(buffer))
                buffer = []
                
        return result
