import json

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        lt = 0
        obj = {"stops":[]}
        pos = 0
        total = 0
        for s in strs:
            for c in s:
                o = ord(c)
                ls = obj.get(o,[])
                ls.append(pos)
                obj[o] = ls
                pos += 1
            lt += len(s)
            obj["stops"].append(lt)
        return json.dumps(obj, ensure_ascii=False)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        obj = json.loads(s)
        stops = obj['stops']
        del obj['stops']
        if len(stops) == 0: return []
        ls = [''] * stops[-1]
        for k,v in obj.iteritems():
            c = unichr(int(k))
            for pos in v:
                ls[pos] = c
        res = []
        lt = 0
        for rt in stops:
            res.append(''.join(ls[lt:rt]))
            lt = rt
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
