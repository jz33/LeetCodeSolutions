'''
1261. Find Elements in a Contaminated Binary Tree
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contamined binary tree,
you need to recover it first.
bool find(int target) Return if the target value exists in the recovered binary tree.
 

Example 1:

Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 

Example 2:

Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False

Example 3:

Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:
    
    def __init__(self, root: TreeNode):
        '''
        Increase each node' value by 1
            0          1             1
         1    2   => 2    3   => 10     11
        3 4  5 6    4 5  6 7  100 101 110 111
        
        There is no need to recovery!
        '''
        self.root = root
    
    def find(self, target: int) -> bool:
        if not self.root:
            return False
 
        t = target + 1
        
        # Find left most bit
        b = 1
        while b <= t:
            b <<= 1
        b = b >> 2
        
        # Only need to go 1 direction, according to bit
        p = self.root
        while b > 0:
            if (b & t) == 0:
                if not p.left:
                    return False
                p = p.left
            else:
                if not p.right:
                    return False
                p = p.right
            b >>= 1
        return True
