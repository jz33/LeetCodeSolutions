import random
'''
27 Remove Elements
https://oj.leetcode.com/problems/remove-elements/
'''
# generate a random int array with limits [a,b]
def createRandList(n,a,b):
    A = []
    for i in range(n):
        A.append(random.randint(a,b))
    return A

def removeElements(array, tag):
    i = 0
    j = 0
    while i < len(array):
        while i < len(array) and array[i] == tag: 
            i += 1
        if i < len(array):
            array[j] = array[i]
            i += 1
            j += 1
    return array[0:j]
    
def main():
    array = createRandList(20,1,6)
    print array
    print removeElements(array,2)

if __name__ == "__main__":
    main()
