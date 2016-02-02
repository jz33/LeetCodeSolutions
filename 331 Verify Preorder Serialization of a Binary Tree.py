def isValidSerialization(preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    arr = preorder.split(',')
    if len(arr) == 0: return True
    stack = 0
    for i in xrange(len(arr)-1):
        if arr[i] == '#':
            if stack == 0: return False
            stack -= 1
        else:
            stack += 1
    return arr[-1] == '#' and stack == 0
