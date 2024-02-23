'''
666. Path Sum IV
https://leetcode.com/problems/path-sum-iv/

If the depth of a tree is smaller than 5,
then this tree can be represented by an array of three-digit integers.
For each integer in this array:

    The hundreds digit represents the depth d of this node where 1 <= d <= 4.

    The tens digit represents the position p of this node in the level it belongs to where 1 <= p <= 8.
    The position is the same as that in a full binary tree.

    The units digit represents the value v of this node where 0 <= v <= 9.

Given an array of ascending three-digit integers nums representing a binary tree with a depth smaller than 5,
return the sum of all paths from the root towards the leaves.

It is guaranteed that the given array represents a valid connected binary tree.

Example 1:

Input: nums = [113,215,221]
Output: 12
Explanation: The tree that the list represents is shown.
The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:

Input: nums = [113,221]
Output: 4
Explanation: The tree that the list represents is shown. 
The path sum is (3 + 1) = 4.

Constraints:
    1 <= nums.length <= 15
    110 <= nums[i] <= 489
    nums represents a valid binary tree with depth less than 5.
'''
def getDepth(numNode: int):
    return numNode // 100

def getPosition(numNode: int):
    return numNode // 10 % 10

def getValue(numNode: int): 
    return numNode % 10

def getParentPosition(position: int): 
    return (position + 1) >> 1

def getLeftChildPosition(position: int):
    return (position << 1) - 1

def getRightChildPosition(position: int):
    return position << 1

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        totalPathSum = 0
        layer = Counter() # {position : path sum}
        newLayer = Counter()

        def addSums():
            '''
            Add possible root to leaf path sum in layer
            Check if the node in layer is leaf by using newLayer
            '''
            nonlocal totalPathSum
            for position, pathSum in layer.items():
                leftChild = getLeftChildPosition(position)
                rightChild = getRightChildPosition(position)
                if leftChild not in newLayer and rightChild not in newLayer:
                    # If this node is a leaf, add to result
                    totalPathSum += pathSum

        currentDepth = 1
        for numNode in nums:
            depth = getDepth(numNode)
            position = getPosition(numNode)
            value = getValue(numNode)

            if depth != currentDepth:
                # Add sum in layer and move to new layer
                addSums()
                layer, newLayer = newLayer, Counter()
                currentDepth += 1

            parentPosition = getParentPosition(position)
            newLayer[position] = layer[parentPosition] + value

        # This is to add sum in the layer, aka 2nd last level
        addSums()
        # This is to add last level
        lastLayerSum = sum(newLayer.values())
        return totalPathSum + lastLayerSum