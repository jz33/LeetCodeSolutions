/*
666. Path Sum IV
https://leetcode.com/problems/path-sum-iv/

If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers. For each integer in this array:

    The hundreds digit represents the depth d of this node where 1 <= d <= 4.
    The tens digit represents the position p of this node in the level it belongs to where 1 <= p <= 8. The position is the same as that in a full binary tree.
    The units digit represents the value v of this node where 0 <= v <= 9.

Given an array of ascending three-digit integers nums representing a binary tree with a depth smaller than 5, return the sum of all paths from the root towards the leaves.

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


*/
const getDepth = (numNode: number): number => Math.floor(numNode / 100);
const getPosition = (numNode: number): number => Math.floor(numNode / 10) % 10;
const getValue = (numNode: number): number => numNode % 10;

const getParentPosition = (position: number): number => (position + 1) >> 1;
const getLeftChildPosition = (position: number): number => (position << 1) - 1;
const getRightChildPosition = (position: number): number => position << 1;

function pathSum(nums: number[]): number {
    let totalPathSum = 0;
    let layer = new Map<number, number>(); // {position : path sum}
    let newLayer = new Map<number, number>();
    let currentDepth = 0;

    /**
     * Notice the path is not necessarily from root to last layer,
     * it can from root to inner leaves
     */
    const addInnerPaths = () => {
        for (const [position, pathSum] of layer.entries()) {
            const leftChild = getLeftChildPosition(position);
            const rightChild = getRightChildPosition(position);
            if (!newLayer.has(leftChild) && !newLayer.has(rightChild)) {
                totalPathSum += pathSum;
            }
        }
    };

    for (const numNode of nums) {
        const depth = getDepth(numNode);
        const position = getPosition(numNode);
        const value = getValue(numNode);

        if (depth !== currentDepth) {
            addInnerPaths();
            // Move to new layer
            layer = newLayer;
            newLayer = new Map<number, number>();
            currentDepth++;
        }
        const parentPosition = getParentPosition(position);
        newLayer.set(position, (layer.get(parentPosition) ?? 0) + value);
    }

    addInnerPaths();
    const lastLayerSum = Array.from(newLayer.values()).reduce(
        (prevSum, currSum) => prevSum + currSum,
        0
    );
    return totalPathSum + lastLayerSum;
}
