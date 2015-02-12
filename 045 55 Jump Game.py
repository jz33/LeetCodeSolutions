import random
'''
45 Jump Game II
https://oj.leetcode.com/problems/jump-game-ii/
55 Jump Game
https://oj.leetcode.com/problems/jump-game/
'''
def jumpGame2(ls):
    lt = 0
    rt = 0
    ctr = 0
    if len(ls) is 0 : return ctr
    while rt < len(ls) - 1:
        maxJump = rt
        for i in range(lt,rt+1):
            maxJump = max(maxJump,ls[i] + i)

        # happens when element in ls can <= 0
        if maxJump == rt: return -1
        
        lt = lt + 1
        rt = maxJump
        ctr += 1
    return ctr

def main():
    # ls = [2,3,1,1,4]
    
    ls = []
    n = 10
    for i in range(n):
        ls.append(random.randint(1,3))
    
    print ls
    print jumpGame2(ls)
    
if __name__ == "__main__":
    main()
