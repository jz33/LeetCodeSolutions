'''
135 Candy
https://oj.leetcode.com/problems/candy/
'''  
def candy(ratings):
    n = len(ratings)
    if n == 0 : return

    candies = [0]
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candies.append(candies[i-1]+1)
        else:
            candies.append(1)
    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1;

    print candies
    sum = 0
    for v in candies: sum += v
    return sum

def main():
    ratings = [5,1,3,5,7,9,3,1,5,7,11,9]
    candies = []
    print candy(ratings)
    
if __name__ == "__main__":
    main()
