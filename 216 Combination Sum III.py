class Solution:
    def combinationSum3(self, count: int, target: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        
        # The buf[t] is the list of all possible combination that sums to target
        buf = [[] for _ in range(target+1)]
        buf[0].append([])
    
        for c in candidates:
            for t in range(c, target+1):
                # Build buf[t] based on buf[t-c]
                for ls in buf[t-c]:
                    # Length check is the restriction of this problem
                    if len(ls) < count:
                        # Try to avoid using c more than once.
                        # If t-c < c, c is never used;
                        # Else, need to check if c is used
                        if t-c < c or c not in ls:
                            buf[t].append(ls + [c])

        return list(filter(lambda ls: len(ls) == count, buf[target]))
            
