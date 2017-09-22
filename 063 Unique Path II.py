'''
063 Unique Path II.py
Shorter DP approach
'''
 def uniquePathsWithObstacles(obstacleGrid):
      """
      Try to understand why only 1-D buf is good enough
      """
      width = len(obstacleGrid[0])
      buf = [0]*width
      buf[0] = 1
      for row in obstacleGrid:
          for j in xrange(width):
              if row[j] == 1:
                  buf[j] = 0
              elif j > 0:
                  buf[j] += buf[j-1] # from left + up
      return buf[width-1]
