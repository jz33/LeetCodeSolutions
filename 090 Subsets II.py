from copy import deepcopy
'''
Subsets II
https://oj.leetcode.com/problems/subsets-ii/
'''
pool = []

def combinationsRec(input, sofar, repeat):
    global pool
    if len(sofar) ==  repeat:
        pool.append(deepcopy(sofar))
    else:
        for i in xrange(0,len(input)):
	    
            # An important check to reduce branching
            if len(sofar) + len(input) - i < repeat: break;
            
            # Avoid duplicates
            if i > 0 and input[i] == input[i-1]: 
                continue;

            sofar.append(input[i]);
            combinationsRec(input[i+1:], sofar, repeat);
            sofar.pop();
			
def subsetsWithDup(input):
    global pool
    del pool[:]
    
    input.sort()
    sofar = []
    for i in xrange(0,len(input)+1):
        combinationsRec(input,sofar,i);
    return pool

input = [1,2,2]
subsetsWithDup(input);
print pool
