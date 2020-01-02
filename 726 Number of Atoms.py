'''
726. Number of Atoms
https://leetcode.com/problems/number-of-atoms/

Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1.
If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.
For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order),
followed by its count (if that count is more than 1), followed by the second name (in sorted order),
followed by its count (if that count is more than 1), and so on.

Example 1:
Input: 
formula = "H2O"
Output: "H2O"
Explanation: 
The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input: 
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input: 
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
'''
from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        def compute():
            nonlocal stack, atom, count
            if count > 0:
                if not atom:
                    # This is the case when right out of ')' and got a number
                    ctr = stack.pop()
                    for key in ctr:
                        ctr[key] = ctr[key] * count
                    stack.append(ctr)
                else:
                    # e.g., H2, O32
                    atomName = ''.join(atom)
                    stack.append(Counter({atomName : count}))
            elif atom:
                # e.g., HOU
                atomName = ''.join(atom)
                stack.append(Counter({atomName : 1}))
            
            # If both atom and count is empty, this is the very beginning or
            # case like (OH)A, out of a parenthese, and get no number but next atom.
            # Do nothing.

            atom = []
            count = 0
            
        def collapse():
            nonlocal stack
            
            cc = Counter()
            while stack and isinstance(stack[-1], Counter):
                cc += stack.pop()
                
            if stack:
                # Computing {...}, there must be an "(" ahead
                stack.pop()
            stack.append(cc)
            
        atom = []
        count = 0
        stack = [] # stack of Counters or operator string
        for char in formula:
            if char.isdecimal():
                count = count * 10 + int(char)
                
            elif char.islower():
                atom.append(char)
                
            elif char.isupper():
                compute()
                atom.append(char) 
                
            elif char == '(':
                compute()
                stack.append('(')
                
            elif char == ')':
                compute()                
                collapse()

        compute()
        collapse()

        # Rearrange final output
        ls = sorted(stack.pop().items(), key = lambda x : x[0])
        res = []
        for atom, ct in ls:
            if ct == 1:
                res.append(atom)
            else:
                res.append(atom + str(ct))
        return ''.join(res)
