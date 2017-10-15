from collections import deque
'''
207 Course Schedule
https://leetcode.com/problems/course-schedule/
'''
def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    parents = [0] * numCourses # parents count
    graph = {} # parent : set(children)
    
    # parse
    for pair in prerequisites:
        c = pair[0] # child
        p = pair[1] # parent
        cs = graph.get(p,set())
        cs.add(c)
        graph[p] = cs
        parents[c] += 1
    
    # entries nodes who have no parents
    entries = [i for i in xrange(numCourses) if parents[i] == 0]

    # DFS
    dq = deque()
    dq.extend(entries)   
    reached = len(dq)
    while len(dq) > 0:
        p = dq.popleft()
        cs = graph.get(p,set())
        for c in cs:
            if parents[c] == 1: # ready to take
                dq.append(c)
                reached += 1
            else:
                parents[c] -= 1

    return reached == numCourses


numCourses = 2
prerequisites = [[0,1]]

print canFinish(numCourses, prerequisites)
