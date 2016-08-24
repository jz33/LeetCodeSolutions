'''
First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
'''
def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    size = len(s)
    ref = [size] * 26
    for i,c in enumerate(s):
        d = ord(c) - ord('a')
        ref[d] = i if ref[d] == size else size + 1
    m = min(ref)
    return m if m < size else -1


s = "itwqbtcdprfsuprkrjkausiterybzncbmdvkgljxuekizvaivszowqtmrttiihervpncztuoljftlxybpgwnjb"
print firstUniqChar(s)
h = s[61]
print h
print s.index(h),s.rindex(h)
