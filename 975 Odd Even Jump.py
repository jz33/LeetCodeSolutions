class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        # Need to build 2 maps for odd/even jumps
        # oddyNext[i] gives the next index where i can jump to in odd jump
        N = len(A)

        # Build oddyNext in O(NlogN)
        oddyNext = [None] * N
        acsend_A = sorted(range(N), key = lambda x : A[x])
        stack = [] # The stack is decsending...
        for i in acsend_A:
            while stack and i > stack[-1]:
                j = stack.pop()
                # Current index is bigger than last index means
                # there is a valid odd jump from last index to current index
                # because the array is sorted, A[current] >= A[last]
                oddyNext[j] = i
            stack.append(i)
        # print(oddyNext)

        # Build evenNext
        evenNext = [None] * N
        decsend_A = sorted(range(N), key = lambda x : -A[x])
        stack = [] # The stack is asceding...
        for i in decsend_A:
            while stack and i > stack[-1]:
                j = stack.pop()
                # Current index is bigger than last index means
                # there is a valid event jump from last index to current index
                # because the array is reversely sorted, A[current] <= A[last]
                evenNext[j] = i
            stack.append(i)
        # print(evenNext)

        # Finally
        # oddyReachable[i] is True means oddyReachable[i] is a point where it can reach last index if this point is reached in odd jump
        oddyReachable = [False] * N
        evenReachable = [False] * N
        oddyReachable[-1] = True
        evenReachable[-1] = True

        for i in range(N-2, -1, -1):
            if oddyNext[i] is not None:
                oddyReachable[i] = evenReachable[oddyNext[i]]
            if evenNext[i] is not None:
                evenReachable[i] = oddyReachable[evenNext[i]]
b
        # print(oddyReachable)
        return sum(i for i in oddyReachable if i is True)
