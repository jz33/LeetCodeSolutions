'''
https://leetcode.com/discuss/interview-question/435536/Google-or-Onsite-or-Design-a-Cord
https://leetcode.com/discuss/interview-question/413991/

I was asked a question to design a cord data structure and write a function that finds a certain index of
the leaf nodes in this cord.

https://en.wikipedia.org/wiki/Rope_(data_structure)

I got this same question. They asked me to implement:

char_at(index) -
    easy got it quick. The solution is recursive.

substring_at(start_index, end_index) -
    was able to explain in words but did not have for code. The solution is recursive.

'''
class Node:
    def __init__(self, text = None):
        self.text = text
        self.left = None
        self.right = None

        weight = 0 if not text else len(text)
        self.weight = weight # length of left branch
        self.total = weight # total length of left and right branch
        
def fromChildren(left, right = None) -> Node: # static
    n = Node()
    n.left = left
    n.right = right
    n.weight = left.total
    n.total = left.total + (right.total if right is not None else 0)
    return n

class RopeTree:
    '''
    Give a hard coded rope tree just like on Wikipedia
    https://en.wikipedia.org/wiki/Rope_%28data_structure%29
    '''
    def __init__(self):
        self.text = 'Hello_my_name_is_Simon'

        E = Node('Hello_')
        F = Node('my_')
        J = Node('na')
        K = Node('me_i')
        M = Node('s')
        N = Node('_Simon')

        C = fromChildren(E, F)
        G = fromChildren(J, K)
        H = fromChildren(M, N)
        D = fromChildren(G, H)
        B = fromChildren(C, D)

        self.A = fromChildren(B)


    def index(self, i: int) -> str:
        '''
        Get char at index i
        '''
        node = self.A
        while node:
            # Not node.weight < i
            if node.weight <= i and node.right:
                i -= node.weight
                node = node.right
            elif node.left:
                node = node.left
            else:
                break
        return node.text[i]


    def report(self, left: int, right: int) -> str:
        '''
        Get substring in i...j inclusive
        '''
        # 1. Find the closest "parent" node where
        # left index should be in its left branch or itself,
        # right index should be in its right branch or itself.
        node = self.A
        i = left
        j = right
        while node:
            if node.weight <= i and node.right:
                i -= node.weight
                j -= node.weight
                node = node.right
            elif j < node.weight and node.left:
                node = node.left
            else:
                break

        if not node:
            return ''

        # 2. Inorder traversal, collect text on leaves
        stack = []
        res = []
        while node or stack:
            if node:
                # Go left
                stack.append((node, i, j))
                node = node.left
            else:
                node, i, j = stack.pop()
                if node.text:
                    # Get text on leaf node.
                    # Notice the boundaries
                    sub = node.text[max(0, i) : min(j+1, len(node.text))]
                    if sub:
                        res.append(sub)

                # Go right
                i -= node.weight
                j -= node.weight
                node = node.right

        return ''.join(res)


def testIndexes(tree):
    for i, c in enumerate(tree.text):
        print(i, c, tree.index(i))


tree = RopeTree()
testIndexes(tree)

print(tree.report(0, len(tree.text)-1))
