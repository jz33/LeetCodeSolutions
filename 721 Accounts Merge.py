'''
721. Accounts Merge
https://leetcode.com/problems/accounts-merge/

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if
there is some email that is common to both accounts. Note that even if two accounts have the same name,
they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name,
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

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
class UnionFind:
    def __init__(self):
        # {node : parent node}
        self.parents = {} 

    def addNode(self, i):
        self.parents[i] = i

    def find(self, i):
        parents = self.parents   
        if parents[i] != i:
            parents[i] = self.find(parents[i])
        return parents[i]

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)      
        if ri != rj:
            self.parents[rj] = ri
            
    def tree(self):
        '''
        Return a {root : [children]} dict
        '''
        tree = collections.defaultdict(list)
        for i in self.parents:
            root = self.find(i)
            tree[root].append(i)
        return tree
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = UnionFind()    
        emailToName = {} # {email : user name}, for building final result
        
        # Initialize graph
        for line in accounts:
            name = line[0]
            for i, email in enumerate(line[1:]):
                graph.addNode(email)
                emailToName[email] = name
   
        # Union Find on emails within same account
        for line in accounts:
            firstEmail = line[1]
            for i, email in enumerate(line[2:]):
                graph.union(firstEmail, email)
        
        # Build result
        tree = graph.tree()
        res = []
        for root, emails in tree.items():
            name = emailToName[root]
            res.append([name] + sorted(emails))          
        return res
