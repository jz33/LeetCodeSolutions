'''
135 Candy
https://oj.leetcode.com/problems/candy/
'''  
def candy(ratings):
    n = len(ratings)
    if n == 0 : return

    candies = [1 for x in xrange(0,n)]
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1]+1
        else:
            candies[i] = 1
            
    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1;

    print candies # debug
    sum = 0
    for v in candies: sum += v
    return sum

def main():
    ratings = [1,2,2]
    print candy(ratings)
    
if __name__ == "__main__":
    main()
