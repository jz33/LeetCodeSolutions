from typing import List

def sumSubarrayMins(A: List[int]) -> int:
    # Maintain a minList like B[(min0, count0), (min1, count1)...]
    # B can be expanded based on count, to M[min0, min0, min1, min1, min1,...]
    # Where each M[i] means the minimun of A[i : len(M)]
    # Therefore min1 > min0, and so on. 

    result = 0
    B = [] # [(value, count)]
    previousSum = 0

    for i, e in enumerate(A):
        count = 1
        while B and e <= B[-1][0]:
            previousMin, previousCount = B.pop()
            count += previousCount
            previousSum -= previousMin * previousCount

        B.append((e, count))
        previousSum = previousSum + e * count
        result += previousSum

    return result % (10**9 + 7)
