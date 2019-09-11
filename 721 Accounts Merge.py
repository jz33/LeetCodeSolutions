'''
721. Accounts Merge
https://leetcode.com/problems/accounts-merge/

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

More Example:
Input:
[["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
Output:
[["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
'''
from typing import Tuple

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        Union-Find
        Think email address as graph node, then parsing each account is to
        add nodes to graph.
        '''
        emailToIndex = {} # email : index, to simplify graph lookup
        indexToNameEmail = {} # index : (name, email) just for building final result
        graph = {} #  email index : root email index
        
        def getRoot(index: int) -> Tuple[int, int]:
            depth = 0
            while True:
                parent = graph.get(index, -1)
                if parent == -1: # not existed
                    break
                if parent == index: # parent is self, then self is a root
                    depth += 1
                    break
                index = parent
                depth +=1
            return index, depth
        
        for account in accounts:
            name = account[0]
            emails = account[1:]
            
            maxDepth = -1
            maxDepthRoot = None
            roots = [None] * len(emails)
            for i, email in enumerate(emails):
                index = -1
                
                # Get index of email, update helper dict
                if email in emailToIndex:
                    index = emailToIndex[email]
                else:
                    index = len(emailToIndex)
                    emailToIndex[email] = index                   
                    indexToNameEmail[index] = (name, email)
                
                # Get root
                root, depth = getRoot(index)
                if depth > maxDepth:
                    maxDepth = depth
                    maxDepthRoot = root
                roots[i] = root
                       
            # Union, update all found root
            for root in roots:
                graph[root] = maxDepthRoot
                     
        # print(emailToIndex)
        # print(indexToNameEmail)
        # print(graph)

        rootTochilden = {} # root index : children node indexes
        for index, root in graph.items():
            maxRoot, _ = getRoot(root)
            if maxRoot in rootTochilden:
                rootTochilden[maxRoot].append(index)
            else:
                rootTochilden[maxRoot] = [index]
                
        # print(rootTochilden)
        
        res = []
        for root, children in rootTochilden.items():
            name = indexToNameEmail[root][0]
            
            emails = [None] * len(children)
            for i, child in enumerate(children):
                emails[i] = indexToNameEmail[child][1]
                
            res.append([name] + sorted(emails))
            
        return res
        
        
        
            
            
        
