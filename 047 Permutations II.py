from copy import deepcopy
'''
Permutation II
https://leetcode.com/problems/permutations-ii/

A backtracking permutation implementation without duplicates
'''
pool = []

def permutationRec(input, sofar, repeat):
    global pool
    if len(sofar) ==  repeat:
        pool.append(deepcopy(sofar))
    else:
        for i in xrange(0,len(input)):

            # Avoid duplicates
            if i > 0 and input[i] == input[i-1]: 
                continue;

            sofar.append(input[i]);
            permutationRec(input[:i]+input[i+1:], sofar, repeat);
            sofar.pop();

def permuteUnique(input):
    global pool
    del pool[:]
    
    input.sort()
    sofar = []
    permutationRec(input,sofar,len(input));
    return pool
        
