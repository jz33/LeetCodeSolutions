import pprint
pp = pprint.PrettyPrinter(indent=4)

class Codec:
    '''
    Encode and Decode Strings
    https://leetcode.com/problems/encode-and-decode-strings/
    '''
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        buf = []
        for s in strs:
            buf.append(str(len(s)) + '*' +s)
        return ''.join(buf)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i = 0
        size = len(s)
        buf = []
        while i < size:
            p = s.index('*',i)
            l = int(s[i:p])
            buf.append(s[p+1:p+1+l])
            i = p+1+l
        return buf

sol = Codec()        
strs = [
    'abc',
    'er*wr',
    '***',
    ''
]
e = sol.encode(strs)
pp.pprint(e)
d = sol.decode(e)
pp.pprint(d)
    
