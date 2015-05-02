import random
'''
02 Median of Two Sorted Arrays
https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''
'''
sa : starting index of array A
ea : ending index of array A
la : left index limit of elimination, const
ra : right index limit of elimination, const

obviously, if(len(A)%2 == 1) la==ra
'''
# if an int is even
def isEven(i):
    return True if i&1 == 0 else False

# generate a random int array with limits [a,b]
def createRandList(n,a,b):
    A = []
    for i in range(n):
        A.append(random.randint(a,b))
    return A

# merge 2 sorted lists
def mergeTwoSorted(A,B):
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
median of a sorted int list
s: staring index
l: length
'''
def medianSorted(A,s,l):
    if isEven(l):
        return A[(l>>1)+s] + A[(l>>1)+s-1] >>1
    else:
        return A[(l>>1)+s]

# median of a sorted int list plus 1 extra element
def medianSortedPlus1(A,s,l,one):
    if isEven(l):
        ml = A[(l>>1)+s-1]
        mr = A[(l>>1)+s]
        if one < ml : return ml
        elif one > mr : return mr
        else : return one
    else:
        if l == 1:
            return A[s]+one >>1
        else:
            ml = A[(l>>1)+s-1]
            mm = A[(l>>1)+s]
            mr = A[(l>>1)+s+1]
            if one < ml : return ml+mm >>1
            elif one > mr : return mr+mm >>1
            else : return mm+one >> 1
    
# median of a sorted int list plus 2 extra elements
# can be done without merge
def medianSortedPlus2(A,sa,la,B,sb):
    A = A[sa:sa+la]
    B = B[sb:sb+2]
    C = mergeTwoSorted(A,B)
    return medianSorted(C,0,la+2)
    
def medianTwoSortedRec(A, sa, la, B, sb, lb):
    # bottom case
    if la == 1:
        return medianSortedPlus1(B,sb,lb,A[sa])
    elif la == 2:
        return medianSortedPlus2(B,sb,lb,A,sa)
    if lb == 1:
        return medianSortedPlus1(A,sa,la,B[sb])
    elif lb == 2:
        return medianSortedPlus2(A,sa,la,B,sb)
    
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
    if len(A) < 1 or len(B) < 1:
        return -1
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
