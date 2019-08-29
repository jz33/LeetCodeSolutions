'''
Combination Sum IV
https://leetcode.com/problems/combination-sum-iii/
'''
def combinationSum4(candidates: List[int], target: int) -> int:
    buf = [0] * (target+1) # buf[t] means how many combinations when target equals t
    buf[0] = 1

    # Loop range, then loop candidates
    # If loop candidates first, it becomes Combindation Sum I
    for t in range(target+1):
        for c in candidates:
            if t - c >= 0:
                buf[t] += buf[t-c]

    return buf[target]
