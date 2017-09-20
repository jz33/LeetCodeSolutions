def checkSubarraySum(nums, k):
      ref = {0:-1} # in case of [k,k],k
      s = 0
      for i,e in enumerate(nums):
          s += e
          if k != 0: 
              s %= k
          j = ref.get(s)
          if j is None:
              ref[s] = i
          elif i - j > 1:
              return True
      return False
