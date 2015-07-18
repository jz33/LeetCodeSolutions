import string,random
'''
30 Substring with Concatenation of All Words
https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/
'''
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

def find(S, L):
    res = []
    str_len = len(L[0])

    # notice L can have duplicate strings
    ori = dict((x,L.count(x)) for x in set(L))
    
    for i in range(0, len(S)+1 - len(L) * str_len):
        ref = {}
        j = 0
        while j < len(L):
            substring = S[i + j * str_len:i + j * str_len + str_len]
            if not substring in ori:
                break
            else:
                ref[substring] = ref.get(substring, 0) + 1
                if ref[substring] > ori[substring]:
                    break
                j = j + 1
        if j == len(L):
            res.append(i)
     
    return res
    
def main():
    S = r'barfoothefoobarman'
    L = ['foo', 'bar']
    print S
    print L
    print find(S,L)

if __name__ == "__main__":
    main()
