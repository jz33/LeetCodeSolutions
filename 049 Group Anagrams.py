PRIMES =[2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107]
A = ord('a')

def group(strs):
    ans = []
    map = {}
    for s in strs:
        hash = 1
        for e in s:
            hash *= PRIMES[ord(e) - A]
        if hash in map:
            map[hash].append(s)
        else:
            map[hash] = [s]
    
    for v in map.itervalues():
        ans.append(sorted(v))
        
    return ans
