from collections import Counter
'''
149 Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/
'''
INFINITE = 'infinite'

def maxPoints(self, points):
    ret = 1
    for p in points:
        duplicates = 0
        ctr = Counter()
        for q in points:
            x = q.x - p.x
            y = q.y - p.y
            if x == 0 and y == 0:
                duplicates += 1
            if x == 0:
                ctr[INFINITE] += 1
            else:
                ctr[float(y)/x] += 1
        ctr[INFINITE] -= duplicates
        ret = max(ret, duplicates + max(ctr.values()))
    return ret
