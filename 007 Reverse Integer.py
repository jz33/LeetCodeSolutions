'''
07 Reverse Integer
https://oj.leetcode.com/problems/reverse-integer/

Accepted
'''
def reverse(x):
    if x == 0 or x > 2147483647 or x < -2147483647:
        return 0
        
    sign = -1 if x < 0 else 1
  
    ori = str(x)
    if sign == -1:
        ori = ori[1:]
        
    rev = ori[::-1]
    rev = rev.strip('0')
    
    y = int(rev)
    if y > 2147483647:
        return 0
    
    return y if sign == 1 else -y
    

def main():
    xs = [-1234000,-123456789]
    for x in xs:
        print x,reverse(x)
    
if __name__ == '__main__':
    main()
