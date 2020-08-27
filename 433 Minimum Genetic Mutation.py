'''
433. Minimum Genetic Mutation
https://leetcode.com/problems/minimum-genetic-mutation/

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"),
where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end".
If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
 

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
 

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
'''
class Solution:
    def toBit(self, gene: str) -> int:
        '''
        Same hashing idea as 187. Repeated DNA Sequences 
        'A' - 64 : 1 : 00001 : 001 :  00
        'C' - 64 : 3 : 00011 : 011 :  01
        'G' - 64 : 7 : 00111 : 111 :  11
        'T' - 64 :20 : 10100 : 100 :  10
        '''
        h = 0
        for g in gene:
            h |= ((ord(g) - 64) & 6) >> 1
            h <<= 2
        h >>= 2
        return h
            
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bitBank = set(self.toBit(b) for b in bank)
        bitEnd = self.toBit(end)
        if bitEnd not in bitBank:
            return -1

        bitStart = self.toBit(start)
        stack = [bitStart]
        seen = {bitStart}
        steps = 1
        while stack:
            newStack = []
            for gene in stack:  
                # Iterate 8 char positions
                for i in range(0, 16, 2):
                    d0 = 1 << i
                    d1 = 1 << (i+1)
                    # For example, for '01', need to get '00', '10', '11',
                    # then flip d0 bit, flip d1 bit, or flip both d0 & d1
                    for newGene in (gene ^ d0, gene ^ d1, gene ^ d0 ^ d1):
                        if newGene in bitBank and newGene not in seen:
                            if newGene == bitEnd:
                                return steps
                            newStack.append(newGene)
                            seen.add(newGene)
            steps += 1
            stack = newStack
        return -1
