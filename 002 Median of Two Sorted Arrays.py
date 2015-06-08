import random
'''
02 Median of Two Sorted Arrays
https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).
'''
# generate a random int array with limits [a,b]
def createRandList(n,a,b):
    A = []
    for i in range(n):
        A.append(random.randint(a,b))
    return A

# if an int is even
def isEven(i):
    return True if i&1 == 0 else False

# merge 2 sorted lists
def mergeTwoSorted(A,B):
    if len(A) == 0:
        return B
    if len(B) == 0:
        return A
    
    C = []   
    i = 0
    j = 0
    while i< len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i< len(A):
        C.append(A[i])
        i += 1
    while j< len(B):
        C.append(B[j])
        j += 1
    return C
'''
median of a sorted list
'''
def medianSorted(A,s,l):
    if l & 1 == 0:
        return (float(A[(l>>1)+s]) + float(A[(l>>1)+s-1])) / 2.0
    else:
        return A[(l>>1)+s]
    
def medianTwoSortedRec(A, sa, la, B, sb, lb):
    # bottom case, use lasy approach
    if (la >=0 and la < 3) or (lb >= 0 and lb < 3):
        C = mergeTwoSorted(A,B)
        return medianSorted(C,0,len(C))
    
    # compute possible cut range length
    ca = (la>>1)-1 if isEven(la) else la>>1
    cb = (lb>>1)-1 if isEven(lb) else lb>>1
    c = min(ca,cb)
    ma = medianSorted(A,sa,la)
    mb = medianSorted(B,sb,lb)
    if ma < mb:
        return medianTwoSortedRec(A,sa+c,la-c,B,sb,lb-c)
    else:
        return medianTwoSortedRec(A,sa,la-c,B,sb+c,lb-c)
            
def medianTwoSorted(A, B):
    return medianTwoSortedRec(A,0,len(A),B,0,len(B))
    
def main():
    repeat = 5
    for i in range(repeat):
        n = i+5
        A = createRandList(n,i*2,(i+n)*2)
        B = createRandList(n+1,i*2,(i+n)*2)
        A.sort()
        B.sort()
        print A
        print B
        print medianTwoSorted(A,B)
        
        #test
        C = mergeTwoSorted(A,B)
        print C
        print medianSorted(C,0,len(C))

if __name__ == "__main__":
    main()
