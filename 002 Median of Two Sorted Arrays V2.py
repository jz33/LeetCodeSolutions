import random

class Solution(object):
    def __init__(self):
        self.debug = False

    def median(self,s,l,nums):
        '''
        l > 0
        '''
        if (l & 1) == 0:
            return (float(nums[(l>>1)+s]) + float(nums[(l>>1)+s-1])) / 2.0
        else:
            return nums[(l>>1)+s]
        
    def base(self,s1,l1,nums1,s2,l2,nums2):
        '''
        l1 > 0 && l2 > 0. 1 is smaller array
        '''
        if l1 == 1:
            a = nums1[s1]
            if l2 == 1:
                return (float(a) + float(nums2[s2]) ) / 2.0
            elif l2 == 2:
                b = nums2[s2]
                c = nums2[s2+1]
                if a <= b: return b
                elif a <= c : # b < a <= c
                    return a
                else:
                    return c
            else:
                if (l2 & 1) == 1: # l2 is oddy
                    b = nums2[(l2>>1)+s2]
                    c = nums2[(l2>>1)+s2+1] # right next of b
                    d = nums2[(l2>>1)+s2-1] # left next of b 
                    if a > c:
                        return (float(b) + float(c)) / 2.0
                    elif a < d:
                        return (float(b) + float(d)) / 2.0
                    else:
                        return (float(b) + float(a)) / 2.0
                else:
                    b = nums2[(l2>>1)+s2-1] # middle left
                    c = nums2[(l2>>1)+s2] # middle right
                    if a < b: return b
                    elif a > c: return c
                    else: return a
        else: # l1 == 2, too complicated
            s = sorted(nums1[s1:s1+l1]+nums2[s2:s2+l2])
            return self.median(0,len(s),s)
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums2) == 0: return 0
        elif len(nums1) == 0:
            return self.median(0,len(nums2),nums2)
        elif len(nums2) == 0:
            return self.median(0,len(nums1),nums1)
    
        s1 = 0 # start point
        l1 = len(nums1) # length
        s2 = 0
        l2 = len(nums2)
        
        while True:
            if l1 < 3:
                if self.debug: 
                    print "base:"
                    print nums1[s1:s1+l1]
                    print nums2[s2:s2+l2]
                return self.base(s1,l1,nums1,s2,l2,nums2)
            elif l2 < 3:
                if self.debug: 
                    print "base:"
                    print nums1[s1:s1+l1]
                    print nums2[s2:s2+l2]
                return self.base(s2,l2,nums2,s1,l1,nums1)
            else:
                c1 = (l1 >> 1) if (l1 & 1) else (l1 >> 1) - 1
                c2 = (l2 >> 1) if (l2 & 1) else (l2 >> 1) - 1
                cm = min(c1,c2)
                m1 = self.median(s1,l1,nums1)
                m2 = self.median(s2,l2,nums2)
                if self.debug:
                    print m1,m2,c1,c2,cm
                    print nums1[s1:s1+l1]
                    print nums2[s2:s2+l2]
                if m1 < m2:
                    s1 += cm
                else:
                    s2 += cm
                l1 -= cm
                l2 -= cm
                

def HardCodedTest(sol,mat):
    for nums1,nums2 in mat:
        print sol.findMedianSortedArrays(nums1,nums2),
        s = sorted(nums1 + nums2)
        print sol.median(0,len(s),s)

def RandomTest(sol):
    a = 0
    b = 10
    for _ in xrange(50):
        l1 = random.randint(a,b)
        nums1 = sorted([random.randint(0,100) for _ in xrange(l1)])
        l2 = random.randint(a,b)
        nums2 = sorted([random.randint(0,100) for _ in xrange(l2)])
        s = sorted(nums1 + nums2)
        expected = 0 if len(s) == 0 else sol.median(0,len(s),s)
        actual = -1
        try:
            actual = sol.findMedianSortedArrays(nums1,nums2)
            if expected != actual:
                sol.debug = True
                sol.findMedianSortedArrays(nums1,nums2)
                break
        except Exception, e:
            print str(e)
        finally:
            if expected != actual:
                print actual,expected
                print nums1
                print nums2
                print s

mat = [\
([10],[11]),\
([10],[11,12]),\
([10],[9,12]),\
([10],[8,9]),\
([11],[8,9,10]),\
([7],[8,9,10]),\
([9.5],[8,9,10]),\
([9.5],[8,9,10,11]),\
([10.5],[8,9,10,11]),\
([8.5],[8,9,10,11]),\
([8,12],[8,9,10]),\
([8,8.5],[8,9,10]),\
([9.5,9.5],[8,9,10]),\
([2,8.5],[8,9,10,11]),\
([2,9.5],[8,9,10,11]),\
([9.2,9.5],[8,9,10,11]),\
([9.2,15],[8,9,10,11]),\
([10.2,10.5],[8,9,10,11]),\
]

sol = Solution()
HardCodedTest(sol,mat)
RandomTest(sol)

