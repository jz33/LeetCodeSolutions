
def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = map(lambda x : int(x), version1.split("."))
    v2 = map(lambda x : int(x), version2.split("."))
    
    while len(v1) < len(v2): v1.append(0)
    while len(v1) > len(v2): v2.append(0)
    
    for i in xrange(0,len(v1)):
      if v1[i] > v2[i]:
          return 1
      elif v1[i] < v2[i]:
          return -1
    return 0
