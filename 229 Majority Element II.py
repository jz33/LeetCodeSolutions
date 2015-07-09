'''
Majority Element II
https://leetcode.com/problems/majority-element-ii/
'''
def majorityElement(ls):
    if len(ls) == 1: return [ls[0]]
    
    # There are at most 2 this kinda elements
    major = []
    counter = [0,0]
    for i in xrange(0,len(ls)):
        e = ls[i]
        if counter[0] > 0 and counter[1] > 0:
            if e == major[0]:
                counter[0] += 1
            elif e == major[1]:
                counter[1] += 1
            else:
                counter[0] -= 1
                counter[1] -= 1
        elif counter[0] > 0:
            if e == major[0]:
                counter[0] += 1
            else:
                if len(major) == 1:
                    major.append(e)
                else: 
                    major[1] = e
                counter[1] = 1
        elif counter[1] > 0:
            if e == major[1]:
                counter[1] += 1
            else:
                major[0] = e
                counter[0] = 1
        else:
            if len(major) == 0:
                major.append(e)
                counter[0] = 1
            elif len(major) == 1:
                if e == major[0]:
                    counter[0] = 1
                else:
                    major.append(e)
                    counter[1] = 1
            else:
                if e == major[0]:
                    counter[0] = 1
                elif e == major[1]:
                    counter[1] = 1
                else:
                    major[0] = e 
                    counter[0] = 1
                
        print major,counter
    
    ret = []
    for m in major:
        ctr = 0
        for e in ls:
            if e == m:
                ctr += 1
            if ctr > len(ls) / 3:
                ret.append(m)
                break
    
    return ret        

    
#ls = [1,1,3,1,2,2,2,3,1,3,3]
ls = [0,-1,2,-1]
print ls
print majorityElement(ls)
