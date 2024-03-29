'''
40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''
class Solution:
    '''
    Similar idea to 90. Subsets II to avoid dups
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates) # {value : count}
        pool = []
        dp = [([], 0)] # [(combination, sum)]
        for value, count in counter.items():
            newDp = []
            for times in range(count + 1):
                # For each value, add [0,...,count] values
                for comb, total in dp:
                    newTotal = total + value * times
                    if newTotal == target:
                        # No need to append further values
                        pool.append(comb + [value] * times)
                    elif newTotal < target:
                        # Only keep looking if less than target
                        newDp.append((comb + [value] * times, newTotal))
            dp = newDp
        return pool
    
'''
Facebook interview questions: if exists a subsequence sum that equals target
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=1048003&page=1#pid19323052
'''
def subsequenceSum(nums: List[int], target: int) -> bool:
    if sum(nums) < target:
        # Assume all nums are positive, this is a quick check
        return False
    
    dp = {0} # {sums so far}
    for n in nums:
        # Add n to all v in dp
        newDp = set()
        for v in dp:
            total = v + n
            if total == target:
                return True
            elif total < target:
                newDp.add(total)
        # Expand dp, including all v (without n) and all v + n
        dp |= newDp
    return False

class Solution:
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:   
            # The DP matrix is same as Combination I, that
            # buf is a 3-D matrix. buf[i] contains all the combination sums to i
            # The correct matrix built-up of example [1,1,2,2], 4:
            # 1
            # [[[]], [[1]], [], [], [], [], []]
            # 1
            # [[[]], [[1]], [[1, 1]], [], [], [], []]
            # 2
            # [[[]], [[1]], [[1, 1], [2]], [[1, 2]], [[1, 1, 2]], [], []]
            # 2
            # [[[]], [[1]], [[1, 1], [2]], [[1, 2]], [[1, 1, 2], [2, 2]], [[1, 2, 2]], [[1, 1, 2, 2]]]

            buf = [[] for _ in range(target+1)]
            buf[0].append([])

            # Count inside an array how many element is equal to c from back
            # The arr here is ascending, and c should be the largest
            def countFromBack(arr: List[int], c: int) -> int:
                ct = 0
                for i in range(len(arr)-1, -1, -1):
                    if arr[i] == c:
                        ct += 1
                    else:
                        break
                return ct

            counter = Counter(candidates)   
            # Iterate different c
            for c,n in sorted(counter.items(), key = lambda p : p[0]):
                # Iterate same c, but different j
                for j in range(n):
                    # For first c, update buf[c], obviously;
                    # but for 2nd c, buf[c] till buf[2c] is already updated, so we move to 2c directly
                    for t in range(c + j * c, target+1):
                        # Now update buf[t] based on buf[t-c]
                        # Avoid duplicates here. There are 2 source of duplicates:
                        # 1: The duplicates generated in 4th for loop (the loop below),
                        # for example, c is added on buf[x], and on buf[x+c], c is used again;
                        # 2: The duplicates generated in 2nd for loop (when iterating c),
                        # for example, c is added on buf[x], and on buf[x] again (with different j), c is used again
                        for arr in buf[t-c]:
                            ct = countFromBack(arr, c)
                            # The arr of buf[t-c] we need here is the arr with exactly
                            # j number of c counted from back.
                            # If count of c is j + 1, it is just used in the 4th for loop;
                            # If count of c is less than j, it is already used in previous iteration of c, the 2nd for loop
                            # If count of c is j, then this arr is just generated from previous iteration of 2nd for loop, which is exactly what we need here.
                            if ct == j:
                                buf[t].append(arr + [c])
            return buf[target]
          
          

