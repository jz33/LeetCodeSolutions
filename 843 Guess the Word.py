'''
843. Guess the Word
https://leetcode.com/problems/guess-the-word/

This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.
The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.
Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls,
if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.
The letters of each word in those testcases were chosen independently at random from 'a' to 'z',
such that every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Note:  Any solutions that attempt to circumvent the judge will result in disqualification.
'''
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
from typing import List, Tuple
from collections import Counter, deque, defaultdict
from itertools import combinations, permutations

def matchCount(A: str, B: str) -> int:
    return sum(1 for i in range(6) if A[i] == B[i])

class Master:
    def __init__(self, wordlist: List[str], secret: str):
        self.wordSet = set(wordlist)
        self.secret = secret
        self.counter = 0

    def guess(self, word: str) -> int:       
        if len(word) != 6:
            raise IndexError("Incorret word size!")

        if word not in self.wordSet:
            return -1

        self.counter += 1
        print("Try times: ", self.counter)

        mc = matchCount(self.secret, word)
        if mc == 6:
            print("You found it!")
        return mc

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        '''
        The core of the algorithm is: which to word to guess?
        If we chose a word (A), guess it, got the guess result (R), we can be sure that
        the secret word (S) is among the words whose match count is R to A.
        Since words are randomly generated, so 0 match is the most common guess result.
        Therefore, choose the word whose has minimum 0 match count with other words
        '''
        candidates = range(len(wordlist))

        while True:
            # Use permutation not combination here, as combination only computes half and so has bias
            book = Counter(w1 for w1, w2 in permutations(candidates, 2) if matchCount(wordlist[w1], wordlist[w2]) == 0)
            guessWordIndex = min(candidates, key = lambda wi : book[wi])

            guessWord = wordlist[guessWordIndex]
            guessResult = master.guess(guessWord)
            if guessResult == 6:
                return

            candidates = [i for i in candidates if matchCount(wordlist[i], guessWord) == guessResult]
            
sol = Solution()

secret = "eiowzz"
wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

secret = "hbaczn"
wordlist = ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]

ms = Master(wordlist, secret)
sol.findSecretWord(wordlist, ms)
