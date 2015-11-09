class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        oddy = 0
        map = {}
        for c in s:
            ctr = map.get(c,0)
            if ctr % 2 == 0:
                oddy += 1
            else:
                oddy -= 1
            map[c] = ctr + 1
        return oddy < 2
