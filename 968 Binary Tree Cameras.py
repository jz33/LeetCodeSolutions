'''
968. Binary Tree Cameras
https://leetcode.com/problems/binary-tree-cameras/

You are given the root of a binary tree. We install cameras on the tree nodes where each camera at
a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:

Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    Node.val == 0
'''
HasCamera = 1 # the node has camera
NoCameraMonitored = 2 # the node has no camera, but monitored by other nodes
NoCameraNotMonitored = 3 # the node has no camera, and not monitored by other nodes

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameraNeeded = 0
        
        def postorder(node: Optional[TreeNode]) -> int:
            nonlocal cameraNeeded

            if not node:
                return NoCameraMonitored
            
            leftState = postorder(node.left)
            rightState = postorder(node.right)

            if leftState == NoCameraNotMonitored or rightState == NoCameraNotMonitored:
                cameraNeeded += 1
                return HasCamera
            if leftState == HasCamera or rightState == HasCamera:
                return NoCameraMonitored
            else: # leftState == NoCameraMonitored and rightState == NoCameraMonitored
                return NoCameraNotMonitored
            
        state = postorder(root)
        if state == NoCameraNotMonitored:
            cameraNeeded += 1
        return cameraNeeded
