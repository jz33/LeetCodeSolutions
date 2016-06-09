def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ref = set(nums1)
    res = set()
    for e in nums2:
        if e in ref:
            res.add(e)
    return list(res)
