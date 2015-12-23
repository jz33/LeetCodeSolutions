def hash(word):
    l = len(word)
    if l == 0: return 0
    elif l == 1: return ord(word[0])
    elif l == 2: return ord(word[0]) * 100 + ord(word[-1])
    else: return l * 10000 + ord(word[0]) * 100 + ord(word[-1])

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        m = {}
        for word in dictionary:
            h = hash(word)
            s = m.get(h,set())
            s.add(word)
            m[h] = s
        self.m = m

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        h = hash(word)
        m = self.m
        return h not in m or len(m[h]) == 1 and word in m[h]

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
