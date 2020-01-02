'''
1087. Brace Expansion
https://leetcode.com/problems/brace-expansion/
1096. Brace Expansion II
https://leetcode.com/problems/brace-expansion-ii/

Under a grammar given below, strings can represent a set of lowercase words.
Let's use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

    Single letters represent a singleton set containing that word.
        R("a") = {"a"}
        R("w") = {"w"}
    When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
        R("{a,b,c}") = {"a","b","c"}
        R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
    When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
        R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
        R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

Formally, the 3 rules for our grammar:

    For every lowercase letter x, we have R(x) = {x}
    For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
    For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}, where + denotes concatenation, and × denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

Example 1:

Input: "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]

Example 2:

Input: "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.

'''
ADD = 0x0005
PRODUCT = 0x0006

def product(a, b):
    '''
    @a: set of strings or a string
    @b: set of strings or a string
    '''
    if isinstance(a, set) and isinstance(b, set):
        return set(''.join(t) for t in itertools.product(a, b))
    if isinstance(a, set): # a is set, b is string
        return set(t+b for t in a)
    if isinstance(b, set): # a is string, b is set
        return set(a+t for t in b)

class Solution:
    def compute(self, operator: int, item: object, stack: List[object]):
        '''
        @item: set of strings or a char list
        '''
        ss = None
        if isinstance(item, set) and len(item) > 0:
            ss = item
        elif isinstance(item, list) and len(item) > 0:
            ss = ''.join(item)
            
        if ss:
            if operator == ADD:
                stack.append(ss)
            elif operator == PRODUCT:
                stack.append(product(stack.pop(), ss))

    def collapse(self, stack: List[object]):
        '''
        Calculate between <operater, {...}> or final result <[set or stirng]>
        '''
        ss = set()
        while stack and (isinstance(stack[-1], str) or isinstance(stack[-1], set)):
            if isinstance(stack[-1], str):
                ss.add(stack.pop())
            elif isinstance(stack[-1], set):
                ss = ss | stack.pop()
        
        if stack:
            # Computing {...}, there must be an operator ahead
            operator = stack.pop()
            self.compute(operator, ss, stack)
        else:
            # Compute final result
            stack.append(ss)

    def braceExpansionII(self, expression: str) -> List[str]:
        # stack contains set of string, string, or operator integers
        operator = ADD # either '*' or '+'
        stack = []
        text = []
        for i, c in enumerate(expression):
            if c.isalpha():
                text.append(c)

            elif c == ',':
                self.compute(operator, text, stack)
                operator = ADD
                text = []

            elif c == '{':
                self.compute(operator, text, stack)

                if i > 0 and expression[i-1].isalpha():
                    # {a,b},abc{a,b}
                    stack.append(PRODUCT)
                else:
                    stack.append(operator)
                
                operator = ADD
                text = []

            elif c == '}':
                self.compute(operator, text, stack)
                self.collapse(stack)
                operator = PRODUCT # {a,b}abc
                text = []

        self.compute(operator, text, stack)
        self.collapse(stack)
        return sorted(list(stack.pop()))
    
'''
More examples:
expr = r"{a,b}{c,d}{e,f}" # ["ace","acf","ade","adf","bce","bcf","bde","bdf"]
expr = r"{a,b}c{{d,e}}" # ["acd","ace","bcd","bce"]
expr = r"{{a,z},a{b,c},{ab,z}}" # ["a","ab","ac","z"]
expr = r"{a,b}{c,{d,e}}" #  ["ac","ad","ae","bc","bd","be"]
expr = r"{a,b}abc{a,b}" # ["aabca","aabcb","babca","babcb"]
expr = r"{f,g},abc{a,b}" # ['abca', 'abcb', 'f', 'g']
'''
