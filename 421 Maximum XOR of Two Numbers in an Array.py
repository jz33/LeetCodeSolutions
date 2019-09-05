'''
421. Maximum XOR of Two Numbers in an Array
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/130427/()-92
'''
class Trie:
    '''
    A binary trie with only 2 possible children [0, 1]
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = -1; # if there is a number ends here, val will > 0
        self.children = [None, None]
        
    def insert(self, n: int) -> None:
        """
        Inserts a word into the trie.
        """
        this = self # use this pointer to avoid recursive
        i = 0x80000000 # Get bit from left to right
        while i:
            # Get left most digit of i
            d = 1 if (n & i) else 0
            if this.children[d] is None:
                this.children[d] = Trie()
            this = this.children[d]
            i = (i >> 1)
        this.val = n

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        head = Trie()
        for n in nums:
            head.insert(n)
        
        ret = 0
        for n in nums:
            p = head
            i = 0x80000000
            while i:
                if p.children[0] is not None and p.children[1] is not None:
                    d = 1 if (n & i) else 0
                    if d == 1:
                        # Choose 0 branch first
                        p = p.children[0]
                    else:
                        p = p.children[1]
                elif p.children[0]:
                    p = p.children[0]
                elif p.children[1]:
                    p = p.children[1]
                else:
                    # Reached leaf 
                    break

                i = (i >> 1)

            ret = max(ret, p.val ^ n)

        return ret
            
            
        
        
