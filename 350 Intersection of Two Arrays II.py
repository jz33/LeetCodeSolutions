def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if len(nums1) > len(nums2):
        nums1,nums2 = nums2,nums1
    ref = {}
    for e in nums1:
        ref[e] = ref.get(e,0)+1
    res = []
    for e in nums2:
        if e in ref:
            c = ref[e]
            if c == 1:
                del ref[e]
            else:
                ref[e] = c - 1
            res.append(e)
    return res
