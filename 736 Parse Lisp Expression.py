'''
736. Parse Lisp Expression

You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let",
then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is
assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2,
and so on sequentially; and then the value of this let-expression is the value of the expression expr.

An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two expressions e1, e2,
and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.

A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two expressions e1, e2,
and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.

For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter,
then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let",
or "mult" are protected and will never be used as variable names.

Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation,
the innermost scope (in terms of parentheses) is checked first for the value of that variable,
and then outer scopes are checked sequentially. It is guaranteed that every expression is legal.
Please see the examples for more details on scope.

Evaluation Examples:
Input: (add 1 2)
Output: 3

Input: (mult 3 (add 2 3))
Output: 15

Input: (let x 2 (mult x 5))
Output: 10

Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

Input: (let x 3 x 2 x)
Output: 2
Explanation: Assignment in let statements is processed sequentially.

Input: (let x 1 y 2 x (add x y) (add x y))
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

Input: (let x 2 (add (let x 3 (let x 4 x)) x))
Output: 6
Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.

Input: (let a1 3 b2 (add a1 1) b2) 
Output 4
Explanation: Variable names can contain digits after the first character.

Note:

The given string expression is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
'''
def isInt(e):
    try:
        i = int(e)
        return True
    except:
        return False

class Scope:
    def __init__(self):
        self.mapper = {} # stores "let" results
        self.result = None # stores "add", "mult" results

        # Below 3 are temporary storage when having new '('
        self.op = None
        self.num = None
        self.vari = None

    def add(self, vari, value):
        self.mapper[vari] = value

    def get(self, vari):
        return self.mapper.get(vari, None)

class Solution:
    def getValue(self, e, scopes) -> int:
        if isinstance(e, int):
            return e

        if isInt(e):
            return int(e)

        for scope in scopes[::-1]:
            val = scope.get(e)
            if val is not None:
                return val

        raise ValueError()

    def compute(self, op, left, right, scopes):
        '''
        @left, right: can be integer or digit string or variable string
        '''
        if op == 1:
            y = self.getValue(right, scopes)
            scopes[-1].add(left, y)
            scopes[-1].result = y
        elif op == 2:
            scopes[-1].result = self.getValue(left, scopes) + self.getValue(right, scopes)
        elif op == 3:
            scopes[-1].result = self.getValue(left, scopes) * self.getValue(right, scopes)

    def tryCompute(self, op, num, vari, e, scopes) -> bool:
        if op is not None and (num is not None or vari is not None):
            if num is not None:
                self.compute(op, num, e, scopes)
            else: # vari is not None
                self.compute(op, vari, e, scopes)
            return True
        return False

    def evaluate(self, expression: str) -> int:
        op = None # operator, 1: let, 2: add, 3: mult
        num = None # number integer
        vari = None # variable string. variable and num cannot both be non-None
        scopes = [] # stack of scopes

        def reset():
            nonlocal op, num, vari
            op, num, vari = None, None, None

        def push():
            nonlocal op, num, vari, scopes
            if len(scopes) > 0:
                scopes[-1].op = op
                scopes[-1].num = num
                scopes[-1].vari = vari
            reset()
            scopes.append(Scope())

        src = expression.split()
        for e in src:
            tailBracketsCount = 0 # how many tail brackets

            if e[0] == '(':
                push()
                e = e[1:]

            elif e[-1] == ')':
                for i in range(len(e)-1,-1,-1):
                    if e[i] == ')':
                        tailBracketsCount += 1
                    else:
                        break
                e = e[:i+1]

            if e == 'let':
                op = 1
            elif e == 'add':
                op = 2
            elif e == 'mult':
                op = 3
            else: # variable or digit
                if self.tryCompute(op, num, vari, e, scopes):
                    # reset
                    num = None
                    vari = None
                    if op != 1: # do not reset 'let'
                        op = None
                elif isInt(e):
                    num = int(e)
                else:
                    vari = e

            for _ in range(tailBracketsCount):
                # determine the final result of this scope
                result = None
                if num is not None:
                    result = num # {let x 3 4}
                elif vari is not None:
                    result = self.getValue(vari, scopes) # {let x 3 y}
                else:
                    result = scopes[-1].result

                scopes.pop()

                # Compute with outer scope
                if len(scopes) == 0:
                    return result

                if self.tryCompute(scopes[-1].op, scopes[-1].num, scopes[-1].vari, result, scopes):
                    num = None
                    vari = None
                else:
                    # scopes[-1].num and scopes[-1].vari are both None                     
                    num = result
                op = scopes[-1].op

        raise ValueError() # not reachable

# Test
sol = Solution()
exprs = [
('(add 1 2)', 3), 
('(mult 3 (add 2 3))', 15),
('(mult (add 2 3) 3)', 15),
('(let x 2 (mult x 5))', 10),
('(let x 2 (mult x (let x 3 y 4 (add x y))))', 14),
('(let x 3 x 2 x)', 2),
('(let x 1 y 2 x (add x y) (add x y))', 5),
('(let x 2 (add (let x 3 (let x 4 x)) x))', 6),
('(let a1 3 b2 (add a1 1) b2)', 4),
('(let x 7 -12)', -12),
]

for expr, er in exprs:
    print(expr, er, sol.evaluate(expr))
