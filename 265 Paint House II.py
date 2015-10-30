'''
Paint House II
https://leetcode.com/problems/paint-house-ii/
'''
def minCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    H = len(costs)
    if H == 0: return 0
    C = len(costs[0])
    if C == 0: return 0
    if C == 1:
        return costs[0][0] if H == 1 else 0
    
    # buffer for colors of 1 house
    row = [0 for i in xrange(C)]
    min1 = 0 # smallest index
    min2 = 1 # second smallest index, must be different of min1
    for i in xrange(C):
        row[i] = costs[0][i]
        if i == 1:
            # check if row[min1] < row[min2]
            if row[min1] > row[min2]:
                min1, min2 = min2, min1
        elif i > 1:
            if row[i] < row[min2]:
                if row[i] < row[min1]:
                    min2 = min1
                    min1 = i
                else:
                    min2 = i
    print row, min1, min2
                
    for j in xrange(1,H):
        newRow = [0 for i in xrange(C)]
        newMin1 = 0
        newMin2 = 1
        for i in xrange(C):
            # greedy, choose smallest cost of previous
            if i != min1:
                newRow[i]  = row[min1] + costs[j][i]
            # if house index is same, choose second smallest
            else:
                newRow[i]  = row[min2] + costs[j][i]
            
            if i == 1:
                if newRow[newMin1] > newRow[newMin2]:
                    newMin1, newMin2 = newMin2, newMin1
            elif i > 1:
                if newRow[i] < newRow[newMin2]:
                    if newRow[i] < newRow[newMin1]:
                        newMin2 = newMin1
                        newMin1 = i
                    else:
                        newMin2 = i
        row = newRow
        min1 = newMin1
        min2 = newMin2
        print row, min1, min2
        
    return row[min1]
'''   
costs = [
    [17,2,17],
    [16,16,5],
    [14,3,19]
]
'''
costs = [
    [3,5,3],
    [6,17,6],
    [7,13,18],
    [9,10,18]
]

print minCost(costs)
