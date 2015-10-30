class Solution(object):
    def threeSumSmaller(self, arr, tag):
        count = 0
        arr.sort()
        for i in xrange(len(arr)):
            j = i + 1
            k = len(arr) - 1
            while j < k:
                if arr[i] + arr[j] + arr[k] < tag:
                    count += k - j
                    print i,j,k
                    j += 1
                else:
                    k -= 1
        return count
        
sol = Solution()
arr = [3,1,0,-2]
tag = 4
print sol.threeSumSmaller(arr,tag)
