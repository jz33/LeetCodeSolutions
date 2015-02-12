'''
87 Scramble String
https://oj.leetcode.com/problems/scramble-string/
O(3^n)
'''
def isScramble(s0,s1):
    if len(s0) != len(s1): return False
    if s0 == s1: return True
    size = len(s0)
    
    ts0 = ''.join(sorted(s0))
    ts1 = ''.join(sorted(s1))
    if ts0 != ts1: return False

    for i in range(1,size):
        lt0 = s0[:i]
        rt0 = s0[i:]
        lt1 = s1[:i]
        rt1 = s1[i:]
        if isScramble(lt0,lt1) and isScramble(rt0,rt1):
            return True
        lt1 = s1[size - i:]
        rt1 = s1[:size - i]
        if isScramble(lt0,lt1) and isScramble(rt0,rt1):
            return True
    return False

def main():
    s0 = r'rgtae'
    s1 = r'great'
    print isScramble(s0,s1)
    
if __name__ == "__main__":
    main()
