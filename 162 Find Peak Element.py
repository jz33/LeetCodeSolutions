'''
162 Find Peak Element
https://oj.leetcode.com/problems/find-peak-element/

Using 2 stacks
'''  
def peak(ls, lt, rt, ret):
    if lt <= rt and len(ret) == 0:
        mid = (lt+rt)>>1
        if (mid == len(ls)-1 and ls[mid] > ls[mid-1]) or \
           (mid == 0 and ls[mid] > ls[mid+1]) or \
           (ls[mid] > ls[mid-1] and ls[mid] > ls[mid+1]):
            ret.append(mid)
        else:
            peak(ls,lt,mid-1,ret)
            peak(ls,mid+1,rt,ret)

def main():
    ls = [0,1,2,3,4,3,2,1,2,1] # 4,2
    ret = [] # mutable list can be passed by reference
    peak(ls,0,len(ls)-1,ret)
    print ret
    
if __name__ == "__main__":
    main()
