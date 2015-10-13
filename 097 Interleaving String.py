'''
Interleaving String
https://leetcode.com/problems/interleaving-string/

The largest possible $prev:
10 : (0,10),(1,9),...(9,1),(10,0)
'''
def Interleaving(x, y, z):
    if len(x)+ len(y) != len(z): 
        return False
    prev = set() # Use list if needs to record answers
    prev.add((0,0))
    for e in z:
        next = set()
        for t in prev:
            if t[0] < len(x) and e == x[t[0]]:
                next.add((t[0]+1,t[1]))
            if t[1] < len(y) and e == y[t[1]]:
                next.add((t[0],t[1]+1))
        if len(next) == 0:
            return False 
        prev = next
        print prev
    return True
    
x = "aabcc"
y = "dbbca"
z = "aadbbcbcac"
print Interleaving(x,y,z)
