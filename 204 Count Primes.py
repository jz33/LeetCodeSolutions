'''
204. Count Primes
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Eratosthenes
        '''
        result = 0
        
        # primes[i] is prime if True
        primes = [True] * n
        
        for i in range(2, n):
            if primes[i]:
                result += 1
                
                # Mark all multiple as non-prime
                m = i
                while m * i < n:
                    primes[m * i] = False
                    m += 1

        return result
