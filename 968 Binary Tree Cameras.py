'''
968. Binary Tree Cameras
https://leetcode.com/problems/binary-tree-cameras/

Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:

Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree.
The above image shows one of the valid configurations of camera placement.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from enum import Enum
class State(Enum):
    HasCamera = 1
    NoCameraMonitored = 2
    NoCameraNotMonitored = 3

class Solution:
    def postorder(self, node: TreeNode) -> State:
        if not node:
            return State.NoCameraMonitored
        
        leftState = self.postorder(node.left)
        rightState = self.postorder(node.right)
        
        # This has to be first condition, because any of the children who is no camera and
        # not monitored, this node has to install a camera
        if leftState == State.NoCameraNotMonitored or rightState == State.NoCameraNotMonitored:
            self.cameraCount += 1
            return State.HasCamera

        elif leftState == State.HasCamera or rightState == State.HasCamera:
            return State.NoCameraMonitored
        
        else: # leftState == State.NoCameraMonitored and rightState == State.NoCameraMonitored:
            return State.NoCameraNotMonitored
        
    def minCameraCover(self, root: TreeNode) -> int:
        self.cameraCount = 0
        state = self.postorder(root)
        if state == State.NoCameraNotMonitored:
            self.cameraCount += 1
        return self.cameraCount
