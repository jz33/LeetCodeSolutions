'''
Longest Substring with At Most K Distinct Characters My Submissions QuestionEditorial Solution
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
'''
def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if len(s) <= k: return len(s)
    j = 0
    maxSize = k
    #maxStr = ''
    ref = {}
    for i,c in enumerate(s):
        ref[c] = ref.get(c,0)+1
        while len(ref) > k:
            jc = s[j]
            v = ref.get(jc)
            if v == 1:
                del ref[jc]
            else:
                ref[jc] = v - 1
            j += 1
        if i + 1 - j > maxSize:
            maxSize = i + 1 - j
            #maxStr = s[j:i+1]
    #print maxStr
    return maxSize
