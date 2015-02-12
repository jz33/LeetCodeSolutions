import random
'''
169 Majority Element
https://oj.leetcode.com/problems/majority-element/
http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html#step13
'''
INVALID = -1

def creatRandomList(size):
    ls = []
    for i in range(0,size):
        ls.append(random.randint(0,size))
    return ls

def majorityElement(ls):
    global INVALID
    if len(ls) < 2: return ls[0]

    # assign 'major' an invalid value
    major = INVALID
    counter = 0
    for e in ls:
        if major == INVALID:
            major = e
            counter = 1
        elif major == e:
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            major = INVALID
    return major        
        
def main():
    ls = creatRandomList(15)
    print ls
    print majorityElement(ls)

if __name__ == "__main__":
    main()
