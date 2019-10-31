'''
809. Expressive Words
https://leetcode.com/problems/expressive-words/

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".
In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications
of the following extension operation: choose a group consisting of characters c,
and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo",
but we cannot get "helloo" since the group "oo" has size less than 3.
Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".
If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations:
query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

Example:

Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1

Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more
'''
class Solution:
    def groups(self, exp: str):
        groups = [] # [(char, count)]
        ctr = 0
        for i,c in enumerate(exp):
            if i > 0 and c != exp[i-1]:
                groups.append((exp[i-1], ctr))
                ctr = 0
            ctr += 1

        if ctr > 0:
            groups.append((exp[-1], ctr))

        return groups 

    def sameGroup(self, ga, gb):
        if len(ga) != len(gb):
            return False
                
        for i in range(len(ga)):
            if ga[i][0] != gb[i][0]: # same char
                return False
            
            diff = ga[i][1] - gb[i][1] # count diff
            if diff < 0:
                return False
            
            if not (ga[i][1] > 2 or diff == 0):
                return False
        
        return True
    
    def expressiveWords(self, S: str, words: List[str]) -> int:
        gs = self.groups(S)
        return sum(1 for word in words if self.sameGroup(gs, self.groups(word)))
