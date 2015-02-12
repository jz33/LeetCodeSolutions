import random,string
'''
26 Remove Duplicated from Sorted Array
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
80 Remove Duplicated from Sorted Array II
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''
# generate a random int array with limits [a,b]
def randInList(n,a,b):
    A = []
    for i in range(n):
        A.append(random.randint(a,b))
    return A
'''
generate a random string with length 's'
http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
'''
def randString(s):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(s))
 
'''
generate a random string list with length 'n'
each string has same length as 's'
'''
def randStringList(s,n):
    A = []
    for i in range(n):
        A.append(randString(s))
    return A
    
# 80
def removeDup2(array):
    if len(array) < 2: return array
    i = 1
    j = 0
    while i < len(array):
        if array[i] == array[j]:
            i += 1
            j += 1
        while i < len(array) and array[i] == array[j]: 
            i += 1
        j += 1
        if i < len(array):
            array[j] = array[i]
        i += 1
    return array[0:j]

# 26
def removeDup(array):
    if len(array) < 2: return array
    i = 1
    j = 0
    while i < len(array):
        while i < len(array) and array[i] == array[j]: 
            i += 1
        j += 1
        if i < len(array):
            array[j] = array[i]
        i += 1
    return array[0:j]

def main():
    array = randInList(10,1,6)
    array = sorted(array)
    print array
    print removeDup2(array)

    chars = randString(20)
    chars = sorted(chars)
    print chars
    print removeDup(chars)
    
if __name__ == "__main__":
    main()
