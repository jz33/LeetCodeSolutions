'''
1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
'''
def removeDuplicates(src: str) -> str:
    stack = [] # List[character]
    for e in src:
        stack.append(e)

        # Remove all equal character pairs
        while len(stack) > 1 and stack[-1] == stack[-2]:
            stack = stack[:-2]

    return ''.join([c for c in stack])
