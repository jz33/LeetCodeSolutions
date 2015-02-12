'''
152 Maximum Product Subarray
https://oj.leetcode.com/problems/maximum-product-subarray/
''' 
# just print
def maxProduct(ls):
    ls.append(0)

    ret_end = 0
    ret_max = ls[0]
    pos = 1
    neg = 1
    
    for i,v in enumerate(ls):
        if v > 0:
            pos *= v
            neg *= v
        elif v == 0:
            if pos > ret_max:    
                ret_end = i
                ret_max = pos
            pos = 1
            neg = 1
        else:
            neg *= v
            if neg < 0:
                if pos > ret_max:    
                    ret_end = i
                    ret_max = pos
                pos = 1
            else:
                pos = neg
        
    print "max product: ", ret_max
    print "ended at index: ", ret_end

def simple_test(func):
    ls = [0,1,0,1,0,1]
    func(ls)
    ls = [2,3,4,-4,2,3]
    func(ls)
    ls = [2,3,0,-4,2,-2]
    func(ls)
    
def main():
    simple_test(maxProduct)
    
if __name__ == "__main__":
    main()
