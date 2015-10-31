# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1 : return -1
        cel = 0
        '''
        if i knows j, i cannot be celebrity
        if j knows i, j cannot be celebrity
        '''
        for i in xrange(1,n):
            if knows(cel,i):
            	cel = i
        '''
        Check whether cel does not know anyone previously
        '''
        for i in xrange(cel):
            if knows(cel,i):
                return -1
        '''
        Check whether anyone knows cel
        '''
        for i in xrange(n):
            if i != cel and not knows(i,cel):
                return -1
        return cel
