'''
Jump Game I
https://leetcode.com/problems/jump-game/
'''
def canJump(self, arr):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(arr) == 0: return True
    lt = 0
    rt = lt + arr[lt]
    while rt < len(arr) and lt <= rt:
        if rt < lt + arr[lt]:
            rt = lt + arr[lt]
        lt += 1
    return rt >= len(arr) - 1
