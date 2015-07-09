import random
'''
169 Majority Element
https://oj.leetcode.com/problems/majority-element/
http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html#step13
'''
def creatRandomList(size):
    ls = []
    for i in range(0,size):
        ls.append(random.randint(0,size))
    return ls

def majorityElement(ls):
    if len(ls) == 1: return ls[0]

    major = ls[0]
    counter = 1
    for i in xrange(1,len(ls)):
        e = ls[i]
        if major == e:
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            major = e
            counter = 1
    return major        

    
ls = [3,2,3]
print ls
print majorityElement(ls)
