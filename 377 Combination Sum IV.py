'''
Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
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
